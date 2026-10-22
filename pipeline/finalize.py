"""Hoàn thiện video xuất từ Remotion theo T2.1: loudnorm 2 lượt về -14 LUFS / -1 dBTP,
H.264 yuv420p 30fps, AAC 48 kHz, +faststart.

Dùng: python -I pipeline/finalize.py --in <render.mp4> --out <final.mp4>
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import find_ffmpeg  # noqa: E402

TARGET = {"I": -14.0, "TP": -1.0, "LRA": 11.0}


def measure(src: str) -> dict:
    proc = subprocess.run(
        [find_ffmpeg(), "-hide_banner", "-nostats", "-i", src, "-af",
         f"loudnorm=I={TARGET['I']}:TP={TARGET['TP']}:LRA={TARGET['LRA']}:print_format=json",
         "-f", "null", "-"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", check=True,
    )
    return json.loads(re.findall(r"\{[^{}]*\}", proc.stderr)[-1])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    m = measure(args.src)
    print(f"Trước: {m['input_i']} LUFS, true peak {m['input_tp']} dBTP")
    af = (
        f"loudnorm=I={TARGET['I']}:TP={TARGET['TP']}:LRA={TARGET['LRA']}"
        f":measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
        f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true"
    )
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [find_ffmpeg(), "-hide_banner", "-loglevel", "error", "-y", "-i", args.src,
         # Remotion xuất khung JPEG dải màu đầy đủ (yuvj420p) → đổi về dải TV chuẩn yuv420p.
         "-vf", "scale=out_range=tv,format=yuv420p", "-color_range", "tv",
         "-af", af, "-ar", "48000", "-ac", "2", "-c:a", "aac", "-b:a", "192k",
         "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", "30",
         "-crf", "18", "-preset", "medium", "-movflags", "+faststart", args.out],
        check=True,
    )
    print(f"Đã xuất: {args.out}")


if __name__ == "__main__":
    main()
