---
id: loc-san-thuong
name: "Sân thượng tòa nhà"
variants: [day, dusk]
ambience_sfx: null           # chưa có mã ambience gió/thành phố đã đăng ký (P6.2) — xem điểm cần anh quyết
status: draft
---

# Sân thượng tòa nhà

## Mô tả
- Không gian, vật dụng chính, ánh sáng: sân thượng có lan can kính/thép, chậu cây, một băng ghế, đường chân trời thành phố chung chung (không địa danh thật).
  - `day`: trời xanh trong, mây nhẹ.
  - `dusk`: hoàng hôn cam hồng, giờ vàng, bóng đổ dài.
- Cảm giác / dùng cho loại cảnh nào: thở ra, tâm sự, quyết định; lời hỏi ep11 và câu trả lời mở ep12.
- Chi tiết nhận diện: lan can + bầu trời chiếm nửa trên khung.

## Bố cục cho sprite
- Tầm mắt ở y ≈ 45% (lan can ngang khoảng 50–55%).
- Hai người `left`/`right` nhìn nhau, bầu trời phía sau; băng ghế đặt lệch phải.

## Prompt tạo hình
```
<LOCATION_STYLE bible §10>, rooftop of an office building, metal and glass railing, potted plants, a wooden bench on the right, generic city skyline without landmarks, wide sky in the upper half, <variant>
```
- `day`: `clear blue sky with soft clouds, bright daylight`
- `dusk`: `sunset, golden hour, orange and pink sky, long soft shadows, romantic warm light`

Negative: `<LOCATION_NEGATIVE bible §10>, famous landmark, billboard`

## Tập sử dụng
- ep05, ep09 (`day`); ep11 chiều, ep12 mở tập (`dusk`).
