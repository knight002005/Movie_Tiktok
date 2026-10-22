"""Tạo bộ sprite nhân vật nhất quán (rules/03-visual-style.md V3.3) — chạy trên Kaggle/Colab GPU
miễn phí, hoặc CPU để kiểm thử với model nhỏ.

Cách giữ nhân vật giống nhau qua mọi biểu cảm:
  1. Mỗi pose tạo MỘT ảnh gốc (seed cố định, character tag cố định, miệng khép).
  2. Biểu cảm = inpaint CHỈ vùng mặt của ảnh gốc → tóc, áo, phụ kiện giữ nguyên từng pixel.
  3. Biến thể nhắm mắt = inpaint CHỈ dải mắt của ảnh biểu cảm.
  4. (SDXL, tùy chọn) pose thứ 2 trở đi dùng IP-Adapter với ảnh gốc pose 1 làm tham chiếu.
  5. Tách nền bằng rembg (model isnet-anime), xuất PNG trong suốt, ghi tọa độ mặt/mắt/miệng.

Đầu ra cho mỗi nhân vật <out>/<char-id>/:
  refs/<pose>_base.png       ảnh gốc có nền (để anh duyệt)
  sprites/<pose>_<expr>.png  và <pose>_<expr>_blink.png (nền trong suốt)
  manifest.json              hộp mặt + tọa độ mắt/miệng ước lượng cho profile.md
  contact_sheet.jpg          lưới mọi sprite để soát nhất quán bằng mắt

Dùng: python sprite_gen.py --spec spec.json --out out_dir [--only linh] [--max-expr 3]
"""
import argparse
import json
import sys
import urllib.request
from pathlib import Path

import cv2
import numpy as np
import torch
from diffusers import AutoPipelineForInpainting, AutoPipelineForText2Image
from PIL import Image, ImageDraw, ImageFilter

# Console Windows mặc định không phải UTF-8 → in tiếng Việt sẽ lỗi.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8")

CASCADE_URL = "https://raw.githubusercontent.com/nagadomi/lbpcascade_animeface/master/lbpcascade_animeface.xml"

EXPRESSION_PROMPTS = {
    "neutral": "neutral expression, closed mouth",
    "smile": "gentle smile, closed mouth",
    "angry": "angry, furrowed eyebrows, glaring, closed mouth",
    "sad": "sad, downcast eyes, closed mouth",
    "surprised": "surprised, wide open eyes, raised eyebrows, closed mouth",
    "embarrassed": "embarrassed, blushing cheeks, looking away, closed mouth",
    "cold": "cold expression, half-closed eyes, expressionless, closed mouth",
    "cry": "crying, tears streaming down cheeks, closed mouth",
    "smirk": "smirk, one corner of mouth raised, closed mouth",
    "panic": "panicked, wide eyes, small pupils, sweat, closed mouth",
    "love": "lovestruck, soft eyes, blushing, closed mouth",
}


# ---------- Model ----------

def load_pipes(cfg: dict):
    cuda = torch.cuda.is_available()
    dtype = torch.float16 if cuda else torch.float32
    kwargs = {"torch_dtype": dtype}
    try:  # ưu tiên trọng số fp16 (tải nhẹ bằng nửa); trên CPU tự nâng lên float32
        t2i = AutoPipelineForText2Image.from_pretrained(cfg["model_id"], variant="fp16", **kwargs)
    except (OSError, ValueError):
        t2i = AutoPipelineForText2Image.from_pretrained(cfg["model_id"], **kwargs)
    t2i = t2i.to("cuda" if cuda else "cpu")
    if cuda and cfg.get("low_vram"):
        t2i.enable_model_cpu_offload()
    ip_adapter = False
    if cfg.get("ip_adapter"):
        try:
            ipa = cfg["ip_adapter"]
            t2i.load_ip_adapter(ipa["repo"], subfolder=ipa["subfolder"], weight_name=ipa["weight"])
            ip_adapter = True
        except Exception as e:  # IP-Adapter là tùy chọn — lỗi thì chạy tiếp bằng prompt
            print(f"[cảnh báo] Không nạp được IP-Adapter: {e}")
    # Tạo pipeline inpaint SAU khi nạp IP-Adapter để dùng chung image_encoder.
    inpaint = AutoPipelineForInpainting.from_pipe(t2i)
    return t2i, inpaint, ip_adapter


