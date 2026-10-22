# Danh sách ảnh cần tạo — Sếp Ơi, Em Không Cố Ý!

> casting-designer, 2026-10-22T00:10:00+07:00. Đường dẫn tính từ `series/sep-oi-em-khong-co-y/`.
> STYLE, NEGATIVE, LOCATION_STYLE, LOCATION_NEGATIVE, INSERT_STYLE: xem `bible.md` §10. Character tag: xem `characters/<id>/profile.md` §5 (trùng y nguyên `sprites.spec.json`).
> Đánh dấu ☑ khi ảnh đã tạo **và** anh đã soát (đúng nhân vật, không chữ, không lỗi tay).

## 0. Tổng số

| Nhóm | Số ảnh | Cách tạo |
|---|---|---|
| Ảnh gốc tham chiếu (`refs/p1_base`, `refs/p2_base` × 4 nhân vật) | 8 | Tự sinh khi chạy notebook — **duyệt trước**, không tính vào tổng |
| Sprite nhân vật (pose × biểu cảm × {thường, nhắm mắt}) | **156** | Notebook Kaggle `sprite_gen.py` (tự động) |
| Nền bối cảnh | **12** bắt buộc + 1 tùy chọn | Notebook Kaggle (mảng `locations` — chờ code tạo nền) |
| CG sự kiện (bible §9b) | **3** | **Tạo riêng, thủ công** |
| Insert vật thể (bible §9) | **6** (4 theo bible + 2 đề xuất) | Tạo riêng, thủ công (cùng model) |
| **Tổng cần tạo** | **177** (178 nếu dùng phòng trọ) | |

Chi tiết sprite: Linh 40 · Khải 36 · Vy 40 · Tùng 40.

## 1. Cách tạo (miễn phí)

1. **Sprite (ưu tiên):** build notebook rồi chạy trên Kaggle (GPU T4/P100 miễn phí theo hạn mức tuần):
   `python -I pipeline/sprites/build_notebook.py --spec series/sep-oi-em-khong-co-y/sprites.spec.json --out series/sep-oi-em-khong-co-y/kaggle_sprites.ipynb`
   - Chạy thử trước: `--only linh --max-expr 2` → soát `refs/p1_base.png`, `refs/p2_base.png`. Đạt thì chạy cả 4 nhân vật.
   - Mỗi nhân vật trả `sprites/` (PNG nền trong suốt, cao 1800px), `manifest.json` (tọa độ mặt/mắt/miệng → điền vào `profile.md` mục `sprites.poses.<pose>.mouth/eyes`), `contact_sheet.jpg` (soát nhất quán tại GATE-SERIES).
   - Tải về, chép `sprites/*.png` vào `characters/<id>/sprites/`, `refs/*_base.png` vào `characters/<id>/refs/`.
   - Ước tính: ~35 giây/biểu cảm (ảnh + nhắm mắt) → cả 4 nhân vật dưới 1 giờ GPU.
2. **Nền:** khi code đọc mảng `locations` đã có, chạy cùng notebook. Trong lúc chờ: dùng chính model và `LOCATION_STYLE` trên Kaggle/Colab bằng ô lệnh text2img thường (768×1344, seed trong spec), biến thể thứ hai img2img từ biến thể đầu (strength ~0.55) để giữ bố cục; phóng lên 1440×2560.
3. **CG & insert (thủ công):** cùng model `animagine-xl-4.0`, cùng STYLE/NEGATIVE (V3.1). Gợi ý: dùng sprite/ảnh gốc đã duyệt làm ảnh tham chiếu (IP-Adapter) hoặc img2img; với CG hai người, có thể ghép thô hai sprite lên nền rồi img2img (strength 0.45–0.6) để giữ đúng mặt và trang phục. **Mọi chữ, số, giờ trên giấy/điện thoại do code vẽ đè** (V3.12) — ảnh luôn để giấy trống.
4. **Tách nền:** sprite đã tự tách (rembg `isnet-anime`). Nền, CG, insert giữ nguyên nền.
5. Công cụ web tạo ảnh miễn phí chỉ dùng dự phòng — kiểm tra điều khoản thương mại và sẽ khó giữ nhất quán.

