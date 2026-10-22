# A4 — Âm thanh, giọng đọc, khẩu hình

## A4.1 Casting giọng
- Mỗi nhân vật có **một giọng cố định cho cả series**, khai báo trong hồ sơ nhân vật: `engine`, `voice_id`, `rate`, `pitch`, `volume`.
- Hai nhân vật cùng giới phải phân biệt rõ khi nghe không nhìn (khác cao độ ≥ 15Hz và/hoặc khác tốc độ ≥ 10%, khác cách nói).
- Lời dẫn (narrator) nếu có: giọng riêng, trung tính.

## A4.2 Engine TTS (ngân sách 0 đồng)
| Engine | Ghi chú |
|---|---|
| **VieNeu-TTS v3 Turbo** (`engine: vieneu`, **mặc định**) | Apache-2.0 (code, trọng số, codec MOSS-Audio-Tokenizer-Nano) — thẻ model cho phép dùng trong nội dung thương mại/kiếm tiền. Chạy CPU (~2× thời gian thực trên i7-9750H), 48 kHz. 25 giọng mẫu (nam/nữ, Bắc/Trung/Nam) mà người đọc đã đồng ý cho AI. Clone giọng + **cảm xúc** từ ghi âm mẫu 3–8s (`series/<slug>/voices/<id>/<emotion>.wav`). Không trả mốc thời gian → `pipeline/align.py` (faster-whisper) căn mốc và đo tỷ lệ khớp. Có watermark âm thanh AI (giữ nguyên) |
| edge-tts (`engine: edge`, dự phòng) | Miễn phí; chỉ 2 giọng tiếng Việt (`vi-VN-HoaiMyNeural`, `vi-VN-NamMinhNeural`); có mốc thời gian sẵn. Thư viện không chính thức dùng dịch vụ Microsoft — rủi ro bị chặn/đổi điều khoản |
| Đã loại | F5-TTS Vietnamese (CC-BY-NC-SA), V-TTS (CC BY-NC), XTTS-v2 (giấy phép phi thương mại) — không dùng cho kênh có thể kiếm tiền |
| ElevenLabs và dịch vụ trả phí | **Không dùng** khi chưa được anh cho phép (vi phạm ngân sách 0 đồng) |
- **Không clone giọng người thật** (người nổi tiếng, người quen) khi không có sự đồng ý bằng văn bản.

## A4.2a Thử giọng bắt buộc trước khi chốt
Chất lượng TTS tiếng Việt chênh lệch rất nhiều giữa nhà cung cấp và giữa các giọng. **Không chốt giọng khi chưa nghe thử.**
- Mỗi vai: tạo 5 câu thử từ chính kịch bản/hồ sơ nhân vật — 1 câu bình thường, 1 câu giận, 1 câu buồn/thì thầm, 1 câu hỏi, 1 câu có từ khó (tên riêng, tiếng Anh công sở, số).
- Thử ít nhất 2 engine (nếu có) × vài mức `rate`/`pitch`. Lưu file thử tại `series/<slug>/voice-tests/`.
- Chấm theo thang 1–5: đúng dấu thanh, tự nhiên (không "robot"), thể hiện cảm xúc, phân biệt được với vai khác, đọc đúng từ khó.
- Kết quả ghi vào bible mục 11; **anh nghe và duyệt tại GATE-SERIES**. Giọng < 3/5 ở tiêu chí "đúng dấu thanh" → loại.
- Đổi engine/giọng giữa series chỉ khi bắt buộc (giọng thay đổi làm khán giả mất cảm giác nhân vật).

## A4.3a Giọng theo tính cách và biểu cảm (bắt buộc — không đọc "ngang")
Anh yêu cầu: **giọng không được đều đều như người máy; mỗi nhân vật có tính cách giọng riêng; mỗi câu đọc theo biểu cảm.** Cài đặt trong `pipeline/voice_emotion.py`, mỗi câu dựng từ 3 lớp:
1. **Giọng gốc nhân vật** — `voice_id`, `rate`, `pitch`, `volume` (hồ sơ nhân vật).
2. **Tính cách giọng** — `expressiveness` (0.5 kiềm chế … 1.5 bộc lộ) nhân với độ lệch của cảm xúc; tùy chọn `emotion_overrides` để một nhân vật "giận kiểu riêng" (ví dụ người lạnh lùng giận thì chậm và trầm hơn chứ không to hơn).
3. **Cảm xúc của câu** — `emotion` × `intensity` (1–5) theo bảng: `neutral, smile, happy, panic, angry, cold, sad, cry, embarrassed, surprised, smirk, threat, whisper, love`. Câu được tách theo dấu câu: `?` lên giọng, `!` mạnh lên, `…` chậm và ngập ngừng, có khoảng lặng riêng; kèm hiệu ứng âm (run giọng khi khóc/hoảng, mỏng khi thì thầm, dồn nén khi giận).
- Độ lệch tối đa so với giọng gốc: cao độ ±25Hz, tốc độ ±30%, âm lượng ±35% — vượt quá giọng méo.
- `director` **bắt buộc** điền `line.delivery.emotion` và `intensity` cho mọi câu thoại; không để trống (trống = `neutral` = dễ "ngang").
- Mẫu tính cách khởi điểm: nhân vật bốc đồng 1.2–1.4, điềm tĩnh/lạnh 0.5–0.7, phản diện kiểm soát 0.8–1.0, hài 1.3–1.5.
- **Nguồn cảm xúc, theo thứ tự chất lượng:** (1) ghi âm diễn cảm đúng cảm xúc của người cho giọng (VieNeu clone cả cảm xúc; lớp ngữ điệu tự giảm còn 35%); (2) giọng mẫu VieNeu + lớp ngữ điệu (tempo/pitch bằng rubberband giữ formant, không méo); (3) edge-tts + lớp ngữ điệu.
- **Đã kiểm chứng (2026-10-21):** "tự tạo mẫu cảm xúc" từ giọng mẫu VieNeu KHÔNG hiệu quả (giọng mẫu luôn đọc kiểu trung tính) → cảm xúc thật chỉ đến từ ghi âm người thật diễn. Hướng dẫn thu & mẫu đồng ý: `series/<slug>/voices/README.md`.
- **Kiểm tra phát âm tự động:** mỗi câu VieNeu có `match` (Whisper nghe lại, không gợi ý kịch bản). `match` < 0,85 → đánh dấu "nghe lại" trong thử giọng/QA; Whisper bản nhỏ cũng hay nghe nhầm câu rất ngắn nên cờ là để anh nghe, không tự kết luận là sai.

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
