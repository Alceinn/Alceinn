import math
import os
import xml.etree.ElementTree as ET

def generate_smooth_orbiting_blackholes_svg():
    """
    Ultra-smooth, organic black-hole merger simulation for Gojo's Hollow Purple:
    - NO detached floating orbit rings / dashed circles causing visual clutter.
    - Soft, gorgeous gravitational lensing and celestial glow around Blue & Red.
    - Black Hole inspiral physics:
        Blue starts at (240, 190), Red starts at (940, 190).
        Center is (590, 190).
        0% - 30%: Gentle approach towards center, breathing gravitational auras.
        30% - 78%: Smooth circular / spiral inspiral around each other (2.5 orbits).
                   Radius gracefully shrinks from 260px down to 8px.
                   Calculated with dozens of dense, continuous keyframe steps (cos/sin),
                   guaranteeing silky smooth, perfectly fluid motion with zero jerky jumps!
        78% - 81%: Fusion into Singularity at (590, 190).
        81% - 94%: Supernova Hollow Purple blast (nebula burst + shock rings, bounded).
        94% - 100%: Graceful fade & loop reset.
    - Incantations appear above with clean, smooth opacity transitions, zero overlap.
    """

    total_steps = 100
    blue_kf = []
    red_kf = []

    cx, cy = 590, 190
    init_blue_x, init_red_x = 240, 940
    start_r = 350.0

    for step in range(total_steps + 1):
        pct = step # 0 to 100 %

        if pct <= 30:
            # Stage 1: Linear & smooth deceleration towards orbit entry distance (r = 220)
            t_stage = pct / 30.0
            # Ease out
            ease = math.sin(t_stage * math.pi / 2.0)
            curr_r = start_r - (start_r - 220.0) * ease
            bx = cx - curr_r
            by = cy
            rx = cx + curr_r
            ry = cy
            scale = 1.0 + 0.1 * math.sin(t_stage * math.pi)
            op = min(1.0, pct / 4.0)

        elif pct <= 78:
            # Stage 2: Inspiral (Two orbiting black holes coalescing)
            # 30% to 78% is 48% of the cycle
            t_stage = (pct - 30.0) / 48.0
            # 2.2 complete graceful revolutions
            revolutions = 2.2
            angle = t_stage * revolutions * 2.0 * math.pi

            # Radius smoothly decays from 220 down to 6 px
            r_decay = (1.0 - t_stage) ** 1.3
            curr_r = 220.0 * r_decay + 6.0

            # Blue position (starts on left side, angle = 0 is left: -cos)
            bx = cx - curr_r * math.cos(angle)
            by = cy - curr_r * math.sin(angle) * 0.58 # slightly elliptical perspective

            # Red position (diametrically opposite)
            rx = cx + curr_r * math.cos(angle)
            ry = cy + curr_r * math.sin(angle) * 0.58

            scale = 1.05 + 0.35 * t_stage
            op = 1.0

        elif pct <= 81:
            # Stage 3: Immediate singularity collapse at exact center
            t_stage = (pct - 78.0) / 3.0
            bx, by = cx, cy
            rx, ry = cx, cy
            scale = max(0.01, 1.4 * (1.0 - t_stage))
            op = max(0.0, 1.0 - t_stage)

        else:
            # Stage 4: Supernova phase (Blue and Red merged)
            bx, by = cx, cy
            rx, ry = cx, cy
            scale = 0.0
            op = 0.0

        blue_kf.append(f"{pct}% {{ transform: translate({bx - 160:.2f}px, {by - 190:.2f}px) scale({scale:.3f}); opacity: {op:.3f}; }}")
        red_kf.append(f"{pct}% {{ transform: translate({rx - 1020:.2f}px, {ry - 190:.2f}px) scale({scale:.3f}); opacity: {op:.3f}; }}")

    blue_kf_str = "\n        ".join(blue_kf)
    red_kf_str = "\n        ".join(red_kf)

    svg_code = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 340" width="1180" height="340" fill="none" overflow="hidden">
  <defs>
    <style><![CDATA[
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap');
      .font-sans {{ font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif; }}

      /* ========================================================================= */
      /* ULTRA-SMOOTH BLACK HOLE INSPIRAL TIMELINE (16 SECONDS TOTAL)               */
      /* ========================================================================= */

      @keyframes blue-orbit-smooth {{
        {blue_kf_str}
      }}

      @keyframes red-orbit-smooth {{
        {red_kf_str}
      }}

      /* SINGULARITY PULSE & EXPLOSION */
      @keyframes purple-supernova {{
        0%, 78% {{ transform: scale(0); opacity: 0; }}
        80% {{ transform: scale(0.3); opacity: 0.9; }}
        82% {{ transform: scale(1.1); opacity: 1; }}
        86% {{ transform: scale(2.0); opacity: 0.95; }}
        93% {{ transform: scale(2.8); opacity: 0; }}
        100% {{ transform: scale(0); opacity: 0; }}
      }}

      /* SHOCKWAVE RINGS */
      @keyframes shockwave-outer {{
        0%, 79% {{ transform: scale(0.01); opacity: 0; }}
        81% {{ transform: scale(0.4); opacity: 0.95; }}
        89% {{ transform: scale(3.5); opacity: 0.5; }}
        95% {{ transform: scale(5.8); opacity: 0; }}
        100% {{ transform: scale(0); opacity: 0; }}
      }}

      @keyframes shockwave-inner {{
        0%, 80.5% {{ transform: scale(0.01); opacity: 0; }}
        82.5% {{ transform: scale(0.5); opacity: 0.85; }}
        90% {{ transform: scale(4.2); opacity: 0.35; }}
        96% {{ transform: scale(6.5); opacity: 0; }}
        100% {{ transform: scale(0); opacity: 0; }}
      }}

      @keyframes beam-burst {{
        0%, 79% {{ opacity: 0; transform: scaleX(0.05); }}
        81.5% {{ opacity: 1; transform: scaleX(1); }}
        88% {{ opacity: 0.85; transform: scaleX(1.3); }}
        94% {{ opacity: 0; transform: scaleX(1.8); }}
        100% {{ opacity: 0; }}
      }}

      /* ========================================================================= */
      /* SEQUENTIAL INCANTATIONS HUD (SOFT, CLEAR, ZERO OVERLAP)                   */
      /* ========================================================================= */
      @keyframes phase-1 {{
        0% {{ opacity: 0; transform: translateY(6px); }}
        3% {{ opacity: 1; transform: translateY(0); }}
        17% {{ opacity: 1; transform: translateY(0); }}
        21% {{ opacity: 0; transform: translateY(-6px); }}
        22%, 100% {{ opacity: 0; }}
      }}

      @keyframes phase-2 {{
        0%, 21% {{ opacity: 0; }}
        24% {{ opacity: 0; transform: translateY(6px); }}
        27% {{ opacity: 1; transform: translateY(0); }}
        38% {{ opacity: 1; transform: translateY(0); }}
        42% {{ opacity: 0; transform: translateY(-6px); }}
        43%, 100% {{ opacity: 0; }}
      }}

      @keyframes phase-3 {{
        0%, 42% {{ opacity: 0; }}
        45% {{ opacity: 0; transform: translateY(6px); }}
        48% {{ opacity: 1; transform: translateY(0); }}
        59% {{ opacity: 1; transform: translateY(0); }}
        63% {{ opacity: 0; transform: translateY(-6px); }}
        64%, 100% {{ opacity: 0; }}
      }}

      @keyframes phase-4 {{
        0%, 63% {{ opacity: 0; }}
        66% {{ opacity: 0; transform: translateY(6px); }}
        69% {{ opacity: 1; transform: translateY(0); }}
        76% {{ opacity: 1; transform: translateY(0); }}
        80% {{ opacity: 0; transform: translateY(-6px); }}
        81%, 100% {{ opacity: 0; }}
      }}

      @keyframes phase-5 {{
        0%, 79% {{ opacity: 0; transform: scale(0.92); }}
        82% {{ opacity: 1; transform: scale(1.04); }}
        93% {{ opacity: 1; transform: scale(1); }}
        97% {{ opacity: 0; transform: scale(1.08); }}
        100% {{ opacity: 0; }}
      }}

      .anim-blue-bh {{ animation: blue-orbit-smooth 16s linear infinite; }}
      .anim-red-bh  {{ animation: red-orbit-smooth 16s linear infinite; }}
      .anim-nova    {{ animation: purple-supernova 16s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 190px; }}
      .anim-ring1   {{ animation: shockwave-outer 16s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 190px; }}
      .anim-ring2   {{ animation: shockwave-inner 16s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 190px; }}
      .anim-beam    {{ animation: beam-burst 16s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 190px; }}

      .hud-p1 {{ animation: phase-1 16s ease-in-out infinite; }}
      .hud-p2 {{ animation: phase-2 16s ease-in-out infinite; }}
      .hud-p3 {{ animation: phase-3 16s ease-in-out infinite; }}
      .hud-p4 {{ animation: phase-4 16s ease-in-out infinite; }}
      .hud-p5 {{ animation: phase-5 16s ease-in-out infinite; }}
    ]]></style>

    <!-- Boundary clip to ensure 0% overflow outside card -->
    <clipPath id="card-bounds">
      <rect x="0" y="0" width="1180" height="340" rx="18" />
    </clipPath>

    <!-- Deep Void Canvas Gradient -->
    <radialGradient id="canvas-void" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#0E0922" />
      <stop offset="55%" stop-color="#060412" />
      <stop offset="100%" stop-color="#030208" />
    </radialGradient>

    <!-- Soft Black Hole Blue Gravitational Lens Gradient -->
    <radialGradient id="blue-bh-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="20%" stop-color="#7DD3FC" />
      <stop offset="55%" stop-color="#0284C7" stop-opacity="0.8" />
      <stop offset="80%" stop-color="#0369A1" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#082F49" stop-opacity="0" />
    </radialGradient>

    <!-- Soft Black Hole Red Gravitational Lens Gradient -->
    <radialGradient id="red-bh-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="20%" stop-color="#FDA4AF" />
      <stop offset="55%" stop-color="#E11D48" stop-opacity="0.8" />
      <stop offset="80%" stop-color="#BE123C" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#4C0519" stop-opacity="0" />
    </radialGradient>

    <!-- Hollow Purple Singularity Detonation Gradient -->
    <radialGradient id="purple-singularity" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="22%" stop-color="#F5D0FE" />
      <stop offset="50%" stop-color="#C084FC" />
      <stop offset="78%" stop-color="#7E22CE" />
      <stop offset="100%" stop-color="#3B0764" stop-opacity="0" />
    </radialGradient>

    <!-- Horizontal Laser Surge Gradient -->
    <linearGradient id="surge-laser" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0" />
      <stop offset="25%" stop-color="#38BDF8" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="1" />
      <stop offset="75%" stop-color="#FB7185" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0" />
    </linearGradient>

    <!-- Lensing Filters -->
    <filter id="soft-lens" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="7" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="hyper-lens" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="12" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Deep Velvet Space Canvas -->
  <rect width="1180" height="340" rx="18" fill="url(#canvas-void)" stroke="rgba(255,255,255,0.12)" stroke-width="1.2" />

  <!-- Strictly clipped scene (no element ever escapes the card) -->
  <g clip-path="url(#card-bounds)">

    <!-- Subtle Celestial Latitude Grid (No floating circles!) -->
    <g opacity="0.08">
      <line x1="0" y1="100" x2="1180" y2="100" stroke="#FFFFFF" stroke-dasharray="4 8" />
      <line x1="0" y1="190" x2="1180" y2="190" stroke="#FFFFFF" stroke-dasharray="4 8" />
      <line x1="0" y1="280" x2="1180" y2="280" stroke="#FFFFFF" stroke-dasharray="4 8" />
    </g>

    <!-- ========================================================================= -->
    <!-- CHANT HUD (TOP CENTER, ZERO OVERLAP, 100% HIGH LEGIBILITY)                -->
    <!-- ========================================================================= -->
    <g class="font-sans" transform="translate(590, 52)">
      <!-- Phase 1: 九綱 -->
      <g class="hud-p1" text-anchor="middle">
        <rect x="-230" y="-28" width="460" height="56" rx="28" fill="rgba(2,132,199,0.12)" stroke="rgba(56,189,248,0.5)" stroke-width="1.2" />
        <text x="0" y="-4" fill="#38BDF8" font-size="18" font-weight="900" letter-spacing="4">九 綱</text>
        <text x="0" y="16" fill="#FFFFFF" font-size="11" font-weight="700" letter-spacing="2">INCANTATION PHASE 01 : NINE ROPES</text>
      </g>

      <!-- Phase 2: 偏光 -->
      <g class="hud-p2" text-anchor="middle">
        <rect x="-240" y="-28" width="480" height="56" rx="28" fill="rgba(225,29,72,0.12)" stroke="rgba(251,113,133,0.5)" stroke-width="1.2" />
        <text x="0" y="-4" fill="#FB7185" font-size="18" font-weight="900" letter-spacing="4">偏 光</text>
        <text x="0" y="16" fill="#FFFFFF" font-size="11" font-weight="700" letter-spacing="2">INCANTATION PHASE 02 : POLARIZED LIGHT</text>
      </g>

      <!-- Phase 3: 烏と声明 -->
      <g class="hud-p3" text-anchor="middle">
        <rect x="-260" y="-28" width="520" height="56" rx="28" fill="rgba(168,85,247,0.14)" stroke="rgba(192,132,252,0.5)" stroke-width="1.2" />
        <text x="0" y="-4" fill="#C084FC" font-size="18" font-weight="900" letter-spacing="4">烏 と 声 明</text>
        <text x="0" y="16" fill="#FFFFFF" font-size="11" font-weight="700" letter-spacing="2">INCANTATION PHASE 03 : CROW &amp; DECLARATION</text>
      </g>

      <!-- Phase 4: 表裏の間 -->
      <g class="hud-p4" text-anchor="middle">
        <rect x="-260" y="-28" width="520" height="56" rx="28" fill="rgba(147,51,234,0.16)" stroke="rgba(232,121,249,0.5)" stroke-width="1.2" />
        <text x="0" y="-4" fill="#E879F9" font-size="18" font-weight="900" letter-spacing="4">表 裏 の 間</text>
        <text x="0" y="16" fill="#FFFFFF" font-size="11" font-weight="700" letter-spacing="2">INCANTATION PHASE 04 : BETWEEN FRONT &amp; BACK</text>
      </g>

      <!-- Phase 5: 虚式「茈」 -->
      <g class="hud-p5" text-anchor="middle">
        <rect x="-280" y="-30" width="560" height="60" rx="30" fill="rgba(10,5,24,0.96)" stroke="#C084FC" stroke-width="1.8" filter="url(#soft-lens)" />
        <text x="0" y="-5" fill="#FFFFFF" font-size="20" font-weight="900" letter-spacing="3">虚 式 「 茈 」</text>
        <text x="0" y="17" fill="#E879F9" font-size="11.5" font-weight="800" letter-spacing="2">UNRESTRICTED HOLLOW PURPLE · 200% OUTPUT</text>
      </g>
    </g>

    <!-- ========================================================================= -->
    <!-- BLUE BLACK HOLE (術式順転「蒼」) - ORBITING ENTITY                        -->
    <!-- ========================================================================= -->
    <g class="anim-blue-bh">
      <!-- Soft Gravitational Lensing Aura -->
      <circle cx="160" cy="190" r="70" fill="url(#blue-bh-glow)" filter="url(#hyper-lens)" opacity="0.85" />
      <!-- Event Horizon Core -->
      <circle cx="160" cy="190" r="32" fill="url(#blue-bh-glow)" filter="url(#soft-lens)" />
      <!-- Radiant Singularity Center -->
      <circle cx="160" cy="190" r="14" fill="#FFFFFF" />

      <!-- Minimal Soft Technique Label (Follows Orb) -->
      <text x="160" y="242" fill="#38BDF8" font-size="12" font-weight="800" letter-spacing="1" text-anchor="middle" class="font-sans">術式順転「蒼」</text>
      <text x="160" y="255" fill="rgba(255,255,255,0.4)" font-size="9" font-weight="600" letter-spacing="1.5" text-anchor="middle" class="font-sans">LAPSE: BLUE</text>
    </g>

    <!-- ========================================================================= -->
    <!-- RED BLACK HOLE (術式反転「赫」) - ORBITING ENTITY                         -->
    <!-- ========================================================================= -->
    <g class="anim-red-bh">
      <!-- Soft Gravitational Lensing Aura -->
      <circle cx="1020" cy="190" r="70" fill="url(#red-bh-glow)" filter="url(#hyper-lens)" opacity="0.85" />
      <!-- Event Horizon Core -->
      <circle cx="1020" cy="190" r="32" fill="url(#red-bh-glow)" filter="url(#soft-lens)" />
      <!-- Radiant Singularity Center -->
      <circle cx="1020" cy="190" r="14" fill="#FFFFFF" />

      <!-- Minimal Soft Technique Label (Follows Orb) -->
      <text x="1020" y="242" fill="#FB7185" font-size="12" font-weight="800" letter-spacing="1" text-anchor="middle" class="font-sans">術式反転「赫」</text>
      <text x="1020" y="255" fill="rgba(255,255,255,0.4)" font-size="9" font-weight="600" letter-spacing="1.5" text-anchor="middle" class="font-sans">REVERSAL: RED</text>
    </g>

    <!-- ========================================================================= -->
    <!-- CENTER: COLLAPSE & SUPERNOVA HOLLOW PURPLE DETONATION                     -->
    <!-- ========================================================================= -->

    <!-- Laser Shockwave Beam Surge -->
    <g class="anim-beam">
      <ellipse cx="590" cy="190" rx="490" ry="34" fill="url(#surge-laser)" filter="url(#hyper-lens)" />
      <line x1="100" y1="190" x2="1080" y2="190" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" />
    </g>

    <!-- Expanding Lensing Rings -->
    <g class="anim-ring2">
      <circle cx="590" cy="190" r="65" stroke="#FFFFFF" stroke-width="1.5" fill="none" opacity="0.65" />
    </g>
    <g class="anim-ring1">
      <circle cx="590" cy="190" r="50" stroke="#E879F9" stroke-width="2.2" fill="none" opacity="0.85" />
      <circle cx="590" cy="190" r="75" stroke="#C084FC" stroke-width="1.4" fill="none" opacity="0.75" />
    </g>

    <!-- Supernova Singularity Core -->
    <g class="anim-nova">
      <circle cx="590" cy="190" r="68" fill="#7E22CE" opacity="0.35" filter="url(#hyper-lens)" />
      <circle cx="590" cy="190" r="45" fill="url(#purple-singularity)" filter="url(#soft-lens)" />
      <circle cx="590" cy="190" r="16" fill="#FFFFFF" />
    </g>

  </g> <!-- End card-bounds clip -->

  <!-- Outer Razor Frame -->
  <rect x="1" y="1" width="1178" height="338" rx="17.5" fill="none" stroke="rgba(255,255,255,0.12)" stroke-width="1.4" />

  <!-- Bottom Coordinate Strip -->
  <g class="font-sans" transform="translate(590, 322)" text-anchor="middle">
    <text x="0" y="0" fill="rgba(255,255,255,0.32)" font-size="10" font-weight="600" letter-spacing="2">DOMAIN STATUS : MAXIMUM UNRESTRICTED OUTPUT · TARGET : INFINITE HORIZON</text>
  </g>
</svg>"""

    scratch_path = r"C:\Users\leven\.gemini\antigravity\brain\c3fec2c6-884c-4ac6-b9ac-403ef9ea1318\scratch\hollow_purple_wave.svg"
    repo_path    = r"C:\Users\leven\.gemini\antigravity\scratch\Alceinn_repo\hollow_purple_wave.svg"
    for p in [scratch_path, repo_path]:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(svg_code)

    ET.parse(repo_path)
    print(f"SUCCESS: Ultra-smooth Black Hole merger SVG generated and validated ({os.path.getsize(repo_path)//1024} KB)")

if __name__ == "__main__":
    generate_smooth_orbiting_blackholes_svg()
