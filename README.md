# Movie_tiktok — Xưởng phim drama anime ngắn

Hệ thống agent (Claude Code) sản xuất phim drama ngắn phong cách **anime motion comic** cho TikTok — tiếng Việt, 9:16, 0 đồng, mục tiêu 3 tập/tuần.

## Bắt đầu nhanh
Mở Claude Code tại thư mục này rồi gõ:

| Bước | Lệnh | Kết quả |
|---|---|---|
| 1 | `/new-series "drama tình ái công sở: nhân viên mới mắng nhầm sếp"` | Bible + nhân vật + bối cảnh + giọng → anh duyệt |
| 2 | (thủ công) tạo ảnh theo `series/<slug>/asset-checklist.md` | Sprite + nền |
| 3 | `/plan-week <slug>` | Outline 3 tập kế tiếp |
| 4 | `/make-episode <slug> ep01` | Kịch bản → phản biện → anh duyệt → phân cảnh → gói đăng |
| 5 | `/publish-pack <slug> ep01` | Gói đăng + duyệt phát hành |
| — | `/series-status` | Bảng trạng thái |
| — | `/review-script <slug> ep01` | Phản biện lại một kịch bản |
| — | `/learn <slug>` | Học từ số liệu TikTok hàng tuần |

## Cấu trúc
```
CLAUDE.md                  luật gốc cho Claude
rules/                     6 bộ quy tắc (nghề phim, TikTok, hình, âm, an toàn, pipeline)
workflow/                  quy trình + checklist 3 cổng duyệt
library/                   25 hook, 16 cliffhanger, trope công sở, cấu trúc tập/series, bài học
templates/                 mẫu bible, nhân vật, bối cảnh, outline, kịch bản, review, QA, gói đăng
schemas/                   scenes.schema.json (đầu ra phân cảnh → đầu vào dựng phim)
.claude/agents/            8 agent chuyên trách
.claude/skills/            9 kỹ năng
.claude/commands/          8 lệnh điều phối
series/                    dữ liệu sản xuất
pipeline/  studio/         ⏳ hậu kỳ tự động (giọng, Remotion, render) — giai đoạn sau
assets/                    nhạc, SFX, font dùng chung (kèm giấy phép)
```

## Ba cổng anh duyệt
1. **GATE-SERIES** — câu chuyện, nhân vật, giọng (1 lần/series)
2. **GATE-SCRIPT** — kịch bản từng tập (~10 phút/tập)
3. **GATE-RELEASE** — video + gói đăng (~5 phút/tập)

## Trạng thái
- ✅ Tiền kỳ hoàn chỉnh: series → kịch bản → phản biện → phân cảnh → gói đăng.
- ⏳ Chưa xây: TTS + khẩu hình, ghép Remotion, render, QA video tự động (xem `pipeline/README.md`).
- Cần chuẩn bị: cài FFmpeg, giải phóng ổ C (≥ 25–30GB) hoặc dùng ổ khác cho tài sản/video.
