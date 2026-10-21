# T2 — Quy tắc nền tảng TikTok

> Cập nhật lần cuối: 2026-10-21. **Chính sách TikTok thay đổi thường xuyên** — rà soát mỗi quý tại
> https://www.tiktok.com/community-guidelines và Trung tâm trợ giúp. Mục gắn **[cần kiểm tra]** là điều chưa xác minh được tại thời điểm viết — kiểm tra trước khi dựa vào.

## T2.1 Thông số kỹ thuật xuất file
| Mục | Giá trị |
|---|---|
| Khung hình | 9:16, **1080×1920** |
| Tốc độ khung hình | 30 fps (cố định, không VFR) |
| Video codec | H.264 (High profile), yuv420p, bitrate ~8–12 Mbps |
| Audio | AAC 48 kHz stereo, 192–320 kbps |
| Âm lượng | **-14 LUFS** integrated, true peak ≤ **-1 dBTP** |
| Container | MP4, `+faststart` |
| Dung lượng | Giữ dưới ~200MB cho tập ≤ 90s (thường chỉ 60–120MB) |

## T2.2 Vùng an toàn (safe zone) trên canvas 1080×1920
UI của TikTok che các vùng sau — **không đặt mặt nhân vật, phụ đề, chữ quan trọng** vào đó:
- **Trên:** 0–160 px (thanh trạng thái, tab "Đang Follow / Dành cho bạn").
- **Dưới:** 1440–1920 px (tên kênh, caption, nhạc, thanh tiến độ). Caption dài có thể che tới ~1400.
- **Phải:** 940–1080 px (avatar, tim, bình luận, chia sẻ).
- **Trái:** chừa lề 60 px.
→ **Vùng an toàn nội dung: x 60–940, y 160–1440.** Phụ đề: tâm ở y ≈ 1250–1350. Mặt nhân vật: y ≈ 420–1000.
- `studio/` phải có lớp debug vẽ safe zone; QA bật lớp này khi trích khung hình kiểm tra.

## T2.3 Định dạng series trên TikTok
- Tên trên màn hình (2 giây đầu, góc trên trái trong vùng an toàn, cỡ nhỏ): `Phần X · <Tên series>`.
- Dùng **Danh sách phát (Playlist)** để gom các tập theo series. **[cần kiểm tra]** điều kiện mở tính năng cho tài khoản.
- Mỗi tập: **ghim bình luận** dẫn sang tập trước/tập sau.
- Đăng đều đặn theo lịch cố định (xem T2.8). Không xóa rồi đăng lại cùng một video (bị coi là spam, mất tương tác).
- Chương trình Creator Rewards (kiếm tiền từ video > 1 phút) có giới hạn quốc gia **[cần kiểm tra: khả dụng tại Việt Nam]**. Dù vậy vẫn giữ tập ≥ 60s vì drama cần thời lượng để giữ chân.

## T2.4 Nhãn nội dung AI (bắt buộc)
- Hình ảnh nhân vật/bối cảnh do AI tạo → **luôn bật "Nội dung do AI tạo"** (AI-generated content) trong phần cài đặt khi đăng.
- Không gỡ metadata C2PA/watermark AI nếu công cụ tạo ảnh có gắn.
- Không mô phỏng người thật, tin tức thật, hay sự kiện thật bằng AI.

## T2.5 Bản quyền
- **Nhạc:** xuất video **không có nhạc có bản quyền**. Chỉ dùng nhạc miễn phí bản quyền đã ghi nguồn trong `assets/LICENSES.md`, hoặc thêm âm thanh từ thư viện của TikTok ngay trong app khi đăng (tài khoản doanh nghiệp chỉ được dùng Commercial Music Library).
- **SFX:** chỉ dùng nguồn CC0 / miễn phí thương mại; ghi nguồn.
- **Font:** chỉ dùng font giấy phép mở (OFL) — ví dụ Be Vietnam Pro, Montserrat, Nunito.
- **Thương hiệu & người thật:** không dùng tên/logo công ty có thật, sản phẩm có thật, người nổi tiếng. Công ty trong phim là hư cấu.
- **Không reup**, không ghép nội dung của người khác. Mỗi tập là sáng tác gốc (tránh bị đánh giá "nội dung không nguyên bản").
- **Công cụ dựng:** Remotion miễn phí cho cá nhân và công ty nhỏ (khoảng ≤ 3 người); quy mô lớn hơn phải mua license — kiểm tra lại tại remotion.dev khi đội ngũ hoặc mô hình kinh doanh thay đổi.
- **Nhạc trend không lấy được qua code.** Muốn dùng nhạc trend → thêm trong app lúc đăng (tài khoản cá nhân); tài khoản doanh nghiệp chỉ chọn trong Commercial Music Library.

## T2.6 Tiêu chuẩn cộng đồng liên quan trực tiếp đến drama
Chi tiết và cách xử lý trong kịch bản: `rules/05-content-safety.md`. Tóm tắt rủi ro bị gỡ hoặc giảm phân phối:
- Nội dung tình dục, gợi dục, khỏa thân (kể cả anime).
- Nhân vật trông như trẻ vị thành niên trong bối cảnh tình cảm.
- Bạo lực, máu me, tự hại, hành vi nguy hiểm có thể bắt chước.
- Quấy rối, bắt nạt, ngôn từ thù ghét (kể cả trong vai diễn — phải được phim phê phán, không cổ vũ).
- Rượu bia, thuốc lá, cờ bạc được tô vẽ hấp dẫn.
- Nội dung tĩnh, chất lượng thấp → ít được đề xuất. Motion comic phải có chuyển động liên tục (R1.C2).

