import { random, useCurrentFrame } from "remotion";
import { Mouth } from "./Mouth";
import type { Expression, MouthShape } from "./timeline";

// Nhân vật TẠM vẽ bằng SVG để kiểm chứng kỹ thuật (khẩu hình, chớp mắt, biểu cảm).
// Sprite thật sẽ là PNG từ model ảnh; lớp miệng/mắt dùng lại đúng cơ chế này (V3.3).

const HAIR = "#4a2e24";
const HAIR_LIGHT = "#6d4536";
const SKIN = "#ffe5d6";
const SKIN_SHADE = "#f3c9b5";
const LINE = "#3b2219";
const IRIS = "#8a4b2a";

export const MOUTH_ANCHOR = { x: 300, y: 398 };

const BROWS: Record<Expression, [string, string]> = {
  neutral: ["M 222 250 Q 250 240 280 247", "M 320 247 Q 350 240 378 250"],
  panic: ["M 222 252 Q 252 240 280 230", "M 320 230 Q 348 240 378 252"],
  surprised: ["M 220 236 Q 250 218 280 230", "M 320 230 Q 350 218 380 236"],
  embarrassed: ["M 222 250 Q 252 242 280 236", "M 320 236 Q 348 242 378 250"],
};

/** Lịch chớp mắt ngẫu nhiên nhưng cố định theo seed: mỗi 2,5–5 giây, mỗi lần 5 frame. */
const isBlinking = (frame: number, fps: number): boolean => {
  let t = Math.round(1.2 * fps);
  let i = 0;
  while (t <= frame) {
    if (frame < t + 5) return frame >= t + 1 && frame <= t + 3;
    t += Math.round((2.5 + random(`blink-${i}`) * 2.5) * fps);
    i++;
  }
  return false;
};

const Eye: React.FC<{ cx: number; expression: Expression; closed: boolean }> = ({ cx, expression, closed }) => {
  const cy = 305;
  if (closed) {
    return <path d={`M ${cx - 30} ${cy} Q ${cx} ${cy + 12} ${cx + 30} ${cy}`} stroke={LINE} strokeWidth={5} fill="none" strokeLinecap="round" />;
  }
  const wide = expression === "panic" || expression === "surprised";
  const ry = wide ? 40 : expression === "embarrassed" ? 30 : 36;
  const irisR = expression === "surprised" ? 14 : expression === "panic" ? 18 : 22;
  const look = expression === "embarrassed" ? -8 : 0; // nhìn lảng sang một bên
  return (
    <g>
      <ellipse cx={cx} cy={cy} rx={30} ry={ry} fill="#fff" />
      <ellipse cx={cx + look} cy={cy + 4} rx={irisR} ry={irisR * 1.3} fill={IRIS} />
      <ellipse cx={cx + look} cy={cy + 8} rx={irisR * 0.5} ry={irisR * 0.7} fill="#2b130b" />
      <circle cx={cx + look - irisR * 0.35} cy={cy - irisR * 0.45} r={irisR * 0.32} fill="#fff" />
      <circle cx={cx + look + irisR * 0.4} cy={cy + irisR * 0.5} r={irisR * 0.15} fill="#fff" />
      <path
        d={`M ${cx - 34} ${cy - ry * 0.55} Q ${cx} ${cy - ry - 8} ${cx + 34} ${cy - ry * 0.55}`}
        stroke={LINE}
        strokeWidth={7}
        fill="none"
        strokeLinecap="round"
      />
    </g>
  );
};

