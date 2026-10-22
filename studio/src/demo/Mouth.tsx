import type { MouthShape } from "./timeline";

const LIP = "#7a2a35";
const INNER = "#5a1622";
const TONGUE = "#e0707a";

/** Miệng anime vẽ bằng SVG, đặt tại gốc (0,0) — rules/04-audio-voice.md A4.4. */
export const Mouth: React.FC<{ shape: MouthShape; open: number }> = ({ shape, open }) => {
  switch (shape) {
    case "M":
      return <path d="M -13 0 Q 0 1.5 13 0" stroke={LIP} strokeWidth={3.5} fill="none" strokeLinecap="round" />;
    case "A": {
      const h = 24 * open;
      return (
        <g>
          <path d={`M -14 0 Q 0 -3 14 0 Q 10 ${h} 0 ${h} Q -10 ${h} -14 0 Z`} fill={INNER} stroke={LIP} strokeWidth={2} />
          <ellipse cx={0} cy={h * 0.72} rx={8} ry={h * 0.22} fill={TONGUE} />
        </g>
      );
    }
    case "O": {
      const h = 11 * open;
      return <ellipse cx={0} cy={h * 0.6} rx={8 * (0.8 + 0.2 * open)} ry={h} fill={INNER} stroke={LIP} strokeWidth={2} />;
    }
    case "E": {
      const h = 10 * open;
      return (
        <g>
          <path d={`M -17 0 Q 0 -2 17 0 Q 11 ${h} 0 ${h} Q -11 ${h} -17 0 Z`} fill={INNER} stroke={LIP} strokeWidth={2} />
          <path d="M -14 0.5 Q 0 -1 14 0.5 L 13 3 Q 0 2 -13 3 Z" fill="#fff" />
        </g>
      );
    }
    case "H": {
      const h = 13 * open;
      return <path d={`M -11 0 Q 0 -2 11 0 Q 7 ${h} 0 ${h} Q -7 ${h} -11 0 Z`} fill={INNER} stroke={LIP} strokeWidth={2} />;
    }
    default:
      return <path d="M -12 0 Q 0 4 12 0" stroke={LIP} strokeWidth={3} fill="none" strokeLinecap="round" />;
  }
};
