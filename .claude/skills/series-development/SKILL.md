---
name: series-development
description: Quy trình phát triển một series drama anime ngắn từ ý tưởng thành series bible hoàn chỉnh — logline, trope có nét lật, nhân vật want/need/flaw/bí mật, ma trận xưng hô, arc 12 tập, motif. Dùng khi tạo hoặc sửa series bible.
---

# Phát triển series

## Bước 1 — Mổ ý tưởng (5 câu hỏi)
1. **Ai** là người khán giả theo dõi? (nữ chính / nam chính / cả hai)
2. **Họ muốn gì** rõ ràng, đo được? (giữ việc, được thăng chức, trả thù, che giấu thân phận…)
3. **Điều gì cản** họ — và cản ngày càng mạnh?
4. **Lời hứa cảm xúc**: khán giả đến để cảm thấy gì? (ngọt, gắt, hả hê, thổn thức)
5. **Cái mới**: điều gì làm series này khác hàng trăm phim "sếp lạnh lùng" khác?

## Bước 2 — Logline
Mẫu: *"Khi [biến cố], [nhân vật + đặc điểm] phải [mục tiêu] trước khi [hạn chót/hậu quả], nhưng [trở ngại lớn nhất là chính người/điều họ…]."*
Kiểm tra: đọc logline cho người lạ — họ có hỏi "rồi sao nữa?" không?

## Bước 3 — Chọn trope
- Chọn 1 trope chính + 2 trope phụ từ `library/tropes-office-romance.md`.
- Mỗi trope viết **một nét lật** (cột "Nét lật gợi ý" là điểm khởi đầu, không chép nguyên).
- Lọc qua C5.3 (quyền lực & đồng thuận). Trope sếp – nhân viên: ghi rõ cách đảm bảo không lạm quyền.

## Bước 4 — Nhân vật (3–5 người)
Cho mỗi nhân vật: want · need · flaw · bí mật · nỗi sợ · điều không bao giờ làm · câu cửa miệng · màu chủ đạo.
Kiểm tra cặp đôi chính: **flaw của người này chạm đúng vết thương của người kia** → xung đột tự sinh.
Phản diện: viết một đoạn 3 câu từ góc nhìn của chính họ — nếu họ không thấy mình đúng, động cơ còn yếu (R1.D2).

## Bước 5 — Ma trận xưng hô
Lập bảng mọi cặp (A → B): xưng gì, gọi gì, khi nào đổi. Ví dụ:
| A → B | Xưng | Gọi | Đổi khi | Thành |
|---|---|---|---|---|
| Khải → Linh | tôi | cô | thừa nhận tình cảm (ep7) | anh / em |
| Linh → Khải | em | sếp / anh | cãi nhau to (ep3, tạm thời) | tôi / anh |
Lần đổi xưng hô đầu tiên là **một khoảnh khắc kịch tính có chủ đích** — đánh dấu tập nào.

## Bước 6 — Arc 12 tập
- Bắt đầu từ bảng mặc định trong `library/story-structures.md` mục 3, chỉnh theo câu chuyện.
- Mỗi tập: tiêu đề tạm, tóm tắt 1–2 câu, thay đổi giá trị, hook dự kiến (mã H), cliffhanger dự kiến (mã CH), mức quan hệ 0–10.
- Kiểm tra chu kỳ **ức chế → vả mặt** mỗi 2–4 tập và "phần thưởng lớn" mỗi 3–4 tập (R1.F4).
- Không dùng cùng mã hook hai tập liền.

## Bước 7 — B-plot, motif, bối cảnh
- B-plot gắn với nhân vật phụ, giao với A-plot ít nhất ở midpoint và cao trào.
- 1 motif vật thể (ví dụ: chiếc ô, ly cà phê, sticky note) xuất hiện ≥ 4 lần, ý nghĩa thay đổi theo quan hệ.
- Liệt kê 6–12 bối cảnh đủ cho cả series (ít bối cảnh = ít ảnh phải tạo = 0 đồng bền vững).

## Bước 8 — Tự rà trước khi giao
- [ ] Mọi mục của `templates/series-bible.md` đã điền (trừ mục casting để "chờ casting").
- [ ] Không có 🔴 C5; 🟡 đã ghi cách xử lý ở mục 14.
- [ ] Tên công ty, nhân vật hư cấu; không trùng người nổi tiếng.
- [ ] `continuity.md` khởi tạo.
