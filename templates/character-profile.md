---
id: <char-id>
name: "<Tên hiển thị>"
age: <≥22 nếu trong tuyến tình cảm>
role: <nữ chính | nam chính | phản diện | phụ>
subtitle_color: "#RRGGBB"
voice:
  engine: edge-tts
  voice_id: vi-VN-HoaiMyNeural
  rate: "+0%"
  pitch: "+0Hz"
  volume: "+0%"
sprites:
  base_dir: series/<slug>/characters/<char-id>/sprites
  height_px: 1800
  poses:
    p1: { desc: "<đứng ¾, tay buông>", mouth: { x: 0, y: 0, w: 0 }, eyes: { x: 0, y: 0 } }
    p2: { desc: "<khoanh tay / cầm điện thoại>", mouth: { x: 0, y: 0, w: 0 }, eyes: { x: 0, y: 0 } }
  expressions: [neutral, smile, angry, sad, surprised, embarrassed, cold, cry]
status: draft          # draft | approved
---

# <Tên nhân vật>

## 1. Nhận diện trong 1 giây (R1.D5)
- Dáng & chiều cao:
- Tóc:
- Màu mắt:
- Trang phục cố định:
- Phụ kiện nhận diện:
- Màu chủ đạo:

## 2. Tâm lý
- **Want** (muốn gì ngoài mặt):
- **Need** (thật sự cần gì):
- **Flaw** (khuyết điểm gây rắc rối):
- **Bí mật**:
- **Nỗi sợ**:
- **Điều không bao giờ làm** (giữ nhất quán R1.D4):

## 3. Cách nói (R1.E5, R1.E6)
- Nhịp nói: <nhanh/chậm, câu dài/ngắn>
- Câu cửa miệng / từ đệm:
- Xưng hô mặc định: xem ma trận trong bible
- 3 câu thoại mẫu thể hiện giọng nhân vật:
  1.
  2.
  3.

## 4. Arc trong series
- Đầu series:
- Midpoint (ep06):
- Cuối series:

## 5. Prompt tạo hình (giữ y nguyên giữa các lần tạo)
**Mô tả cố định (character tag):**
```
<adult woman, 24 years old, office worker, shoulder-length dark brown hair with side bangs, ...>
```
**Prompt sprite (thay <POSE> và <EXPRESSION>):**
```
<style prompt chung của series>, <character tag>, half body, <POSE>, <EXPRESSION> expression, mouth closed, plain white background, centered, full color, clean lineart
```
**Negative:**
```
<negative chung>, child, chibi, nsfw, revealing clothes, text, watermark, extra fingers, deformed hands
```
**Danh sách cần tạo:** pose × biểu cảm × (thường + nhắm mắt) = <số> ảnh.

## 6. Ảnh tham chiếu đã duyệt
- refs/front.png — <ngày duyệt>
- refs/three-quarter.png — <ngày duyệt>

## Nhật ký sửa
- <ngày> — <thay đổi>
