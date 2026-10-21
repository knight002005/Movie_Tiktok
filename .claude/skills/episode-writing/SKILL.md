---
name: episode-writing
description: Quy trình viết một tập phim drama anime ngắn 60–90s — từ arc trong bible đến outline theo beat sheet, rồi kịch bản đúng định dạng xưởng, có đếm âm tiết và ước lượng thời lượng. Dùng cho screenwriter khi viết hoặc sửa tập.
---

# Viết tập phim

## Bước 0 — Nạp ngữ cảnh
- Dòng của tập này trong arc (bible mục 7): chức năng, thay đổi giá trị, hook/cliffhanger dự kiến.
- `continuity.md`: ai biết gì, mức quan hệ, câu hỏi đang mở, motif đã gieo.
- Câu cuối + shot cuối của tập trước (để re-hook).
- `library/learnings.md`: hook nào đang hiệu quả / kém.

## Bước 1 — Outline (`templates/episode-outline.md`)
1. Viết **logline tập** 1 câu.
2. Xác định **thay đổi giá trị** (trước → sau) và **mức quan hệ** (trước → sau).
3. Chọn **hook** (skill `hook-cliffhanger`) và **cliffhanger**; viết sẵn câu/hình cụ thể.
4. Điền beat sheet 60s hoặc 90s (`library/story-structures.md`). Mỗi beat 1–2 câu diễn biến.
5. Liệt kê tài sản cần dùng; đối chiếu với hồ sơ nhân vật/bối cảnh. Thiếu → dừng, báo.
6. Ghi các điểm 🟡 C5.

## Bước 2 — Kịch bản (`templates/episode-script.md`)
- Viết theo đúng quy ước định dạng trong mẫu (tiêu đề cảnh, nhãn beat, hành động, thoại có biểu cảm).
- Hành động: chỉ viết những gì **thấy được** trên màn hình motion comic (biểu cảm, vị trí, vật thể, tin nhắn). Không viết "cô ấy nhớ lại tuổi thơ" nếu không có hồi tưởng.
- Mỗi dòng thoại: áp dụng skill `dialogue-writing`.
- Ưu tiên công cụ "rẻ mà mạnh" của motion comic: **tin nhắn chat, cận mặt phản ứng, im lặng, vật thể cận cảnh, chữ trên màn hình**.
- Gợi ý `> fx | sfx | camera` cho những khoảnh khắc then chốt (director quyết định cuối cùng).

## Bước 3 — Đếm & cân thời lượng
1. Đếm âm tiết thoại từng nhân vật (1 chữ tiếng Việt = 1 âm tiết).
2. Thời lượng ≈ tổng âm tiết ÷ 3,2 + (số shot không thoại × ~1,2s) + 2s end card.
3. Ngoài 60–90s → cắt hoặc thêm beat. **Cắt thoại trước, giữ phản ứng** (phản ứng mạnh hơn lời).

## Bước 4 — Đọc to (giả lập)
Đọc từng câu thoại như diễn viên: câu nào vấp, dài, sượng → sửa. Câu nào nhân vật khác cũng nói được → làm riêng hơn (R1.E6).

## Bước 5 — Tự rà (trước khi giao script-doctor)
- [ ] 3 giây đầu: nhân vật + chuyển động + xung đột; câu hook ≤ 12 âm tiết.
- [ ] Tập ≥ 2: nối cliffhanger tập trước trong ≤ 3s.
- [ ] ≤ 2s luôn có thay đổi hình (đánh dấu những đoạn dài).
- [ ] Nhân vật chính chủ động ít nhất một lần.
- [ ] Xưng hô đúng ma trận; có đổi xưng hô thì có chủ đích.
- [ ] Kết bằng cliffhanger + end card.
- [ ] Biểu cảm đều là mã sprite hợp lệ; bối cảnh có thật trong series.
- [ ] Không 🔴 C5.
- [ ] Đã điền "Thống kê" và front matter (`est_syllables`, `est_duration_s`).
