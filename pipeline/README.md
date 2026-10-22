# pipeline/ — Hậu kỳ tự động

| Script | Trạng thái | Đầu vào → Đầu ra |
|---|---|---|
| `voice.py` + `voice_emotion.py` | ✅ chạy được | `lines.json` → `<id>.mp3` + `timings.json`. Engine `vieneu` (mặc định, mỗi nhân vật một giọng, clone cảm xúc từ ghi âm mẫu) hoặc `edge`; lớp ngữ điệu cảm xúc theo tính cách nhân vật; cache theo nội dung |
| `align.py` | ✅ chạy được | Whisper căn mốc từng âm tiết theo chữ kịch bản + tỷ lệ khớp phát âm |
| `audition.py` | ✅ chạy được | file thử giọng → `cast-audition.mp3` + bảng khớp |
| `visemes.py` | ✅ chạy được | `timings.json` + audio → `visemes.json` (hình miệng X/M/A/O/E/H + độ mở theo frame, A4.4) |
| `finalize.py` | ✅ chạy được | render Remotion → MP4 chuẩn T2.1 (-14 LUFS, yuv420p, AAC 48k, faststart) |
| `qa_check.py` | ✅ chạy được | MP4 → bảng PASS/FAIL kỹ thuật + khung hình trích + `qa-metrics.json` |
| `sprites/sprite_gen.py` | ✅ code + notebook; ⚠️ chất lượng thật cần chạy trên Kaggle | spec nhân vật → sprite PNG trong suốt (pose × biểu cảm × mở/nhắm mắt) + manifest tọa độ + contact sheet |
| `compose` (scenes.json → props Remotion) | ⏳ chưa xây | Hiện demo dùng `studio/src/demo/timeline.ts` dựng tay |

## Lệnh mẫu (chạy từ thư mục gốc dự án)
```bash
python -I -X utf8 pipeline/voice.py --lines studio/src/demo/lines.json --out studio/public/demo
python -I pipeline/visemes.py  --timings studio/public/demo/timings.json --audio-dir studio/public/demo --out studio/src/demo/visemes.json
cd studio && npx remotion render Demo out/demo.mp4 && cd ..
python -I pipeline/finalize.py --in studio/out/demo.mp4 --out studio/out/demo-final.mp4
python -I pipeline/qa_check.py --video studio/out/demo-final.mp4 --expect-duration 12.03 --frames 0.5,3,9.2 --out-dir studio/out/qa
```

## Tạo sprite
- Kaggle (khuyến nghị): `python -I pipeline/sprites/build_notebook.py` → tải `pipeline/sprites/kaggle_sprites.ipynb` lên Kaggle → GPU + Internet → Run All → tải `sprites_out.zip`.
- Máy anh: GTX 1650 cần **cập nhật driver NVIDIA** (hiện 451.67, quá cũ cho PyTorch) mới dùng GPU được; 4GB VRAM chỉ hợp model SD1.5.
- Kiểm thử code trên CPU: `python -I pipeline/sprites/sprite_gen.py --spec pipeline/sprites/spec.cpu-test.json --out <scratch>` (model nhỏ, chỉ để chắc code chạy).

## Yêu cầu chung
- **Chốt chặn kịch bản (P6.4a):** khi có bước `compose` cho tập thật, mọi script kiểm tra `status.json` → `gates.script.approved = true` và `gates.script.version` trùng `version` trong `script.md`; sai → thoát với lỗi, không sinh file.
- Mỗi script chạy lại được độc lập, có cache theo nội dung khi có thể.
- Engine bên ngoài (TTS, model ảnh) đi qua tham số/cấu hình để đổi được mà không sửa agent.
- Không gọi dịch vụ trả phí. FFmpeg được tìm qua `FFMPEG_DIR` → PATH → thư mục cài của winget.