export const Character: React.FC<{
  expression: Expression;
  mouth: [MouthShape, number];
  fps: number;
}> = ({ expression, mouth, fps }) => {
  const frame = useCurrentFrame();
  const closed = isBlinking(frame, fps);
  const speaking = mouth[0] !== "X";
  const breathe = Math.sin((frame / fps) * Math.PI * 0.5) * 4;
  const tilt = speaking ? Math.sin(frame * 0.18) * 1.2 : 0;
  const [browL, browR] = BROWS[expression];

  return (
    <svg viewBox="0 0 600 900" width="100%" height="100%" style={{ overflow: "visible" }}>
      {/* Thân */}
      <g transform={`translate(0 ${breathe * 0.5})`}>
        <path d="M 140 900 Q 140 570 228 522 L 278 500 L 322 500 L 372 522 Q 460 570 460 900 Z" fill="#f4ecd8" stroke="#d9cbb0" strokeWidth={3} />
        <path d="M 278 500 L 300 560 L 322 500" fill="#fffaf0" stroke="#d9cbb0" strokeWidth={3} />
        <rect x={278} y={430} width={44} height={75} fill={SKIN_SHADE} />
      </g>

      <g transform={`translate(0 ${breathe}) rotate(${tilt} 300 420)`}>
        {/* Tóc sau */}
        <path d="M 172 262 Q 158 132 300 118 Q 442 132 428 262 L 446 498 Q 404 526 382 470 L 218 470 Q 196 526 154 498 Z" fill={HAIR} />
        {/* Mặt */}
        <path d="M 196 240 Q 192 362 256 422 Q 284 448 300 450 Q 316 448 344 422 Q 408 362 404 240 Q 400 150 300 148 Q 200 150 196 240 Z" fill={SKIN} />
        <path d="M 240 432 Q 300 462 360 432 Q 330 452 300 452 Q 270 452 240 432 Z" fill={SKIN_SHADE} opacity={0.6} />

        {/* Má hồng khi ngượng */}
        {expression === "embarrassed" ? (
          <g opacity={0.75}>
            <ellipse cx={238} cy={372} rx={26} ry={11} fill="#ff8fa3" />
            <ellipse cx={362} cy={372} rx={26} ry={11} fill="#ff8fa3" />
            {[-12, 0, 12].map((dx) => (
              <g key={dx}>
                <line x1={232 + dx} y1={378} x2={240 + dx} y2={366} stroke="#e8607a" strokeWidth={2} />
                <line x1={356 + dx} y1={378} x2={364 + dx} y2={366} stroke="#e8607a" strokeWidth={2} />
              </g>
            ))}
          </g>
        ) : null}

        <Eye cx={250} expression={expression} closed={closed} />
        <Eye cx={350} expression={expression} closed={closed} />
        <path d={browL} stroke={HAIR} strokeWidth={6} fill="none" strokeLinecap="round" />
        <path d={browR} stroke={HAIR} strokeWidth={6} fill="none" strokeLinecap="round" />
        <path d="M 298 362 Q 303 370 297 375" stroke="#d9a08a" strokeWidth={2.5} fill="none" strokeLinecap="round" />

        <g transform={`translate(${MOUTH_ANCHOR.x} ${MOUTH_ANCHOR.y})`}>
          <Mouth shape={mouth[0]} open={mouth[1]} />
        </g>

        {/* Tóc mái + kẹp ngôi sao */}
        <path
          d="M 184 262 Q 186 146 300 136 Q 414 146 416 262 Q 404 206 372 192 Q 362 238 332 248 Q 338 206 312 186 Q 290 232 248 242 Q 262 206 246 196 Q 214 218 204 272 Z"
          fill={HAIR}
        />
        <path d="M 230 168 Q 280 150 330 160" stroke={HAIR_LIGHT} strokeWidth={8} fill="none" strokeLinecap="round" opacity={0.7} />
        <polygon points="388,196 394,210 409,211 397,220 401,235 388,226 375,235 379,220 367,211 382,210" fill="#f2c14e" stroke="#c9952a" strokeWidth={2} />

        {/* Giọt mồ hôi anime khi bối rối */}
        {expression === "embarrassed" ? (
          <path d="M 420 205 Q 434 232 428 246 Q 418 258 408 246 Q 402 232 420 205 Z" fill="#a8dcff" stroke="#5fa8d8" strokeWidth={2.5} />
        ) : null}
      </g>
    </svg>
  );
};
