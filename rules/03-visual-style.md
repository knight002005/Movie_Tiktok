# V3 — Phong cách hình ảnh: Anime Motion Comic / Visual Novel

## V3.1 Định hướng
- Phong cách: **anime 2D hiện đại, cel-shading, nét sạch**, màu tươi sáng; tâm trạng thay đổi bằng ánh sáng/hiệu ứng, không đổi nét vẽ.
- Cách dựng: **sprite nhân vật (PNG nền trong suốt) đặt trên ảnh nền bối cảnh**, chuyển động do code (Remotion) đảm nhiệm: camera, trượt vào/ra, đổi biểu cảm, chớp mắt, nhép miệng, hiệu ứng.
- Toàn bộ hình trong một series phải **cùng một model + cùng style prompt + cùng seed policy** (khóa ở series bible). Không trộn phong cách.

## V3.2 Nhân vật trưởng thành (bắt buộc)
- Mọi nhân vật trong tuyến tình cảm phải **rõ ràng là người trưởng thành (≥ 22 tuổi)**: tỉ lệ cơ thể người lớn, trang phục công sở, gương mặt trưởng thành. Tránh kiểu "chibi", mắt quá to, dáng trẻ con.
- Ghi tuổi trong hồ sơ nhân vật và nhắc trong prompt tạo ảnh ("adult woman, 24 years old, office worker").

## V3.3 Spec sprite nhân vật
| Mục | Quy định |
|---|---|
| Định dạng | PNG, nền trong suốt, sRGB |
| Khung | Nửa người (đầu → hông), chiều cao 1800 px; tùy chọn toàn thân 2400 px |
| Tư thế (pose) | Tối thiểu 2: `p1` đứng thẳng nhìn chính diện ¾, `p2` khoanh tay/chỉ tay/cầm điện thoại (tùy tính cách) |
| Biểu cảm | Tối thiểu 8: `neutral`, `smile`, `angry`, `sad`, `surprised`, `embarrassed` (má hồng), `cold`, `cry`. Tùy chọn: `smirk`, `panic`, `love` |
| Mắt | Mỗi biểu cảm có thêm biến thể **mắt nhắm** (`*_blink.png`) để chớp mắt |
| Miệng | Ảnh gốc vẽ **miệng khép tự nhiên**; miệng nói được vẽ đè bằng code (xem `rules/04-audio-voice.md` A4.4) |
| Mốc tọa độ | Mỗi pose ghi tọa độ `mouth` (x, y, width) và `eyes` trong hồ sơ nhân vật để code đặt lớp miệng/hiệu ứng |
| Đặt tên | `series/<slug>/characters/<id>/sprites/<pose>_<expression>[_blink].png` |
| Nhất quán | Tóc, màu mắt, trang phục, phụ kiện **giống hệt** giữa mọi biểu cảm; sai lệch → tạo lại |

## V3.4 Spec bối cảnh
- Ảnh 1080×1920 trở lên (khuyến nghị 1440×2560 để zoom/pan không vỡ), không có người.
- Mỗi bối cảnh có biến thể `day`, `night` (và `rain` nếu cần).
- Tầm mắt đặt khoảng y ≈ 38–45% để sprite đứng tự nhiên.
- Tên: `series/<slug>/locations/<id>/<id>_<variant>.png`.

## V3.5 Bố cục khung hình
- Tôn trọng safe zone (`rules/02-tiktok-platform.md` T2.2).
- Vị trí sprite: `left` (tâm x≈320), `center` (x≈540), `right` (x≈760). Hai người nói chuyện: trái–phải, nhìn vào nhau.
- Người đang nói được **làm nổi**: sáng hơn, scale 1.03, người nghe tối nhẹ (brightness 0.85).
- Không để phụ đề đè lên mặt.

## V3.6 Ngữ pháp máy quay (dùng trong `scenes.json`)
| Mã `type` | Mô tả | Zoom | Dùng khi |
|---|---|---|---|
| `establishing` | Toàn cảnh bối cảnh, không/ít nhân vật | 1.0 → 1.08 pan chậm | Mở cảnh mới (≤ 1,5s) |
| `two-shot` | Hai nhân vật cùng khung | 1.0–1.15 | Đối thoại, quan hệ |
| `single` | Một nhân vật trung cảnh | 1.2–1.4 | Thoại thường |
| `close-up` | Cận mặt | 1.6–2.0 | Cảm xúc, câu quan trọng |
| `extreme-close-up` | Cận mắt/môi/tay | 2.5–3.2 | Sốc, bí mật, căng thẳng |
| `reaction` | Cận người nghe, không thoại | 1.5–1.8 | Sau câu bom, 0,8–1,5s |
| `insert` | Cận vật thể (ảnh riêng) | — | Nhẫn, tài liệu, tách cà phê |
| `phone-chat` | Màn hình chat dựng bằng code | — | Tin nhắn |
| `phone-call` | Chia đôi màn hình 2 người gọi điện | — | Cuộc gọi |
| `title-card` | Chữ trên nền | — | "3 ngày trước…", end card |
| `flashback` | Như các loại trên + bộ lọc hồi tưởng | — | Ký ức |

