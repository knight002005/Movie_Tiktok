---
id: vy
name: "Vy"
full_name: "Lê Hoàng Vy"
age: 27
role: phản diện
subtitle_color: "#FF7A9A"      # hồng đỏ — độ sáng HSL ~74%
voice:
  engine: vieneu
  voice_id: "Ngọc Huyền"
  f0_hz: 200                   # thấp hơn Linh 20Hz (A4.1 ≥ 15Hz)
  ref_dir: series/sep-oi-em-khong-co-y/voices/vy
  rate: "-5%"                  # chậm, ngọt, kéo dài cuối câu — chậm hơn Linh ~10% → cần nghe lại
  pitch: "+0Hz"
  volume: "+0%"
  expressiveness: 0.9          # phản diện kiểm soát
  emotion_overrides:
    smile: { rate: -8, pitch: 8, volume: 0 }                     # ngọt ngào: chậm lại, kéo dài "nha", "em à"
    angry: { rate: 12, pitch: -8, volume: 18, fx: angry }        # lộ mặt: câu cụt, sắc, nhanh — không gào
  signature_emotions: [smile, smirk, threat, cry]
sprites:
  base_dir: series/sep-oi-em-khong-co-y/characters/vy/sprites
  height_px: 1800
  poses:
    p1: { desc: "đứng thanh lịch, hai tay ôm máy tính bảng trước ngực", mouth: { x: 0, y: 0, w: 0 }, eyes: { x: 0, y: 0 } }
    p2: { desc: "một tay chống hông, tay kia cầm máy tính bảng buông bên người", mouth: { x: 0, y: 0, w: 0 }, eyes: { x: 0, y: 0 } }
  expressions: [neutral, smile, angry, sad, surprised, embarrassed, cold, cry, smirk, panic]
status: draft
---

# Vy (Lê Hoàng Vy)

## 1. Nhận diện trong 1 giây (R1.D5)
- Dáng & chiều cao: ~1m63, dáng thẳng, thanh lịch; vai blazer đứng phom.
- Tóc: **đen, dài quá vai, uốn sóng nhẹ**, mái lệch — hình bóng duy nhất có tóc xõa dài.
- Màu mắt: nâu đậm.
- Trang phục cố định: **blazer đỏ rượu**, sơ mi lụa tím oải hương, chân váy bút chì đen dài đến gối.
- Phụ kiện nhận diện: khuyên tai ngọc trai; **luôn cầm máy tính bảng** (màn hình quay đi, mọi nội dung màn hình do code vẽ).
- Màu chủ đạo: đỏ rượu + tím.

## 2. Tâm lý
- **Want:** lên phó phòng quý này; được Khải công nhận.
- **Need:** tin vào năng lực của mình mà không phải hạ người khác; buông người không thuộc về mình.
- **Flaw:** so sánh, kiểm soát; thao túng bằng nửa sự thật.
- **Bí mật:** (1) từng tỏ tình với Khải, bị từ chối; (2) xóa file của Linh (ep05); (3) lấy trang 1 lá đơn của Khải, cắt ảnh, tung tin ẩn danh (ep08–09).
- **Nỗi sợ:** bị thay thế; 5 năm công sức thành vô nghĩa.
- **Điều không bao giờ làm:** không nói dối trắng trợn, chỉ nói một nửa — mọi câu đều đúng về mặt chữ.

## 3. Cách nói (R1.E5, R1.E6, A4.3a)
- Tính cách giọng: ngọt, chậm, kéo dài cuối câu ("nha", "em à"); khi lộ mặt thì câu cụt, sắc.
- Cảm xúc thể hiện thế nào: đe dọa → chậm, nhỏ, sát tai (không to). Giận khi lộ mặt → nhanh, cụt, sắc, có lực nhưng không gào. Khóc (ep08 hồi ức, ep11) → run, vỡ ngọt. Khác Linh: Linh giận thì to và vội; Vy giận thì gọn và lạnh.
- Nhịp nói: chậm vừa, câu ngọt dài; câu lộ mặt cực ngắn.
- Câu cửa miệng: *"Chị chỉ muốn tốt cho em thôi."* · tự bào chữa *"Chị có nói sai câu nào đâu?"*
- Xưng hô mặc định: xem ma trận bible §6.
- 3 câu thoại mẫu:
  1. "Chị dọn giúp rồi. Mai mười giờ họp nhóm nha."
  2. "Chị nói mười giờ họp nhóm mà em."
  3. "Cô chỉ là một sự cố biết đi!"

## 4. Arc trong series
- Đầu series: "chị kèm em" ngọt ngào, ngấm ngầm gài bẫy bằng nửa sự thật.
- Midpoint (ep06): phương án dự phòng hết cửa, cứng mặt; ep08–09 leo thang (lấy đơn, cắt ảnh).
- Cuối series: vỡ trận ở ep11, mất đề cử, chuyển nhóm; ep12 xin lỗi nói đủ cả câu.

## 5. Prompt tạo hình (giữ y nguyên giữa các lần tạo)
**Character tag:**
```
1girl, solo, adult woman, office lady, 27 years old, Vietnamese, elegant, mature face, long softly wavy black hair falling past shoulders, side-swept bangs, dark brown eyes, wine red tailored blazer, lavender silk blouse, black knee-length pencil skirt, pearl stud earrings
```
**Prompt sprite:**
```
<STYLE chung bible §10>, <character tag>, <POSE>, <EXPRESSION>, half body, upper body, facing viewer, three-quarter view, centered, simple white background
```
- `<POSE>` p1: `standing elegantly, holding a tablet computer against her chest with both arms, tablet screen facing away`
- `<POSE>` p2: `one hand on hip, other hand holding a tablet computer at her side, confident posture`

**Negative:** `<NEGATIVE chung bible §10>` + `1boy, male, ponytail, short hair`

**Danh sách cần tạo:** 2 pose × 10 biểu cảm × 2 = **40 ảnh** (+ 2 ảnh gốc).

## 6. Ảnh tham chiếu đã duyệt
- refs/p1_base.png — (chưa có)
- refs/p2_base.png — (chưa có)

## Nhật ký sửa
- 2026-10-22T00:10:00+07:00 — casting-designer — tạo hồ sơ; giọng VieNeu "Ngọc Huyền"; giận kiểu riêng (cụt, sắc).
