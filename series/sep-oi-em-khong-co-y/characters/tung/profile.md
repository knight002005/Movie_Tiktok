---
id: tung
name: "Tùng"
full_name: "Đỗ Thanh Tùng"
age: 27
role: phụ (bạn thân nữ chính)
subtitle_color: "#9BE15D"      # xanh lá chuối — độ sáng HSL ~62%
voice:
  engine: vieneu
  voice_id: "Adam bựa"         # tên giọng mẫu có chữ "bựa" — chỉ là tên kỹ thuật, không xuất hiện trên màn hình
  f0_hz: 130
  ref_dir: series/sep-oi-em-khong-co-y/voices/tung
  rate: "+6%"                  # nhanh hơn Khải ~12% (A4.1) → cần nghe lại
  pitch: "+0Hz"
  volume: "+0%"
  expressiveness: 1.4          # hài, bộc lộ
  emotion_overrides:
    embarrassed: { rate: 14, pitch: 10, volume: -4 }             # ngượng thì nói lấp liếm, nhanh
    cold: { rate: -6, pitch: -6, volume: 2 }                     # "nghiêm túc" của Tùng (ep10–11) — trầm lại nhẹ, không băng giá như Khải
  signature_emotions: [happy, panic, embarrassed, cold]
sprites:
  base_dir: series/sep-oi-em-khong-co-y/characters/tung/sprites
  height_px: 1800
  poses:
    p1: { desc: "đứng thả lỏng, hai tay đút túi trước áo hoodie, hơi khom", mouth: { x: 0, y: 0, w: 0 }, eyes: { x: 0, y: 0 } }
    p2: { desc: "một tay cầm điện thoại ngang ngực, màn hình quay đi", mouth: { x: 0, y: 0, w: 0 }, eyes: { x: 0, y: 0 } }
  expressions: [neutral, smile, angry, sad, surprised, embarrassed, cold, cry, panic, smirk]
status: draft
---

# Tùng (Đỗ Thanh Tùng)

## 1. Nhận diện trong 1 giây (R1.D5)
- Dáng & chiều cao: ~1m72, **dáng thả lỏng, hơi khom**; hình bóng tròn, phồng (hoodie + tai nghe).
- Tóc: **nâu sáng nhuộm, rối bồng** — tóc sáng màu nhất dàn.
- Màu mắt: nâu, ánh mắt thân thiện.
- Trang phục cố định: **hoodie xanh lá chuối**, áo thun cam nhạt bên trong.
- Phụ kiện nhận diện: tai nghe chụp tai màu đen đeo cổ; bút vẽ (stylus) gài trên tai.
- Màu chủ đạo: xanh lá chuối + cam nhạt.

## 2. Tâm lý
- **Want:** mọi người vui, không ai giận ai; "thuyền" Linh – Khải cập bến; được Vy nhìn thấy mình.
- **Need:** dám chọn phe và nói sự thật dù mất lòng người mình quý.
- **Flaw:** né va chạm, đùa để trốn chuyện nghiêm túc; vô tư chụp và chia sẻ, thiếu ý thức riêng tư.
- **Bí mật:** (1) thầm thích Vy; (2) thấy Vy ngồi ở máy Linh đêm file bị xóa nhưng im lặng.
- **Nỗi sợ:** mất người bạn thân nhất từ ngày vào công ty (Vy).
- **Điều không bao giờ làm:** không để ai ăn trưa một mình.

## 3. Cách nói (R1.E5, R1.E6, A4.3a)
- Tính cách giọng: nhanh, tưng tửng, nhiều nhạc tính; so sánh hài. Lúc nghiêm túc hiếm hoi thì trầm lại và chậm, khiến người nghe giật mình.
- Cảm xúc thể hiện thế nào: hoảng → nhanh, cao, lặp từ ("Chết rồi, chết rồi!"). Ngượng → lấp liếm nhanh. Nghiêm túc (ep10) → giọng hạ xuống, câu ngắn, không đùa.
- Nhịp nói: nhanh, câu dài vừa, hay mở bằng "Nói thật nhé…" khi sắp nói dối hoặc nói tránh.
- Câu cửa miệng: *"Thuyền này tôi chèo!"* · "Nói thật nhé…" · "Bà lại bỏ bữa à?"
- Xưng hô mặc định: xem ma trận bible §6.
- 3 câu thoại mẫu:
  1. "Thuyền này tôi chèo!"
  2. "Tôi sẽ nói, kể cả với Vy."
  3. "Tôi vẫn ở đây."

## 4. Arc trong series
- Đầu series: "đội trưởng đẩy thuyền", chụp và chia sẻ vô tư.
- Midpoint (ep06): suýt nói sự thật thì bị Vy kéo đi.
- Cuối series: thú nhận, xin lỗi Linh (ep10), làm chứng bằng hình (ep11), ở bên Vy với tư cách bạn (ep12).

## 5. Prompt tạo hình (giữ y nguyên giữa các lần tạo)
**Character tag:**
```
1boy, solo, adult male, 27 years old, Vietnamese, graphic designer, average height, mature face, messy fluffy light brown dyed hair, friendly brown eyes, lime green hoodie with light orange t-shirt underneath, black over-ear headphones around neck, stylus pen tucked behind ear
```
**Prompt sprite:**
```
<STYLE chung bible §10>, <character tag>, <POSE>, <EXPRESSION>, half body, upper body, facing viewer, three-quarter view, centered, simple white background
```
- `<POSE>` p1: `standing relaxed, both hands in hoodie front pocket, slightly slouched`
- `<POSE>` p2: `holding a smartphone in one hand at chest height, phone screen facing away from viewer`

**Negative:** `<NEGATIVE chung bible §10>` + `1girl, female, necktie, suit, glasses`

**Danh sách cần tạo:** 2 pose × 10 biểu cảm × 2 = **40 ảnh** (+ 2 ảnh gốc).

## 6. Ảnh tham chiếu đã duyệt
- refs/p1_base.png — (chưa có)
- refs/p2_base.png — (chưa có)

## Nhật ký sửa
- 2026-10-22T00:10:00+07:00 — casting-designer — tạo hồ sơ; giọng VieNeu "Adam bựa"; "cold" của Tùng được hạ nhẹ thành "nghiêm túc".
