"""Đo kỹ thuật cho QA (skill video-qa, rules/02-tiktok-platform.md T2.1) và trích khung hình.

In bảng PASS/FAIL và ghi <out-dir>/qa-metrics.json. Thoát mã 1 nếu có mục FAIL.

Dùng: python -I pipeline/qa_check.py --video <final.mp4> [--expect-duration 12.0]
       [--frames 0.5,3,6.5 --out-dir <thư mục>]
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import find_ffmpeg, write_json  # noqa: E402


def run(args: list[str]) -> str:
    proc = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return proc.stdout + proc.stderr


def probe(video: str) -> dict:
    out = run([find_ffmpeg("ffprobe"), "-v", "error", "-show_entries",
               "stream=codec_type,codec_name,width,height,r_frame_rate,pix_fmt,sample_rate,channels",
               "-show_entries", "format=duration,size", "-of", "json", video])
    return json.loads(out)


def loudness(video: str) -> tuple[float, float]:
    out = run([find_ffmpeg(), "-hide_banner", "-nostats", "-i", video, "-af", "ebur128=peak=true",
               "-f", "null", "-"])
    summary = out[out.rfind("Summary:"):]
    integrated = float(re.search(r"I:\s+(-?[\d.]+) LUFS", summary).group(1))
    peak = float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", summary).group(1))
    return integrated, peak


def detect(video: str, vf: str, key: str) -> list[str]:
    out = run([find_ffmpeg(), "-hide_banner", "-i", video, "-vf", vf, "-an", "-f", "null", "-"])
    return [line.strip() for line in out.splitlines() if key in line]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--video", required=True)
    ap.add_argument("--expect-duration", type=float)
    ap.add_argument("--frames", default="")
    ap.add_argument("--out-dir")
    args = ap.parse_args()

    info = probe(args.video)
    v = next(s for s in info["streams"] if s["codec_type"] == "video")
    a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    duration = float(info["format"]["duration"])
    size_mb = int(info["format"]["size"]) / 1_048_576
    lufs, peak = loudness(args.video)
    black = detect(args.video, "blackdetect=d=0.2:pix_th=0.10", "black_start")
    freeze = detect(args.video, "freezedetect=n=0.003:d=2.5", "freeze_start")

    checks = [
        ("Độ phân giải 1080×1920", f"{v['width']}×{v['height']}", v["width"] == 1080 and v["height"] == 1920),
        ("FPS 30", v["r_frame_rate"], v["r_frame_rate"] == "30/1"),
        ("Video h264 / yuv420p", f"{v['codec_name']} / {v['pix_fmt']}", v["codec_name"] == "h264" and v["pix_fmt"] == "yuv420p"),
        ("Audio aac / 48000", f"{a['codec_name']} / {a['sample_rate']}" if a else "không có", bool(a) and a["codec_name"] == "aac" and a["sample_rate"] == "48000"),
        ("Loudness -14 ±1 LUFS", f"{lufs} LUFS", abs(lufs + 14) <= 1),
        ("True peak ≤ -1 dBTP", f"{peak} dBFS", peak <= -1.0),
        ("Không khung đen", f"{len(black)} đoạn", not black),
        ("Không đứng hình > 2,5s", f"{len(freeze)} đoạn", not freeze),
        ("Dung lượng < 200MB", f"{size_mb:.1f} MB", size_mb < 200),
    ]
    if args.expect_duration:
        checks.append(("Thời lượng ±0,5s", f"{duration:.2f}s / {args.expect_duration:.2f}s",
                       abs(duration - args.expect_duration) <= 0.5))
    else:
        checks.append(("Thời lượng", f"{duration:.2f}s", True))

    for name, actual, ok in checks:
        print(f"{'PASS' if ok else 'FAIL'}  {name:<26} {actual}")

    if args.out_dir:
        out_dir = Path(args.out_dir)
        (out_dir / "frames").mkdir(parents=True, exist_ok=True)
        for t in [x for x in args.frames.split(",") if x]:
            run([find_ffmpeg(), "-hide_banner", "-loglevel", "error", "-y", "-ss", t, "-i", args.video,
                 "-frames:v", "1", "-q:v", "2", str(out_dir / "frames" / f"t{t}.jpg")])
        write_json(out_dir / "qa-metrics.json", {
            "video": args.video, "duration_s": duration, "lufs": lufs, "true_peak": peak,
            "black": black, "freeze": freeze,
            "checks": [{"name": n, "actual": act, "pass": ok} for n, act, ok in checks],
        })

    sys.exit(0 if all(ok for _, _, ok in checks) else 1)


if __name__ == "__main__":
    main()
