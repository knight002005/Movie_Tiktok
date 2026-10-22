"""Đóng gói sprite_gen.py + spec thành notebook Kaggle (một nguồn mã duy nhất).

Dùng: python -I pipeline/sprites/build_notebook.py [--spec pipeline/sprites/spec.kaggle.json]
Đầu ra: pipeline/sprites/kaggle_sprites.ipynb → tải lên Kaggle, bật GPU + Internet, Run All.
"""
import argparse
import json
import sys
from pathlib import Path

# Console Windows mặc định không phải UTF-8 → in tiếng Việt sẽ lỗi.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

HERE = Path(__file__).resolve().parent


def md(text: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": text}


def code(text: str) -> dict:
    return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [], "source": text}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", default=str(HERE / "spec.kaggle.json"))
    ap.add_argument("--out", default=str(HERE / "kaggle_sprites.ipynb"))
    args = ap.parse_args()

    source = (HERE / "sprite_gen.py").read_text(encoding="utf-8")
    spec = Path(args.spec).read_text(encoding="utf-8")

    cells = [
        md(
            "# Tạo sprite nhân vật — Movie_tiktok\n\n"
            "1. **Settings → Accelerator: GPU** (T4 x2 hoặc P100), **Internet: On** (cần xác minh số điện thoại Kaggle).\n"
            "2. Sửa cell `spec.json` nếu cần (thường casting-designer đã điền sẵn).\n"
            "3. **Run All**. Mỗi nhân vật 2 pose × 9 biểu cảm × 2 (mở/nhắm mắt) ≈ 15–25 phút trên T4.\n"
            "4. Tải `sprites_out.zip` ở tab Output → giải nén vào `series/<slug>/characters/`.\n\n"
            "Cách giữ nhân vật đồng nhất: mỗi pose tạo 1 ảnh gốc, biểu cảm chỉ vẽ lại vùng mặt, "
            "nhắm mắt chỉ vẽ lại dải mắt → tóc/áo/phụ kiện giữ nguyên từng pixel."
        ),
        # Ghim đúng phiên bản đã chạy thử thành công (không dùng -U "mới nhất").
        # torchao cài sẵn trên Kaggle quá cũ so với diffusers → gỡ đi (không cần dùng).
        # OpenCV 5 đã bỏ CascadeClassifier (bộ dò mặt anime) → ghim <5.
        code("!pip uninstall -y -q torchao\n"
             "!pip install -q diffusers==0.41.0 transformers==5.20.2 accelerate==1.15.0 "
             "\"rembg[gpu]==2.0.85\" \"opencv-python-headless<5\"\n"
             "import diffusers, transformers; print('diffusers', diffusers.__version__, '| transformers', transformers.__version__)"),
        code("%%writefile sprite_gen.py\n" + source),
        code("%%writefile spec.json\n" + spec),
        code("!python sprite_gen.py --spec spec.json --out /kaggle/working/sprites_out"),
        code(
            "from IPython.display import Image, display\n"
            "import glob\n"
            "for p in sorted(glob.glob('/kaggle/working/sprites_out/*/contact_sheet.jpg')):\n"
            "    print(p); display(Image(filename=p, width=900))"
        ),
        code("!cd /kaggle/working && zip -qr sprites_out.zip sprites_out -x 'sprites_out/.cache/*' && ls -lh sprites_out.zip"),
    ]
    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    Path(args.out).write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Đã tạo {args.out}")


if __name__ == "__main__":
    main()
