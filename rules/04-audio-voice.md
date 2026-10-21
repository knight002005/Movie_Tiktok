# A4 — Âm thanh, giọng đọc, khẩu hình

## A4.1 Casting giọng
- Mỗi nhân vật có **một giọng cố định cho cả series**, khai báo trong hồ sơ nhân vật: `engine`, `voice_id`, `rate`, `pitch`, `volume`.
- Hai nhân vật cùng giới phải phân biệt rõ khi nghe không nhìn (khác cao độ ≥ 15Hz và/hoặc khác tốc độ ≥ 10%, khác cách nói).
- Lời dẫn (narrator) nếu có: giọng riêng, trung tính.

## A4.2 Engine TTS (ngân sách 0 đồng)
| Engine | Ghi chú |
|---|---|
| **edge-tts** (mặc định) | Miễn phí; giọng `vi-VN-HoaiMyNeural` (nữ), `vi-VN-NamMinhNeural` (nam); hỗ trợ `rate`, `pitch`, `volume`; trả mốc thời gian theo từ (WordBoundary). Là thư viện không chính thức dùng dịch vụ của Microsoft — rủi ro bị chặn/đổi điều khoản; giữ engine sau một lớp adapter để thay được |
| TTS tiếng Việt mã nguồn mở chạy cục bộ | Phương án dự phòng / thêm giọng (có thể clone giọng mẫu **có quyền sử dụng**). Cần đánh giá chất lượng & tốc độ trên GTX 1650 trước khi dùng |
| ElevenLabs và dịch vụ trả phí | **Không dùng** khi chưa được anh cho phép (vi phạm ngân sách 0 đồng) |
- **Không clone giọng người thật** (người nổi tiếng, người quen) khi không có sự đồng ý bằng văn bản.

## A4.2a Thử giọng bắt buộc trước khi chốt
Chất lượng TTS tiếng Việt chênh lệch rất nhiều giữa nhà cung cấp và giữa các giọng. **Không chốt giọng khi chưa nghe thử.**
- Mỗi vai: tạo 5 câu thử từ chính kịch bản/hồ sơ nhân vật — 1 câu bình thường, 1 câu giận, 1 câu buồn/thì thầm, 1 câu hỏi, 1 câu có từ khó (tên riêng, tiếng Anh công sở, số).
- Thử ít nhất 2 engine (nếu có) × vài mức `rate`/`pitch`. Lưu file thử tại `series/<slug>/voice-tests/`.
- Chấm theo thang 1–5: đúng dấu thanh, tự nhiên (không "robot"), thể hiện cảm xúc, phân biệt được với vai khác, đọc đúng từ khó.
- Kết quả ghi vào bible mục 11; **anh nghe và duyệt tại GATE-SERIES**. Giọng < 3/5 ở tiêu chí "đúng dấu thanh" → loại.
- Đổi engine/giọng giữa series chỉ khi bắt buộc (giọng thay đổi làm khán giả mất cảm giác nhân vật).

## A4.3 Diễn xuất bằng TTS
- Cảm xúc thể hiện qua: dấu câu (`…`, `!`, `?`), độ dài câu, `rate` (+10–20% khi gấp/giận, -10–15% khi buồn/lạnh), `pitch` (±5–15Hz), khoảng lặng.
- Trường `delivery` trong `scenes.json` mô tả cảm xúc; pipeline chuyển thành tham số TTS theo bảng ánh xạ trong `pipeline/`.
- Khoảng lặng giữa các câu: 150–300 ms (đối thoại nhanh), 400–800 ms (sau câu bom, trước phản ứng). Cãi nhau có thể chồng nhẹ 100–200 ms.
- Từ dễ đọc sai (tên riêng, tiếng Anh, viết tắt, số) → ghi cách đọc trong `pronunciation` của series bible.

## A4.4 Khẩu hình (lip-sync bằng code)
Miệng nói được vẽ bằng code (SVG) đè lên vùng `mouth` của sprite, điều khiển bởi **mốc thời gian từng từ** + **âm lượng (RMS) theo khung hình**.

| Hình miệng | Mã | Khi nào |
|---|---|---|
| Nghỉ / khép | `X` | Âm lượng dưới ngưỡng, giữa các câu |
| Mím môi | `M` | Âm đầu `m`, `b`, `p`; âm cuối `-m`, `-p` (2–3 frame cuối âm tiết) |
| Mở rộng | `A` | Nguyên âm chính `a`, `ă`, `â`, `oa`, `ai`, `ao` |
| Tròn | `O` | `o`, `ô`, `u`, `uô`, `ôi`, `ui` |
| Dẹt | `E` | `e`, `ê`, `i`, `y`, `iê`, `ia` |
| Hé | `H` | `ơ`, `ư`, `ươ` và mặc định khi không xác định |

Quy tắc chạy:
- Mỗi âm tiết: hình miệng theo nguyên âm chính chiếm ~70% thời lượng, sau đó về `M` (nếu âm cuối m/p) hoặc `H`.
- Độ mở miệng nhân thêm theo RMS (0.6–1.0) để câu hét mở to hơn câu thì thầm.
- Không đổi hình miệng nhanh hơn mỗi 2 frame (tránh rung giật).
- Người **không nói** luôn ở `X`. Chớp mắt ngẫu nhiên mỗi 2,5–5 giây, mỗi lần 4–6 frame.

## A4.5 Âm lượng & mix
- Đầu ra cuối: **-14 LUFS**, true peak ≤ -1 dBTP (T2.1).
- Thoại là ưu tiên số 1. Nhạc nền thấp hơn thoại 12–18 dB và **tự động hạ (ducking)** khi có thoại.
- SFX không át thoại; SFX va chạm có thể vượt nhạc nhưng ≤ thoại +3 dB.

## A4.6 Nhạc
- Chỉ dùng nhạc miễn phí bản quyền, ghi nguồn tại `assets/LICENSES.md` (T2.5). Hoặc xuất bản không nhạc và chọn âm thanh trong app TikTok.
- Thư viện nhạc theo cảm xúc: `tension`, `romance`, `comedy`, `sad`, `villain`, `reveal`. Mỗi cảm xúc 2–3 bài dùng lại suốt series để tạo "chủ đề âm nhạc".
- Đổi nhạc đúng nhịp lật (beat), không đổi giữa câu thoại.

## A4.7 SFX
- Thư viện mã `sfx.*` (ví dụ: `sfx.elevator-ding`, `sfx.coffee-splash`, `sfx.door`, `sfx.phone-vibrate`, `sfx.message-pop`, `sfx.typing`, `sfx.whoosh`, `sfx.impact`, `sfx.heartbeat`, `sfx.crowd-gasp`, `sfx.office-ambience`).
- Mỗi bối cảnh có âm nền (ambience) nhẹ, -30 dB.
- Hiệu ứng hình mạnh (`fx.shock-flash`, `quick-zoom`) nên đi kèm SFX tương ứng.

## A4.8 Im lặng có chủ đích
- Trước câu bom hoặc tiết lộ: cắt nhạc 0,3–0,6 giây. Im lặng là một công cụ, không phải lỗi.
