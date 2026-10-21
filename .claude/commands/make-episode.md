---
description: Sản xuất một tập — kịch bản, phản biện (≤2 vòng), trình GATE-SCRIPT; sau khi duyệt thì phân cảnh và soạn gói đăng
argument-hint: <series-slug> <epNN>
---

Sản xuất tập: $ARGUMENTS

Đọc `CLAUDE.md`, `workflow/WORKFLOW.md` (giai đoạn II), `rules/06-pipeline-conventions.md` trước.

## Điều kiện
- `series.json` → `gates.series.approved = true`.
- Tập ≥ 2: tập trước phải có `script.md` đã duyệt (để nối cliffhanger). Nếu chưa → hỏi anh có muốn tiếp tục không.
- Đọc `episodes/epNN/status.json` (chưa có → tạo từ mẫu) và **tiếp tục từ trạng thái hiện tại**, không làm lại bước đã xong.

## Các bước
1. **Kịch bản** (`subagent_type: screenwriter`): viết `outline.md` nếu chưa có, rồi `script.md`. State → `script_draft`.
2. **Phản biện** (`subagent_type: script-doctor`): `review.md`. State → `script_reviewed`; tăng `review_rounds`.
3. FAIL → screenwriter sửa theo `review.md` → script-doctor chấm lại. **Tối đa 2 vòng.**
4. **Trình GATE-SCRIPT** theo `workflow/checklists/gate-script.md`:
   - Tóm tắt 3 dòng, điểm review, điểm 🟡, ước lượng thời lượng.
   - Hiển thị **toàn bộ kịch bản** (anh cần đọc).
   - Hỏi: **Duyệt / Sửa (ý kiến) / Viết lại**.
5. Anh **Sửa** → screenwriter sửa theo ý anh (sửa nhỏ không cần qua script-doctor) → trình lại.
6. Anh **Duyệt** → ghi `gates.script` (`approved: true`, `version` = version hiện tại của `script.md`, thời điểm) + state `script_approved` vào `status.json`; screenwriter cập nhật `continuity.md`.
   **Không có câu đồng ý rõ ràng của anh → dừng tại đây, không chạy bước 7 trở đi** (P6.4a).
7. **Phân cảnh** (`subagent_type: director`): `scenes.json`. State → `directed`.
8. **Hậu kỳ ⏳**: nếu `pipeline/` chưa có công cụ chạy được → dừng tại đây, báo anh rõ ràng. (Khi có: voice → compose → render → `qa-reviewer` → state `qa_passed`.)
9. **Gói đăng** (`subagent_type: publisher`): `publish.md` (có thể soạn trước dựa trên kịch bản).
10. Báo cáo cuối: trạng thái, các file đã tạo, việc tiếp theo.

Mọi thời điểm ghi vào `history` dùng thời gian thật.
