"""Tiện ích dùng chung cho pipeline hậu kỳ."""
import json
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Console Windows mặc định không phải UTF-8 → in tiếng Việt sẽ lỗi.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")


def find_ffmpeg(name: str = "ffmpeg") -> str:
    """Tìm ffmpeg/ffprobe: biến môi trường FFMPEG_DIR → PATH → thư mục cài của winget."""
    env_dir = os.environ.get("FFMPEG_DIR")
    if env_dir:
        cand = Path(env_dir) / f"{name}.exe"
        if cand.exists():
            return str(cand)
    found = shutil.which(name)
    if found:
        return found
    winget = Path(os.environ.get("LOCALAPPDATA", "")) / "Microsoft" / "WinGet" / "Packages"
    for cand in sorted(winget.glob(f"Gyan.FFmpeg*/ffmpeg-*/bin/{name}.exe"), reverse=True):
        return str(cand)
    raise FileNotFoundError(f"Không tìm thấy {name}. Cài: winget install Gyan.FFmpeg")


def read_json(path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