## T2.6a Rủi ro định dạng motion comic (đọc kỹ)
Đồ họa chuyển động thuần thường **kém tương tác hơn** video có người thật hoặc cảnh quay thật trên TikTok. Định dạng anime motion comic của kênh chịu rủi ro này. Cách giảm thiểu:
- **Câu chuyện là sản phẩm, hình là phương tiện**: sức giữ chân đến từ hook, xung đột, thoại, cliffhanger (R1) — không đến từ hiệu ứng.
- **Template xoay quanh hook, không xoay quanh hiệu ứng**: 3 giây đầu luôn được thiết kế trước, các phần khác dựng theo.
- **Cảm giác "sống"**: nhân vật nhép miệng, chớp mắt, đổi biểu cảm, camera chuyển động liên tục (R1.C2, A4.4); không để khung tĩnh kiểu slideshow.
- **Kiểm chứng sớm bằng số liệu**: sau 6 tập đầu, `analyst` so tỷ lệ giữ chân 3s và tỷ lệ xem hết với mục tiêu T2.10. Không đạt → đề xuất anh điều chỉnh định dạng (ví dụ: thêm vài shot video AI cho khoảnh khắc cao trào khi có ngân sách, đổi phong cách kể).
- Không đánh giá sau 1–2 tập: tài khoản mới cần thời gian để TikTok xác định tệp người xem.

## T2.7 Caption, hashtag, tìm kiếm
- **Dòng đầu caption** (~80 ký tự hiển thị) phải là một hook phụ hoặc câu hỏi, không lặp nguyên văn hook video.
- Chứa từ khóa tìm kiếm tự nhiên: "phim ngắn", "ngôn tình công sở", "anime", tên series, "Phần X".
- **3–5 hashtag**: 1–2 rộng (#phimngan, #anime), 2–3 ngách (#ngontinhcongso, #dramacongso, #<tenseries>). Không nhồi hashtag không liên quan, không dùng hashtag trend sai chủ đề.
- Một câu hỏi kéo bình luận ("Nếu là bạn, bạn có tha thứ không?") — **không** câu kiểu lừa tương tác ("like để nhận…").
- Chữ trên ảnh bìa (cover): ≤ 6 từ, đọc được ở kích thước thumbnail, đúng vùng an toàn.

## T2.8 Lịch đăng (giả thuyết ban đầu — kiểm chứng bằng số liệu)
- 3 tập/tuần, ví dụ **Thứ 3 · Thứ 5 · Thứ 7**, khung **19:30–21:30** giờ Việt Nam (hoặc 11:30–12:30). `analyst` điều chỉnh sau 4 tuần dữ liệu.
- Luôn có **kho dự trữ ≥ 3 tập đã duyệt** trước ngày đăng.
- Không đăng 2 tập cùng series trong cùng một ngày trừ khi có chiến lược rõ ràng.

## T2.8a Đăng bài: thủ công, không tự động
- **Anh tự đăng bằng app/web TikTok.** Hệ thống chỉ chuẩn bị video + gói đăng (`publish.md`), không đăng thay.
- Lý do: TikTok Content Posting API yêu cầu ứng dụng qua kiểm duyệt; trước khi được duyệt, video đăng qua API chỉ ở chế độ **riêng tư**. Không dùng công cụ/bot đăng tự động không chính thức (rủi ro khóa tài khoản).
- **Tránh nội dung na ná nhau**: đăng hàng loạt video cùng khuôn dễ bị giảm phân phối. Mỗi tập phải khác biệt rõ: hook khác mã (R1.B5), bìa khác bố cục/biểu cảm, caption viết riêng, không dùng lại nguyên văn câu mở đầu.
- Chỉ xem xét đăng tự động khi: có ứng dụng được TikTok duyệt **và** anh đồng ý bằng văn bản.

## T2.9 Tài khoản & tuân thủ pháp luật Việt Nam
- Tài khoản đăng ở Việt Nam cần xác thực bằng số điện thoại theo Nghị định 147/2024/NĐ-CP **[cần kiểm tra quy định hiện hành]**.
- Không mua view/follow/tương tác, không dùng bot tương tác.
- Nội dung có tài trợ → bật nhãn "Nội dung thương hiệu" và tuân thủ quy định quảng cáo.
- Chủ tài khoản ≥ 18 tuổi để dùng các tính năng kiếm tiền/LIVE.

## T2.10 Chỉ số theo dõi (dành cho `analyst`)
| Chỉ số | Ý nghĩa | Mục tiêu khởi điểm |
|---|---|---|
| Tỷ lệ giữ chân 3s | Hook có hiệu quả không | ≥ 65% |
| Thời gian xem trung bình / độ dài | Nhịp có giữ chân không | ≥ 50% |
| Tỷ lệ xem hết | Cấu trúc & cliffhanger | ≥ 30% |
| Bình luận / 1.000 view | Mức độ "nhập vai" | ≥ 5 |
| Chia sẻ, lưu | Sức lan tỏa | theo dõi xu hướng |
| Follow / 1.000 view | Chuyển đổi thành người xem series | ≥ 3 |
Mục tiêu trên là điểm xuất phát, cập nhật theo dữ liệu thật của kênh.
