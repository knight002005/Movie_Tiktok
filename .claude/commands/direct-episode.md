---
description: Phân cảnh lại (scenes.json) cho một tập đã duyệt kịch bản
argument-hint: <series-slug> <epNN>
---

Phân cảnh: $ARGUMENTS

1. Kiểm tra `episodes/epNN/status.json` → `gates.script.approved = true`. Chưa duyệt → dừng.
2. Nếu đã có `scenes.json` → đổi tên bản cũ thành `scenes.prev.json`.
3. Gọi **director** (`subagent_type: director`).
4. Kiểm tra JSON hợp lệ bằng Node; đối chiếu nhanh: mọi `line.text` có trong `script.md`.
5. Cập nhật state `directed` + history. Báo số cảnh, số shot, thời lượng ước tính.
