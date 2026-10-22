"""Diễn xuất bằng TTS (rules/04-audio-voice.md A4.3, A4.3a).

edge-tts tiếng Việt không có "style" cảm xúc, chỉ có rate / pitch / volume cho cả lần đọc.
Để giọng bớt "ngang", mỗi câu được dựng từ 3 lớp:
  1. Giọng gốc của nhân vật (voice_id + rate/pitch/volume cơ bản).
  2. Cảm xúc của câu × cường độ (1–5) × độ biểu cảm của nhân vật (tính cách).
  3. Ngữ điệu theo đoạn: tách câu ở dấu câu; câu hỏi lên giọng, câu cảm thán mạnh lên,
     "…" chậm lại và ngập ngừng — mỗi đoạn đọc với tham số riêng rồi ghép lại.
Sau đó áp hiệu ứng âm thanh theo cảm xúc (run giọng khi khóc, mỏng khi thì thầm…).
"""
import re
from dataclasses import dataclass

# Độ lệch so với giọng gốc ở cường độ 3/5. rate/volume: %, pitch: Hz.
# pause: hệ số nhân khoảng lặng giữa các đoạn; fx: hiệu ứng ffmpeg sau khi ghép.
EMOTIONS: dict[str, dict] = {
    "neutral":     {"rate": 0,   "pitch": 0,   "volume": 0,   "pause": 1.0, "fx": None},
    "smile":       {"rate": 6,   "pitch": 10,  "volume": 5,   "pause": 0.9, "fx": None},
    "happy":       {"rate": 10,  "pitch": 14,  "volume": 8,   "pause": 0.8, "fx": None},
    "panic":       {"rate": 18,  "pitch": 18,  "volume": 15,  "pause": 0.55, "fx": "shaky"},
    "angry":       {"rate": 10,  "pitch": -6,  "volume": 25,  "pause": 0.7, "fx": "angry"},
    "cold":        {"rate": -12, "pitch": -14, "volume": -5,  "pause": 1.4, "fx": None},
    "sad":         {"rate": -15, "pitch": -10, "volume": -12, "pause": 1.5, "fx": "soft"},
    "cry":         {"rate": -18, "pitch": 6,   "volume": -6,  "pause": 1.6, "fx": "cry"},
    "embarrassed": {"rate": 4,   "pitch": 8,   "volume": -10, "pause": 1.3, "fx": None},
    "surprised":   {"rate": 6,   "pitch": 22,  "volume": 12,  "pause": 0.9, "fx": None},
    "smirk":       {"rate": -6,  "pitch": 4,   "volume": 0,   "pause": 1.2, "fx": None},
    "threat":      {"rate": -14, "pitch": -12, "volume": -8,  "pause": 1.5, "fx": "close"},
    "whisper":     {"rate": -8,  "pitch": -4,  "volume": -35, "pause": 1.2, "fx": "whisper"},
    "love":        {"rate": -8,  "pitch": 6,   "volume": -6,  "pause": 1.3, "fx": "soft"},
}

# Chuỗi lọc ffmpeg cho hiệu ứng theo cảm xúc (không đổi thời lượng → mốc từ vẫn đúng).
FX_FILTERS: dict[str, str] = {
    "shaky": "tremolo=f=7:d=0.12",
    "angry": "acompressor=threshold=-20dB:ratio=4:attack=5:release=60,volume=2dB",
    "soft": "lowpass=f=5200",
    "cry": "tremolo=f=5.5:d=0.32,lowpass=f=6000",
    "close": "lowpass=f=4500,acompressor=threshold=-24dB:ratio=3",
    "whisper": "highpass=f=350,lowpass=f=4200,volume=4dB",
}

# Ngữ điệu theo dấu câu kết thúc đoạn (cộng thêm vào tham số của đoạn đó).
PUNCT_CONTOUR = {
    "?": {"pitch": 14, "rate": -2, "volume": 0},
    "!": {"pitch": 6, "rate": 6, "volume": 12},
    "…": {"pitch": -4, "rate": -12, "volume": -6},
    ".": {"pitch": -3, "rate": 0, "volume": 0},
    ",": {"pitch": 2, "rate": 0, "volume": 0},
}
# Khoảng lặng cơ bản sau mỗi loại dấu (ms), trước khi nhân hệ số "pause" của cảm xúc.
PUNCT_PAUSE_MS = {"?": 280, "!": 240, "…": 520, ".": 300, ",": 140, "": 0}

LIMITS = {"rate": (-50, 60), "pitch": (-40, 50), "volume": (-60, 50)}
# Mức lệch tối đa so với giọng gốc của nhân vật — vượt quá thì giọng biến dạng ("chuột chít", méo).
MAX_DELTA = {"rate": 30, "pitch": 25, "volume": 35}


@dataclass
class Segment:
    text: str
    rate: str
    pitch: str
    volume: str
    pause_after_ms: int


def _parse(value: str | int | float | None) -> float:
    if value is None:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)
    return float(re.sub(r"[^0-9.+-]", "", value) or 0)


def _fmt(kind: str, value: float) -> str:
    lo, hi = LIMITS[kind]
    v = int(round(max(lo, min(hi, value))))
    unit = "Hz" if kind == "pitch" else "%"
    return f"{'+' if v >= 0 else ''}{v}{unit}"


def split_phrases(text: str) -> list[tuple[str, str]]:
    """Tách câu thành (đoạn, dấu kết thúc). '...' được chuẩn hóa thành '…'."""
    text = text.replace("...", "…")
    parts = re.findall(r"[^,.!?…]+[,.!?…]*", text)
    out = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        m = re.search(r"[,.!?…]+$", p)
        punct = m.group(0) if m else ""
        key = "?" if "?" in punct else "!" if "!" in punct else "…" if "…" in punct else punct[:1]
        out.append((p, key))
    return out or [(text, "")]


def plan_segments(line: dict) -> tuple[list[Segment], str | None]:
    """Từ một câu thoại (giọng nhân vật + cảm xúc) → danh sách đoạn có tham số riêng + hiệu ứng."""
    emotion = EMOTIONS.get(line.get("emotion", "neutral"), EMOTIONS["neutral"])
    intensity = max(1, min(5, int(line.get("intensity", 3))))
    expressiveness = float(line.get("expressiveness", 1.0))
    k = (intensity / 3) * expressiveness

    base = {kind: _parse(line.get(kind)) for kind in ("rate", "pitch", "volume")}
    overrides = line.get("emotion_overrides", {}).get(line.get("emotion", "neutral"), {})
    phrases = split_phrases(line["text"])
    segments = []
    for i, (phrase, punct) in enumerate(phrases):
        contour = PUNCT_CONTOUR.get(punct, {"pitch": 0, "rate": 0, "volume": 0})
        vals = {}
        for kind in ("rate", "pitch", "volume"):
            delta = overrides.get(kind, emotion[kind]) * k + contour[kind] * min(1.5, expressiveness)
            cap = MAX_DELTA[kind]
            vals[kind] = base[kind] + max(-cap, min(cap, delta))
        is_last = i == len(phrases) - 1
        pause = 0 if is_last else int(PUNCT_PAUSE_MS.get(punct, 120) * emotion["pause"])
        segments.append(Segment(phrase, _fmt("rate", vals["rate"]), _fmt("pitch", vals["pitch"]),
                                _fmt("volume", vals["volume"]), pause))
    fx = overrides.get("fx", emotion["fx"])
    return segments, FX_FILTERS.get(fx) if fx else None