## 2. Ảnh gốc tham chiếu (duyệt trước khi chạy hết)

| File đích | Prompt (phần thay đổi) | Trạng thái |
|---|---|---|
| characters/linh/refs/p1_base.png | p1, neutral | ☐ |
| characters/linh/refs/p2_base.png | p2, neutral | ☐ |
| characters/khai/refs/p1_base.png | p1, neutral | ☐ |
| characters/khai/refs/p2_base.png | p2, neutral | ☐ |
| characters/vy/refs/p1_base.png | p1, neutral | ☐ |
| characters/vy/refs/p2_base.png | p2, neutral | ☐ |
| characters/tung/refs/p1_base.png | p1, neutral | ☐ |
| characters/tung/refs/p2_base.png | p2, neutral | ☐ |

## 3. Sprite nhân vật

Prompt đầy đủ = `STYLE, <character tag>, <POSE>, <EXPRESSION>, FRAMING`. Cột dưới chỉ ghi phần thay đổi.

### 3.1 Linh (seed 24101) — p1: đứng, tay buông · p2: cầm ly cà phê giấy — 40 ảnh

| File đích | Prompt (phần thay đổi) | Trạng thái |
|---|---|---|
| characters/linh/sprites/p1_neutral.png | p1, neutral | ☐ |
| characters/linh/sprites/p1_neutral_blink.png | p1, neutral, eyes closed | ☐ |
| characters/linh/sprites/p1_smile.png | p1, smile | ☐ |
| characters/linh/sprites/p1_smile_blink.png | p1, smile, eyes closed | ☐ |
| characters/linh/sprites/p1_angry.png | p1, angry | ☐ |
| characters/linh/sprites/p1_angry_blink.png | p1, angry, eyes closed | ☐ |
| characters/linh/sprites/p1_sad.png | p1, sad | ☐ |
| characters/linh/sprites/p1_sad_blink.png | p1, sad, eyes closed | ☐ |
| characters/linh/sprites/p1_surprised.png | p1, surprised | ☐ |
| characters/linh/sprites/p1_surprised_blink.png | p1, surprised, eyes closed | ☐ |
| characters/linh/sprites/p1_embarrassed.png | p1, embarrassed | ☐ |
| characters/linh/sprites/p1_embarrassed_blink.png | p1, embarrassed, eyes closed | ☐ |
| characters/linh/sprites/p1_cold.png | p1, cold | ☐ |
| characters/linh/sprites/p1_cold_blink.png | p1, cold, eyes closed | ☐ |
| characters/linh/sprites/p1_cry.png | p1, cry | ☐ |
| characters/linh/sprites/p1_cry_blink.png | p1, cry, eyes closed | ☐ |
| characters/linh/sprites/p1_panic.png | p1, panic | ☐ |
| characters/linh/sprites/p1_panic_blink.png | p1, panic, eyes closed | ☐ |
| characters/linh/sprites/p1_love.png | p1, love | ☐ |
| characters/linh/sprites/p1_love_blink.png | p1, love, eyes closed | ☐ |
| characters/linh/sprites/p2_neutral.png | p2, neutral | ☐ |
| characters/linh/sprites/p2_neutral_blink.png | p2, neutral, eyes closed | ☐ |
| characters/linh/sprites/p2_smile.png | p2, smile | ☐ |
| characters/linh/sprites/p2_smile_blink.png | p2, smile, eyes closed | ☐ |
| characters/linh/sprites/p2_angry.png | p2, angry | ☐ |
| characters/linh/sprites/p2_angry_blink.png | p2, angry, eyes closed | ☐ |
| characters/linh/sprites/p2_sad.png | p2, sad | ☐ |
| characters/linh/sprites/p2_sad_blink.png | p2, sad, eyes closed | ☐ |
| characters/linh/sprites/p2_surprised.png | p2, surprised | ☐ |
| characters/linh/sprites/p2_surprised_blink.png | p2, surprised, eyes closed | ☐ |
| characters/linh/sprites/p2_embarrassed.png | p2, embarrassed | ☐ |
| characters/linh/sprites/p2_embarrassed_blink.png | p2, embarrassed, eyes closed | ☐ |
| characters/linh/sprites/p2_cold.png | p2, cold | ☐ |
| characters/linh/sprites/p2_cold_blink.png | p2, cold, eyes closed | ☐ |
| characters/linh/sprites/p2_cry.png | p2, cry | ☐ |
| characters/linh/sprites/p2_cry_blink.png | p2, cry, eyes closed | ☐ |
| characters/linh/sprites/p2_panic.png | p2, panic | ☐ |
| characters/linh/sprites/p2_panic_blink.png | p2, panic, eyes closed | ☐ |
| characters/linh/sprites/p2_love.png | p2, love | ☐ |
| characters/linh/sprites/p2_love_blink.png | p2, love, eyes closed | ☐ |

