---
name: character-design
description: Thiết kế nhân vật & bối cảnh anime cho motion comic với ngân sách 0 đồng — character tag cố định, prompt sprite theo pose × biểu cảm, danh sách ảnh cần tạo, cách tạo ảnh miễn phí nhất quán (Kaggle/Colab, công cụ web), casting giọng edge-tts, đo tọa độ miệng/mắt. Dùng cho casting-designer.
---

# Thiết kế nhân vật & bối cảnh

## 1. Thiết kế nhận diện
- Mỗi nhân vật một **silhouette** khác: chiều cao, kiểu tóc (dài/ngắn/buộc), dáng (thẳng/khom/khoanh tay).
- Một **màu chủ đạo** (trang phục/phụ kiện) không trùng nhân vật khác; màu phụ đề lấy theo màu này nhưng đủ tương phản trên viền đen (độ sáng ≥ 60%).
- Một **phụ kiện nhận diện** (kính, kẹp tóc, đồng hồ, cà vạt màu).

## 2. Prompt nhất quán
Cấu trúc prompt = `STYLE` (chung series) + `CHARACTER TAG` (cố định từng nhân vật) + `POSE` + `EXPRESSION` + `FRAMING`.
- **STYLE** ví dụ: `anime style, modern josei illustration, clean lineart, cel shading, soft pastel lighting, high quality`
- **CHARACTER TAG** ví dụ: `adult woman, 24 years old, Vietnamese office worker, shoulder-length dark brown hair with side bangs, warm brown eyes, cream blouse, navy pencil skirt, small gold star hairclip`
- **FRAMING**: `half body, facing three-quarter view, centered, plain white background, mouth closed`
- **NEGATIVE** chung: `child, loli, chibi, nsfw, revealing clothes, cleavage, text, watermark, logo, extra fingers, deformed hands, multiple people`
Không bao giờ thay đổi CHARACTER TAG giữa các lần tạo. Muốn sửa nhân vật → sửa tag, tạo lại **toàn bộ** sprite.

## 3. Danh sách ảnh cần tạo
Cho mỗi nhân vật: `pose (≥2) × biểu cảm (≥8) × {mở mắt, nhắm mắt}` ≈ 32 ảnh. Ghi vào `asset-checklist.md`:
| File đích | Prompt (phần thay đổi) | Trạng thái |
|---|---|---|
| characters/linh/sprites/p1_neutral.png | p1, neutral | ☐ |
| characters/linh/sprites/p1_neutral_blink.png | p1, neutral, eyes closed | ☐ |

Mẹo giảm số ảnh: tạo `p1_<expr>` trước; biến thể nhắm mắt có thể làm bằng **chỉnh sửa ảnh** (inpaint vùng mắt) thay vì tạo mới — giữ nhân vật giống hệt.

## 4a. Công cụ tạo sprite của xưởng (ưu tiên dùng)
- `pipeline/sprites/sprite_gen.py` + `pipeline/sprites/spec.kaggle.json`: điền mỗi nhân vật một mục `characters[]` gồm `id`, `seed` (cố định), `tag` (= CHARACTER TAG ở mục 2, dạng tag tiếng Anh), `poses` (p1, p2 → mô tả), `expressions` (theo hồ sơ).
- Ghi spec của series vào `series/<slug>/sprites.spec.json` (chép từ spec.kaggle.json rồi thay `characters`), sau đó build notebook: `python -I pipeline/sprites/build_notebook.py --spec series/<slug>/sprites.spec.json --out series/<slug>/kaggle_sprites.ipynb`.
- Nguyên lý nhất quán: ảnh gốc mỗi pose → biểu cảm chỉ inpaint vùng mặt → nhắm mắt chỉ inpaint dải mắt. `manifest.json` trả tọa độ mặt/mắt/miệng để điền vào `profile.md`; `contact_sheet.jpg` để anh soát tại GATE-SERIES.

