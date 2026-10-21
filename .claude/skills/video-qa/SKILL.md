---
name: video-qa
description: Lệnh ffprobe/ffmpeg và checklist để kiểm tra video tập phim đã render — thông số, loudness, khung đen/đứng hình, trích khung hình tại các mốc quan trọng để soát safe zone, phụ đề, nhất quán nhân vật, khẩu hình. Dùng cho qa-reviewer.
---

# QA video

Yêu cầu: FFmpeg trong PATH. Thay `<V>` bằng `series/<slug>/episodes/epNN/out/final.mp4`.

## 1. Thông số
```bash
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt,sample_rate,channels -show_entries format=duration,size,bit_rate -of json "<V>"
```
So với T2.1: h264 · 1080×1920 · 30/1 · yuv420p · aac 48000 · 2 kênh · dung lượng < 200MB.

## 2. Loudness
```bash
ffmpeg -hide_banner -nostats -i "<V>" -af ebur128=peak=true -f null - 2>&1 | tail -n 12
```
Đọc `I:` (mục tiêu -14 ±1 LUFS) và `Peak:` (≤ -1 dBFS true peak).

## 3. Khung đen & đứng hình
```bash
ffmpeg -hide_banner -i "<V>" -vf "blackdetect=d=0.2:pix_th=0.10" -an -f null - 2>&1 | grep blackdetect
ffmpeg -hide_banner -i "<V>" -vf "freezedetect=n=0.003:d=2.5" -an -f null - 2>&1 | grep freeze
```
Khung đen chỉ chấp nhận ở `fade-black` đã khai báo. Đứng hình > 2,5s là vi phạm R1.C2 (trừ end card).

## 4. Trích khung hình
Mốc bắt buộc: 0,5s · 3,0s (hết hook) · đầu mỗi scene · giữa shot có câu bom · 2s trước end card · end card.
```bash
ffmpeg -hide_banner -ss <giây> -i "<V>" -frames:v 1 -q:v 2 "<out>/frames/t<giây>.jpg"
```
Nếu pipeline hỗ trợ bản render có lớp safe zone (`--debug-safezone`), trích thêm từ bản đó.

## 5. Soát khung hình (xem từng ảnh)
| Kiểm | Tiêu chí |
|---|---|
| Safe zone | Mặt, phụ đề, chữ nằm trong x 60–940, y 160–1440 |
| Phụ đề | Đúng nguyên văn `scenes.json`, đủ dấu tiếng Việt, ≤ 2 dòng, không đè mặt, đúng màu nhân vật |
| Nhân vật | Tóc, mắt, trang phục, phụ kiện khớp ảnh tham chiếu `characters/<id>/refs/` |
| Biểu cảm | Khớp `expression` trong scenes.json |
| Bố cục | Người nói được làm nổi; hướng nhìn đúng |
| Lỗi hình | Viền cắt sprite lộ, sprite bị vỡ khi zoom, chữ AI lạ trong nền |

## 6. Khẩu hình & âm (giới hạn)
QA không nghe được trực tiếp. Kiểm gián tiếp:
- Đối chiếu `audio/timings.json` với thời điểm shot có thoại trong video (lệch ≤ 2 frame).
- Trích 3 khung giữa câu thoại: miệng người nói mở, người nghe ở `X`.
- Ghi rõ trong báo cáo: "Độ khớp khẩu hình cảm nhận cần anh nghe xem ở GATE-RELEASE."

## 7. Viết báo cáo
Điền `templates/qa-report.md`. Mỗi lỗi: mức (chặn/nên sửa), mốc giây, mô tả, công đoạn sửa (script / director / casting / pipeline).
