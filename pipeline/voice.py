"""Sinh giọng đọc có diễn xuất + mốc thời gian từng âm tiết (rules/04-audio-voice.md A4.2–A4.3a).

Hai engine (chọn theo trường "engine" của từng câu):
  - "vieneu" (mặc định khuyến nghị): VieNeu-TTS v3 Turbo, Apache-2.0, chạy CPU. Mỗi nhân vật một giọng
    thật sự khác nhau. Giọng lấy theo thứ tự: <ref_dir>/<emotion>.wav (ghi âm diễn cảm)
    → <ref_dir>/neutral.wav → giọng mẫu "voice". Mốc thời gian lấy bằng align.py (Whisper).
  - "edge": edge-tts (dự phòng), có sẵn mốc thời gian.

Đầu vào: JSON {"lines": [{
    "id", "text", "engine",
    "voice",                                  # vieneu: tên giọng mẫu; edge: voice_id
    "ref_dir"?,                               # vieneu: thư mục ghi âm mẫu của nhân vật
    "f0_hz"?,                                 # cao độ trung bình giọng (đổi Hz → tỉ lệ pitch), mặc định 200
    "rate", "pitch", "volume",                # chỉnh nền của nhân vật
    "expressiveness",                         # tính cách: 0.5 kiềm chế … 1.5 bộc lộ
    "emotion", "intensity",                   # cảm xúc của câu, cường độ 1–5
    "emotion_overrides"?
}]}
Đầu ra:  <out>/<id>.mp3 và <out>/timings.json
         timings = {"<id>": {"hash", "engine", "duration_s", "segments", "fx", "words", "match"?, "ref"?}}

Mỗi câu được tách thành các đoạn theo dấu câu, đọc với ngữ điệu riêng, chèn khoảng lặng,
ghép lại và áp hiệu ứng cảm xúc. Cache theo nội dung: câu không đổi thì không đọc lại.

Dùng: python -I -X utf8 pipeline/voice.py --lines <lines.json> --out <thư mục>
"""
import argparse
import asyncio
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import find_ffmpeg, read_json, write_json  # noqa: E402
from voice_emotion import plan_segments  # noqa: E402

TICKS_PER_SECOND = 10_000_000  # edge-tts dùng đơn vị 100ns
SAMPLE_RATE = 48000
VERSION = 5  # đổi khi thay thuật toán để cache tự làm mới
# Khi đã có ghi âm diễn cảm đúng cảm xúc, cảm xúc nằm sẵn trong giọng → chỉ giữ một phần lớp ngữ điệu.
PROSODY_SCALE_WITH_EMOTION_REF = 0.35

HASH_KEYS = ("text", "engine", "voice", "ref_dir", "f0_hz", "rate", "pitch", "volume",
             "expressiveness", "emotion", "intensity", "emotion_overrides")

_VIENEU = None


def vieneu():
    global _VIENEU
    if _VIENEU is None:
        from vieneu import Vieneu

        _VIENEU = Vieneu()
    return _VIENEU


def pick_ref(line: dict) -> tuple[Path | None, bool]:
    """(file ghi âm mẫu, có phải ghi âm đúng cảm xúc không)."""
    if not line.get("ref_dir"):
        return None, False
    d = Path(line["ref_dir"])
    emo = d / f"{line.get('emotion', 'neutral')}.wav"
    if emo.exists():
        return emo, line.get("emotion", "neutral") != "neutral"
    neutral = d / "neutral.wav"
    return (neutral, False) if neutral.exists() else (None, False)


def line_hash(line: dict) -> str:
    ref, _ = pick_ref(line)
    ref_sig = f"{ref}:{ref.stat().st_mtime_ns}" if ref else None
    key = json.dumps({k: line.get(k) for k in HASH_KEYS} | {"v": VERSION, "ref": ref_sig},
                     ensure_ascii=False, sort_keys=True)
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:12]


