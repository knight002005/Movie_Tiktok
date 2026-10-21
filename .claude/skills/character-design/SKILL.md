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
- Liệt kê giọng có sẵn: `edge-tts --list-voices` (lọc `vi-VN`).
- Phân vai theo `voice_id` + `rate` + `pitch`. Ví dụ khởi điểm (nghe thử rồi chỉnh):
| Vai | voice_id | rate | pitch |
|---|---|---|---|
| Nữ chính tươi, nhanh | vi-VN-HoaiMyNeural | +8% | +10Hz |
| Nữ phản diện lạnh, chậm | vi-VN-HoaiMyNeural | -6% | -12Hz |
| Nam chính trầm, kiệm lời | vi-VN-NamMinhNeural | -8% | -10Hz |
| Nam phụ vui tính | vi-VN-NamMinhNeural | +12% | +12Hz |
- Tạo một câu thử cho mỗi vai (câu cửa miệng của nhân vật) để anh nghe trước GATE-SERIES — chỉ khi pipeline TTS đã sẵn sàng.

## 7. Bối cảnh
- Ưu tiên bối cảnh **dùng lại nhiều**: bàn làm việc nữ chính, phòng sếp, phòng họp, pantry, thang máy, hành lang, sân thượng, quán cà phê, căn hộ nữ chính, đường phố đêm mưa.
- Mỗi bối cảnh 2 biến thể day/night; tạo khổ lớn hơn 1080×1920 để pan/zoom.
- Không có chữ/logo trong ảnh (V3.12) — biển hiệu nếu cần sẽ do code vẽ.
