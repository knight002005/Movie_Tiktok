---
id: loc-thang-may
name: "Thang máy & sảnh thang máy tầng 15"
variants: [day, lobby]
ambience_sfx: null           # chưa có mã ambience thang máy đã đăng ký; dùng sfx.elevator-ding theo shot
status: draft
---

# Thang máy & sảnh thang máy tầng 15

## Mô tả
- Không gian, vật dụng chính, ánh sáng:
  - `day` — trong cabin: vách inox xước, vách sau là gương, đèn trần ấm, bảng nút bấm **không có số** (số tầng nếu cần do code vẽ), cửa thép đóng.
  - `lobby` — sảnh chờ tầng 15: hai cửa thang máy inox, sàn đá sáng, chậu cây, ánh sáng ban ngày từ cửa sổ cuối hành lang.
- Cảm giác / dùng cho loại cảnh nào: không gian hẹp, ép hai người đứng gần → va chạm, oan gia; đối xứng mở – kết series.
- Chi tiết nhận diện: vách inox + gương, cửa thép hai cánh.

## Bố cục cho sprite
- Tầm mắt ở y ≈ 40% chiều cao ảnh.
- `day`: cabin hẹp — hai người đứng `left` và `right`, sát vách; tránh `center` vì gương sau lưng (sprite không có ảnh phản chiếu, gương nên để mờ/đặt ở phần trên).
- `lobby`: `left`/`center`/`right` đều được; cửa thang máy ở giữa làm hậu cảnh.

## Prompt tạo hình
```
<LOCATION_STYLE bible §10>, modern office building on the 15th floor, clean contemporary interior, <variant>
```
- `day`: `inside a spacious elevator cabin, brushed stainless steel walls, softly blurred mirrored back wall, warm ceiling lights, button panel without numbers, closed steel doors, bright morning`
- `lobby`: `elevator lobby hallway, two closed brushed steel elevator doors, blank floor indicator, light marble floor, potted plant, soft daylight from a window at the end of the hallway`

Negative: `<LOCATION_NEGATIVE bible §10>, reflection of a person`

## Tập sử dụng
- ep01 (va chạm cà phê, CG `cg-ep01-ca-phe`), ep12 (thang máy cuối, CG `cg-ep12-thang-may`).
