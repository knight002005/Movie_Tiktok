import timings from "./timings.json";
import visemes from "./visemes.json";

export const FPS = 30;
export const WIDTH = 1080;
export const HEIGHT = 1920;

export type Expression = "panic" | "embarrassed" | "surprised" | "neutral";
export type MouthShape = "X" | "M" | "A" | "O" | "E" | "H";

type Word = { text: string; start: number; end: number };
type Timing = { duration_s: number; words: Word[] };

export type LineCue = {
  id: string;
  text: string;
  expression: Expression;
  /** Khung hình bắt đầu (tuyệt đối trong video) */
  from: number;
  /** Số frame của file audio */
  audioFrames: number;
  /** Số frame tới hết từ cuối cùng */
  speechFrames: number;
  words: { text: string; from: number; to: number }[];
  mouth: [MouthShape, number][];
};

// Đạo diễn demo: câu thoại, biểu cảm, khoảng lặng sau câu (giây).
const DIRECTION: { id: string; text: string; expression: Expression; pauseAfter: number }[] = [
  { id: "l01", text: "Chờ em với! Cửa thang máy sắp đóng rồi!", expression: "panic", pauseAfter: 0.5 },
  { id: "l02", text: "Trời ơi… em làm đổ cà phê lên áo anh rồi.", expression: "embarrassed", pauseAfter: 0.6 },
  { id: "l03", text: "Khoan đã… anh là trưởng phòng mới sao?", expression: "surprised", pauseAfter: 1.2 },
];

const LEAD_IN_S = 0.4;
export const END_CARD_FRAMES = Math.round(1.6 * FPS);

const t = timings as Record<string, Timing>;
const v = visemes as unknown as { fps: number; lines: Record<string, [MouthShape, number][]> };

const buildLines = (): LineCue[] => {
  let cursor = LEAD_IN_S;
  return DIRECTION.map((d) => {
    const timing = t[d.id];
    const from = Math.round(cursor * FPS);
    const lastEnd = timing.words[timing.words.length - 1].end;
    cursor += lastEnd + d.pauseAfter;
    return {
      id: d.id,
      text: d.text,
      expression: d.expression,
      from,
      audioFrames: Math.ceil(timing.duration_s * FPS),
      speechFrames: Math.ceil(lastEnd * FPS),
      words: timing.words.map((w) => ({
        text: w.text,
        from: from + Math.round(w.start * FPS),
        to: from + Math.round(w.end * FPS),
      })),
      mouth: v.lines[d.id],
    };
  });
};

export const LINES = buildLines();

const last = LINES[LINES.length - 1];
export const END_CARD_FROM =
  last.from + last.speechFrames + Math.round(DIRECTION[DIRECTION.length - 1].pauseAfter * FPS);
export const TOTAL_FRAMES = END_CARD_FROM + END_CARD_FRAMES;

/** Câu thoại đang "sở hữu" khung hình (để chọn biểu cảm/phụ đề). */
export const lineAt = (frame: number): LineCue => {
  let current = LINES[0];
  for (const line of LINES) {
    if (frame >= line.from) current = line;
  }
  return current;
};

/** Hình miệng tại khung hình tuyệt đối. Ngoài câu thoại → X. */
export const mouthAt = (frame: number): [MouthShape, number] => {
  for (const line of LINES) {
    const local = frame - line.from;
    if (local >= 0 && local < line.mouth.length) return line.mouth[local];
  }
  return ["X", 0];
};
