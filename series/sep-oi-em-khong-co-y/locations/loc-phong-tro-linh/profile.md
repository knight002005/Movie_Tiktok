---
id: loc-phong-tro-linh
name: "Phòng trọ của Linh"
variants: [night]
ambience_sfx: null           # chưa có mã ambience phòng đã đăng ký
optional: true               # bible §9: chỉ tạo khi screenwriter thực sự dùng
status: draft
---

# Phòng trọ của Linh (tùy chọn)

## Mô tả
- Không gian, vật dụng chính, ánh sáng: phòng trọ nhỏ gọn, giường đơn chăn vàng, bàn nhỏ có laptop và giấy nhớ vàng (trống), dây đèn trang trí, cửa sổ nhìn thành phố đêm; ấm áp nhưng chật.
  - `night`: đèn bàn vàng + dây đèn, ngoài cửa sổ xanh tím.
- Cảm giác / dùng cho loại cảnh nào: một mình, suy nghĩ lại, độc thoại.
- Chi tiết nhận diện: chăn vàng + giấy nhớ trên bàn (màu của Linh).

## Bố cục cho sprite
- Tầm mắt ở y ≈ 42%.
- Linh đứng/ngồi `center`; bàn ở trái, giường ở phải.

## Prompt tạo hình
```
<LOCATION_STYLE bible §10>, small cozy rented studio room, single bed with a yellow blanket on the right, small desk with a closed laptop and blank yellow sticky notes on the left, string lights on the wall, window with a night city view, <variant>
```
- `night`: `night, warm desk lamp and string lights, blue and purple city glow outside the window, quiet lonely mood`

Negative: `<LOCATION_NEGATIVE bible §10>, posters with writing`

## Tập sử dụng
- ep08 (tùy chọn).