# ---------- Vùng mặt ----------

def load_cascade(cache_dir: Path):
    """Bộ dò mặt anime (LBP cascade). OpenCV 5 đã bỏ CascadeClassifier → trả None, dùng hộp dự phòng."""
    if not hasattr(cv2, "CascadeClassifier"):
        print("[cảnh báo] OpenCV không có CascadeClassifier (cần opencv<5) → dùng hộp mặt dự phòng trong spec")
        return None
    path = cache_dir / "lbpcascade_animeface.xml"
    if not path.exists():
        cache_dir.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(CASCADE_URL, path)
    return cv2.CascadeClassifier(str(path))


def detect_face(img: Image.Image, cascade, fallback: list[float]) -> tuple[list[int], bool]:
    """Trả (x, y, w, h) của mặt và cờ có phát hiện thật hay dùng hộp dự phòng (tỉ lệ ảnh)."""
    faces = []
    if cascade is not None:
        gray = cv2.equalizeHist(cv2.cvtColor(np.array(img.convert("RGB")), cv2.COLOR_RGB2GRAY))
        faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(64, 64))
    if len(faces):
        x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
        return [int(x), int(y), int(w), int(h)], True
    W, H = img.size
    fx, fy, fw, fh = fallback
    return [int(fx * W), int(fy * H), int(fw * W), int(fh * H)], False