### 3.2 Khải (seed 29201) — p1: đứng thẳng · p2: khoanh tay — 36 ảnh

| File đích | Prompt (phần thay đổi) | Trạng thái |
|---|---|---|
| characters/khai/sprites/p1_neutral.png | p1, neutral | ☐ |
| characters/khai/sprites/p1_neutral_blink.png | p1, neutral, eyes closed | ☐ |
| characters/khai/sprites/p1_smile.png | p1, smile | ☐ |
| characters/khai/sprites/p1_smile_blink.png | p1, smile, eyes closed | ☐ |
| characters/khai/sprites/p1_angry.png | p1, angry | ☐ |
| characters/khai/sprites/p1_angry_blink.png | p1, angry, eyes closed | ☐ |
| characters/khai/sprites/p1_sad.png | p1, sad | ☐ |
| characters/khai/sprites/p1_sad_blink.png | p1, sad, eyes closed | ☐ |
| characters/khai/sprites/p1_surprised.png | p1, surprised | ☐ |
| characters/khai/sprites/p1_surprised_blink.png | p1, surprised, eyes closed | ☐ |
| characters/khai/sprites/p1_embarrassed.png | p1, embarrassed | ☐ |
| characters/khai/sprites/p1_embarrassed_blink.png | p1, embarrassed, eyes closed | ☐ |
| characters/khai/sprites/p1_cold.png | p1, cold | ☐ |
| characters/khai/sprites/p1_cold_blink.png | p1, cold, eyes closed | ☐ |
| characters/khai/sprites/p1_cry.png | p1, cry | ☐ |
| characters/khai/sprites/p1_cry_blink.png | p1, cry, eyes closed | ☐ |
| characters/khai/sprites/p1_love.png | p1, love | ☐ |
| characters/khai/sprites/p1_love_blink.png | p1, love, eyes closed | ☐ |
| characters/khai/sprites/p2_neutral.png | p2, neutral | ☐ |
| characters/khai/sprites/p2_neutral_blink.png | p2, neutral, eyes closed | ☐ |
| characters/khai/sprites/p2_smile.png | p2, smile | ☐ |
| characters/khai/sprites/p2_smile_blink.png | p2, smile, eyes closed | ☐ |
| characters/khai/sprites/p2_angry.png | p2, angry | ☐ |
| characters/khai/sprites/p2_angry_blink.png | p2, angry, eyes closed | ☐ |
| characters/khai/sprites/p2_sad.png | p2, sad | ☐ |
| characters/khai/sprites/p2_sad_blink.png | p2, sad, eyes closed | ☐ |
| characters/khai/sprites/p2_surprised.png | p2, surprised | ☐ |
| characters/khai/sprites/p2_surprised_blink.png | p2, surprised, eyes closed | ☐ |
| characters/khai/sprites/p2_embarrassed.png | p2, embarrassed | ☐ |
| characters/khai/sprites/p2_embarrassed_blink.png | p2, embarrassed, eyes closed | ☐ |
| characters/khai/sprites/p2_cold.png | p2, cold | ☐ |
| characters/khai/sprites/p2_cold_blink.png | p2, cold, eyes closed | ☐ |
| characters/khai/sprites/p2_cry.png | p2, cry | ☐ |
| characters/khai/sprites/p2_cry_blink.png | p2, cry, eyes closed | ☐ |
| characters/khai/sprites/p2_love.png | p2, love | ☐ |
| characters/khai/sprites/p2_love_blink.png | p2, love, eyes closed | ☐ |

