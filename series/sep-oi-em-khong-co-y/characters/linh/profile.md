---
id: linh
name: "Linh"
full_name: "Nguyễn Gia Linh"
age: 24
role: nữ chính
subtitle_color: "#FFD84D"      # vàng giấy nhớ — độ sáng HSL ~65%, đủ tương phản trên viền đen
voice:
  engine: vieneu
  voice_id: "Trúc Ly"          # giọng mẫu VieNeu (khi gọi pipeline/voice.py: trường "voice")
  f0_hz: 220                   # cao độ trung bình giọng mẫu, dùng đổi Hz → tỉ lệ pitch
  ref_dir: series/sep-oi-em-khong-co-y/voices/linh
  rate: "+5%"                  # Linh nói nhanh hơn Vy ~10% (A4.1); thử giọng cũ chạy ở +0% → cần nghe lại
  pitch: "+0Hz"
  volume: "+0%"
  expressiveness: 1.2          # bốc đồng, cảm xúc lộ hết ra mặt
  emotion_overrides:
    angry: { rate: 16, pitch: 8, volume: 22, fx: angry }        # giận kiểu bật lại: nhanh, cao, to — khác Khải (trầm) và Vy (cụt, sắc)
    embarrassed: { rate: 10, pitch: 12, volume: -6 }             # ngượng thì nói nhanh, lí nhí, lên giọng
    cold: { rate: -16, pitch: -12, volume: -8 }                  # ep09 "Tôi hiểu rồi, anh Khải." — lạnh khác thường, chậm hẳn
  signature_emotions: [panic, angry, embarrassed, sad]
sprites:
  base_dir: series/sep-oi-em-khong-co-y/characters/linh/sprites
  height_px: 1800
  poses:
    p1: { desc: "đứng ¾, tay buông, người hơi đổ về trước (năng động)", mouth: { x: 0, y: 0, w: 0 }, eyes: { x: 0, y: 0 } }
    p2: { desc: "hai tay cầm ly cà phê giấy trước ngực", mouth: { x: 0, y: 0, w: 0 }, eyes: { x: 0, y: 0 } }
  expressions: [neutral, smile, angry, sad, surprised, embarrassed, cold, cry, panic, love]
status: draft
---

# Linh (Nguyễn Gia Linh)

## 1. Nhận diện trong 1 giây (R1.D5)
- Dáng & chiều cao: tầm trung (~1m58), dáng nhanh nhẹn, người hơi đổ về trước như sắp lao đi. Khi đứng cạnh Khải: Linh scale 1.00, Khải 1.06.
- Tóc: nâu sẫm, **buộc đuôi ngựa cao**, mái lệch; **một cây bút chì vàng cài ở dây buộc tóc** → hình bóng đỉnh đầu khác hẳn ba người còn lại.
- Màu mắt: nâu ấm.
- Trang phục cố định: **cardigan vàng mù tạt** khoác ngoài sơ mi kem, chân váy be dài đến gối.
- Phụ kiện nhận diện: mấy tờ giấy nhớ vàng (trống, không chữ) dán ở mép cardigan; bút chì trên tóc.
- Màu chủ đạo: vàng giấy nhớ + kem.

## 2. Tâm lý
- **Want:** qua 2 tháng thử việc; khẩu hiệu viết trên giấy nhớ ngày đầu được chọn cho Cú Mất Ngủ.
- **Need:** thôi tự coi mình là "sự cố"; tin vào giá trị bản thân và hành động có chủ đích thay vì xin lỗi rồi bỏ chạy.
- **Flaw:** bốc đồng, nói trước nghĩ sau; hậu đậu; bị phủ nhận là muốn bỏ cuộc ngay (xin lỗi quá nhiều, viết đơn nghỉ).
- **Bí mật:** (1) từng trượt thử việc ở công ty trước sau 3 tuần; (2) hay vẽ biếm họa "Sếp Tủ Lạnh" lên giấy nhớ.
- **Nỗi sợ:** bị coi là gánh nặng, "sự cố biết đi"; trượt thử việc lần thứ hai.
- **Điều không bao giờ làm:** không đổ lỗi khi không có bằng chứng, kể cả khi biết rõ ai hại mình.

## 3. Cách nói (R1.E5, R1.E6, A4.3a)
- Tính cách giọng: nói nhanh, sáng, cảm xúc lộ hết; giận thì bật lại to và nhanh, ngượng thì lí nhí và vội.
- Cảm xúc thể hiện thế nào: giận → nhanh, cao, to (khác Khải trầm xuống và Vy cụt, sắc). Buồn → chậm, nhỏ, hay bỏ lửng "…". Ngượng → nói dồn, cuối câu lên giọng. Lạnh (chỉ ep09–11) → chậm hẳn, phẳng, trái ngược tính cách nên rất "đau".
- Nhịp nói: nhanh, câu cảm thán ngắn; hay mở bằng "Ơ…", chốt bằng "Thôi xong."
- Câu cửa miệng / từ đệm: *"Em không cố ý mà!"*, "Ơ…", "Thôi xong."
- Xưng hô mặc định: xem ma trận bible §6.
- 3 câu thoại mẫu:
  1. "Em không cố ý mà!"
  2. "Em hay gây sự cố thật. Nhưng em chưa từng cố ý hại ai."
  3. "Sếp ơi… à không. Anh Khải. Lần này em cố ý."

## 4. Arc trong series
- Đầu series: "sự cố biết đi", gặp chuyện là xin lỗi rồi muốn bỏ chạy.
- Midpoint (ep06): dựng lại ý tưởng từ chính cái "tật" dán giấy khắp nơi; phát hiện tờ giấy nhớ trong sổ Khải → rung động.
- Cuối series: vò đơn nghỉ việc (ep10), tự gỡ oan (ep11), chủ động trả lời và hẹn: *"Lần này em cố ý."*

## 5. Prompt tạo hình (giữ y nguyên giữa các lần tạo)
**Character tag (khóa, chép y nguyên trong `sprites.spec.json`):**
```
1girl, solo, adult woman, office lady, 24 years old, Vietnamese, medium height, mature face, dark brown hair in a high ponytail, a yellow pencil stuck in her hair tie, side bangs, warm brown eyes, mustard yellow cardigan over cream blouse, beige knee-length skirt, small blank yellow sticky notes stuck on cardigan hem
```
**Prompt sprite (thay <POSE> và <EXPRESSION>):**
```
<STYLE chung bible §10>, <character tag>, <POSE>, <EXPRESSION>, half body, upper body, facing viewer, three-quarter view, centered, simple white background
```
- `<POSE>` p1: `standing, arms relaxed at sides, leaning slightly forward, energetic posture`
- `<POSE>` p2: `holding a plain paper coffee cup with both hands near chest`

**Negative:** `<NEGATIVE chung bible §10>` + `1boy, male, beard`

**Danh sách cần tạo:** 2 pose × 10 biểu cảm × (thường + nhắm mắt) = **40 ảnh** (+ 2 ảnh gốc `refs/p1_base.png`, `refs/p2_base.png` để duyệt).

## 6. Ảnh tham chiếu đã duyệt
- refs/p1_base.png — (chưa có)
- refs/p2_base.png — (chưa có)

## Nhật ký sửa
- 2026-10-22T00:10:00+07:00 — casting-designer — tạo hồ sơ từ bible v2; giọng VieNeu "Trúc Ly"; tag hình theo cột "nhận diện 1 giây" bible §4b.
