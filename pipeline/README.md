# pipeline/ — Hậu kỳ tự động ⏳ (chưa xây)

Hợp đồng đầu vào/đầu ra để xây ở giai đoạn sau. Các agent tiền kỳ đã sinh dữ liệu theo đúng hợp đồng này.

| Script | Đầu vào | Đầu ra | Công cụ (0 đồng) |
|---|---|---|---|
| `voice` | `scenes.json`, hồ sơ nhân vật (voice) | `audio/<shot-id>.mp3`, `audio/timings.json` (mốc từng từ, thời lượng từng shot) | edge-tts (adapter, thay được) |
| `visemes` | `timings.json`, audio | `audio/visemes.json` (hình miệng theo frame, A4.4) | Node/Python + phân tích RMS |
| `compose` | `scenes.json`, `timings.json`, `visemes.json`, sprite, nền | `out/props.json` cho Remotion | Node |
| `render` | `props.json` | `out/final.mp4` (+ bản `--debug-safezone`) | Remotion + FFmpeg (loudnorm -14 LUFS) |
| `qa-check` | `final.mp4` | số đo cho `qa.md` | ffprobe/ffmpeg (skill `video-qa`) |

Yêu cầu chung:
- **Chốt chặn kịch bản (P6.4a):** mọi script kiểm tra `status.json` → `gates.script.approved = true` và `gates.script.version` trùng `version` trong `script.md`; sai → thoát với lỗi, không sinh file.
- Mỗi script chạy lại được độc lập (idempotent), có cache theo hash nội dung — sửa 1 câu thoại chỉ sinh lại audio câu đó.
- Mọi engine bên ngoài đi qua lớp adapter (`providers/`) để đổi được mà không sửa agent.
- Không gọi dịch vụ trả phí.