### 3.3 Vy (seed 27301) — p1: ôm máy tính bảng · p2: chống hông — 40 ảnh

| File đích | Prompt (phần thay đổi) | Trạng thái |
|---|---|---|
| characters/vy/sprites/p1_neutral.png | p1, neutral | ☐ |
| characters/vy/sprites/p1_neutral_blink.png | p1, neutral, eyes closed | ☐ |
| characters/vy/sprites/p1_smile.png | p1, smile | ☐ |
| characters/vy/sprites/p1_smile_blink.png | p1, smile, eyes closed | ☐ |
| characters/vy/sprites/p1_angry.png | p1, angry | ☐ |
| characters/vy/sprites/p1_angry_blink.png | p1, angry, eyes closed | ☐ |
| characters/vy/sprites/p1_sad.png | p1, sad | ☐ |
| characters/vy/sprites/p1_sad_blink.png | p1, sad, eyes closed | ☐ |
| characters/vy/sprites/p1_surprised.png | p1, surprised | ☐ |
| characters/vy/sprites/p1_surprised_blink.png | p1, surprised, eyes closed | ☐ |
| characters/vy/sprites/p1_embarrassed.png | p1, embarrassed | ☐ |
| characters/vy/sprites/p1_embarrassed_blink.png | p1, embarrassed, eyes closed | ☐ |
| characters/vy/sprites/p1_cold.png | p1, cold | ☐ |
| characters/vy/sprites/p1_cold_blink.png | p1, cold, eyes closed | ☐ |
| characters/vy/sprites/p1_cry.png | p1, cry | ☐ |
| characters/vy/sprites/p1_cry_blink.png | p1, cry, eyes closed | ☐ |
| characters/vy/sprites/p1_smirk.png | p1, smirk | ☐ |
| characters/vy/sprites/p1_smirk_blink.png | p1, smirk, eyes closed | ☐ |
| characters/vy/sprites/p1_panic.png | p1, panic | ☐ |
| characters/vy/sprites/p1_panic_blink.png | p1, panic, eyes closed | ☐ |
| characters/vy/sprites/p2_neutral.png | p2, neutral | ☐ |
| characters/vy/sprites/p2_neutral_blink.png | p2, neutral, eyes closed | ☐ |
| characters/vy/sprites/p2_smile.png | p2, smile | ☐ |
| characters/vy/sprites/p2_smile_blink.png | p2, smile, eyes closed | ☐ |
| characters/vy/sprites/p2_angry.png | p2, angry | ☐ |
| characters/vy/sprites/p2_angry_blink.png | p2, angry, eyes closed | ☐ |
| characters/vy/sprites/p2_sad.png | p2, sad | ☐ |
| characters/vy/sprites/p2_sad_blink.png | p2, sad, eyes closed | ☐ |
| characters/vy/sprites/p2_surprised.png | p2, surprised | ☐ |
| characters/vy/sprites/p2_surprised_blink.png | p2, surprised, eyes closed | ☐ |
| characters/vy/sprites/p2_embarrassed.png | p2, embarrassed | ☐ |
| characters/vy/sprites/p2_embarrassed_blink.png | p2, embarrassed, eyes closed | ☐ |
| characters/vy/sprites/p2_cold.png | p2, cold | ☐ |
| characters/vy/sprites/p2_cold_blink.png | p2, cold, eyes closed | ☐ |
| characters/vy/sprites/p2_cry.png | p2, cry | ☐ |
| characters/vy/sprites/p2_cry_blink.png | p2, cry, eyes closed | ☐ |
| characters/vy/sprites/p2_smirk.png | p2, smirk | ☐ |
| characters/vy/sprites/p2_smirk_blink.png | p2, smirk, eyes closed | ☐ |
| characters/vy/sprites/p2_panic.png | p2, panic | ☐ |
| characters/vy/sprites/p2_panic_blink.png | p2, panic, eyes closed | ☐ |

