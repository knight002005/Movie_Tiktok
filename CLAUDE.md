# Movie_tiktok — Xưởng phim drama anime ngắn cho TikTok

## Dự án
Hệ thống multi-agent sản xuất **phim drama ngắn phong cách anime motion comic / visual novel** cho TikTok.
- Ngôn ngữ: tiếng Việt. Khung hình 9:16 (1080×1920, 30fps).
- Series đầu tiên: tình ái công sở. Nhịp sản xuất mục tiêu: **3 tập/tuần**, mỗi tập 60–90 giây.
- Ngân sách: **0 đồng**. Không gọi dịch vụ trả phí; nếu một bước buộc phải tốn tiền → dừng và hỏi anh.
- Máy: i7-9750H, RAM 16GB, GTX 1650 4GB VRAM → không chạy model video AI cục bộ; việc nặng (tạo ảnh hàng loạt) dùng Kaggle/Colab miễn phí.
- Xưng hô với người dùng: người dùng xưng "anh", Claude xưng "em".

## Nguyên tắc cốt lõi (luôn áp dụng)
1. **Tài sản làm một lần, dùng lại mãi.** Nhân vật (sprite), bối cảnh, giọng đọc được khóa ở cấp series. Không tự thêm nhân vật/bối cảnh mới trong một tập khi chưa qua `casting-designer` và cổng GATE-SERIES.
2. **Kịch bản là nguồn sự thật.** `scenes.json`, audio, video đều sinh từ `script.md` đã duyệt. Muốn đổi nội dung → sửa kịch bản → sinh lại phía sau, không vá tay ở hạ nguồn.
3. **Audio-first.** Thời lượng cảnh có thoại lấy theo độ dài giọng đọc thật.
4. **Không vượt cổng khi chưa có anh duyệt** (GATE-SERIES, GATE-SCRIPT, GATE-RELEASE). Ghi quyết định vào `status.json`.
   - **Kịch bản trước, video sau:** không bước nào thuộc hậu kỳ (phân cảnh, giọng, dựng, render) được chạy khi `gates.script.approved` chưa là `true`. Luôn trình **toàn văn kịch bản** cho anh đọc trước khi xin duyệt.
   - Kịch bản đã duyệt mà bị sửa (dù một chữ) → cổng tự mất hiệu lực (`approved: false`), phải trình lại bản mới kèm phần thay đổi.
5. **Tuân thủ** `rules/05-content-safety.md` và `rules/02-tiktok-platform.md` ở mọi bước — không phải chỉ lúc đăng.
6. Nội dung viết bằng **tiếng Việt có dấu đầy đủ**; tên file, slug, id: không dấu, kebab-case.

## Bản đồ tài liệu
| Thư mục | Nội dung | Khi nào đọc |
|---|---|---|
| `rules/01-short-drama-craft.md` | Nghề viết & dựng phim ngắn (mã R1.x) | Viết/duyệt series, kịch bản |
| `rules/02-tiktok-platform.md` | Thông số, safe zone, chính sách, đăng bài (mã T2.x) | Phân cảnh, QA, đăng |
| `rules/03-visual-style.md` | Phong cách hình, sprite, ngữ pháp máy quay, hiệu ứng (mã V3.x) | Casting, phân cảnh, dựng |
| `rules/04-audio-voice.md` | Giọng, diễn xuất TTS, khẩu hình, âm lượng (mã A4.x) | Casting giọng, phân cảnh, dựng |
| `rules/05-content-safety.md` | An toàn nội dung (mã C5.x) | **Mọi bước** |
| `rules/06-pipeline-conventions.md` | Thư mục, đặt tên, trạng thái, quyền ghi file (mã P6.x) | Mọi agent trước khi ghi file |
| `workflow/WORKFLOW.md` | Quy trình đầy đủ, cổng duyệt, lịch tuần | Điều phối |
| `workflow/checklists/` | Checklist cho từng cổng | Trước khi trình anh duyệt |
| `templates/` | Mẫu bible, nhân vật, bối cảnh, outline, kịch bản, báo cáo | Khi tạo file mới |
| `library/` | Thư viện hook, cliffhanger, trope, cấu trúc, bài học | Sáng tác |
| `schemas/` | JSON Schema cho dữ liệu máy đọc | Phân cảnh, pipeline |
| `series/<slug>/` | Dữ liệu sản xuất thật | — |

## Bộ agent (`.claude/agents/`)
| Agent | Vai trò |
|---|---|
| `story-architect` | Phát triển series: bible, nhân vật, arc 12 tập |
| `casting-designer` | Hồ sơ nhân vật & bối cảnh, spec sprite, prompt tạo ảnh, chọn giọng |
| `screenwriter` | Biên kịch: outline tập và kịch bản tập |
| `script-doctor` | Phản biện độc lập, chấm điểm theo rubric, không tự viết lại |
| `director` | Phân cảnh: kịch bản → `scenes.json` (góc máy, biểu cảm, hiệu ứng, âm thanh) |
| `qa-reviewer` | Kiểm tra video đã render (kỹ thuật + hình + tuân thủ) |
| `publisher` | Gói đăng TikTok: caption, hashtag, ảnh bìa, comment ghim, checklist |
| `analyst` | Đọc số liệu TikTok, rút bài học vào `library/learnings.md` |

Subagent không gọi được subagent khác → **việc điều phối luôn do phiên chính thực hiện qua các lệnh** dưới đây.

## Lệnh (`.claude/commands/`)
`/new-series` · `/plan-week` · `/make-episode` · `/review-script` · `/direct-episode` · `/publish-pack` · `/series-status` · `/learn`

## Trạng thái triển khai
- ✅ Tiền kỳ: series → kịch bản → phản biện → phân cảnh (`scenes.json`) → gói đăng.
- ⏳ Hậu kỳ tự động (giọng, ghép Remotion, render, QA video): `pipeline/` và `studio/` — **chưa xây**. Khi chưa có, dừng ở `directed` và báo anh.
