---
id: khai
name: "Khải"
full_name: "Phạm Minh Khải"
age: 29
role: nam chính
subtitle_color: "#8FD3FF"      # xanh băng — độ sáng HSL ~78%
voice:
  engine: vieneu
  voice_id: "Hải Đăng"
  f0_hz: 120
  ref_dir: series/sep-oi-em-khong-co-y/voices/khai
  rate: "-6%"                  # chậm hơn Tùng ~12% (A4.1: hai giọng nam chỉ lệch 10Hz cao độ) → cần nghe lại
  pitch: "+0Hz"
  volume: "+0%"
  expressiveness: 0.6          # kiềm chế, lạnh
  emotion_overrides:
    angry: { rate: -14, pitch: -16, volume: 4, fx: close }       # giận thì CHẬM và TRẦM hơn, không to hơn
    surprised: { rate: -4, pitch: 8, volume: 0 }                 # giật mình nhưng kìm lại, không vọt giọng
    love: { rate: -10, pitch: -4, volume: -8, fx: soft }         # dịu kiểu trầm ấm, không lên giọng
    sad: { rate: -14, pitch: -12, volume: -10, fx: soft }
  signature_emotions: [cold, angry, surprised, love]
sprites:
  base_dir: series/sep-oi-em-khong-co-y/characters/khai/sprites
  height_px: 1800
  poses:
    p1: { desc: "đứng thẳng ¾, tay buông, tư thế ngay ngắn", mouth: { x: 0, y: 0, w: 0 }, eyes: { x: 0, y: 0 } }
    p2: { desc: "khoanh tay trước ngực", mouth: { x: 0, y: 0, w: 0 }, eyes: { x: 0, y: 0 } }
  expressions: [neutral, smile, angry, sad, surprised, embarrassed, cold, cry, love]
status: draft
---

# Khải (Phạm Minh Khải)

## 1. Nhận diện trong 1 giây (R1.D5)
- Dáng & chiều cao: cao nhất dàn (~1m80), vai rộng, **đứng thẳng như thước kẻ**; khi đứng cạnh Linh: scale 1.06.
- Tóc: đen, ngắn, gọn gàng — hình bóng đầu gọn nhất dàn.
- Màu mắt: xám đậm, ánh nhìn sắc.
- Trang phục cố định: **sơ mi trắng, cà vạt xanh navy**, kẹp cà vạt xanh băng, quần âu navy. ep01 có vết cà phê → vẽ đè bằng code (`fx.coffee-stain`), không tạo bộ sprite thứ hai.
- Phụ kiện nhận diện: đồng hồ kim loại bạc; kẹp cà vạt xanh băng.
- Màu chủ đạo: xanh navy + xanh băng.

## 2. Tâm lý
- **Want:** đưa phòng thắng hợp đồng Cú Mất Ngủ; giữ phòng "sạch tin đồn".
- **Need:** hiểu rằng bảo vệ một người là đứng ra minh bạch, nói đủ cả câu, không phải đóng băng và im lặng.
- **Flaw:** kiệm lời đến mức lạnh; kiểm soát; quyết định không giải thích.
- **Bí mật:** (1) giữ tờ giấy nhớ dính cà phê từ ngày đầu Linh đi làm; (2) ba năm trước im lặng để đàn em Trần Thảo bị tin đồn đẩy khỏi công ty.
- **Nỗi sợ:** tình cảm hay sự tử tế của mình làm hại người khác.
- **Điều không bao giờ làm:** không đóng cửa khi gặp riêng nhân viên; không nhắn tin riêng cho nhân viên; không dùng vị trí để xin điều gì cá nhân; không chủ động chạm vào nhân viên.

## 3. Cách nói (R1.E5, R1.E6, A4.3a)
- Tính cách giọng: trầm, chậm, câu cực ngắn, không từ đệm; im một nhịp trước câu quan trọng.
- Cảm xúc thể hiện thế nào: giận → **chậm hơn, trầm hơn, nhỏ đi** chứ không to lên (ngược hẳn Linh). Bất ngờ → khựng lại, ngắt câu bằng "…", không vọt cao giọng. Dịu dàng (ep11–12) → vẫn trầm, chậm, mềm đi; đó là "tan băng" chứ không phải đổi giọng.
- Nhịp nói: chậm, câu 2–5 chữ; khoảng lặng dài.
- Câu cửa miệng: *"Để cửa mở."* · *"Làm lại."*
- Xưng hô mặc định: xem ma trận bible §6.
- 3 câu thoại mẫu:
  1. "Để cửa mở."
  2. "Hết giờ. Làm lại."
  3. "Giờ anh không còn chấm điểm em. … Từ chối cũng được. Công việc vẫn là công việc."

## 4. Arc trong series
- Đầu series: sếp lạnh, phán ngắn, giấu tờ giấy nhớ.
- Midpoint (ep06): bí mật tờ giấy bị Linh phát hiện; ep07 lỡ xưng "em", ep07–08 tự khai báo và rút khỏi việc đánh giá.
- Cuối series: nói đủ cả câu trước cuộc họp (ep11), hỏi rồi chờ câu trả lời; "Anh đợi."

## 5. Prompt tạo hình (giữ y nguyên giữa các lần tạo)
**Character tag:**
```
1boy, solo, adult male, businessman, 29 years old, Vietnamese, tall, broad shoulders, mature face, short neat black hair, sharp dark gray eyes, white dress shirt, navy blue necktie, light ice-blue tie clip, silver metal wristwatch, dark navy trousers
```
**Prompt sprite:**
```
<STYLE chung bible §10>, <character tag>, <POSE>, <EXPRESSION>, half body, upper body, facing viewer, three-quarter view, centered, simple white background
```
- `<POSE>` p1: `standing straight, upright posture, arms at sides`
- `<POSE>` p2: `arms crossed over chest, upright posture`

**Negative:** `<NEGATIVE chung bible §10>` + `1girl, female, glasses, beard, loose necktie`

**Danh sách cần tạo:** 2 pose × 9 biểu cảm × 2 = **36 ảnh** (+ 2 ảnh gốc).
Ghi chú: bible §10 gợi ý Khải cầm ly cà phê; em không làm pose cà phê vì hai khoảnh khắc cà phê của Khải (ep01, ep12) đã do CG đảm nhiệm — xem "điểm cần anh quyết" trong `asset-checklist.md`.

## 6. Ảnh tham chiếu đã duyệt
- refs/p1_base.png — (chưa có)
- refs/p2_base.png — (chưa có)

## Nhật ký sửa
- 2026-10-22T00:10:00+07:00 — casting-designer — tạo hồ sơ; giọng VieNeu "Hải Đăng"; giận kiểu riêng (chậm + trầm).
