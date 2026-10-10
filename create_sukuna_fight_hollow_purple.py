import os
import xml.etree.ElementTree as ET

def generate_hollow_purple_cinematic():
    """
    Cinematic Slow-Burn Hollow Purple Climax:
    - Total Cycle: 16 Seconds (Slow, majestic, high-tension buildup)
    - Blue & Red charge gently at their stations
    - Slowly glide towards center (160 -> 450, 1020 -> 730)
    - Orbit/dance around each other in the center vortex
    - Collide & collapse into Singularity
    - Supernova Hollow Purple Blast with expanding shockwaves & shockbeam (strictly clipped inside card!)
    - 5 Chants appear one by one slowly with plenty of reading time and zero overlap!
    """

    svg_code = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 340" width="1180" height="340" fill="none" overflow="hidden">
  <defs>
    <style><![CDATA[
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap');
      .font-main { font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif; }

      /* ========================================================================= */
      /* CINEMATIC TIMELINE: 16 SECONDS TOTAL CYCLE                                */
      /* 0%   - 40%  : Stable Charge & Slow Approach (Nine Ropes & Polarized Light)*/
      /* 40%  - 65%  : Close Approach & Tension (Crow & Declaration)              */
      /* 65%  - 80%  : Orbital Spiral Dance around center (Between Front & Back)   */
      /* 80%  - 83%  : Fusion Collapse into Singularity                            */
      /* 83%  - 95%  : Supernova Hollow Purple Explosion (200% Output)             */
      /* 95%  - 100% : Cool-off fade & seamless loop reset                        */
      /* ========================================================================= */

      /* BLUE (LEFT -> SPIRAL CENTER) */
      /* Starting at (160, 195), Target center is (590, 195) -> deltaX = +430px */
      @keyframes blue-cinematic {
        0% { transform: translate(0px, 0px) scale(0.7); opacity: 0; }
        4% { transform: translate(0px, 0px) scale(1); opacity: 1; }
        36% { transform: translate(0px, 0px) scale(1.05); opacity: 1; }
        /* Slow approach to near center */
        56% { transform: translate(270px, 0px) scale(1.15); opacity: 1; }
        /* Orbital dance around (590, 195) */
        66% { transform: translate(370px, -45px) scale(1.25); opacity: 1; }
        71% { transform: translate(460px, 0px) scale(1.3); opacity: 1; }
        76% { transform: translate(390px, 45px) scale(1.35); opacity: 1; }
        80% { transform: translate(430px, 0px) scale(1.4); opacity: 1; }
        /* Collapse into singularity */
        82.5% { transform: translate(430px, 0px) scale(0.08); opacity: 0; }
        100% { opacity: 0; }
      }

      /* RED (RIGHT -> SPIRAL CENTER) */
      /* Starting at (1020, 195), Target center is (590, 195) -> deltaX = -430px */
      @keyframes red-cinematic {
        0% { transform: translate(0px, 0px) scale(0.7); opacity: 0; }
        4% { transform: translate(0px, 0px) scale(1); opacity: 1; }
        36% { transform: translate(0px, 0px) scale(1.05); opacity: 1; }
        /* Slow approach to near center */
        56% { transform: translate(-270px, 0px) scale(1.15); opacity: 1; }
        /* Orbital dance around (590, 195) - Opposite phase of Blue */
        66% { transform: translate(-370px, 45px) scale(1.25); opacity: 1; }
        71% { transform: translate(-460px, 0px) scale(1.3); opacity: 1; }
        76% { transform: translate(-390px, -45px) scale(1.35); opacity: 1; }
        80% { transform: translate(-430px, 0px) scale(1.4); opacity: 1; }
        /* Collapse into singularity */
        82.5% { transform: translate(-430px, 0px) scale(0.08); opacity: 0; }
        100% { opacity: 0; }
      }

      /* SUPERNOVA HOLLOW PURPLE DETONATION */
      @keyframes supernova-core {
        0%, 80% { transform: scale(0); opacity: 0; }
        82% { transform: scale(0.35); opacity: 1; }
        84.5% { transform: scale(1.3); opacity: 1; }
        89% { transform: scale(2.2); opacity: 0.95; }
        94% { transform: scale(3.2); opacity: 0; }
        100% { transform: scale(0); opacity: 0; }
      }

      /* SHOCKWAVE EXPANDING RINGS */
      @keyframes shock-ring-1 {
        0%, 81.5% { transform: scale(0.01); opacity: 0; }
        83% { transform: scale(0.6); opacity: 1; }
        91% { transform: scale(4.2); opacity: 0.6; }
        96% { transform: scale(6.5); opacity: 0; }
        100% { transform: scale(0); opacity: 0; }
      }

      @keyframes shock-ring-2 {
        0%, 83% { transform: scale(0.01); opacity: 0; }
        85% { transform: scale(0.6); opacity: 0.9; }
        93% { transform: scale(4.8); opacity: 0.45; }
        97% { transform: scale(7.2); opacity: 0; }
        100% { transform: scale(0); opacity: 0; }
      }

      /* EXPANDING HORIZONTAL LASER BEAM SURGE */
      @keyframes beam-flash {
        0%, 81.5% { opacity: 0; transform: scaleX(0.1); }
        83.5% { opacity: 1; transform: scaleX(1); }
        90% { opacity: 0.85; transform: scaleX(1.3); }
        95.5% { opacity: 0; transform: scaleX(1.8); }
        100% { opacity: 0; }
      }

      /* ROTATING ORBITS */
      @keyframes spin-cw { to { transform: rotate(360deg); } }
      @keyframes spin-ccw { to { transform: rotate(-360deg); } }

      /* ========================================================================= */
      /* SLOW, CLEAR, NON-OVERLAPPING SEQUENTIAL CHANTS                            */
      /* ========================================================================= */

      /* PHASE 1: 九綱 (0% - 22%) */
      @keyframes chant-p1 {
        0% { opacity: 0; transform: translateY(7px); }
        3% { opacity: 1; transform: translateY(0); }
        18% { opacity: 1; transform: translateY(0); }
        22% { opacity: 0; transform: translateY(-7px); }
        23%, 100% { opacity: 0; }
      }

      /* PHASE 2: 偏光 (23% - 44%) */
      @keyframes chant-p2 {
        0%, 22% { opacity: 0; }
        25% { opacity: 0; transform: translateY(7px); }
        28% { opacity: 1; transform: translateY(0); }
        40% { opacity: 1; transform: translateY(0); }
        44% { opacity: 0; transform: translateY(-7px); }
        45%, 100% { opacity: 0; }
      }

      /* PHASE 3: 烏と声明 (45% - 65%) */
      @keyframes chant-p3 {
        0%, 44% { opacity: 0; }
        47% { opacity: 0; transform: translateY(7px); }
        50% { opacity: 1; transform: translateY(0); }
        61% { opacity: 1; transform: translateY(0); }
        65% { opacity: 0; transform: translateY(-7px); }
        66%, 100% { opacity: 0; }
      }

      /* PHASE 4: 表裏の間 (66% - 81%) */
      @keyframes chant-p4 {
        0%, 65% { opacity: 0; }
        67.5% { opacity: 0; transform: translateY(7px); }
        70% { opacity: 1; transform: translateY(0); }
        77.5% { opacity: 1; transform: translateY(0); }
        81% { opacity: 0; transform: translateY(-7px); }
        82%, 100% { opacity: 0; }
      }

      /* PHASE 5: 虚式「茈」 CLIMAX (82% - 98%) */
      @keyframes chant-p5 {
        0%, 81% { opacity: 0; transform: scale(0.9); }
        83.5% { opacity: 1; transform: scale(1.05); }
        94% { opacity: 1; transform: scale(1); }
        98% { opacity: 0; transform: scale(1.1); }
        100% { opacity: 0; }
      }

      .anim-blue { animation: blue-cinematic 16s cubic-bezier(0.25, 0.75, 0.35, 1) infinite; }
      .anim-red  { animation: red-cinematic  16s cubic-bezier(0.25, 0.75, 0.35, 1) infinite; }
      .anim-nuke { animation: supernova-core 16s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 195px; }
      .anim-r1   { animation: shock-ring-1 16s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 195px; }
      .anim-r2   { animation: shock-ring-2 16s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 195px; }
      .anim-beam { animation: beam-flash 16s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 195px; }

      .ring-spin-cw  { animation: spin-cw 4.5s linear infinite; }
      .ring-spin-ccw { animation: spin-ccw 4.2s linear infinite; }

      .cp1 { animation: chant-p1 16s ease-in-out infinite; }
      .cp2 { animation: chant-p2 16s ease-in-out infinite; }
      .cp3 { animation: chant-p3 16s ease-in-out infinite; }
      .cp4 { animation: chant-p4 16s ease-in-out infinite; }
      .cp5 { animation: chant-p5 16s ease-in-out infinite; }
    ]]></style>

    <!-- CLIP BOUNDARY: Strictly contains all explosions and animations inside card -->
    <clipPath id="boundary-clip">
      <rect x="0" y="0" width="1180" height="340" rx="18" />
    </clipPath>

    <!-- Deep Void Cosmic Background Gradient -->
    <radialGradient id="void-bg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#0E0B1F" />
      <stop offset="55%" stop-color="#060514" />
      <stop offset="100%" stop-color="#040408" />
    </radialGradient>

    <!-- Blue Core Gradient -->
    <radialGradient id="blue-core" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="30%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#0284C7" />
      <stop offset="100%" stop-color="#0369A1" stop-opacity="0" />
    </radialGradient>

    <!-- Red Core Gradient -->
    <radialGradient id="red-core" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="30%" stop-color="#FB7185" />
      <stop offset="70%" stop-color="#E11D48" />
      <stop offset="100%" stop-color="#9F1239" stop-opacity="0" />
    </radialGradient>

    <!-- Supernova Hollow Purple Singularity Core -->
    <radialGradient id="purple-supernova-core" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="25%" stop-color="#F472B6" />
      <stop offset="55%" stop-color="#C084FC" />
      <stop offset="80%" stop-color="#7E22CE" />
      <stop offset="100%" stop-color="#3B0764" stop-opacity="0" />
    </radialGradient>

    <!-- Horizontal Laser Surge Gradient -->
    <linearGradient id="horizontal-beam" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0" />
      <stop offset="25%" stop-color="#38BDF8" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="1" />
      <stop offset="75%" stop-color="#FB7185" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0" />
    </linearGradient>

    <!-- Blurs & Glows -->
    <filter id="strong-glow" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="9" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <filter id="soft-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Deep Canvas Background -->
  <rect width="1180" height="340" rx="18" fill="url(#void-bg)" stroke="rgba(255,255,255,0.12)" stroke-width="1.2" />

  <!-- ALL ANIMATIONS ARE BOUNDED TO PREVENT OVERFLOW -->
  <g clip-path="url(#boundary-clip)">

    <!-- Cosmic Matrix Guide Lines -->
    <g opacity="0.10">
      <line x1="0" y1="105" x2="1180" y2="105" stroke="#FFFFFF" stroke-dasharray="3 7" />
      <line x1="0" y1="195" x2="1180" y2="195" stroke="#FFFFFF" stroke-dasharray="3 7" />
      <line x1="0" y1="285" x2="1180" y2="285" stroke="#FFFFFF" stroke-dasharray="3 7" />
      <!-- Gravitational Center Marker -->
      <circle cx="590" cy="195" r="90" stroke="#FFFFFF" stroke-width="0.8" stroke-dasharray="4 6" />
      <circle cx="590" cy="195" r="160" stroke="#FFFFFF" stroke-width="0.5" stroke-dasharray="2 8" />
    </g>

    <!-- ========================================================================= -->
    <!-- SLOW & ELEGANT SEQUENTIAL INCANTATION HUD (ONE AT A TIME, NO OVERLAP)     -->
    <!-- ========================================================================= -->
    <g class="font-main" transform="translate(590, 56)">
      <!-- Phase 1: 九綱 (Nine Ropes) -->
      <g class="cp1" text-anchor="middle">
        <rect x="-240" y="-30" width="480" height="60" rx="30" fill="rgba(2,132,199,0.14)" stroke="rgba(56,189,248,0.55)" stroke-width="1.3" />
        <text x="0" y="-5" fill="#38BDF8" font-size="19" font-weight="900" letter-spacing="5">九 綱</text>
        <text x="0" y="17" fill="#FFFFFF" font-size="11.5" font-weight="700" letter-spacing="2.5">INCANTATION PHASE 01 : NINE ROPES</text>
      </g>

      <!-- Phase 2: 偏光 (Polarized Light) -->
      <g class="cp2" text-anchor="middle">
        <rect x="-250" y="-30" width="500" height="60" rx="30" fill="rgba(225,29,72,0.14)" stroke="rgba(251,113,133,0.55)" stroke-width="1.3" />
        <text x="0" y="-5" fill="#FB7185" font-size="19" font-weight="900" letter-spacing="5">偏 光</text>
        <text x="0" y="17" fill="#FFFFFF" font-size="11.5" font-weight="700" letter-spacing="2.5">INCANTATION PHASE 02 : POLARIZED LIGHT</text>
      </g>

      <!-- Phase 3: 烏と声明 (Crow & Declaration) -->
      <g class="cp3" text-anchor="middle">
        <rect x="-280" y="-30" width="560" height="60" rx="30" fill="rgba(168,85,247,0.16)" stroke="rgba(192,132,252,0.55)" stroke-width="1.3" />
        <text x="0" y="-5" fill="#C084FC" font-size="19" font-weight="900" letter-spacing="5">烏 と 声 明</text>
        <text x="0" y="17" fill="#FFFFFF" font-size="11.5" font-weight="700" letter-spacing="2.5">INCANTATION PHASE 03 : CROW &amp; DECLARATION</text>
      </g>

      <!-- Phase 4: 表裏の間 (Between Front & Back) -->
      <g class="cp4" text-anchor="middle">
        <rect x="-280" y="-30" width="560" height="60" rx="30" fill="rgba(147,51,234,0.18)" stroke="rgba(232,121,249,0.55)" stroke-width="1.3" />
        <text x="0" y="-5" fill="#E879F9" font-size="19" font-weight="900" letter-spacing="5">表 裏 の 間</text>
        <text x="0" y="17" fill="#FFFFFF" font-size="11.5" font-weight="700" letter-spacing="2.5">INCANTATION PHASE 04 : BETWEEN FRONT &amp; BACK</text>
      </g>

      <!-- Phase 5: 虚式「茈」 (Hollow Purple Climax 200%) -->
      <g class="cp5" text-anchor="middle">
        <rect x="-290" y="-33" width="580" height="66" rx="33" fill="rgba(8,4,20,0.96)" stroke="#C084FC" stroke-width="2" filter="url(#soft-glow)" />
        <text x="0" y="-6" fill="#FFFFFF" font-size="21" font-weight="900" letter-spacing="3.5">虚 式 「 茈 」</text>
        <text x="0" y="18" fill="#E879F9" font-size="11.5" font-weight="800" letter-spacing="2.5">UNRESTRICTED HOLLOW PURPLE · 200% OUTPUT</text>
      </g>
    </g>

    <!-- ========================================================================= -->
    <!-- BLUE (LAPSE 蒼) : SLOW APPROACH -> SPIRAL DANCE                           -->
    <!-- ========================================================================= -->
    <g class="anim-blue">
      <!-- Glow Halos -->
      <circle cx="160" cy="195" r="75" fill="#0284C7" opacity="0.10" filter="url(#strong-glow)" />
      <circle cx="160" cy="195" r="48" fill="#38BDF8" opacity="0.18" filter="url(#strong-glow)" />
      <!-- Rotating Orbit 1 -->
      <g transform="translate(160, 195)" class="ring-spin-cw">
        <ellipse rx="46" ry="17" stroke="#38BDF8" stroke-width="1.4" fill="none" stroke-dasharray="7 4" opacity="0.9" />
        <circle cx="-46" cy="0" r="2.5" fill="#FFFFFF" />
      </g>
      <!-- Rotating Orbit 2 -->
      <g transform="translate(160, 195)" class="ring-spin-ccw">
        <ellipse rx="34" ry="13" stroke="#38BDF8" stroke-width="0.8" fill="none" stroke-dasharray="4 5" opacity="0.55" transform="rotate(40)" />
      </g>
      <!-- Core -->
      <circle cx="160" cy="195" r="34" fill="url(#blue-core)" filter="url(#strong-glow)" />
      <circle cx="160" cy="195" r="13" fill="#FFFFFF" />
      <!-- Technique Labels -->
      <text x="160" y="254" fill="#38BDF8" font-size="12.5" font-weight="800" letter-spacing="1" text-anchor="middle" class="font-main">術式順転「蒼」</text>
      <text x="160" y="268" fill="rgba(255,255,255,0.45)" font-size="9.5" font-weight="600" letter-spacing="2" text-anchor="middle" class="font-main">LAPSE : BLUE</text>
    </g>

    <!-- ========================================================================= -->
    <!-- RED (REVERSAL 赫) : SLOW APPROACH -> SPIRAL DANCE                         -->
    <!-- ========================================================================= -->
    <g class="anim-red">
      <!-- Glow Halos -->
      <circle cx="1020" cy="195" r="75" fill="#E11D48" opacity="0.10" filter="url(#strong-glow)" />
      <circle cx="1020" cy="195" r="48" fill="#FB7185" opacity="0.18" filter="url(#strong-glow)" />
      <!-- Rotating Orbit 1 -->
      <g transform="translate(1020, 195)" class="ring-spin-ccw">
        <ellipse rx="46" ry="17" stroke="#FB7185" stroke-width="1.4" fill="none" stroke-dasharray="7 4" opacity="0.9" />
        <circle cx="46" cy="0" r="2.5" fill="#FFFFFF" />
      </g>
      <!-- Rotating Orbit 2 -->
      <g transform="translate(1020, 195)" class="ring-spin-cw">
        <ellipse rx="34" ry="13" stroke="#FB7185" stroke-width="0.8" fill="none" stroke-dasharray="4 5" opacity="0.55" transform="rotate(-40)" />
      </g>
      <!-- Core -->
      <circle cx="1020" cy="195" r="34" fill="url(#red-core)" filter="url(#strong-glow)" />
      <circle cx="1020" cy="195" r="13" fill="#FFFFFF" />
      <!-- Technique Labels -->
      <text x="1020" y="254" fill="#FB7185" font-size="12.5" font-weight="800" letter-spacing="1" text-anchor="middle" class="font-main">術式反転「赫」</text>
      <text x="1020" y="268" fill="rgba(255,255,255,0.45)" font-size="9.5" font-weight="600" letter-spacing="2" text-anchor="middle" class="font-main">REVERSAL : RED</text>
    </g>

    <!-- ========================================================================= -->
    <!-- CENTER: HOLLOW PURPLE DETONATION (COLLISION -> SUPERNOVA EXPLOSION)       -->
    <!-- ========================================================================= -->

    <!-- Laser Beam Surge Across Screen -->
    <g class="anim-beam">
      <ellipse cx="590" cy="195" rx="510" ry="38" fill="url(#horizontal-beam)" filter="url(#strong-glow)" />
      <line x1="80" y1="195" x2="1100" y2="195" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" />
    </g>

    <!-- Expanding Shockwave Rings -->
    <g class="anim-r2">
      <circle cx="590" cy="195" r="70" stroke="#FFFFFF" stroke-width="1.6" fill="none" opacity="0.6" />
      <circle cx="590" cy="195" r="88" stroke="#A855F7" stroke-width="1.2" stroke-dasharray="9 6" fill="none" opacity="0.8" />
    </g>
    <g class="anim-r1">
      <circle cx="590" cy="195" r="54" stroke="#E879F9" stroke-width="2.5" fill="none" />
      <circle cx="590" cy="195" r="75" stroke="#C084FC" stroke-width="1.8" fill="none" />
    </g>

    <!-- Supernova Core Singularity -->
    <g class="anim-nuke">
      <circle cx="590" cy="195" r="72" fill="#7E22CE" opacity="0.32" filter="url(#strong-glow)" />
      <circle cx="590" cy="195" r="48" fill="url(#purple-supernova-core)" filter="url(#strong-glow)" />
      <circle cx="590" cy="195" r="17" fill="#FFFFFF" />
    </g>

  </g> <!-- End of boundary-clip -->

  <!-- Outer Border Frame (Pristine, razor-sharp on top of clip) -->
  <rect x="1" y="1" width="1178" height="338" rx="17.5" fill="none" stroke="rgba(255,255,255,0.14)" stroke-width="1.5" />

  <!-- Bottom Status Coordinates Strip -->
  <g class="font-main" transform="translate(590, 323)" text-anchor="middle">
    <text x="0" y="0" fill="rgba(255,255,255,0.35)" font-size="10.5" font-weight="600" letter-spacing="2">DOMAIN STATUS : MAXIMUM UNRESTRICTED OUTPUT · TARGET : INFINITE HORIZON</text>
  </g>
</svg>"""

    scratch_path = r"C:\Users\leven\.gemini\antigravity\brain\c3fec2c6-884c-4ac6-b9ac-403ef9ea1318\scratch\hollow_purple_wave.svg"
    repo_path    = r"C:\Users\leven\.gemini\antigravity\scratch\Alceinn_repo\hollow_purple_wave.svg"
    for p in [scratch_path, repo_path]:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(svg_code)

    ET.parse(repo_path)
    print(f"SUCCESS: Cinematic 16s Hollow Purple generated and strictly validated XML ({os.path.getsize(repo_path)//1024} KB)")

if __name__ == "__main__":
    generate_hollow_purple_cinematic()
