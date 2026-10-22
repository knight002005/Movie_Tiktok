"""Căn mốc thời gian từng âm tiết cho audio KHÔNG có sẵn mốc (VieNeu-TTS, giọng người thật).

Cách làm: faster-whisper nhận dạng có word_timestamps → đối chiếu với văn bản kịch bản (đã biết trước)
bằng SequenceMatcher trên âm tiết bỏ dấu → âm tiết khớp lấy mốc của Whisper, âm tiết lệch nội suy
giữa hai hàng xóm. Phụ đề và khẩu hình luôn dùng CHỮ CỦA KỊCH BẢN, chỉ mượn thời gian của Whisper.

Đồng thời trả `match` = tỷ lệ âm tiết Whisper nghe ĐÚNG CẢ DẤU — câu < 0,85 nên được anh nghe lại
(có thể TTS đọc sai, hoặc Whisper nghe nhầm).
"""
import re
import subprocess
import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import find_ffmpeg  # noqa: E402

_MODEL = None
TAG_RE = re.compile(r"\[[^\]]*\]")  # thẻ cảm xúc VieNeu như [thở dài] — không đọc thành chữ
PUNCT_RE = re.compile(r"[^\w]", re.UNICODE)


def model(size: str = "small"):
    global _MODEL
    if _MODEL is None:
        from faster_whisper import WhisperModel

        _MODEL = WhisperModel(size, device="cpu", compute_type="int8")
    return _MODEL


def load_pcm(path: Path) -> np.ndarray:
    raw = subprocess.run(
        [find_ffmpeg(), "-v", "error", "-i", str(path), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
        capture_output=True, check=True,
    ).stdout
    return np.frombuffer(raw, np.float32)


def script_syllables(text: str) -> list[str]:
    """Âm tiết của kịch bản (giữ dấu thanh, bỏ dấu câu và thẻ cảm xúc)."""
    text = TAG_RE.sub(" ", text).replace("...", "…")
    return [s for s in (PUNCT_RE.sub("", tok) for tok in text.split()) if s]


def _base(s: str) -> str:
    """Bỏ mọi dấu để so khớp vị trí: 'trưởng' → 'truong'."""
    d = unicodedata.normalize("NFD", s.lower().replace("đ", "d"))
    return "".join(c for c in d if unicodedata.category(c) != "Mn")


def align(audio: Path, text: str) -> tuple[list[dict], float]:
    syllables = script_syllables(text)
    pcm = load_pcm(audio)
    duration = len(pcm) / 16000
    # Không truyền kịch bản làm initial_prompt: gợi ý sẽ kéo Whisper "nghe ra" đúng kịch bản → tỷ lệ khớp ảo.
    segments, _ = model().transcribe(pcm, language="vi", word_timestamps=True)

    heard: list[tuple[str, float, float]] = []
    for seg in segments:
        for w in seg.words or []:
            parts = [p for p in (PUNCT_RE.sub("", x) for x in w.word.split()) if p]
            if not parts:
                continue
            span = (w.end - w.start) / len(parts)
            for i, p in enumerate(parts):
                heard.append((p, w.start + i * span, w.start + (i + 1) * span))

    times: list[tuple[float, float] | None] = [None] * len(syllables)
    exact = 0
    sm = SequenceMatcher(a=[_base(s) for s in syllables], b=[_base(h[0]) for h in heard], autojunk=False)
    for block in sm.get_matching_blocks():
        for k in range(block.size):
            i, j = block.a + k, block.b + k
            times[i] = (heard[j][1], heard[j][2])
            exact += syllables[i].lower() == heard[j][0].lower()

    # Nội suy những âm tiết Whisper bỏ sót / nghe lệch.
    i = 0
    while i < len(times):
        if times[i] is not None:
            i += 1
            continue
        j = i
        while j < len(times) and times[j] is None:
            j += 1
        left = times[i - 1][1] if i > 0 else 0.05
        right = times[j][0] if j < len(times) else max(left + 0.25 * (j - i), duration - 0.1)
        step = max(0.08, (right - left) / (j - i))
        for k in range(i, j):
            times[k] = (left + (k - i) * step, left + (k - i + 1) * step)
        i = j

    words = [{"text": s, "start": round(t[0], 3), "end": round(t[1], 3)} for s, t in zip(syllables, times)]
    return words, round(exact / max(1, len(syllables)), 2)
