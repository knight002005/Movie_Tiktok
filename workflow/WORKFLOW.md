# Quy trình sản xuất phim drama anime ngắn

## 1. Tổng quan

```
═══════════════ GIAI ĐOẠN I — PHÁT TRIỂN SERIES (1 lần / series) ═══════════════
 /new-series "<ý tưởng>"
   ① story-architect   → bible.md (logline, thế giới, nhân vật, ma trận xưng hô, arc 12 tập)
   ② script-doctor     → review bible (rubric series)          ↺ tối đa 2 vòng sửa
   ③ casting-designer  → characters/*/profile.md, locations/*/profile.md,
                         prompt tạo sprite & nền, casting giọng
   🧑 GATE-SERIES       → anh duyệt bible + nhân vật + giọng
   ④ (thủ công/Kaggle) tạo ảnh sprite & nền theo prompt → anh chọn → lưu đúng chỗ

═══════════════ GIAI ĐOẠN II — SẢN XUẤT TẬP (lặp lại, 3 tập/tuần) ═══════════════
 /plan-week <series>          → screenwriter viết outline 3 tập kế tiếp
 /make-episode <series> epNN
   ⑤ screenwriter      → outline.md (nếu chưa có) → script.md
   ⑥ script-doctor     → review.md (điểm + vi phạm + đề xuất)   ↺ tối đa 2 vòng sửa
   🧑 GATE-SCRIPT       → anh duyệt kịch bản
   ⑦ director          → scenes.json (shot, máy quay, biểu cảm, fx, sfx, nhạc)
   ── ⏳ HẬU KỲ (pipeline/ + studio/ — chưa xây) ───────────────────────────
   ⑧ voice             → audio/lineNN.mp3 + timings.json (edge-tts)
   ⑨ compose + render  → Remotion: nền + sprite + khẩu hình + camera + phụ đề → final.mp4
   ⑩ qa-reviewer       → qa.md (kỹ thuật + khung hình + tuân thủ)   ↺ sửa & render lại
   ──────────────────────────────────────────────────────────────────────
   ⑪ publisher         → publish.md (caption, hashtag, cover, comment ghim, giờ đăng)
   🧑 GATE-RELEASE      → anh duyệt → anh tự đăng lên TikTok → state = published

═══════════════ GIAI ĐOẠN III — HỌC TỪ SỐ LIỆU (hàng tuần) ═══════════════
 /learn <series>      → analyst đọc số liệu anh nhập → library/learnings.md
                        → đề xuất chỉnh rules / hook / lịch đăng (anh duyệt mới áp dụng)
```

## 2. Bảng công đoạn

| # | Công đoạn | Thực hiện | Đầu vào | Đầu ra | Skill |
|---|---|---|---|---|---|
| ① | Phát triển series | story-architect | ý tưởng của anh | `bible.md`, `continuity.md` | series-development |
| ② | Phản biện series | script-doctor | `bible.md` | `bible-review.md` | script-review |
| ③ | Casting | casting-designer | `bible.md` | hồ sơ nhân vật/bối cảnh, prompt | character-design |
| ④ | Tạo hình | anh + công cụ miễn phí | prompt | sprite, nền | character-design |
| ⑤ | Biên kịch | screenwriter | bible, continuity, tập trước | `outline.md`, `script.md` | episode-writing, hook-cliffhanger, dialogue-writing |
| ⑥ | Phản biện kịch bản | script-doctor | `script.md` | `review.md` | script-review |
| ⑦ | Phân cảnh | director | `script.md` đã duyệt, hồ sơ | `scenes.json` | scene-direction |
| ⑧–⑨ | Giọng, dựng, render | pipeline ⏳ | `scenes.json`, tài sản | `final.mp4` | — |
| ⑩ | QA video | qa-reviewer | `final.mp4`, `scenes.json` | `qa.md` | video-qa |
| ⑪ | Gói đăng | publisher | script, video | `publish.md` | tiktok-publishing |
| — | Học từ số liệu | analyst | số liệu TikTok | `learnings.md` | — |

## 3. Vòng phản biện (⑥)
1. screenwriter giao `script.md` (bản v1).
2. script-doctor chấm theo rubric (`templates/review-report.md`): **ĐẠT** khi điểm ≥ 75/100, không có vi phạm 🔴, hook ≥ 8/10, cliffhanger ≥ 8/10.
3. Không đạt → screenwriter sửa theo danh sách đề xuất (lưu bản cũ vào `versions/`) → chấm lại.
4. Tối đa **2 vòng**. Sau 2 vòng vẫn chưa đạt → trình anh cả kịch bản lẫn review, để anh quyết.
5. script-doctor là agent **độc lập**: không đọc hội thoại sáng tác, chỉ đọc file + luật.

## 4. Lịch tuần mẫu (3 tập/tuần)
| Ngày | Việc | Thời gian của anh |
|---|---|---|
| Chủ nhật | `/learn` (nhập số liệu tuần trước) → `/plan-week` (outline 3 tập) → anh duyệt nhanh outline | ~15 phút |
| Thứ 2 | `/make-episode` × 3 → anh duyệt 3 kịch bản (GATE-SCRIPT) | ~30 phút |
| Thứ 2–3 | Phân cảnh + hậu kỳ tự động ⏳ | ~0 |
| Thứ 3 | QA + gói đăng → anh xem 3 video (GATE-RELEASE) | ~20 phút |
| T3 · T5 · T7 | Anh đăng theo lịch trong `publish.md` | ~5 phút/tập |
Mục tiêu duy trì **kho dự trữ ≥ 3 tập** đã duyệt (T2.8).

## 5. Xử lý sự cố
| Tình huống | Cách xử lý |
|---|---|
| Kịch bản cần nhân vật/bối cảnh chưa có | Dừng. Đề xuất: viết lại dùng tài sản có sẵn **hoặc** quay lại casting-designer + GATE-SERIES (bổ sung) |
| Sửa kịch bản sau khi đã phân cảnh | Lùi trạng thái về `script_draft`; `scenes.json` cũ đổi tên `scenes.stale.json` |
| Tập trước chưa đăng mà muốn đổi cliffhanger | Sửa cả hai tập; ghi vào `continuity.md` |
| Số liệu cho thấy hook kém nhiều tập liền | analyst đề xuất; anh duyệt → cập nhật `library/hooks.md` hoặc R1.B |
| Hậu kỳ chưa có (⏳) | Dừng ở `directed`, báo anh — không giả lập kết quả |
