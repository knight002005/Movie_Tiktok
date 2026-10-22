import { AbsoluteFill, interpolate, random, useCurrentFrame } from "remotion";
import { HEIGHT, WIDTH } from "./timeline";

/** Nền văn phòng TẠM vẽ bằng SVG (ảnh nền thật: rules/03-visual-style.md V3.4). */
export const OfficeBackground: React.FC = () => (
  <svg viewBox={`0 0 ${WIDTH} ${HEIGHT}`} width={WIDTH} height={HEIGHT}>
    <defs>
      <linearGradient id="wall" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stopColor="#e9eff6" />
        <stop offset="1" stopColor="#c9d6e4" />
      </linearGradient>
      <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
        <stop offset="0" stopColor="#9fd0f0" />
        <stop offset="1" stopColor="#e4f3fb" />
      </linearGradient>
    </defs>
    <rect width={WIDTH} height={HEIGHT} fill="url(#wall)" />
    <rect x={90} y={260} width={900} height={760} rx={12} fill="url(#sky)" stroke="#9aa9ba" strokeWidth={10} />
    {[0, 1, 2, 3, 4, 5, 6, 7].map((i) => (
      <rect
        key={i}
        x={110 + i * 110}
        y={1020 - 180 - random(`b${i}`) * 420}
        width={90}
        height={600}
        fill={i % 2 ? "#b8c9db" : "#a7bbd0"}
      />
    ))}
    <rect x={90} y={630} width={900} height={8} fill="#9aa9ba" />
    <rect x={535} y={260} width={10} height={760} fill="#9aa9ba" />
    <rect x={0} y={1420} width={WIDTH} height={500} fill="#8d9fb3" />
    <rect x={0} y={1420} width={WIDTH} height={18} fill="#7a8ca0" />
  </svg>
);

/** fx.speed-lines — đường tốc độ hướng tâm (V3.8). */
export const SpeedLines: React.FC<{ durationInFrames: number; cx: number; cy: number }> = ({
  durationInFrames,
  cx,
  cy,
}) => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill
      style={{
        opacity: interpolate(frame, [0, 3, durationInFrames - 6, durationInFrames], [0, 1, 1, 0], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        }),
      }}
    >
      <svg viewBox={`0 0 ${WIDTH} ${HEIGHT}`} width={WIDTH} height={HEIGHT}>
        {new Array(70).fill(0).map((_, i) => {
          const angle = random(`a${i}-${Math.floor(frame / 2)}`) * Math.PI * 2;
          const inner = 430 + random(`r${i}`) * 220;
          const outer = 1400;
          return (
            <line
              key={i}
              x1={cx + Math.cos(angle) * inner}
              y1={cy + Math.sin(angle) * inner}
              x2={cx + Math.cos(angle) * outer}
              y2={cy + Math.sin(angle) * outer}
              stroke="#1d1d2b"
              strokeWidth={2 + random(`w${i}`) * 6}
              opacity={0.55}
            />
          );
        })}
      </svg>
    </AbsoluteFill>
  );
};

/** fx.shock-flash — chớp trắng (V3.8). */
export const Flash: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill
      style={{
        backgroundColor: "white",
        opacity: interpolate(frame, [0, 2, 9], [0, 0.85, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }),
      }}
    />
  );
};

/** Lớp debug safe zone (rules/02-tiktok-platform.md T2.2). */
export const SafeZoneOverlay: React.FC = () => {
  const red = "rgba(255,0,0,0.28)";
  return (
    <AbsoluteFill>
      <div style={{ position: "absolute", left: 0, top: 0, width: WIDTH, height: 160, background: red }} />
      <div style={{ position: "absolute", left: 0, top: 1440, width: WIDTH, height: HEIGHT - 1440, background: red }} />
      <div style={{ position: "absolute", left: 940, top: 160, width: WIDTH - 940, height: 1280, background: red }} />
      <div style={{ position: "absolute", left: 0, top: 160, width: 60, height: 1280, background: red }} />
      <div
        style={{
          position: "absolute",
          left: 60,
          top: 160,
          width: 880,
          height: 1280,
          border: "4px dashed rgba(0,200,0,0.9)",
          boxSizing: "border-box",
        }}
      />
    </AbsoluteFill>
  );
};