def probe_duration(path: Path) -> float:
    out = subprocess.run(
        [find_ffmpeg("ffprobe"), "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


def _num(v: str) -> float:
    return float(v.replace("%", "").replace("Hz", ""))


def ffmpeg(*args: str) -> None:
    subprocess.run([find_ffmpeg(), "-v", "error", "-y", *args], check=True)


# ---------- Engine: edge-tts ----------

async def edge_segment(text: str, voice: str, rate: str, pitch: str, volume: str, mp3: Path) -> list[dict]:
    import edge_tts

    comm = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch, volume=volume, boundary="WordBoundary")
    words = []
    with open(mp3, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                start = chunk["offset"] / TICKS_PER_SECOND
                words.append({"text": chunk["text"], "start": start,
                              "end": start + chunk["duration"] / TICKS_PER_SECOND})
    return words


# ---------- Engine: VieNeu-TTS ----------

def vieneu_segment(text: str, line: dict, ref: Path | None, rate: str, pitch: str, volume: str, wav: Path) -> None:
    """Đọc một đoạn bằng VieNeu rồi áp ngữ điệu: tempo/pitch bằng rubberband (không méo giọng), âm lượng."""
    tts = vieneu()
    if ref is not None:
        audio = tts.infer(text, ref_audio=str(ref), denoise=False)
    else:
        audio = tts.infer(text, voice=tts.get_preset_voice(line["voice"]))
    raw = wav.with_suffix(".raw.wav")
    tts.save(audio, str(raw))

    f0 = float(line.get("f0_hz", 200))
    tempo = max(0.6, 1 + _num(rate) / 100)
    pitch_ratio = max(0.7, (f0 + _num(pitch)) / f0)
    gain = max(0.1, 1 + _num(volume) / 100)
    ffmpeg("-i", str(raw), "-af",
           f"rubberband=tempo={tempo:.3f}:pitch={pitch_ratio:.4f}:formant=preserved,volume={gain:.3f}",
           "-ar", str(SAMPLE_RATE), "-ac", "1", str(wav))


# ---------- Ghép câu ----------

async def synth_line(line: dict, out_mp3: Path) -> dict:
    engine = line.get("engine", "edge")
    ref, emotional_ref = pick_ref(line) if engine == "vieneu" else (None, False)
    plan_line = dict(line)
    if emotional_ref:
        plan_line["expressiveness"] = float(line.get("expressiveness", 1.0)) * PROSODY_SCALE_WITH_EMOTION_REF
    if engine == "vieneu":
        # Giọng mẫu VieNeu đã là giọng tự nhiên của nhân vật → "rate/pitch/volume" của câu là độ lệch thêm.
        plan_line.setdefault("rate", "+0%")
        plan_line.setdefault("pitch", "+0Hz")
    segments, fx = plan_segments(plan_line)

    words: list[dict] = []
    parts: list[Path] = []
    cursor = 0.0
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        for i, seg in enumerate(segments):
            seg_wav = tmp_dir / f"s{i}.wav"
            if engine == "vieneu":
                vieneu_segment(seg.text, line, ref, seg.rate, seg.pitch, seg.volume, seg_wav)
            else:
                seg_mp3 = tmp_dir / f"s{i}.mp3"
                for w in await edge_segment(seg.text, line["voice"], seg.rate, seg.pitch, seg.volume, seg_mp3):
                    words.append({"text": w["text"], "start": round(cursor + w["start"], 3),
                                  "end": round(cursor + w["end"], 3)})
                ffmpeg("-i", str(seg_mp3), "-ac", "1", "-ar", str(SAMPLE_RATE), str(seg_wav))
            parts.append(seg_wav)
            cursor += probe_duration(seg_wav)
            if seg.pause_after_ms:
                gap = tmp_dir / f"g{i}.wav"
                ffmpeg("-f", "lavfi", "-i", f"anullsrc=r={SAMPLE_RATE}:cl=mono",
                       "-t", f"{seg.pause_after_ms / 1000:.3f}", str(gap))
                parts.append(gap)
                cursor += seg.pause_after_ms / 1000

        concat_list = tmp_dir / "list.txt"
        concat_list.write_text("".join(f"file '{p.as_posix()}'\n" for p in parts), encoding="utf-8")
        args = ["-f", "concat", "-safe", "0", "-i", str(concat_list)]
        if fx:
            args += ["-af", fx]
        ffmpeg(*args, "-ar", "48000", "-ac", "1", "-c:a", "libmp3lame", "-b:a", "160k", str(out_mp3))

    result = {
        "engine": engine,
        "duration_s": round(probe_duration(out_mp3), 3),
        "segments": [{"text": s.text, "rate": s.rate, "pitch": s.pitch, "volume": s.volume,
                      "pause_after_ms": s.pause_after_ms} for s in segments],
        "fx": fx,
    }
    if engine == "vieneu":
        from align import align

        result["words"], result["match"] = align(out_mp3, line["text"])
        result["ref"] = str(ref) if ref else f"preset:{line['voice']}"
    else:
        result["words"] = words
    return result


async def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lines", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    timings_path = out_dir / "timings.json"
    old = read_json(timings_path) if timings_path.exists() else {}

    timings = {}
    for line in read_json(args.lines)["lines"]:
        mp3 = out_dir / f"{line['id']}.mp3"
        h = line_hash(line)
        cached = old.get(line["id"])
        if cached and cached.get("hash") == h and mp3.exists():
            timings[line["id"]] = cached
            print(f"[cache] {line['id']}")
            continue
        result = await synth_line(line, mp3)
        timings[line["id"]] = {"hash": h, **result}
        match = f"  khớp {result['match']:.0%}" if "match" in result else ""
        warn = "  ⚠️ nên nghe lại" if result.get("match", 1) < 0.85 else ""
        print(f"[{result['engine']}] {line['id']}  {line.get('emotion', 'neutral')}×{line.get('intensity', 3)}  "
              f"{result['duration_s']}s  {len(result['words'])} âm tiết{match}{warn}")

    write_json(timings_path, timings)


if __name__ == "__main__":
    asyncio.run(main())
