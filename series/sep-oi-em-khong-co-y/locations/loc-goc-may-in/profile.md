---
id: loc-goc-may-in
name: "Góc máy in hành lang"
variants: [day, night]
ambience_sfx: sfx.office-ambience
status: draft
---

# Góc máy in hành lang

## Mô tả
- Không gian, vật dụng chính, ánh sáng: hốc tường hành lang với **máy in đa năng cỡ lớn**, **thùng rác chung đặt ngay cạnh**, kệ ram giấy, hành lang kéo dài phía sau. Đây là máy in duy nhất trong tuyến lá đơn ep08–10.
  - `day`: đèn trần trắng, sáng đều.
  - `night`: hành lang tối, chỉ một đèn trần chiếu vùng máy in, cửa sổ đen; cô độc.
- Cảm giác / dùng cho loại cảnh nào: bí mật, đánh rơi, lộ sự thật (trang 1 bị lấy, đơn nghỉ việc, trang 2 lộ ra).
- Chi tiết nhận diện: máy in lớn + thùng rác cạnh bên.

## Bố cục cho sprite
- Tầm mắt ở y ≈ 42%.
- Máy in và thùng rác ở nửa phải; nhân vật đứng `left`/`center` quay về máy in. Giữ khay giấy ra lộ rõ để cắt sang `insert-may-in-khay`.

## Prompt tạo hình
```
<LOCATION_STYLE bible §10>, office hallway alcove with a large multifunction office printer on the right, a shared trash bin right next to the printer, shelf with paper reams, hallway extending into the background, <variant>
```
- `day`: `bright white fluorescent ceiling lights, clean neutral tones`
- `night`: `night, dark hallway, a single ceiling light illuminating only the printer area, dark windows, lonely quiet mood, blue tones`

Negative: `<LOCATION_NEGATIVE bible §10>, printed documents with writing`

## Tập sử dụng
- ep08 (`day`), ep09 (cliff, `night`), ep10 (`night`). Shot "in lại ở phòng nhân sự" ep08 dùng `insert-may-in-khay`, không thêm bối cảnh.
