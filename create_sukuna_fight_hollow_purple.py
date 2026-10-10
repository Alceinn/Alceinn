import math
import os
import xml.etree.ElementTree as ET

def generate_true_blackhole_merger_svg():
    """
    True Black Hole Binary Inspiral & Merger:
    - Center is strictly (cx=590, cy=190).
    - Blue & Red groups are drawn at (0, 0) locally.
    - Each keyframe uses pure `transform: translate(x px, y px) scale(s)`.
      This eliminates ALL SVG transform-origin / scale displacement bugs!
    
    Motion Choreography (16s cycle):
    0% - 25%:
      - Blue charges at (180, 190), Red charges at (1000, 190).
      - Breathing glow.
    25% - 48%:
      - Both glide straight towards the center (590, 190).
      - Blue moves from 180 -> 440 (distance 150px from center).
      - Red moves from 1000 -> 740 (distance 150px from center).
    48% - 76%:
      - Gravitational capture & orbital binary spiral!
      - Starting at radius 150px, orbiting around (590, 190).
      - Over 2.5 complete orbits, the radius smoothly decays: 150px -> 6px.
      - As they draw tighter and tighter, they begin overlapping / passing through each other.
    76% - 79%:
      - SUDDEN SHRINK / COMPRESSION:
      - As they coalesce at (590, 190), their scales snap from 1.3 down to 0.05!
      - Extreme gravitational collapse / singularity instant!
    79% - 94%:
      - SUPERNOVA HOLLOW PURPLE BLAST:
      - At (590, 190), Hollow Purple singularity detonates!
      - Expanding shockwave rings & high-energy particle beam.
    94% - 100%:
      - Cool-off fade and seamless loop reset.
    """

    cx, cy = 590, 190
    blue_start_x = 180.0
    red_start_x = 1000.0
    orbit_start_r = 150.0

    blue_kf = []
    red_kf = []

    for step in range(101):
        pct = step # 0 to 100%

        if pct <= 25:
            # Stage 1: Stationary charging at sides
            t_sub = pct / 25.0
            bx = blue_start_x
            by = cy
            rx = red_start_x
            ry = cy
            scale = 1.0 + 0.06 * math.sin(t_sub * math.pi * 2)
            op = min(1.0, pct / 3.0)

        elif pct <= 48:
            # Stage 2: Moving smoothly to center approach distance (orbit_start_r)
            t_sub = (pct - 25.0) / 23.0
            # Smooth ease-in-out
            ease = 0.5 - 0.5 * math.cos(t_sub * math.pi)
            curr_dist = (cx - blue_start_x) - ((cx - blue_start_x) - orbit_start_r) * ease

            bx = cx - curr_dist
            by = cy
            rx = cx + curr_dist
            ry = cy
            scale = 1.0 + 0.15 * ease
            op = 1.0

        elif pct <= 76:
            # Stage 3: Orbiting around each other while inspiraling into the center!
            t_sub = (pct - 48.0) / 28.0
            revolutions = 2.4
            angle = t_sub * revolutions * 2.0 * math.pi

            # Radius decays from orbit_start_r (150px) down to 8px
            r_decay = (1.0 - t_sub) ** 1.35
            curr_r = orbit_start_r * r_decay + 8.0

            # Blue position (starts on left: angle 0 -> -cos)
            bx = cx - curr_r * math.cos(angle)
            by = cy - curr_r * math.sin(angle) * 0.65 # subtle perspective tilt

            # Red position (diametrically opposite)
            rx = cx + curr_r * math.cos(angle)
            ry = cy + curr_r * math.sin(angle) * 0.65

            scale = 1.15 + 0.25 * t_sub # gets denser and hotter
            op = 1.0

        elif pct <= 79:
            # Stage 4: "bir anda kuculup patlayacaklar" - RAPID COMPRESSION TO ZERO!
            t_sub = (pct - 76.0) / 3.0
            bx = cx
            by = cy
            rx = cx
            ry = cy
            # Instant collapse down to tiny dot
            scale = max(0.01, 1.4 * (1.0 - t_sub)**2)
            op = max(0.0, 1.0 - t_sub)

        else:
            # Stage 5: Exploded / merged into Hollow Purple
            bx = cx
            by = cy
            rx = cx
            ry = cy
            scale = 0.0
            op = 0.0

        blue_kf.append(f"{pct}% {{ transform: translate({bx:.2f}px, {by:.2f}px) scale({scale:.3f}); opacity: {op:.3f}; }}")
        red_kf.append(f"{pct}% {{ transform: translate({rx:.2f}px, {ry:.2f}px) scale({scale:.3f}); opacity: {op:.3f}; }}")

    blue_kf_str = "\n        ".join(blue_kf)
    red_kf_str = "\n        ".join(red_kf)

    svg_code = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 340" width="1180" height="340" fill="none" overflow="hidden">
  <defs>
    <style><![CDATA[
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap');
      .font-sans {{ font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif; }}

      /* ========================================================================= */
      /* TRUE BINARY BLACK HOLE INSPIRAL KEYFRAMES                                 */
      /* ========================================================================= */

      @keyframes blue-inspiral {{
        {blue_kf_str}
      }}

      @keyframes red-inspiral {{
        {red_kf_str}
      }}

      /* HOLLOW PURPLE DETONATION: Triggers precisely at 79% right as they compress */
      @keyframes purple-supernova {{
        0%, 78.5% {{ transform: translate(590px, 190px) scale(0); opacity: 0; }}
        79.5% {{ transform: translate(590px, 190px) scale(0.2); opacity: 1; }}
        82% {{ transform: translate(590px, 190px) scale(1.2); opacity: 1; }}
        87% {{ transform: translate(590px, 190px) scale(2.2); opacity: 0.95; }}
        93.5% {{ transform: translate(590px, 190px) scale(3.0); opacity: 0; }}
        100% {{ transform: translate(590px, 190px) scale(0); opacity: 0; }}
      }}

      /* SHOCKWAVE EXPANDING RINGS */
      @keyframes shock-ring-outer {{
        0%, 79% {{ transform: translate(590px, 190px) scale(0.01); opacity: 0; }}
        81% {{ transform: translate(590px, 190px) scale(0.5); opacity: 0.95; }}
        89% {{ transform: translate(590px, 190px) scale(4.0); opacity: 0.5; }}
        95% {{ transform: translate(590px, 190px) scale(6.2); opacity: 0; }}
        100% {{ transform: translate(590px, 190px) scale(0); opacity: 0; }}
      }}

      @keyframes shock-ring-inner {{
        0%, 80.5% {{ transform: translate(590px, 190px) scale(0.01); opacity: 0; }}
        82.5% {{ transform: translate(590px, 190px) scale(0.6); opacity: 0.9; }}
        90.5% {{ transform: translate(590px, 190px) scale(4.6); opacity: 0.35; }}
        96% {{ transform: translate(590px, 190px) scale(6.8); opacity: 0; }}
        100% {{ transform: translate(590px, 190px) scale(0); opacity: 0; }}
      }}

      /* HORIZONTAL LASER BEAM BURST */
      @keyframes laser-burst {{
        0%, 79% {{ opacity: 0; transform: scaleX(0.05); }}
        81.5% {{ opacity: 1; transform: scaleX(1); }}
        88% {{ opacity: 0.9; transform: scaleX(1.3); }}
        94% {{ opacity: 0; transform: scaleX(1.8); }}
        100% {{ opacity: 0; }}
      }}

      /* ========================================================================= */
      /* CHANTS TIMELINE (CLEAN, MUTUALLY EXCLUSIVE, ZERO OVERLAP)                 */
      /* ========================================================================= */

      @keyframes phase-1 {{
        0% {{ opacity: 0; transform: translateY(6px); }}
        3% {{ opacity: 1; transform: translateY(0); }}
        19% {{ opacity: 1; transform: translateY(0); }}
        23% {{ opacity: 0; transform: translateY(-6px); }}
        24%, 100% {{ opacity: 0; }}
      }}

      @keyframes phase-2 {{
        0%, 23% {{ opacity: 0; }}
        25% {{ opacity: 0; transform: translateY(6px); }}
        28% {{ opacity: 1; transform: translateY(0); }}
        43% {{ opacity: 1; transform: translateY(0); }}
        47% {{ opacity: 0; transform: translateY(-6px); }}
        48%, 100% {{ opacity: 0; }}
      }}

      @keyframes phase-3 {{
        0%, 47% {{ opacity: 0; }}
        49% {{ opacity: 0; transform: translateY(6px); }}
        52% {{ opacity: 1; transform: translateY(0); }}
        62% {{ opacity: 1; transform: translateY(0); }}
        66% {{ opacity: 0; transform: translateY(-6px); }}
        67%, 100% {{ opacity: 0; }}
      }}

      @keyframes phase-4 {{
        0%, 66% {{ opacity: 0; }}
        68% {{ opacity: 0; transform: translateY(6px); }}
        71% {{ opacity: 1; transform: translateY(0); }}
        78% {{ opacity: 1; transform: translateY(0); }}
        81% {{ opacity: 0; transform: translateY(-6px); }}
        82%, 100% {{ opacity: 0; }}
      }}

      @keyframes phase-5 {{
        0%, 79% {{ opacity: 0; transform: scale(0.9); }}
        82% {{ opacity: 1; transform: scale(1.05); }}
        93% {{ opacity: 1; transform: scale(1); }}
        97% {{ opacity: 0; transform: scale(1.1); }}
        100% {{ opacity: 0; }}
      }}

      .anim-blue-entity {{ animation: blue-inspiral 16s linear infinite; }}
      .anim-red-entity  {{ animation: red-inspiral 16s linear infinite; }}
      .anim-nova        {{ animation: purple-supernova 16s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; }}
      .anim-ring-out    {{ animation: shock-ring-outer 16s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; }}
      .anim-ring-in     {{ animation: shock-ring-inner 16s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; }}
      .anim-beam        {{ animation: laser-burst 16s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 190px; }}

      .hud-1 {{ animation: phase-1 16s ease-in-out infinite; }}
      .hud-2 {{ animation: phase-2 16s ease-in-out infinite; }}
      .hud-3 {{ animation: phase-3 16s ease-in-out infinite; }}
      .hud-4 {{ animation: phase-4 16s ease-in-out infinite; }}
      .hud-5 {{ animation: phase-5 16s ease-in-out infinite; }}
    ]]></style>

    <!-- Strict Card Bounds -->
    <clipPath id="viewport-boundary">
      <rect x="0" y="0" width="1180" height="340" rx="18" />
    </clipPath>

    <!-- Deep Void Cosmic Canvas Background -->
    <radialGradient id="deep-void" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#0E0922" />
      <stop offset="55%" stop-color="#060412" />
      <stop offset="100%" stop-color="#030208" />
    </radialGradient>

    <!-- Blue Gravitational Aura Gradient -->
    <radialGradient id="blue-gravity" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="22%" stop-color="#7DD3FC" />
      <stop offset="55%" stop-color="#0284C7" stop-opacity="0.85" />
      <stop offset="80%" stop-color="#0369A1" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#082F49" stop-opacity="0" />
    </radialGradient>

    <!-- Red Gravitational Aura Gradient -->
    <radialGradient id="red-gravity" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="22%" stop-color="#FDA4AF" />
      <stop offset="55%" stop-color="#E11D48" stop-opacity="0.85" />
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
    <linearGradient id="laser-beam-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0" />
      <stop offset="25%" stop-color="#38BDF8" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="1" />
      <stop offset="75%" stop-color="#FB7185" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0" />
    </linearGradient>

    <!-- Lensing Blur Filters -->
    <filter id="blur-soft" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="blur-wide" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="12" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Deep Canvas Background -->
  <rect width="1180" height="340" rx="18" fill="url(#deep-void)" stroke="rgba(255,255,255,0.12)" stroke-width="1.2" />

  <!-- Strictly clipped content -->
  <g clip-path="url(#viewport-boundary)">

    <!-- Subtle Celestial Matrix Grid -->
    <g opacity="0.08">
      <line x1="0" y1="100" x2="1180" y2="100" stroke="#FFFFFF" stroke-dasharray="4 8" />
      <line x1="0" y1="190" x2="1180" y2="190" stroke="#FFFFFF" stroke-dasharray="4 8" />
      <line x1="0" y1="280" x2="1180" y2="280" stroke="#FFFFFF" stroke-dasharray="4 8" />
    </g>

    <!-- ========================================================================= -->
    <!-- CHANT HUD (TOP CENTER, ZERO OVERLAP)                                      -->
    <!-- ========================================================================= -->
    <g class="font-sans" transform="translate(590, 52)">
      <!-- Phase 1: 九綱 -->
      <g class="hud-1" text-anchor="middle">
        <rect x="-230" y="-28" width="460" height="56" rx="28" fill="rgba(2,132,199,0.12)" stroke="rgba(56,189,248,0.5)" stroke-width="1.2" />
        <text x="0" y="-4" fill="#38BDF8" font-size="18" font-weight="900" letter-spacing="4">九 綱</text>
        <text x="0" y="16" fill="#FFFFFF" font-size="11" font-weight="700" letter-spacing="2">INCANTATION PHASE 01 : NINE ROPES</text>
      </g>

      <!-- Phase 2: 偏光 -->
      <g class="hud-2" text-anchor="middle">
        <rect x="-240" y="-28" width="480" height="56" rx="28" fill="rgba(225,29,72,0.12)" stroke="rgba(251,113,133,0.5)" stroke-width="1.2" />
        <text x="0" y="-4" fill="#FB7185" font-size="18" font-weight="900" letter-spacing="4">偏 光</text>
        <text x="0" y="16" fill="#FFFFFF" font-size="11" font-weight="700" letter-spacing="2">INCANTATION PHASE 02 : POLARIZED LIGHT</text>
      </g>

      <!-- Phase 3: 烏と声明 -->
      <g class="hud-3" text-anchor="middle">
        <rect x="-260" y="-28" width="520" height="56" rx="28" fill="rgba(168,85,247,0.14)" stroke="rgba(192,132,252,0.5)" stroke-width="1.2" />
        <text x="0" y="-4" fill="#C084FC" font-size="18" font-weight="900" letter-spacing="4">烏 と 声 明</text>
        <text x="0" y="16" fill="#FFFFFF" font-size="11" font-weight="700" letter-spacing="2">INCANTATION PHASE 03 : CROW &amp; DECLARATION</text>
      </g>

      <!-- Phase 4: 表裏の間 -->
      <g class="hud-4" text-anchor="middle">
        <rect x="-260" y="-28" width="520" height="56" rx="28" fill="rgba(147,51,234,0.16)" stroke="rgba(232,121,249,0.5)" stroke-width="1.2" />
        <text x="0" y="-4" fill="#E879F9" font-size="18" font-weight="900" letter-spacing="4">表 裏 の 間</text>
        <text x="0" y="16" fill="#FFFFFF" font-size="11" font-weight="700" letter-spacing="2">INCANTATION PHASE 04 : BETWEEN FRONT &amp; BACK</text>
      </g>

      <!-- Phase 5: 虚式「茈」 -->
      <g class="hud-5" text-anchor="middle">
        <rect x="-280" y="-30" width="560" height="60" rx="30" fill="rgba(10,5,24,0.96)" stroke="#C084FC" stroke-width="1.8" filter="url(#blur-soft)" />
        <text x="0" y="-5" fill="#FFFFFF" font-size="20" font-weight="900" letter-spacing="3">虚 式 「 茈 」</text>
        <text x="0" y="17" fill="#E879F9" font-size="11.5" font-weight="800" letter-spacing="2">UNRESTRICTED HOLLOW PURPLE · 200% OUTPUT</text>
      </g>
    </g>

    <!-- ========================================================================= -->
    <!-- BLUE (術式順転「蒼」) - CENTERED AT LOCAL (0,0)                           -->
    <!-- ========================================================================= -->
    <g class="anim-blue-entity">
      <!-- Outer Gravitational Aura -->
      <circle cx="0" cy="0" r="70" fill="url(#blue-gravity)" filter="url(#blur-wide)" opacity="0.85" />
      <!-- Dense Event Horizon -->
      <circle cx="0" cy="0" r="32" fill="url(#blue-gravity)" filter="url(#blur-soft)" />
      <!-- Radiant Core -->
      <circle cx="0" cy="0" r="14" fill="#FFFFFF" />
      <!-- Subtitle -->
      <text x="0" y="52" fill="#38BDF8" font-size="12" font-weight="800" letter-spacing="1" text-anchor="middle" class="font-sans">術式順転「蒼」</text>
      <text x="0" y="65" fill="rgba(255,255,255,0.4)" font-size="9" font-weight="600" letter-spacing="1.5" text-anchor="middle" class="font-sans">LAPSE: BLUE</text>
    </g>

    <!-- ========================================================================= -->
    <!-- RED (術式反転「赫」) - CENTERED AT LOCAL (0,0)                            -->
    <!-- ========================================================================= -->
    <g class="anim-red-entity">
      <!-- Outer Gravitational Aura -->
      <circle cx="0" cy="0" r="70" fill="url(#red-gravity)" filter="url(#blur-wide)" opacity="0.85" />
      <!-- Dense Event Horizon -->
      <circle cx="0" cy="0" r="32" fill="url(#red-gravity)" filter="url(#blur-soft)" />
      <!-- Radiant Core -->
      <circle cx="0" cy="0" r="14" fill="#FFFFFF" />
      <!-- Subtitle -->
      <text x="0" y="52" fill="#FB7185" font-size="12" font-weight="800" letter-spacing="1" text-anchor="middle" class="font-sans">術式反転「赫」</text>
      <text x="0" y="65" fill="rgba(255,255,255,0.4)" font-size="9" font-weight="600" letter-spacing="1.5" text-anchor="middle" class="font-sans">REVERSAL: RED</text>
    </g>

    <!-- ========================================================================= -->
    <!-- SUPERNOVA HOLLOW PURPLE DETONATION (CENTERED AT LOCAL 0,0)                -->
    <!-- ========================================================================= -->

    <!-- Laser Shockwave Beam Surge -->
    <g class="anim-beam">
      <ellipse cx="590" cy="190" rx="490" ry="34" fill="url(#laser-beam-grad)" filter="url(#blur-wide)" />
      <line x1="100" y1="190" x2="1080" y2="190" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" />
    </g>

    <!-- Expanding Lensing Rings -->
    <g class="anim-ring-out">
      <circle cx="0" cy="0" r="65" stroke="#FFFFFF" stroke-width="1.5" fill="none" opacity="0.65" />
    </g>
    <g class="anim-ring-in">
      <circle cx="0" cy="0" r="50" stroke="#E879F9" stroke-width="2.2" fill="none" opacity="0.85" />
      <circle cx="0" cy="0" r="75" stroke="#C084FC" stroke-width="1.4" fill="none" opacity="0.75" />
    </g>

    <!-- Supernova Singularity Core -->
    <g class="anim-nova">
      <circle cx="0" cy="0" r="68" fill="#7E22CE" opacity="0.35" filter="url(#blur-wide)" />
      <circle cx="0" cy="0" r="45" fill="url(#purple-singularity)" filter="url(#blur-soft)" />
      <circle cx="0" cy="0" r="16" fill="#FFFFFF" />
    </g>

  </g> <!-- End viewport-boundary clip -->

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
    print(f"SUCCESS: True Black Hole merger SVG generated and validated ({os.path.getsize(repo_path)//1024} KB)")

if __name__ == "__main__":
    generate_true_blackhole_merger_svg()
