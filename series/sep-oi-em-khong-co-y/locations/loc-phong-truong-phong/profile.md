---
id: loc-phong-truong-phong
name: "Phòng trưởng phòng"
variants: [day, night]
ambience_sfx: sfx.office-ambience
status: draft
---

# Phòng trưởng phòng (phòng Khải)

## Mô tả
- Không gian, vật dụng chính, ánh sáng: phòng riêng vách kính, **cửa luôn mở toang** (thấy rõ khung cửa mở), tối giản tông trắng – navy; bàn lớn với hồ sơ xếp ngay ngắn và một cuốn sổ bìa đen; **đồng hồ treo tường không số**; **máy in nhỏ trên tủ thấp** cạnh bàn; cửa sổ nhìn thành phố. Ám xanh băng (bible §3).
  - `day`: sáng, trong, lạnh, xanh băng.
  - `night`: đèn bàn vàng ấm, thành phố đêm ngoài cửa sổ, tông xanh tím.
- Cảm giác / dùng cho loại cảnh nào: quyền lực, khoảng cách, "để cửa mở"; về sau là nơi ngọt nhất (ep07).
- Chi tiết nhận diện: vách kính + cửa mở + máy in nhỏ.

## Bố cục cho sprite
- Tầm mắt ở y ≈ 42%.
- Khải sau bàn / cạnh bàn ở `right`; người vào phòng ở `left` (phía cửa). Cửa mở nên nằm bên trái khung để luôn thấy được (motif cửa mở).
- Máy in ep07 (dính cà phê) do code/`insert` thể hiện; ảnh nền giữ máy in sạch, ep08 trở đi coi như máy chết (không cần ảnh khác).

## Prompt tạo hình
```
<LOCATION_STYLE bible §10>, minimalist manager's office with glass partition walls, glass door wide open on the left side, white and navy blue interior, large desk with neatly stacked documents and a black notebook, minimalist wall clock without numerals, small office printer on a low cabinet beside the desk, window with a generic city view, cool ice blue tint, <variant>
```
- `day`: `bright clear daylight, crisp cool atmosphere`
- `night`: `night, warm desk lamp light, city lights outside the window, dark blue and purple tones`

Negative: `<LOCATION_NEGATIVE bible §10>, closed door`

## Tập sử dụng
- ep02, ep04, ep06, ep07 (`night`, tăng ca 20:15), ep08, ep10.
