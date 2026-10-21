---
description: Phân tích số liệu TikTok của các tập đã đăng và rút bài học
argument-hint: <series-slug> [đường dẫn CSV hoặc dán số liệu]
---

Học từ số liệu: $ARGUMENTS

1. Nếu anh chưa đưa số liệu → hướng dẫn anh lấy từ TikTok Studio (mỗi tập: view 24h/7 ngày, giữ chân 3s, thời gian xem TB, tỷ lệ xem hết, like, bình luận, chia sẻ, lưu, follow) và dán vào, hoặc lưu CSV vào `series/<slug>/metrics/`.
2. Gọi **analyst** (`subagent_type: analyst`).
3. Trình anh: 3 phát hiện chính, đề xuất thay đổi luật (kèm bằng chứng), số liệu còn thiếu.
4. Với mỗi đề xuất, hỏi anh **duyệt / bác**. Duyệt → phiên chính sửa đúng file luật/thư viện liên quan, ghi ngày + nguồn bài học; cập nhật trạng thái trong `library/learnings.md`.
