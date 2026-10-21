---
description: Lên outline cho 3 tập kế tiếp của series (kế hoạch sản xuất 1 tuần)
argument-hint: <series-slug> [số tập, mặc định 3]
---

Lên kế hoạch tuần cho series: $ARGUMENTS

1. Đọc `series/<slug>/series.json` — yêu cầu `gates.series.approved = true`. Chưa duyệt → dừng, nhắc `/new-series`.
2. Xác định các tập kế tiếp: tập lớn nhất đã có `script.md` + 1 (mặc định 3 tập). Tạo thư mục `episodes/epNN/` và `status.json` (từ `templates/status.json`, state `idea`).
3. Gọi **screenwriter** (`subagent_type: screenwriter`) **tuần tự từng tập** (tập sau phụ thuộc cliffhanger tập trước) — chỉ viết `outline.md`, chưa viết kịch bản. Cập nhật state → `outlined`.
4. Kiểm tra nhanh: mỗi outline có mã hook khác nhau (không lặp quá 2 tập), cliffhanger tập N được trả lời ở đầu tập N+1, tài sản đều có sẵn.
5. Trình anh bảng tóm tắt:
   | Tập | Tiêu đề | Logline | Hook | Cliffhanger | Thay đổi giá trị | Tài sản thiếu |
6. Hỏi anh duyệt nhanh hướng đi (không phải cổng chính thức). Sau đó gợi ý `/make-episode <slug> epNN` cho từng tập.
