# Ghi âm mẫu cảm xúc cho từng nhân vật (A4.2, A4.3a)

VieNeu-TTS **sao chép cả giọng lẫn cảm xúc** từ đoạn ghi âm mẫu. Muốn nhân vật giận thật, buồn thật → cần một đoạn mẫu **người thật diễn** cảm xúc đó.
Chưa có ghi âm → hệ thống dùng giọng mẫu VieNeu của nhân vật + lớp ngữ điệu tự động (đã chạy được).

## Cấu trúc
```
voices/
├─ linh/  neutral.wav  angry.wav  sad.wav  panic.wav  embarrassed.wav  surprised.wav  whisper.wav  cry.wav ...
├─ khai/  neutral.wav  cold.wav  angry.wav  love.wav ...
├─ vy/    neutral.wav  smirk.wav  threat.wav  angry.wav  cry.wav ...
└─ tung/  neutral.wav  happy.wav  panic.wav  embarrassed.wav ...
```
Tên file = tên cảm xúc trong `pipeline/voice_emotion.py`. Thứ tự hệ thống chọn: `<cảm xúc>.wav` → `neutral.wav` → giọng mẫu VieNeu.

## Mỗi nhân vật = MỘT người đọc
Giọng clone sẽ mang âm sắc của người ghi âm. Bốn nhân vật cần **bốn người khác nhau** (hoặc ít nhất khác giới/vùng miền rõ rệt), nếu không các nhân vật sẽ nghe giống nhau.

## Cách thu (điện thoại là đủ)
1. Phòng yên tĩnh, không quạt/điều hòa ồn, điện thoại cách miệng ~20 cm.
2. Mỗi file **3–8 giây**, một câu trọn vẹn, **diễn đúng cảm xúc** — nói như đang đóng phim, không đọc như đọc bài.
3. Câu nói nên là câu của chính nhân vật (lấy trong kịch bản hoặc `voice-tests/cast-audition.json`).
4. Lưu WAV (hoặc m4a/mp3 rồi đổi): `ffmpeg -i input.m4a -ac 1 -ar 48000 angry.wav`.
5. Chạy thử: `python -I -X utf8 pipeline/audition.py --lines series/sep-oi-em-khong-co-y/voice-tests/cast-audition.json` → nghe `voice-tests/cast-audition.mp3`.

## Bắt buộc: sự đồng ý của người cho giọng
- **Không** dùng giọng người nổi tiếng, giọng cắt từ video/phim/podcast, hay giọng người quen khi chưa đồng ý (A4.2, C5.6).
- Người cho giọng ký đồng ý theo mẫu dưới đây; lưu bản ký **ngoài repo** (có thông tin cá nhân). Ghi vào `CONSENT.md` chỉ: tên vai, ngày, nơi lưu bản ký.

### Mẫu đồng ý cho giọng (tham khảo — không thay thế tư vấn pháp lý)
> Tôi, ____________, đồng ý cho kênh ____________ sử dụng giọng nói tôi ghi âm ngày ___/___/____ để tạo giọng AI cho nhân vật "________" trong series "Sếp Ơi, Em Không Cố Ý!" và các nội dung liên quan, kể cả nội dung có kiếm tiền trên TikTok và nền tảng khác.
> Giọng AI chỉ dùng cho nhân vật hư cấu trong phim; không dùng để mạo danh tôi hay người khác.
> Tôi có thể rút lại sự đồng ý bằng văn bản; khi đó kênh ngừng tạo nội dung mới bằng giọng của tôi.
> Thù lao: ____________ (hoặc: không có thù lao).
> Ký tên: ____________  Ngày: ___/___/____