Chuyển động camera (`camera.move`): `static`, `push-in` (căng thẳng tăng dần), `pull-out` (cô đơn, tiết lộ bối cảnh), `pan-left`/`pan-right` (chuyển giữa hai người), `quick-zoom` (sốc, ≤ 6 frame), `shake` (va chạm, giận dữ), `dutch` (nghiêng 5–8°, bất an).

## V3.7 Chuyển cảnh
- Mặc định **cắt thẳng (cut)**. `whip` (lia nhanh) khi đổi bối cảnh có năng lượng cao; `flash` (chớp trắng) cho sốc/hồi tưởng; `fade-black` chỉ trước end card hoặc nhảy thời gian lớn.
- Không dùng chuyển cảnh kiểu PowerPoint (xoay, lật trang, cube).

## V3.8 Thư viện hiệu ứng anime (mã `fx.*`)
| Mã | Hiệu ứng | Cảm xúc |
|---|---|---|
| `fx.speed-lines` | Đường tốc độ hướng tâm | Sốc, gấp |
| `fx.shock-flash` | Chớp sáng + rung | Bất ngờ |
| `fx.blush` | Má hồng + vạch chéo | Ngượng |
| `fx.sweat-drop` | Giọt mồ hôi anime | Bối rối, cạn lời |
| `fx.anger-vein` | Gân giận chữ thập | Tức |
| `fx.hearts` | Tim bay | Rung động |
| `fx.sparkle` | Lấp lánh | Ngưỡng mộ, "hào quang" |
| `fx.dark-aura` | Khói tím/đen sau lưng | Đe dọa, ghen |
| `fx.rain-gloom` | Mây đen + mưa nhỏ trên đầu | Buồn, xui |
| `fx.vignette` | Tối viền | Căng thẳng, bí mật |
| `fx.flashback` | Desaturate + grain + viền mờ | Hồi tưởng |
| `fx.freeze-frame` | Đóng băng + viền + chữ tên nhân vật | Giới thiệu nhân vật lần đầu |
Hiệu ứng là gia vị: tối đa **1 hiệu ứng mạnh mỗi 5 giây**.

## V3.9 Phụ đề
- Font **Be Vietnam Pro ExtraBold** (OFL), cỡ 62–72 px, viền đen 6–8 px, bóng nhẹ.
- Tối đa **2 dòng**, ≤ 32 ký tự/dòng; ngắt dòng theo cụm nghĩa.
- **Màu theo nhân vật** (khai báo trong hồ sơ nhân vật) để người xem biết ai nói mà không cần nhìn.
- Hiển thị theo từ (karaoke nhẹ: từ đang đọc sáng hơn) hoặc theo câu; chọn một kiểu cho cả series.
- Lời dẫn (V.O.) và độc thoại nội tâm: chữ nghiêng, nền mờ.
- Tin nhắn chat không cần phụ đề.

## V3.10 Màn hình điện thoại / chat
- Giao diện chat **hư cấu**, không sao chép giao diện Messenger/Zalo/Telegram (T2.5).
- Tên liên hệ có thể có emoji tính cách ("Sếp Khải 🧊"). Có trạng thái "đang nhập…", "Đã xem" để tạo kịch tính.

## V3.11 Nhận diện kênh
- Watermark kênh nhỏ (≤ 6% chiều rộng), góc trên trái trong safe zone, độ mờ 60%.
- End card thống nhất cho cả series.

## V3.12 Cấm
- Hở hang, góc máy khêu gợi, tập trung vào bộ phận cơ thể.
- Máu, vết thương chi tiết.
- Logo/thương hiệu thật, người thật, địa danh nhạy cảm.
- Chữ do AI vẽ trong ảnh (thường sai chính tả) → mọi chữ trên màn hình phải do code vẽ.
