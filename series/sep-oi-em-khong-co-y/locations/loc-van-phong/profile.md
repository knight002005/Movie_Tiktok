---
id: loc-van-phong
name: "Khu làm việc chung Phòng Sáng tạo"
variants: [day, night]
ambience_sfx: sfx.office-ambience
status: draft
---

# Khu làm việc chung Phòng Sáng tạo

## Mô tả
- Không gian, vật dụng chính, ánh sáng: văn phòng mở của một agency sáng tạo, bàn gỗ sáng xếp hàng, màn hình máy tính, nhiều cây xanh, cửa sổ lớn nhìn ra thành phố (không địa danh). Tiền cảnh là **bàn của Linh**: mép màn hình dán kín giấy nhớ vàng (trống, chữ do code vẽ). Bàn bên cạnh (Tùng): bảng vẽ điện tử, giá treo tai nghe. Bàn xa hơn (Vy): gọn gàng, đế máy tính bảng.
  - `day`: nắng sáng xiên qua cửa sổ, tông trắng – gỗ sáng – pastel; ấm vàng nhẹ ở góc bàn Linh.
  - `night`: xanh tím, đèn thành phố ngoài cửa sổ, chỉ vài đèn bàn vàng còn sáng, màn hình phát sáng dịu.
- Cảm giác / dùng cho loại cảnh nào: "sân nhà" của Linh; thoại thường, tin đồn lan, tăng ca.
- Chi tiết nhận diện: màn hình dán giấy nhớ vàng.

## Bố cục cho sprite
- Tầm mắt ở y ≈ 42%.
- Bàn Linh ở tiền cảnh trái → Linh đứng `left`/`center`; người đối thoại `right`. Không đặt sprite đè lên chồng giấy nhớ khi shot cần thấy giấy nhớ.

## Prompt tạo hình
```
<LOCATION_STYLE bible §10>, open-plan creative agency office, rows of light wood desks with computer monitors showing blank soft blue screens, many green plants, large windows with a generic city skyline, foreground desk with many blank yellow sticky notes stuck around the monitor edge, neighboring desk with a drawing tablet and a headphone stand, tidy desk with a tablet stand in the background, <variant>
```
- `day`: `bright morning sunlight through the windows, white and light wood tones, pastel colors, cheerful`
- `night`: `late evening, dark blue and purple tones, city lights outside the windows, only a few warm desk lamps on, monitors glowing softly, quiet empty office`

Negative: `<LOCATION_NEGATIVE bible §10>`

## Tập sử dụng
- ep01–ep10, ep12 (`night`: cliff ep04, ep05 Linh làm khuya và hồi ức của Tùng).