def region_mask(size: tuple[int, int], box: list[int], part: str) -> Image.Image:
    """Mặt nạ inpaint: 'face' = mắt + lông mày + miệng; 'eyes' = dải mắt."""
    x, y, w, h = box
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    if part == "eyes":
        d.rectangle([x + 0.08 * w, y + 0.32 * h, x + 0.92 * w, y + 0.66 * h], fill=255)
    else:
        d.ellipse([x + 0.04 * w, y + 0.18 * h, x + 0.96 * w, y + 1.02 * h], fill=255)
    return mask.filter(ImageFilter.GaussianBlur(radius=max(4, w // 30)))


# ---------- Sinh ảnh ----------

def prompt_of(spec: dict, char: dict, pose_desc: str, extra: str) -> str:
    return ", ".join(p for p in [spec["style"], char["tag"], pose_desc, extra, spec["framing"]] if p)


def make_generator(seed: int) -> torch.Generator:
    return torch.Generator(device="cuda" if torch.cuda.is_available() else "cpu").manual_seed(seed)


def run_char(spec: dict, char: dict, pipes, out: Path, cascade, max_expr: int | None) -> dict:
    t2i, inpaint, ip_adapter = pipes
    gen_cfg = spec["generation"]
    W, H = gen_cfg["width"], gen_cfg["height"]
    negative = ", ".join([spec["negative"], char.get("negative", "")]).strip(", ")
    expressions = char["expressions"][:max_expr] if max_expr else char["expressions"]
    (out / "refs").mkdir(parents=True, exist_ok=True)
    (out / "raw").mkdir(parents=True, exist_ok=True)
    manifest = {"id": char["id"], "size": [W, H], "poses": {}}
    first_base = None

    for pose_id, pose_desc in char["poses"].items():
        seed = char["seed"] + list(char["poses"]).index(pose_id)
        # IP-Adapter: pose đầu không có tham chiếu (scale 0); các pose sau tham chiếu ảnh gốc pose đầu.
        ip = {}
        if ip_adapter:
            ref = first_base if first_base is not None else Image.new("RGB", (W, H), "white")
            t2i.set_ip_adapter_scale(0.0 if first_base is None else spec["model"]["ip_adapter"].get("scale", 0.6))
            ip = {"ip_adapter_image": ref}
        base = t2i(
            prompt=prompt_of(spec, char, pose_desc, EXPRESSION_PROMPTS["neutral"]),
            negative_prompt=negative, width=W, height=H,
            num_inference_steps=gen_cfg["steps"], guidance_scale=gen_cfg["guidance"],
            generator=make_generator(seed), **ip,
        ).images[0]
        base.save(out / "refs" / f"{pose_id}_base.png")
        first_base = first_base or base
        if ip_adapter:
            ip = {"ip_adapter_image": first_base}

        box, detected = detect_face(base, cascade, spec["face_fallback_box"])
        x, y, w, h = box
        manifest["poses"][pose_id] = {
            "face_box": box,
            "face_detected": detected,
            "eyes": {"x": x + w // 2, "y": int(y + 0.5 * h)},
            "mouth": {"x": x + w // 2, "y": int(y + 0.82 * h), "w": int(0.22 * w)},
        }
        print(f"[{char['id']}/{pose_id}] seed {seed}, mặt {'phát hiện' if detected else 'DỰ PHÒNG'} {box}")

        face_mask = region_mask(base.size, box, "face")
        eye_mask = region_mask(base.size, box, "eyes")
        for expr in expressions:
            if expr == "neutral":
                img = base
            else:
                img = inpaint(
                    prompt=prompt_of(spec, char, pose_desc, EXPRESSION_PROMPTS.get(expr, expr)),
                    negative_prompt=negative, image=base, mask_image=face_mask, width=W, height=H,
                    strength=gen_cfg["face_strength"], num_inference_steps=gen_cfg["inpaint_steps"],
                    guidance_scale=gen_cfg["guidance"], generator=make_generator(seed + 100), **ip,
                ).images[0]
            blink = inpaint(
                prompt=prompt_of(spec, char, pose_desc, "eyes closed, " + EXPRESSION_PROMPTS.get(expr, expr)),
                negative_prompt=negative, image=img, mask_image=eye_mask, width=W, height=H,
                strength=gen_cfg["eye_strength"], num_inference_steps=gen_cfg["inpaint_steps"],
                guidance_scale=gen_cfg["guidance"], generator=make_generator(seed + 200), **ip,
            ).images[0]
            img.save(out / "raw" / f"{pose_id}_{expr}.png")
            blink.save(out / "raw" / f"{pose_id}_{expr}_blink.png")
            print(f"  ✓ {pose_id}_{expr} (+blink)")

    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


# ---------- Hậu xử lý ----------

def cut_out(raw_dir: Path, sprite_dir: Path, target_height: int) -> list[Path]:
    from rembg import new_session, remove

    session = new_session("isnet-anime")
    sprite_dir.mkdir(parents=True, exist_ok=True)
    outputs = []
    for src in sorted(raw_dir.glob("*.png")):
        img = remove(Image.open(src), session=session)
        scale = target_height / img.height
        img = img.resize((round(img.width * scale), target_height), Image.LANCZOS)
        dst = sprite_dir / src.name
        img.save(dst)
        outputs.append(dst)
    return outputs


def contact_sheet(paths: list[Path], dst: Path, thumb_h: int = 420) -> None:
    thumbs = []
    for p in paths:
        im = Image.open(p).convert("RGBA")
        im = im.resize((round(im.width * thumb_h / im.height), thumb_h), Image.LANCZOS)
        bg = Image.new("RGBA", im.size, (200, 205, 215, 255))
        bg.alpha_composite(im)
        thumbs.append((p.stem, bg.convert("RGB")))
    cols = 4
    tw = max(t.width for _, t in thumbs)
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * (thumb_h + 28)), "white")
    d = ImageDraw.Draw(sheet)
    for i, (name, t) in enumerate(thumbs):
        cx, cy = (i % cols) * tw, (i // cols) * (thumb_h + 28)
        sheet.paste(t, (cx, cy))
        d.text((cx + 6, cy + thumb_h + 6), name, fill="black")
    sheet.save(dst, quality=90)


def run_locations(spec: dict, pipes, out_root: Path, only: str | None) -> None:
    """Ảnh nền bối cảnh (rules/03-visual-style.md V3.4): không người, không chữ, khung dọc,
    phóng lên khổ lớn hơn 1080×1920 để camera pan/zoom không vỡ."""
    from diffusers import AutoPipelineForImage2Image

    t2i, _, ip_adapter = pipes
    gen_cfg = spec["generation"]
    loc_cfg = spec.get("location_generation", {})
    W = loc_cfg.get("width", gen_cfg.get("bg_width", 768))
    H = loc_cfg.get("height", gen_cfg.get("bg_height", 1344))
    out_w, out_h = loc_cfg.get("upscale_to", [None, gen_cfg.get("bg_height_out", 2560)])
    steps = loc_cfg.get("steps", gen_cfg["steps"])
    guidance = loc_cfg.get("guidance", gen_cfg["guidance"])
    style = spec.get("location_style") or f"{spec['style']}, background art, scenery, no humans, vertical composition"
    negative = spec.get("location_negative") or \
        spec["negative"] + ", people, person, 1girl, 1boy, character, text, letters, logo, signage"
    # Biến thể sau (vd. night) img2img từ biến thể đầu để giữ nguyên bố cục căn phòng.
    img2img = AutoPipelineForImage2Image.from_pipe(t2i) if loc_cfg.get("variant_mode") == "img2img_from_first" else None
    ip = {}
    if ip_adapter:  # nền không cần tham chiếu nhân vật
        t2i.set_ip_adapter_scale(0.0)
        ip = {"ip_adapter_image": Image.new("RGB", (W, H), "white")}
    outputs = []
    for loc in spec.get("locations", []):
        if only and loc["id"] != only:
            continue
        loc_dir = out_root / "locations" / loc["id"]
        loc_dir.mkdir(parents=True, exist_ok=True)
        first = None
        for k, (variant, desc) in enumerate(loc.get("variants", {"day": ""}).items()):
            prompt = ", ".join(p for p in [style, loc["prompt"], desc] if p)
            common = dict(prompt=prompt, negative_prompt=negative, num_inference_steps=steps,
                          guidance_scale=guidance, generator=make_generator(loc["seed"] + k), **ip)
            if first is not None and img2img is not None:
                img = img2img(image=first, strength=loc_cfg.get("variant_strength", 0.55), **common).images[0]
            else:
                img = t2i(width=W, height=H, **common).images[0]
            first = first or img
            target_w = out_w or round(W * out_h / H)
            dst = loc_dir / f"{loc['id']}_{variant}.png"
            img.resize((target_w, out_h), Image.LANCZOS).save(dst)
            outputs.append(dst)
            print(f"  ✓ {dst.name}")
    if outputs:
        contact_sheet(outputs, out_root / "locations" / "contact_sheet.jpg", thumb_h=480)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--only", help="Chỉ chạy một id nhân vật hoặc bối cảnh")
    ap.add_argument("--max-expr", type=int, help="Giới hạn số biểu cảm (chạy thử)")
    ap.add_argument("--skip-characters", action="store_true")
    ap.add_argument("--skip-locations", action="store_true")
    args = ap.parse_args()

    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    out_root = Path(args.out)
    pipes = load_pipes(spec["model"])
    if not args.skip_characters:
        cascade = load_cascade(out_root / ".cache")
        for char in spec["characters"]:
            if args.only and char["id"] != args.only:
                continue
            out = out_root / char["id"]
            run_char(spec, char, pipes, out, cascade, args.max_expr)
            sprites = cut_out(out / "raw", out / "sprites", spec["generation"]["sprite_height"])
            contact_sheet(sprites, out / "contact_sheet.jpg")
            print(f"[{char['id']}] xong: {len(sprites)} sprite → {out}")
    if not args.skip_locations:
        run_locations(spec, pipes, out_root, args.only)


if __name__ == "__main__":
    main()
