---
description: Soạn gói đăng TikTok và trình GATE-RELEASE cho một tập
argument-hint: <series-slug> <epNN>
---

Gói đăng: $ARGUMENTS

1. Gọi **publisher** (`subagent_type: publisher`) → `episodes/epNN/publish.md`.
2. Nếu đã có `out/final.mp4` và `qa.md` PASS → trình **GATE-RELEASE** theo `workflow/checklists/gate-release.md` (video, qa, gói đăng). Hỏi: **Duyệt / Sửa**.
   - Duyệt → ghi `gates.release` + state `release_approved`. Nhắc anh đăng theo `scheduled_at` và **bật nhãn nội dung AI**.
3. Nếu chưa có video → chỉ trình gói đăng nháp, không mở cổng.
4. Khi anh báo đã đăng → state `published`, ghi `published_at`.