### 3.4 Tùng (seed 27401) — p1: tay đút túi hoodie · p2: cầm điện thoại — 40 ảnh

| File đích | Prompt (phần thay đổi) | Trạng thái |
|---|---|---|
| characters/tung/sprites/p1_neutral.png | p1, neutral | ☐ |
| characters/tung/sprites/p1_neutral_blink.png | p1, neutral, eyes closed | ☐ |
| characters/tung/sprites/p1_smile.png | p1, smile | ☐ |
| characters/tung/sprites/p1_smile_blink.png | p1, smile, eyes closed | ☐ |
| characters/tung/sprites/p1_angry.png | p1, angry | ☐ |
| characters/tung/sprites/p1_angry_blink.png | p1, angry, eyes closed | ☐ |
| characters/tung/sprites/p1_sad.png | p1, sad | ☐ |
| characters/tung/sprites/p1_sad_blink.png | p1, sad, eyes closed | ☐ |
| characters/tung/sprites/p1_surprised.png | p1, surprised | ☐ |
| characters/tung/sprites/p1_surprised_blink.png | p1, surprised, eyes closed | ☐ |
| characters/tung/sprites/p1_embarrassed.png | p1, embarrassed | ☐ |
| characters/tung/sprites/p1_embarrassed_blink.png | p1, embarrassed, eyes closed | ☐ |
| characters/tung/sprites/p1_cold.png | p1, cold | ☐ |
| characters/tung/sprites/p1_cold_blink.png | p1, cold, eyes closed | ☐ |
| characters/tung/sprites/p1_cry.png | p1, cry | ☐ |
| characters/tung/sprites/p1_cry_blink.png | p1, cry, eyes closed | ☐ |
| characters/tung/sprites/p1_panic.png | p1, panic | ☐ |
| characters/tung/sprites/p1_panic_blink.png | p1, panic, eyes closed | ☐ |
| characters/tung/sprites/p1_smirk.png | p1, smirk | ☐ |
| characters/tung/sprites/p1_smirk_blink.png | p1, smirk, eyes closed | ☐ |
| characters/tung/sprites/p2_neutral.png | p2, neutral | ☐ |
| characters/tung/sprites/p2_neutral_blink.png | p2, neutral, eyes closed | ☐ |
| characters/tung/sprites/p2_smile.png | p2, smile | ☐ |
| characters/tung/sprites/p2_smile_blink.png | p2, smile, eyes closed | ☐ |
| characters/tung/sprites/p2_angry.png | p2, angry | ☐ |
| characters/tung/sprites/p2_angry_blink.png | p2, angry, eyes closed | ☐ |
| characters/tung/sprites/p2_sad.png | p2, sad | ☐ |
| characters/tung/sprites/p2_sad_blink.png | p2, sad, eyes closed | ☐ |
| characters/tung/sprites/p2_surprised.png | p2, surprised | ☐ |
| characters/tung/sprites/p2_surprised_blink.png | p2, surprised, eyes closed | ☐ |
| characters/tung/sprites/p2_embarrassed.png | p2, embarrassed | ☐ |
| characters/tung/sprites/p2_embarrassed_blink.png | p2, embarrassed, eyes closed | ☐ |
| characters/tung/sprites/p2_cold.png | p2, cold | ☐ |
| characters/tung/sprites/p2_cold_blink.png | p2, cold, eyes closed | ☐ |
| characters/tung/sprites/p2_cry.png | p2, cry | ☐ |
| characters/tung/sprites/p2_cry_blink.png | p2, cry, eyes closed | ☐ |
| characters/tung/sprites/p2_panic.png | p2, panic | ☐ |
| characters/tung/sprites/p2_panic_blink.png | p2, panic, eyes closed | ☐ |
| characters/tung/sprites/p2_smirk.png | p2, smirk | ☐ |
| characters/tung/sprites/p2_smirk_blink.png | p2, smirk, eyes closed | ☐ |

## 4. Nền bối cảnh (≥ 1440×2560, không người, không chữ)

