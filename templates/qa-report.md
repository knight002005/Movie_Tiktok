---
episode: <series-slug>/epNN
video: out/final.mp4
reviewer: qa-reviewer
verdict: FAIL           # PASS | FAIL
checked_at: <ISO 8601>
---

# QA video — <series> Phần NN

## 1. Kỹ thuật (ffprobe / ffmpeg)
| Kiểm tra | Yêu cầu | Thực tế | Kết quả |
|---|---|---|---|
| Độ phân giải | 1080×1920 | | |
| FPS | 30 cố định | | |
| Codec video / pix_fmt | h264 / yuv420p | | |
| Codec audio / sample rate | aac / 48000 | | |
| Thời lượng | khớp scenes.json ±0,5s | | |
| Loudness integrated | -14 LUFS ±1 | | |
| True peak | ≤ -1 dBTP | | |
| Khung đen / đứng hình | không có ngoài ý muốn | | |
| Dung lượng | < 200MB | | |

## 2. Hình ảnh (khung hình trích ở các mốc: 0.5s, hook-end, mỗi đầu cảnh, đỉnh, cliffhanger, end card)
| Mốc | Shot | Safe zone | Phụ đề (chính tả/dấu/vị trí) | Nhất quán nhân vật | Lỗi khác |
|---|---|---|---|---|---|
| | | | | | |

## 3. Âm thanh & khẩu hình
- Khẩu hình khớp giọng (kiểm 3 câu ngẫu nhiên):
- Người không nói không nhép miệng:
- Giọng đúng nhân vật:
- Nhạc không át thoại:

## 4. Tuân thủ
- C5 (an toàn nội dung):
- T2.5 (bản quyền nhạc/SFX/font):

## 5. Lỗi cần sửa
| # | Mức (chặn / nên sửa) | Mốc thời gian | Mô tả | Công đoạn sửa |
|---|---|---|---|---|
