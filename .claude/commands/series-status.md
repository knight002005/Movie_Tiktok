---
description: Xem bảng trạng thái sản xuất của một series (hoặc tất cả series)
argument-hint: [series-slug]
---

Trạng thái: $ARGUMENTS

1. Đọc `series/*/series.json` (hoặc series được chỉ định) và mọi `episodes/*/status.json`.
2. Trình bày:
   - Series: tên, cổng GATE-SERIES, tài sản đã đủ chưa (đếm ☑/☐ trong `asset-checklist.md`).
   - Bảng tập: | Tập | Tiêu đề | Trạng thái | Điểm review | Lịch đăng | Việc tiếp theo |
   - **Kho dự trữ**: số tập đã `release_approved` chưa đăng (mục tiêu ≥ 3, T2.8).
   - Cảnh báo: tập kẹt ở một trạng thái > 3 ngày, cliffhanger chưa được trả lời, lịch đăng trống trong 7 ngày tới.
3. Chỉ đọc, không sửa file.
