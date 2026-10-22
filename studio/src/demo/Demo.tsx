import { Audio } from "@remotion/media";
import {
  AbsoluteFill,
  Easing,
  interpolate,
  random,
  Sequence,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { Character } from "./Character";
import { Flash, OfficeBackground, SafeZoneOverlay, SpeedLines } from "./Scenery";
import { fontFamily, Subtitle } from "./Subtitle";
import { END_CARD_FROM, LINES, lineAt, mouthAt } from "./timeline";

export type DemoProps = { showSafeZone: boolean };

const LINH_COLOR = "#ff9ec4";
// Tâm camera đặt vào mặt nhân vật để zoom không đẩy mặt ra khỏi safe zone.
const ORIGIN = "540px 880px";

const [L1, L2, L3] = LINES;
// Cú quick-zoom của câu 3 rơi đúng chữ "trưởng" (từ thứ 5).
const SHOCK_FRAME = L3.words[4].from;

const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

const cameraScale = (frame: number): number => {
  if (frame < L2.from) {
    return interpolate(frame, [L1.from, L2.from], [1, 1.12], { ...clamp, easing: Easing.bezier(0.33, 0, 0.67, 1) });
  }
  if (frame < L3.from) {
    return interpolate(frame, [L2.from, L3.from], [1.38, 1.45], clamp);
  }
  if (frame < SHOCK_FRAME) {
    return 1.15;
  }
  // Zoom tối đa 1.6 để miệng vẫn nằm trên phụ đề (V3.5).
  return interpolate(frame, [SHOCK_FRAME, SHOCK_FRAME + 5, END_CARD_FROM], [1.15, 1.55, 1.6], {
    ...clamp,
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });
};

const shake = (frame: number): string => {
  const local = frame - SHOCK_FRAME;
  if (local < 0 || local > 10) return "0px 0px";
  const amp = 14 * (1 - local / 10);
  return `${(random(`sx${local}`) - 0.5) * 2 * amp}px ${(random(`sy${local}`) - 0.5) * 2 * amp}px`;
};

export const Demo: React.FC<DemoProps> = ({ showSafeZone }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const line = lineAt(frame);

  return (
    <AbsoluteFill style={{ backgroundColor: "#111" }}>
      {/* Lớp camera: nền + nhân vật cùng zoom/rung */}
      <AbsoluteFill style={{ transformOrigin: ORIGIN, scale: String(cameraScale(frame)), translate: shake(frame) }}>
        <OfficeBackground />
        <div style={{ position: "absolute", left: 90, top: 470, width: 900, height: 1350 }}>
          <Character expression={line.expression} mouth={mouthAt(frame)} fps={fps} />
        </div>
      </AbsoluteFill>

      {/* Hook: đường tốc độ trong 0,8 giây đầu */}
      <Sequence durationInFrames={Math.round(0.8 * fps)}>
        <SpeedLines durationInFrames={Math.round(0.8 * fps)} cx={540} cy={880} />
      </Sequence>
      <Sequence from={SHOCK_FRAME} durationInFrames={10}>
        <Flash />
      </Sequence>

      {/* Thoại + phụ đề */}
      {LINES.map((l) => (
        <Sequence key={l.id} from={l.from} durationInFrames={l.audioFrames} layout="none">
          <Audio src={staticFile(`demo/${l.id}.mp3`)} />
        </Sequence>
      ))}
      {LINES.map((l) => (
        <Sequence key={`sub-${l.id}`} from={l.from} durationInFrames={l.speechFrames + 8} layout="none">
          <Subtitle line={l} color={LINH_COLOR} />
        </Sequence>
      ))}

      {/* "Phần X · Tên series" trong 2 giây đầu (T2.3) */}
      <Sequence durationInFrames={2 * fps} layout="none">
        <div
          style={{
            position: "absolute",
            left: 70,
            top: 190,
            fontFamily,
            fontWeight: 800,
            fontSize: 34,
            color: "white",
            padding: "8px 18px",
            borderRadius: 12,
            background: "rgba(0,0,0,0.45)",
          }}
        >
          Phần 1 · Demo kỹ thuật
        </div>
      </Sequence>

      {/* End card (R1.F3) */}
      <Sequence from={END_CARD_FROM} layout="none">
        <EndCard />
      </Sequence>

      {showSafeZone ? <SafeZoneOverlay /> : null}
    </AbsoluteFill>
  );
};

const EndCard: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill
      style={{
        backgroundColor: `rgba(10,10,20,${interpolate(frame, [0, 8], [0, 0.82], clamp)})`,
        justifyContent: "center",
        alignItems: "center",
        fontFamily,
        fontWeight: 800,
        color: "white",
      }}
    >
      <div
        style={{
          fontSize: 120,
          opacity: interpolate(frame, [4, 12], [0, 1], clamp),
          translate: `0px ${interpolate(frame, [4, 14], [40, 0], { ...clamp, easing: Easing.bezier(0.16, 1, 0.3, 1) })}px`,
        }}
      >
        Phần 2 →
      </div>
      <div style={{ fontSize: 44, marginTop: 24, opacity: interpolate(frame, [10, 18], [0, 0.9], clamp) }}>
        Theo dõi để xem tiếp
      </div>
    </AbsoluteFill>
  );
};
