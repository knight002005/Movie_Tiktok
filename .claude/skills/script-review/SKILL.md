---
name: script-review
description: Rubric và quy trình phản biện độc lập cho series bible và kịch bản tập phim drama ngắn — chấm 10 tiêu chí, đối chiếu mã luật, phân loại vi phạm 🔴/🟡/ⓘ, viết đề xuất sửa cụ thể. Dùng cho script-doctor và lệnh /review-script.
---

# Phản biện kịch bản

## A. Quy trình (kịch bản tập)
1. **Đọc một lượt như khán giả** (không ghi chú): ghi lại giây bạn muốn lướt qua, giây bạn bất ngờ, và có muốn xem tập sau không.
2. **Kiểm tra cứng** (lỗi chặn sản xuất → 🔴):
   - Nhân vật/bối cảnh/biểu cảm không có trong series (P6.2).
   - Vi phạm 🔴 trong C5.
   - Tập ≥ 2 không nối cliffhanger tập trước (R1.B4).
   - Thời lượng ước tính ngoài 45–100s.
3. **Chấm 10 tiêu chí** theo bảng trong `templates/review-report.md`, dùng thang dưới đây.
4. **Liệt kê vi phạm** kèm mã luật và vị trí.
5. **Viết đề xuất**: tối đa 10, xếp theo tác động. Mỗi đề xuất: vị trí · hiện tại · đề xuất · lý do. Đề xuất phải **làm được ngay** (viết sẵn câu thay thế), không chung chung kiểu "làm thoại hay hơn".
6. **Ghi điểm mạnh cần giữ** để vòng sửa không làm mất.
7. Kết luận theo quy tắc: có 🔴 → FAIL; ngược lại PASS khi tổng ≥ 75, Hook ≥ 8, Cliffhanger ≥ 8.

## B. Thang điểm từng tiêu chí
| Điểm | Ý nghĩa |
|---|---|
| 9–10 | Xuất sắc, có thể làm ví dụ mẫu cho thư viện |
| 7–8 | Tốt, chỉ cần tinh chỉnh |
| 5–6 | Đạt mức tối thiểu, có vấn đề rõ |
| 3–4 | Yếu, vi phạm luật |
| 0–2 | Thiếu hoàn toàn |

Mốc cụ thể:
- **Hook**: 10 = frame 1 có hành động + câu ≤ 12 âm tiết + hiểu khi tắt tiếng + mới lạ; mất 2 điểm cho mỗi yếu tố thiếu.
- **Cliffhanger**: 10 = câu hỏi cụ thể + cắt ở đỉnh + tăng cược + có thể trả lời ở tập sau; cliffhanger "giả"/không thông tin mới ≤ 4.
- **Thoại**: trừ điểm cho mỗi câu > 25 âm tiết, mỗi câu văn dịch, mỗi câu giải thích điều đã thấy.

## C. Rubric series bible (cho `bible-review.md`)
| # | Tiêu chí |
|---|---|
| 1 | Logline rõ, có xung đột và điểm khác biệt |
| 2 | Trope hấp dẫn + nét lật thật sự |
| 3 | Nhân vật chính: want/need/flaw/bí mật khớp nhau, tạo xung đột tự sinh |
| 4 | Phản diện có động cơ (R1.D2) |
| 5 | Ma trận xưng hô đầy đủ, có điểm đổi xưng hô kịch tính |
| 6 | Arc 12 tập: midpoint, cao trào, chu kỳ ức chế → vả mặt |
| 7 | Mỗi tập có thay đổi giá trị + cliffhanger dự kiến |
| 8 | B-plot & motif |
| 9 | Khả thi 0 đồng: số nhân vật, bối cảnh, biểu cảm hợp lý |
| 10 | An toàn nội dung C5 (đặc biệt C5.3) |
PASS khi tổng ≥ 75, tiêu chí 1, 3, 6 đều ≥ 7, không có 🔴.

## D. Văn phong nhận xét
- Thẳng, cụ thể, có dẫn chứng (trích câu). Không khen chung chung.
- Phê bình kịch bản, không phê bình người viết.
- Tiếng Việt, ngắn gọn.
