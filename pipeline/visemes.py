"""Tính hình miệng theo từng khung hình (rules/04-audio-voice.md A4.4).

Kết hợp hai nguồn:
  1. Mốc thời gian từng âm tiết (timings.json) → hình miệng theo nguyên âm chính.
  2. Âm lượng RMS theo khung hình (giải mã audio bằng ffmpeg) → độ mở miệng, im lặng → X.

Đầu ra: <out>/visemes.json = {"fps": 30, "lines": {"<id>": [[shape, open], ...]}}
  shape ∈ X M A O E H; open ∈ [0, 1].

Dùng: python -I pipeline/visemes.py --timings <timings.json> --audio-dir <dir> --out <visemes.json>
"""
import argparse
import array
import math
import subprocess
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import find_ffmpeg, read_json, write_json  # noqa: E402

SAMPLE_RATE = 16000
TONE_MARKS = {"̀", "́", "̃", "̉", "̣"}  # huyền sắc ngã hỏi nặng
VOWELS = set("aăâeêioôơuưy")
LABIALS = ("m", "b", "p")
MIN_HOLD_FRAMES = 2  # không đổi hình miệng nhanh hơn mỗi 2 frame
SILENCE_RATIO = 0.12  # RMS dưới 12% đỉnh → coi là im lặng


def strip_tones(word: str) -> str:
    """Bỏ dấu thanh nhưng giữ dấu mũ/móc/trăng: 'trưởng' → 'trương'."""
    decomposed = unicodedata.normalize("NFD", word.lower())
    return unicodedata.normalize("NFC", "".join(c for c in decomposed if c not in TONE_MARKS))


def syllable_parts(syl: str) -> tuple[str, str, str]:
    """Tách âm tiết thành (phụ âm đầu, cụm nguyên âm, phụ âm cuối)."""
    s = "".join(c for c in strip_tones(syl) if c.isalpha())
    if s.startswith("qu") and len(s) > 2:
        onset_end = 2
    elif s.startswith("gi") and len(s) > 2 and s[2] in VOWELS:
        onset_end = 2
    else:
        onset_end = 0
        while onset_end < len(s) and s[onset_end] not in VOWELS:
            onset_end += 1
    nucleus_end = onset_end
    while nucleus_end < len(s) and s[nucleus_end] in VOWELS:
        nucleus_end += 1
    return s[:onset_end], s[onset_end:nucleus_end], s[nucleus_end:]


SHAPE_BY_VOWEL = {
    "a": "A", "ă": "A", "â": "A",
    "o": "O", "ô": "O", "u": "O",
    "e": "E", "ê": "E", "i": "E", "y": "E",
    "ơ": "H", "ư": "H",
}


def vowel_shape(nucleus: str) -> str:
    """Hình miệng theo nguyên âm chính. Nguyên âm chính thường là chữ đầu của cụm,
    trừ khi chữ đầu là âm đệm: o trong oa/oă/oe, u trong uy/uê/uâ/uơ."""
    if not nucleus:
        return "H"
    main = nucleus
    if len(main) > 1 and main[0] == "o" and main[1] in "aăe":
        main = main[1:]
    elif len(main) > 1 and main[0] == "u" and main[1] in "yêâơ":
        main = main[1:]
    return SHAPE_BY_VOWEL.get(main[0], "H")


def syllable_frames(syl: str, n: int) -> list[str]:
    """Chuỗi hình miệng cho một âm tiết dài n frame."""
    onset, nucleus, coda = syllable_parts(syl)
    shape = vowel_shape(nucleus)
    frames = []
    for i in range(n):
        t = (i + 0.5) / n
        if onset in LABIALS and t < 0.18:
            frames.append("M")
        elif t < 0.72:
            frames.append(shape)
        elif coda in ("m", "p"):
            frames.append("M")
        else:
            frames.append("H")
    return frames


def rms_per_frame(audio: Path, fps: int) -> list[float]:
    raw = subprocess.run(
        [find_ffmpeg(), "-v", "error", "-i", str(audio), "-ac", "1", "-ar", str(SAMPLE_RATE),
         "-f", "s16le", "-"],
        capture_output=True, check=True,
    ).stdout
    samples = array.array("h", raw)
    hop = SAMPLE_RATE // fps
    out = []
    for i in range(0, len(samples), hop):
        chunk = samples[i:i + hop]
        out.append(math.sqrt(sum(x * x for x in chunk) / len(chunk)) if chunk else 0.0)
    return out


def smooth(shapes: list[str]) -> list[str]:
    """Giữ mỗi hình miệng ít nhất MIN_HOLD_FRAMES frame."""
    out = shapes[:]
    i = 0
    while i < len(out):
        j = i
        while j < len(out) and out[j] == out[i]:
            j += 1
        if j - i < MIN_HOLD_FRAMES and i > 0:
            for k in range(i, j):
                out[k] = out[i - 1]
        i = j
    return out


def line_visemes(timing: dict, audio: Path, fps: int) -> list[list]:
    rms = rms_per_frame(audio, fps)
    total = max(len(rms), math.ceil(timing["duration_s"] * fps))
    shapes = ["X"] * total

    for w in timing["words"]:
        syllables = w["text"].split() or [w["text"]]
        span = (w["end"] - w["start"]) / len(syllables)
        for k, syl in enumerate(syllables):
            f0 = int(round((w["start"] + k * span) * fps))
            f1 = max(f0 + 1, int(round((w["start"] + (k + 1) * span) * fps)))
            for offset, shape in enumerate(syllable_frames(syl, f1 - f0)):
                if f0 + offset < total:
                    shapes[f0 + offset] = shape

    peak = max(rms) or 1.0
    levels = [rms[i] / peak if i < len(rms) else 0.0 for i in range(total)]
    # Im lặng → X trước, rồi mới làm mượt để không còn X lẻ 1 frame giữa câu.
    gated = ["X" if lv < SILENCE_RATIO else s for s, lv in zip(shapes, levels)]
    result = []
    for shape, level in zip(smooth(gated), levels):
        openness = 0.0 if shape == "X" else 0.6 + 0.4 * min(1.0, level / 0.7)  # hét mở to hơn thì thầm
        result.append([shape, round(openness, 2)])
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--timings", required=True)
    ap.add_argument("--audio-dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fps", type=int, default=30)
    args = ap.parse_args()

    timings = read_json(args.timings)
    lines = {}
    for line_id, timing in timings.items():
        lines[line_id] = line_visemes(timing, Path(args.audio_dir) / f"{line_id}.mp3", args.fps)
        speaking = sum(1 for s, _ in lines[line_id] if s != "X")
        print(f"{line_id}: {len(lines[line_id])} frame, {speaking} frame nói")
    write_json(args.out, {"fps": args.fps, "lines": lines})


if __name__ == "__main__":
    main()
