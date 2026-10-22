---
id: loc-phong-hop
name: "Phòng họp"
variants: [day]
ambience_sfx: sfx.office-ambience
status: draft
---

# Phòng họp

## Mô tả
- Không gian, vật dụng chính, ánh sáng: bàn họp dài màu trắng, ghế văn phòng, **màn hình lớn treo tường đang tắt** (nội dung chiếu — danh sách phiếu kín, ảnh gốc ep11 — do code vẽ đè), bảng trắng trống, vách kính, nắng ban ngày.
- Cảm giác / dùng cho loại cảnh nào: công khai, phán xét — họp, chấm kín, buổi xử lý vi phạm ep11.
- Chi tiết nhận diện: bàn dài + màn hình lớn.

## Bố cục cho sprite
- Tầm mắt ở y ≈ 40%.
- Màn hình lớn ở nửa trên khung (để code đặt nội dung chiếu, không bị sprite che); người trình bày `center` hoặc `right`, người ngồi đối diện `left`.

## Prompt tạo hình
```
<LOCATION_STYLE bible §10>, modern meeting room, long white conference table with office chairs, large wall-mounted screen turned off showing plain black, blank whiteboard, glass wall, <variant>
```
- `day`: `bright daylight through the windows, clean professional atmosphere, slightly cool tones`

Negative: `<LOCATION_NEGATIVE bible §10>, projected slides, charts`

## Tập sử dụng
- ep01, ep03, ep04, ep11.
