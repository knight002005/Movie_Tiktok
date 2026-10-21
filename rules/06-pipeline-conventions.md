# P6 — Quy ước pipeline

## P6.1 Cấu trúc thư mục series
```
series/<series-slug>/
├─ series.json                 # trạng thái cấp series + cổng GATE-SERIES
├─ bible.md                    # series bible (templates/series-bible.md)
├─ continuity.md               # sổ liên tục, cập nhật sau mỗi tập
├─ characters/<char-id>/
│  ├─ profile.md               # templates/character-profile.md
│  ├─ refs/                    # ảnh tham chiếu đã duyệt
│  └─ sprites/                 # <pose>_<expression>[_blink].png
├─ locations/<loc-id>/
│  ├─ profile.md               # templates/location-profile.md
│  └─ <loc-id>_<variant>.png
└─ episodes/epNN/
   ├─ status.json              # templates/status.json
   ├─ outline.md               # templates/episode-outline.md
   ├─ script.md                # bản hiện hành (templates/episode-script.md)
   ├─ versions/script.vN.md    # các bản cũ — không xóa
   ├─ review.md                # báo cáo script-doctor (templates/review-report.md)
   ├─ scenes.json              # đầu ra director (schemas/scenes.schema.json)
   ├─ audio/                   # ⏳ pipeline: lineNN.mp3 + timings.json
   ├─ out/                     # ⏳ final.mp4, frames/
   ├─ qa.md                    # templates/qa-report.md
   └─ publish.md               # templates/publish-pack.md
```

## P6.2 Đặt tên & id
- Slug series, id nhân vật, id bối cảnh: không dấu, kebab-case. Ví dụ `sep-oi-em-khong-co-y`, `linh`, `loc-thang-may`.
- Tập: `ep01`, `ep02`… (2 chữ số). Cảnh: `s01`. Shot: `s01-sh03`.
- Biểu cảm và pose dùng đúng danh sách trong `rules/03-visual-style.md` V3.3; muốn thêm → cập nhật hồ sơ nhân vật trước.
- Hiệu ứng `fx.*` và âm thanh `sfx.*` chỉ dùng mã đã có trong V3.8 / A4.7 hoặc đã đăng ký trong `bible.md` → mục "Thư viện bổ sung".

## P6.3 Trạng thái tập (`status.json` → `state`)
```
idea → outlined → script_draft → script_reviewed → script_approved*
     → directed → voiced⏳ → composed⏳ → rendered⏳ → qa_passed⏳
     → release_approved* → published
```
`*` = cổng cần anh duyệt. `⏳` = cần pipeline hậu kỳ (chưa xây).
- Mỗi lần đổi trạng thái: thêm một dòng vào `history` (thời điểm, trạng thái, ai, ghi chú).
- Lùi trạng thái được phép (ví dụ sửa kịch bản sau khi đã `directed` → về `script_draft`, các file hạ nguồn coi như cũ và phải sinh lại).

## P6.4 Cổng duyệt
| Cổng | Khi nào | Checklist |
|---|---|---|
| GATE-SERIES | Sau bible + casting | `workflow/checklists/gate-series.md` |
| GATE-SCRIPT | Sau khi kịch bản qua `script-doctor` | `workflow/checklists/gate-script.md` |
| GATE-RELEASE | Sau QA video + gói đăng | `workflow/checklists/gate-release.md` |
Cổng chỉ được ghi `approved: true` khi **anh nói rõ đồng ý** trong hội thoại. Agent không tự duyệt.

**P6.4a — Kịch bản trước, video sau.**
- Mọi bước từ `directed` trở đi yêu cầu `gates.script.approved = true`; ghi thêm `gates.script.version` = số `version` của `script.md` lúc anh duyệt.
- Mỗi bước hậu kỳ (director, voice, compose, render) phải kiểm tra `version` trong `script.md` **trùng** `gates.script.version`. Không trùng → dừng, báo anh.
- Sửa `script.md` sau khi duyệt → tăng `version`, đặt `gates.script.approved = false`, lùi state về `script_draft`, trình lại anh (kèm danh sách thay đổi).

## P6.5 Quyền ghi file (agent nào được ghi gì)
| Agent | Được ghi | Không được ghi |
|---|---|---|
| story-architect | `bible.md`, `continuity.md` (khởi tạo), `series.json` (trạng thái nháp) | kịch bản tập, sprite |
| casting-designer | `characters/*/profile.md`, `locations/*/profile.md`, mục giọng/hình trong `bible.md` | kịch bản |
| screenwriter | `outline.md`, `script.md`, `versions/`, `continuity.md` (cập nhật sau duyệt) | `review.md`, `scenes.json` |
| script-doctor | `review.md` | `script.md` (chỉ đề xuất, không sửa) |
| director | `scenes.json` | `script.md` |
| qa-reviewer | `qa.md` | mọi file khác |
| publisher | `publish.md` | mọi file khác |
| analyst | `library/learnings.md`, `series/<slug>/metrics/` | rules (chỉ đề xuất sửa) |
| Phiên chính (lệnh) | `status.json`, `series.json` | — |

## P6.6 Phiên bản
- Trước khi ghi đè `script.md`, chép bản cũ sang `versions/script.vN.md`.
- Ghi chú thay đổi ngắn ở cuối file mới (mục "Nhật ký sửa").

## P6.7 Thời gian & nhật ký
- Dùng thời điểm thật từ hệ thống (hook phiên cung cấp) cho `history`, không đoán.
- Định dạng: ISO 8601 có múi giờ, ví dụ `2026-10-21T21:37:22+07:00`.