Prompt đầy đủ = `LOCATION_STYLE, <prompt bối cảnh>, <biến thể>` (xem `sprites.spec.json` → `locations` và `locations/<id>/profile.md`).

| File đích | Seed | Prompt (phần thay đổi) | Trạng thái |
|---|---|---|---|
| locations/loc-thang-may/loc-thang-may_day.png | 51001 | trong cabin thang máy, inox + gương mờ, sáng | ☐ |
| locations/loc-thang-may/loc-thang-may_lobby.png | 51001 | sảnh chờ, hai cửa thang máy, sàn đá, ánh ngày | ☐ |
| locations/loc-van-phong/loc-van-phong_day.png | 51101 | văn phòng mở, bàn Linh dán giấy nhớ, nắng sáng | ☐ |
| locations/loc-van-phong/loc-van-phong_night.png | 51101 | như trên, đêm xanh tím, vài đèn bàn | ☐ |
| locations/loc-phong-truong-phong/loc-phong-truong-phong_day.png | 51201 | phòng kính, cửa mở bên trái, máy in nhỏ, xanh băng | ☐ |
| locations/loc-phong-truong-phong/loc-phong-truong-phong_night.png | 51201 | như trên, đèn bàn vàng, đêm | ☐ |
| locations/loc-phong-hop/loc-phong-hop_day.png | 51301 | bàn họp dài, màn hình lớn tắt | ☐ |
| locations/loc-pantry/loc-pantry_day.png | 51401 | máy pha cà phê bên phải, nắng ấm | ☐ |
| locations/loc-goc-may-in/loc-goc-may-in_day.png | 51501 | máy in lớn + thùng rác cạnh bên, đèn trắng | ☐ |
| locations/loc-goc-may-in/loc-goc-may-in_night.png | 51501 | như trên, hành lang tối, một đèn trần | ☐ |
| locations/loc-san-thuong/loc-san-thuong_day.png | 51601 | lan can, ghế, trời xanh | ☐ |
| locations/loc-san-thuong/loc-san-thuong_dusk.png | 51601 | như trên, hoàng hôn cam hồng | ☐ |
| locations/loc-phong-tro-linh/loc-phong-tro-linh_night.png *(tùy chọn)* | 51701 | phòng trọ nhỏ, chăn vàng, dây đèn, đêm | ☐ |

## 5. CG sự kiện (bible §9b) — **tạo riêng, thủ công**

Đường dẫn đề xuất `cg/<cg-id>.png` (P6.1 chưa có thư mục CG — xem điểm cần anh quyết). Khổ ≥ 1440×2560 (dọc). Cùng model, STYLE, NEGATIVE như sprite; seed ghi lại sau khi chọn được ảnh.
Negative cho CG: `NEGATIVE` **bỏ** `multiple people` (CG có hai người/hai bàn tay), **thêm** `kiss, hug, embrace, holding hands, touching face, text on paper, writing, blood`.