## 4. Cách tạo ảnh miễn phí (gợi ý cho anh — kiểm tra điều khoản từng công cụ trước khi dùng)
| Cách | Ưu | Nhược |
|---|---|---|
| **Kaggle Notebook (GPU miễn phí theo hạn mức tuần)** + model anime mã nguồn mở (SDXL anime) + IP-Adapter/ảnh tham chiếu | Tự động hàng loạt, nhất quán cao, chạy theo danh sách | Cần cài đặt lần đầu; tuân thủ điều khoản Kaggle |
| Google Colab miễn phí | Tương tự Kaggle | Phiên ngắn, có thể bị ngắt |
| Máy anh (GTX 1650 4GB) với giao diện SD chế độ VRAM thấp + model SD1.5 anime | Không phụ thuộc mạng | Chậm, SDXL khó chạy, ổ C thiếu chỗ |
| Công cụ web tạo ảnh miễn phí | Không cần cài | Thủ công, khó nhất quán, kiểm tra quyền thương mại |
Quy trình đề xuất: tạo **ảnh tham chiếu chính diện** → anh duyệt → dùng ảnh đó làm tham chiếu (IP-Adapter / image-to-image) cho mọi sprite còn lại.
Tách nền: dùng công cụ xóa nền mã nguồn mở (rembg) chạy cục bộ.

## 5. Đo tọa độ miệng & mắt
Sau khi có sprite, ghi vào `profile.md` → `sprites.poses.<pose>.mouth {x, y, w}` và `eyes {x, y}` (pixel trên ảnh gốc).
Cách đo: mở ảnh bằng trình xem có tọa độ chuột, hoặc nhờ phiên chính đọc ảnh và ước lượng, sau đó kiểm tra bằng lớp debug của `studio/`.

## 6. Casting giọng (A4)
- **Mặc định VieNeu-TTS** (`engine: vieneu`): mỗi nhân vật chọn MỘT giọng mẫu khác nhau trong 25 giọng (liệt kê: `python -I -X utf8 -c "from vieneu import Vieneu; [print(v) for v in Vieneu().list_preset_voices()]"`). Ghi `voice` (tên giọng), `f0_hz` (~210–230 nữ, ~110–130 nam), `ref_dir: series/<slug>/voices/<id>`. Tránh giọng mẫu mang tên trùng người nổi tiếng. Phân vai series đầu: Linh = Trúc Ly, Khải = Hải Đăng, Vy = Ngọc Huyền, Tùng = Adam bựa (đề xuất, chờ anh nghe duyệt).
- Khi có ghi âm diễn cảm (xem `series/<slug>/voices/README.md`): đặt vào `voices/<id>/<emotion>.wav`, không cần sửa gì khác.
- Dự phòng edge-tts: `edge-tts --list-voices` (lọc `vi-VN`).
- Phân vai theo `voice_id` + `rate` + `pitch`. Ví dụ khởi điểm (nghe thử rồi chỉnh):
| Vai | voice_id | rate | pitch |
|---|---|---|---|
| Nữ chính tươi, nhanh | vi-VN-HoaiMyNeural | +8% | +10Hz |
| Nữ phản diện lạnh, chậm | vi-VN-HoaiMyNeural | -6% | -12Hz |
| Nam chính trầm, kiệm lời | vi-VN-NamMinhNeural | -8% | -10Hz |
| Nam phụ vui tính | vi-VN-NamMinhNeural | +12% | +12Hz |
- Mỗi vai thêm **tính cách giọng** (A4.3a): `expressiveness` + 3–4 `signature_emotions` + `emotion_overrides` nếu nhân vật thể hiện một cảm xúc khác thường (ví dụ Khải giận thì trầm và chậm, không to). Gợi ý khởi điểm: Linh 1.2, Khải 0.6, Vy 0.9, Tùng 1.4.
- **Thử giọng** (A4.2a): viết `series/<slug>/voice-tests/cast-audition.json` — mỗi vai 4 câu, mỗi câu một cảm xúc đặc trưng — rồi chạy
  `python -I pipeline/voice.py --lines series/<slug>/voice-tests/cast-audition.json --out series/<slug>/voice-tests/audio`
  và ghép thành `cast-audition.mp3` để anh nghe tại GATE-SERIES. Mẫu có sẵn trong series đầu tiên.

## 7. Bối cảnh
- Ưu tiên bối cảnh **dùng lại nhiều**: bàn làm việc nữ chính, phòng sếp, phòng họp, pantry, thang máy, hành lang, sân thượng, quán cà phê, căn hộ nữ chính, đường phố đêm mưa.
- Mỗi bối cảnh 2 biến thể day/night; tạo khổ lớn hơn 1080×1920 để pan/zoom.
- Không có chữ/logo trong ảnh (V3.12) — biển hiệu nếu cần sẽ do code vẽ.
