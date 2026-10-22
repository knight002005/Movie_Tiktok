"""Thử giọng (rules/04-audio-voice.md A4.2a): đọc mọi câu trong file thử giọng rồi ghép thành MỘT file mp3
để anh nghe liền mạch, kèm bảng tỷ lệ khớp (Whisper nghe lại) để biết câu nào có thể đọc sai.

Dùng: python -I -X utf8 pipeline/audition.py --lines series/<slug>/voice-tests/cast-audition.json
Đầu ra: <thư mục của file>/audio/*.mp3, <thư mục>/cast-audition.mp3, <thư mục>/cast-audition.md
"""
import argparse
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import find_ffmpeg, read_json  # noqa: E402

GAP_S = 0.9


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lines", required=True)
    args = ap.parse_args()

    lines_path = Path(args.lines)
    out_dir = lines_path.parent
    audio_dir = out_dir / "audio"
    subprocess.run([sys.executable, "-I", "-X", "utf8", str(Path(__file__).parent / "voice.py"),
                    "--lines", str(lines_path), "--out", str(audio_dir)], check=True)

    lines = read_json(lines_path)["lines"]
    timings = read_json(audio_dir / "timings.json")
    inputs, chains = [], []
    for i, line in enumerate(lines):
        inputs += ["-i", str(audio_dir / f"{line['id']}.mp3")]
        chains.append(f"[{i}:a]aresample=48000,apad=pad_dur={GAP_S}[a{i}]")
    graph = ";".join(chains) + ";" + "".join(f"[a{i}]" for i in range(len(lines))) + \
        f"concat=n={len(lines)}:v=0:a=1,loudnorm=I=-16:TP=-1.5[out]"
    mp3 = out_dir / "cast-audition.mp3"
    subprocess.run([find_ffmpeg(), "-v", "error", "-y", *inputs, "-filter_complex", graph, "-map", "[out]",
                    "-c:a", "libmp3lame", "-b:a", "160k", str(mp3)], check=True)

    rows = ["| # | Câu | Giọng | Cảm xúc | Khớp (Whisper) | Ghi chú |", "|---|---|---|---|---|---|"]
    for i, line in enumerate(lines, 1):
        t = timings[line["id"]]
        match = t.get("match")
        note = "⚠️ nghe lại" if match is not None and match < 0.85 else ""
        rows.append(f"| {i} | {line['text']} | {t.get('ref', line['voice'])} | {line.get('emotion')}×{line.get('intensity')} "
                    f"| {'' if match is None else f'{match:.0%}'} | {note} |")
    (out_dir / "cast-audition.md").write_text(
        "# Thử giọng\n\nNghe `cast-audition.mp3` theo đúng thứ tự bảng. Chấm 1–5: đúng dấu thanh, tự nhiên, "
        "cảm xúc, phân biệt được với vai khác (A4.2a).\n\n" + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"Đã tạo {mp3}")


if __name__ == "__main__":
    main()