| File đích | Prompt (phần mô tả, ghép sau STYLE) | Ghi chú | Trạng thái |
|---|---|---|---|
| cg/cg-ep01-ca-phe.png | `close-up, cropped view of a man's white dress shirt and the tip of a navy blue necktie, a plain paper coffee cup tipping over and splashing coffee onto the shirt, a small blank yellow sticky note stuck on the wet shirt hem, a woman's hand in a mustard yellow cardigan sleeve holding the cup, inside an elevator with brushed steel walls, dynamic angle, motion, no faces visible, vertical composition` | Tạo riêng, thủ công. Không lộ mặt. Dùng lại cho flashback ep06–07 | ☐ |
| cg/cg-ep07-giay-toc.png | `1girl, 1boy, view from outside an open office doorway at night, door frame in the foreground at the left and right edges of the frame, inside a minimalist manager's office with glass walls, a tall adult man, 29 years old, short neat black hair, white dress shirt, navy blue necktie, silver wristwatch, standing at arm's length, leaning slightly forward and carefully picking a small yellow sticky note out of the woman's hair with two fingers, an adult woman, 24 years old, dark brown high ponytail with a yellow pencil in her hair tie, mustard yellow cardigan over cream blouse, standing still and looking up, slightly embarrassed, both fully clothed, polite distance between them, both characters in the center third of the frame, desk cluttered with documents and scattered blank yellow sticky notes, small office printer with spilled coffee, warm desk lamp light, at the bottom edge of the frame a hand in a lime green hoodie sleeve holding a takeout food bag, vertical composition` | Tạo riêng, thủ công. **Một file duy nhất**: bản nguyên = ảnh gốc ep11; bản crop (code cắt, bỏ khung cửa + túi đồ ăn) = ảnh cắt ep08–09. Hai người phải nằm ở 1/3 giữa khung để crop không mất đầu. Khung hình phải thể hiện rõ khoảng cách và cửa mở (C5.2, bible §14.2). Hình vẽ "Sếp Tủ Lạnh" trên tờ giấy do code vẽ | ☐ |
| cg/cg-ep12-thang-may.png | `close-up of two hands inside an elevator, a woman's hand in a mustard yellow cardigan sleeve and a man's hand in a white shirt cuff with a silver metal wristwatch, each holding a plain paper coffee cup, the two cups lightly touching, no coffee spilled, a small blank yellow sticky note stuck on the man's cup, brushed stainless steel elevator wall in the background, warm soft light, no faces visible, vertical composition` | Tạo riêng, thủ công. Chữ "Câu trả lời: Có." do code vẽ lên tờ giấy nhớ | ☐ |

## 6. Insert vật thể (bible §9) — tạo riêng, thủ công

Đường dẫn đề xuất `inserts/<id>.png`. Prompt = `INSERT_STYLE` (bible §10) + mô tả; negative = `LOCATION_NEGATIVE`. Giấy luôn **trống** — chữ do code vẽ.

| File đích | Prompt (mô tả) | Dùng cho | Trạng thái |
|---|---|---|---|
| inserts/insert-giay-nho-ca-phe.png | `a single blank yellow sticky note with a dried brown coffee stain, slightly curled corner, on a dark wooden desk, close-up, top-down view` | ep01, ep06 (tờ giấy trong sổ Khải), ep11 | ☐ |
| inserts/insert-giay-a4-trang.png | `a single blank white A4 sheet of paper with faint empty form lines, no writing, lying flat on a light desk, top-down view` | Đơn trang 1, trang 2 (bản sạch), đơn nghỉ việc, danh sách phiếu kín in ra | ☐ |
| inserts/insert-giay-a4-nhau.png | `a crumpled then flattened blank white A4 sheet, heavy wrinkles, slightly torn edge, printer roller marks, no writing, top-down view` | Trang 2 kẹt máy (ep10) | ☐ |
| inserts/insert-may-in-khay.png | `close-up of an office printer output tray with a blank white sheet coming out, soft light, no logo, no display text` | ep08 (máy hành lang + "in lại ở phòng nhân sự"), ep09 cliff, ep10 | ☐ |
| inserts/insert-thung-rac-giay-nho.png *(đề xuất)* | `office trash bin with several crumpled blank yellow sticky notes on top, close-up, soft daylight` | ep02 cliff (Vy vò giấy nhớ), ep03 | ☐ |
| inserts/insert-thung-rac-don.png *(đề xuất)* | `office trash bin at night with one crumpled white sheet of paper on top, partially unfolded crease, dim light, close-up` | ep10 (đơn nghỉ việc vò; chữ "NGHỈ VIỆC" ở nếp gấp do code vẽ) | ☐ |

## 7. Sau khi có ảnh
- Điền tọa độ `mouth {x, y, w}`, `eyes {x, y}` từ `manifest.json` vào `characters/<id>/profile.md`; kiểm tra bằng lớp debug của `studio/`.
- Cập nhật `series.json` → `assets_ready.characters.<id>` / `assets_ready.locations.<id>` (phiên chính).
- Soát `contact_sheet.jpg` của từng nhân vật tại GATE-SERIES: tóc, mắt, trang phục, phụ kiện giống hệt giữa mọi biểu cảm (V3.3); sai lệch → tạo lại.
