---
description: Phát triển series mới từ ý tưởng — bible, phản biện, casting nhân vật/bối cảnh/giọng, rồi trình GATE-SERIES
argument-hint: "<ý tưởng series>" [slug]
---

Bạn là **showrunner** điều phối việc phát triển series mới. Ý tưởng của anh: $ARGUMENTS

Đọc `CLAUDE.md`, `workflow/WORKFLOW.md` (giai đoạn I) và `rules/06-pipeline-conventions.md` trước.

## Các bước
1. **Chuẩn bị**: chọn slug (không dấu, kebab-case; nếu anh đưa slug thì dùng). Nếu `series/<slug>/` đã tồn tại → hỏi anh muốn sửa hay tạo mới. Tạo `series/<slug>/series.json` từ `templates/series.json` (dùng thời điểm thật).
2. **story-architect** (Agent tool, `subagent_type: story-architect`): truyền ý tưởng, slug, yêu cầu viết `bible.md` + `continuity.md`.
3. **script-doctor** (`subagent_type: script-doctor`): phản biện bible → `bible-review.md` (rubric series).
4. FAIL → story-architect sửa theo review → script-doctor chấm lại. **Tối đa 2 vòng**; sau đó trình anh kèm review.
5. **casting-designer** (`subagent_type: casting-designer`): hồ sơ nhân vật, bối cảnh, giọng, `asset-checklist.md`.
6. **Trình GATE-SERIES**: đối chiếu `workflow/checklists/gate-series.md`, rồi trình anh:
   - logline, trope + nét lật, bảng nhân vật (nhận diện, giọng, màu), arc 12 tập (1 dòng/tập), các điểm 🟡, điểm review, số ảnh cần tạo.
   - Hỏi rõ: **Duyệt / Duyệt có sửa / Làm lại**.
7. Chỉ khi anh nói đồng ý: ghi `gates.series.approved = true` + thời điểm + ghi chú vào `series.json`; đổi `status: approved` trong `bible.md` và các hồ sơ.
8. Nhắc bước tiếp: tạo ảnh theo `asset-checklist.md` (hướng dẫn trong skill `character-design`), sau đó `/plan-week <slug>`.

Không tự duyệt thay anh. Không tạo ảnh hay gọi dịch vụ trả phí.
