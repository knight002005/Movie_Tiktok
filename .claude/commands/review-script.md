---
description: Phản biện độc lập một kịch bản tập hoặc series bible bằng script-doctor
argument-hint: <series-slug> [epNN | bible]
---

Phản biện: $ARGUMENTS

1. Xác định file đích: `series/<slug>/episodes/epNN/script.md` hoặc `series/<slug>/bible.md` (khi tham số là `bible` hoặc không có tập).
2. Gọi **script-doctor** (`subagent_type: script-doctor`) với đường dẫn file đích. Không truyền ý kiến chủ quan của bạn để giữ tính độc lập.
3. Trình anh: PASS/FAIL, điểm từng tiêu chí, 3 vấn đề lớn nhất, đề xuất sửa (tóm tắt), điểm 🟡.
4. Hỏi anh có muốn screenwriter/story-architect sửa theo review không. Lệnh này **không** đổi trạng thái cổng.
