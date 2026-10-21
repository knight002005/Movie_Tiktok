---
name: tiktok-publishing
description: Soạn gói đăng TikTok cho tập phim drama anime — chữ ảnh bìa, caption tối ưu tìm kiếm, hashtag, comment ghim nối tập, giờ đăng, cài đặt nhãn AI và playlist, rà soát tuân thủ. Dùng cho publisher.
---

# Gói đăng TikTok

## 1. Chữ ảnh bìa (≤ 6 từ)
- Tạo tò mò, không spoil cliffhanger. Đọc được ở thumbnail (chữ to, 1–2 dòng).
- Công thức: `[Tình huống] + [cảm xúc]` — ví dụ: "Mắng nhầm sếp ngày đầu 😱", "Sếp nhắn lúc 2 giờ sáng".
- Chọn khung bìa: cận mặt biểu cảm mạnh nhất (thường ở hook hoặc đỉnh), mặt trong vùng an toàn.

## 2. Caption
```
Dòng 1 (≤ 80 ký tự): hook phụ hoặc câu hỏi — KHÔNG lặp nguyên câu hook trong video
Dòng 2: Phần NN · <Tên series> (từ khóa tìm kiếm)
Dòng 3: câu hỏi kéo bình luận về lựa chọn/đạo đức/dự đoán
Hashtag
```
- Câu hỏi bình luận hay: dự đoán ("Bạn nghĩ người gõ cửa là ai?"), lựa chọn ("Tha thứ hay nghỉ việc?"), đứng về phe ("Team Linh hay team Vy?").
- Tránh: "Like và follow để xem phần 2" đơn thuần, "Bình luận 1 nếu…" (lừa tương tác).

## 3. Hashtag (3–5)
- 1–2 rộng: `#phimngan` `#anime`
- 2–3 ngách: `#ngontinhcongso` `#dramacongso` `#<tenseries-khongdau>`
- Theo dõi hiệu quả trong `library/learnings.md`; đổi bộ hashtag khi có bằng chứng.

## 4. Comment ghim
`📌 Phần trước: Phần NN-1 | Phần tiếp: <thứ> lúc <giờ>h — bật thông báo để không lỡ nhé!`
Sau khi tập sau lên: cập nhật comment ghim tập này thành link/tên tập sau (anh làm trong app).

## 5. Giờ đăng
- Theo `series.json` → `posting_schedule`. Nếu `learnings.md` có bài học đã duyệt về giờ đăng → dùng bài học.
- Ghi `scheduled_at` dạng ISO 8601 +07:00.

## 6. Cài đặt khi đăng (nhắc anh)
- Bật **Nội dung do AI tạo** (T2.4) — bắt buộc.
- Thêm vào **danh sách phát** của series (nếu tài khoản có tính năng).
- Nhạc: giữ âm gốc; nếu muốn thêm nhạc trend thì chọn trong app ở mức âm lượng thấp để không át thoại.
- Tắt "Nội dung thương hiệu" trừ khi có tài trợ.

## 7. Rà soát cuối
- [ ] Không spoil, không lừa tương tác.
- [ ] Không vi phạm C5 (kể cả trong caption/bìa).
- [ ] Không tên thương hiệu/người thật.
- [ ] `ai_label: true`.
