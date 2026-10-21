---
name: scene-direction
description: Phân cảnh kịch bản thành scenes.json cho anime motion comic — chia shot theo thoại và phản ứng, chọn loại shot, chuyển động camera, biểu cảm, vị trí nhân vật, hiệu ứng fx, sfx, nhạc, chuyển cảnh; tuân thủ safe zone và nhịp ≤2 giây. Dùng cho director.
---

# Phân cảnh (kịch bản → scenes.json)

## 1. Nguyên tắc chia shot
- **Một câu thoại = ít nhất một shot.** Câu > 4 giây (~13 âm tiết) → cân nhắc đổi góc giữa câu (bằng `expression_change` hoặc tách shot nếu kịch bản tách câu).
- **Sau câu bom luôn có `reaction`** của người nghe (0,8–1,5s, không thoại).
- **Mở cảnh mới**: `establishing` ≤ 1,5s — hoặc bỏ nếu hook cần vào thẳng.
- **Đối thoại 2 người**: luân phiên `single`/`close-up` theo người nói, chen `two-shot` mỗi 3–4 lượt để giữ không gian.
- **Mức độ cảm xúc ↑ → cỡ cảnh chặt hơn**: two-shot → single → close-up → extreme-close-up.

## 2. Bảng chọn camera theo cảm xúc
| Cảm xúc của beat | Shot | Camera | fx gợi ý | sfx gợi ý |
|---|---|---|---|---|
| Sốc, bất ngờ | close-up | quick-zoom | fx.shock-flash / fx.speed-lines | sfx.impact |
| Căng thẳng tăng dần | single → close-up | push-in chậm | fx.vignette | sfx.heartbeat |
| Giận dữ | close-up | shake | fx.anger-vein | sfx.impact |
| Ngượng, rung động | close-up | static / push-in nhẹ | fx.blush / fx.hearts | — |
| Bối rối, hài | single | static | fx.sweat-drop | sfx.whoosh |
| Đe dọa (phản diện) | close-up | dutch / push-in | fx.dark-aura | — |
| Buồn, cô đơn | single | pull-out | fx.rain-gloom (hài) / filter buồn | — |
| Tiết lộ vật thể | insert | push-in | fx.vignette | sfx.heartbeat |
| Giới thiệu nhân vật lần đầu | single | static | fx.freeze-frame | sfx.whoosh |

## 3. Vị trí & hướng nhìn
- Hai người: người A `left` + `facing: right`, người B `right` + `facing: left`. Giữ nguyên trong suốt cảnh (quy tắc 180°) trừ khi có chủ đích.
- Người nói = `focus`. Người mới vào cảnh: `enter: slide-left/right` theo phía cửa của bối cảnh.
- Mặt luôn trong safe zone (T2.2): khi zoom ≥ 1.6, `target: face`.

## 4. Thời lượng
- Shot có thoại: **không đặt** `duration_s` (pipeline lấy theo audio); dùng `pause_before_ms` / `pause_after_ms` để tạo nhịp.
- Shot không thoại: reaction 0,8–1,5s; insert 1–2s; establishing ≤ 1,5s; title-card 1,5–2,5s; chat: ~0,9s mỗi tin nhắn + 0,5s.
- Kiểm tra: không shot nào > 4s mà không có `camera.move` khác `static` hoặc `expression_change` (R1.C2).

## 5. Âm thanh & nhạc
- Mỗi scene khai báo `ambience` theo hồ sơ bối cảnh.
- Nhạc: `start` ở hook hoặc setup; `change` tại beat ĐỈNH; `stop` 0,3–0,6s trước câu bom (A4.8) và trước cliffhanger.
- sfx gắn vào mốc: `start`, `line_end`, `word:<n>`.

## 6. Shot đặc biệt
- **phone-chat**: điền `chat.contact`, `chat.owner`, `messages[]` (me/them, status). Không cần `line`.
- **phone-call**: hai nhân vật, `line` của người nói; pipeline chia đôi màn hình.
- **title-card**: `text_overlay` ("3 ngày trước…"), `duration_s`.
- **flashback**: đặt ở cấp scene `filter: flashback`; vào/ra bằng `transition_out: flash`.

## 7. Quy trình
1. Đọc kịch bản đã duyệt, đánh dấu: câu bom, đổi xưng hô, chỗ im lặng, tin nhắn, vật thể.
2. Chia scene theo tiêu đề `## CẢNH`; gán `beat` theo nhãn trong kịch bản.
3. Chia shot theo mục 1, chọn camera/fx/sfx theo mục 2.
4. Điền JSON theo `schemas/scenes.schema.json`; id `sNN-shMM` liên tục.
5. Tự kiểm: JSON hợp lệ; `line.text` khớp nguyên văn; mọi id tồn tại; ≤ 1 hiệu ứng mạnh / 5s; tổng thời lượng ước tính 60–90s.
