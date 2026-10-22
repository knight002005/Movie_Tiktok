import { loadFont } from "@remotion/google-fonts/BeVietnamPro";
import { useCurrentFrame } from "remotion";
import type { LineCue } from "./timeline";

const { fontFamily } = loadFont("normal", { weights: ["800"], subsets: ["vietnamese", "latin"] });

export { fontFamily };

/**
 * Phụ đề karaoke nhẹ (rules/03-visual-style.md V3.9): màu theo nhân vật, từ đang đọc sáng trắng.
 * Tâm phụ đề ở y ≈ 1300, trong safe zone.
 */
export const Subtitle: React.FC<{ line: LineCue; color: string }> = ({ line, color }) => {
  // Trong <Sequence from={line.from}>, useCurrentFrame() là frame cục bộ; mốc từ là tuyệt đối.
  const frame = useCurrentFrame() + line.from;
  return (
    <div
      style={{
        position: "absolute",
        left: 90,
        width: 820,
        top: 1250,
        height: 180,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        textAlign: "center",
        fontFamily,
        fontWeight: 800,
        fontSize: 66,
        lineHeight: 1.18,
        WebkitTextStroke: "14px #111",
        paintOrder: "stroke fill",
        textShadow: "0 6px 12px rgba(0,0,0,0.35)",
      }}
    >
      <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "center", columnGap: 22, rowGap: 4 }}>
        {line.words.map((w, i) => {
          const active = frame >= w.from && frame < w.to;
          return (
            <span key={i} style={{ color: active ? "#ffffff" : color, scale: active ? "1.08" : "1" }}>
              {/* Lấy chữ từ kịch bản theo thứ tự từ để giữ dấu câu */}
              {line.text.split(/\s+/)[i] ?? w.text}
            </span>
          );
        })}
      </div>
    </div>
  );
};
