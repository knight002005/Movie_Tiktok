"""Chạy notebook tạo sprite trên Kaggle hoàn toàn bằng API (không cần mở trình duyệt).

1. Build notebook từ spec (build_notebook.py) vào thư mục tạm + kernel-metadata.json
   (riêng tư, GPU T4, bật Internet).
2. `kaggle kernels push` → chạy ở chế độ lưu phiên bản (có output tải về được).
3. Theo dõi trạng thái tới khi complete/error.
4. Tải output về --dest.

Yêu cầu: token Kaggle ở ~/.kaggle/access_token (hoặc kaggle.json), tài khoản đã xác minh SĐT.
Dùng: python -I -X utf8 pipeline/sprites/kaggle_run.py --spec <spec.json> --slug movie-tiktok-sprites-test --dest kaggle-test
"""
import argparse
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
POLL_S = 60
MAX_WAIT_S = 3 * 3600


def kaggle(*args: str) -> str:
    proc = subprocess.run(["kaggle", *args], capture_output=True, text=True, encoding="utf-8", errors="replace",
                          env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
    out = (proc.stdout + proc.stderr).strip()
    if proc.returncode != 0:
        raise RuntimeError(f"kaggle {' '.join(args)} lỗi:\n{out}")
    return out


def username() -> str:
    # Dòng dữ liệu đầu tiên của danh sách kernel: "<user>/<slug> ..." — tránh đọc token trực tiếp.
    out = kaggle("config", "view")
    for line in out.splitlines():
        if line.strip().startswith("- username:"):
            return line.split(":", 1)[1].strip()
    raise RuntimeError("Không xác định được username Kaggle (kiểm tra token).")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--slug", required=True, help="tên kernel, vd. movie-tiktok-sprites")
    ap.add_argument("--dest", required=True, help="thư mục nhận output")
    ap.add_argument("--accelerator", default="NvidiaTeslaT4")
    args = ap.parse_args()

    user = username()
    kernel_id = f"{user}/{args.slug}"
    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        nb = tmp_dir / f"{args.slug}.ipynb"
        subprocess.run([sys.executable, "-I", "-X", "utf8", str(HERE / "build_notebook.py"),
                        "--spec", args.spec, "--out", str(nb)], check=True)
        meta = {
            "id": kernel_id, "title": args.slug, "code_file": nb.name,
            "language": "python", "kernel_type": "notebook",
            "is_private": "true", "enable_gpu": "true", "enable_internet": "true",
            "machine_shape": args.accelerator,
            "dataset_sources": [], "competition_sources": [], "kernel_sources": [], "model_sources": [],
        }
        (tmp_dir / "kernel-metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
        print(kaggle("kernels", "push", "-p", str(tmp_dir), "--accelerator", args.accelerator))

    print(f"Đang chạy trên Kaggle: https://www.kaggle.com/code/{kernel_id}")
    started = time.time()
    status = ""
    while time.time() - started < MAX_WAIT_S:
        time.sleep(POLL_S)
        try:
            status = kaggle("kernels", "status", kernel_id)
        except RuntimeError as e:
            print(f"[{int(time.time() - started)}s] chưa đọc được trạng thái: {str(e).splitlines()[-1]}")
            continue
        print(f"[{int(time.time() - started)}s] {status.splitlines()[-1]}", flush=True)
        low = status.lower()
        if "complete" in low or "error" in low or "cancel" in low:
            break

    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)
    print(kaggle("kernels", "output", kernel_id, "-p", str(dest)))
    if "error" in status.lower():
        print("⚠️ Notebook lỗi — xem log đã tải về trong", dest)
        sys.exit(1)
    print("Xong →", dest)


if __name__ == "__main__":
    main()
