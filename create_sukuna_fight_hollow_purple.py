import os
import xml.etree.ElementTree as ET

def generate_hollow_purple_sukuna_climax():
    """
    Creates an epic Hollow Purple Fusion & Incantation animation inspired by
    Gojo vs Sukuna climax (Unlimited Hollow Purple):
    - Left: Blue (蒼 - Ao)
    - Right: Red (赫 - Aka)
    - They rush to the center and collide into Hollow Purple (茈 - Murasaki)
    - Epic expanding Supernova shockwave & energy explosion
    - Incantations (九綱 -> 偏光 -> 烏と声明 -> 表裏の間 -> 虚式「茈」) appear sequentially in center without overlapping!
    - 100% valid XML with CDATA wrapped CSS and escaped entities!
    """

    svg_code = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 340" width="1180" height="340" fill="none">
  <defs>
    <style><![CDATA[
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&display=swap');
      
      .font-sans {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      }

      /* ========================================================================= */
      /* ANIMATION TIMINGS (TOTAL CYCLE: 8.5 SECONDS)                               */
      /* ========================================================================= */

      /* BLUE ORB (LEFT -> CENTER) */
      @keyframes blue-climax-motion {
        0% { transform: translate(0px, 0px) scale(0.6); opacity: 0; }
        6% { transform: translate(0px, 0px) scale(1); opacity: 1; }
        50% { transform: translate(0px, 0px) scale(1.15); opacity: 1; }
        62% { transform: translate(260px, 0px) scale(1.3); opacity: 1; }
        70% { transform: translate(410px, 0px) scale(1.4); opacity: 1; }
        73% { transform: translate(430px, 0px) scale(0.2); opacity: 0; }
        100% { opacity: 0; }
      }

      /* RED ORB (RIGHT -> CENTER) */
      @keyframes red-climax-motion {
        0% { transform: translate(0px, 0px) scale(0.6); opacity: 0; }
        6% { transform: translate(0px, 0px) scale(1); opacity: 1; }
        50% { transform: translate(0px, 0px) scale(1.15); opacity: 1; }
        62% { transform: translate(-260px, 0px) scale(1.3); opacity: 1; }
        70% { transform: translate(-410px, 0px) scale(1.4); opacity: 1; }
        73% { transform: translate(-430px, 0px) scale(0.2); opacity: 0; }
        100% { opacity: 0; }
      }

      /* PURPLE SUPERNOVA EXPLOSION (CENTER 590, 205) */
      @keyframes purple-supernova {
        0%, 68% { transform: scale(0); opacity: 0; }
        71% { transform: scale(0.4); opacity: 0.9; }
        74% { transform: scale(1.3); opacity: 1; }
        78% { transform: scale(2.2); opacity: 1; }
        86% { transform: scale(4.8); opacity: 0.7; }
        94% { transform: scale(7.5); opacity: 0; }
        100% { transform: scale(0); opacity: 0; }
      }

      /* EXPANDING SHOCKWAVE RING 1 */
      @keyframes shock-ring-1 {
        0%, 71% { transform: scale(0.1); opacity: 0; }
        73% { transform: scale(0.5); opacity: 1; }
        88% { transform: scale(3.8); opacity: 0.6; }
        96% { transform: scale(6.2); opacity: 0; }
        100% { transform: scale(0); opacity: 0; }
      }

      /* EXPANDING SHOCKWAVE RING 2 */
      @keyframes shock-ring-2 {
        0%, 74% { transform: scale(0.1); opacity: 0; }
        76% { transform: scale(0.6); opacity: 0.9; }
        90% { transform: scale(4.5); opacity: 0.4; }
        98% { transform: scale(7.0); opacity: 0; }
        100% { transform: scale(0); opacity: 0; }
      }

      /* ENERGY BEAM SURGE ACROSS SCREEN */
      @keyframes surge-flash {
        0%, 71% { opacity: 0; transform: scaleX(0.1); }
        74% { opacity: 1; transform: scaleX(1); }
        86% { opacity: 0.8; transform: scaleX(1.4); }
        95% { opacity: 0; transform: scaleX(2.0); }
        100% { opacity: 0; }
      }

      /* ROTATING ORBITAL RINGS */
      @keyframes spin-cw {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
      }
      @keyframes spin-ccw {
        0% { transform: rotate(360deg); }
        100% { transform: rotate(0deg); }
      }

      /* ========================================================================= */
      /* CHANTS TIMELINE (MUTUALLY EXCLUSIVE - ZERO OVERLAP)                       */
      /* ========================================================================= */

      /* PHASE 1: 九綱 (NINE ROPES) [0% - 20%] */
      @keyframes chant-phase-1 {
        0% { opacity: 0; transform: translateY(8px); }
        4% { opacity: 1; transform: translateY(0px); }
        17% { opacity: 1; transform: translateY(0px); }
        21% { opacity: 0; transform: translateY(-8px); }
        22%, 100% { opacity: 0; }
      }

      /* PHASE 2: 偏光 (POLARIZED LIGHT) [22% - 40%] */
      @keyframes chant-phase-2 {
        0%, 21% { opacity: 0; }
        24% { opacity: 0; transform: translateY(8px); }
        27% { opacity: 1; transform: translateY(0px); }
        37% { opacity: 1; transform: translateY(0px); }
        41% { opacity: 0; transform: translateY(-8px); }
        42%, 100% { opacity: 0; }
      }

      /* PHASE 3: 烏と声明 (CROW AND DECLARATION) [42% - 58%] */
      @keyframes chant-phase-3 {
        0%, 41% { opacity: 0; }
        44% { opacity: 0; transform: translateY(8px); }
        47% { opacity: 1; transform: translateY(0px); }
        56% { opacity: 1; transform: translateY(0px); }
        60% { opacity: 0; transform: translateY(-8px); }
        61%, 100% { opacity: 0; }
      }

      /* PHASE 4: 表裏の間 (BETWEEN FRONT AND BACK) [61% - 72%] */
      @keyframes chant-phase-4 {
        0%, 60% { opacity: 0; }
        62% { opacity: 0; transform: translateY(8px); }
        64% { opacity: 1; transform: translateY(0px); }
        70% { opacity: 1; transform: translateY(0px); }
        73% { opacity: 0; transform: translateY(-8px); }
        74%, 100% { opacity: 0; }
      }

      /* PHASE 5: 虚式「茈」 (HOLLOW PURPLE CLIMAX) [73% - 98%] */
      @keyframes chant-phase-5 {
        0%, 72% { opacity: 0; transform: scale(0.85); }
        75% { opacity: 1; transform: scale(1.05); }
        92% { opacity: 1; transform: scale(1); }
        97% { opacity: 0; transform: scale(1.15); }
        100% { opacity: 0; }
      }

      .anim-blue { animation: blue-climax-motion 8.5s cubic-bezier(0.2, 0.8, 0.4, 1) infinite; }
      .anim-red { animation: red-climax-motion 8.5s cubic-bezier(0.2, 0.8, 0.4, 1) infinite; }
      .anim-nuke { animation: purple-supernova 8.5s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 205px; }
      .anim-ring-1 { animation: shock-ring-1 8.5s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 205px; }
      .anim-ring-2 { animation: shock-ring-2 8.5s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 205px; }
      .anim-surge { animation: surge-flash 8.5s cubic-bezier(0.1, 0.9, 0.2, 1) infinite; transform-origin: 590px 205px; }
      
      .spin-blue { animation: spin-cw 4s linear infinite; transform-origin: 160px 205px; }
      .spin-red { animation: spin-ccw 4s linear infinite; transform-origin: 1020px 205px; }

      .p1 { animation: chant-phase-1 8.5s ease-in-out infinite; }
      .p2 { animation: chant-phase-2 8.5s ease-in-out infinite; }
      .p3 { animation: chant-phase-3 8.5s ease-in-out infinite; }
      .p4 { animation: chant-phase-4 8.5s ease-in-out infinite; }
      .p5 { animation: chant-phase-5 8.5s ease-in-out infinite; }
    ]]></style>

    <!-- Deep Void Cosmic Radial -->
    <radialGradient id="hollowVoidBg" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="#0E0B1F" />
      <stop offset="60%" stop-color="#060511" />
      <stop offset="100%" stop-color="#040408" />
    </radialGradient>

    <!-- Blue (Lapse) Glow -->
    <radialGradient id="blueGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="35%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#0284C7" />
      <stop offset="100%" stop-color="#0369A1" stop-opacity="0" />
    </radialGradient>

    <!-- Red (Reversal) Glow -->
    <radialGradient id="redGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="35%" stop-color="#FB7185" />
      <stop offset="70%" stop-color="#E11D48" />
      <stop offset="100%" stop-color="#9F1239" stop-opacity="0" />
    </radialGradient>

    <!-- Hollow Purple Singularity Core -->
    <radialGradient id="purpleNukeCore" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="25%" stop-color="#F472B6" />
      <stop offset="50%" stop-color="#C084FC" />
      <stop offset="80%" stop-color="#7E22CE" />
      <stop offset="100%" stop-color="#3B0764" stop-opacity="0" />
    </radialGradient>

    <!-- Horizontal Laser Surge Gradient -->
    <linearGradient id="horizontalSurge" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0" />
      <stop offset="30%" stop-color="#C084FC" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="1" />
      <stop offset="70%" stop-color="#F43F5E" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0" />
    </linearGradient>

    <filter id="hyperGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="10" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Canvas Container -->
  <rect width="1180" height="340" rx="18" fill="url(#hollowVoidBg)" stroke="rgba(255,255,255,0.12)" stroke-width="1.2" />

  <!-- Constellation Ambient Background Grid -->
  <g opacity="0.12">
    <line x1="0" y1="95" x2="1180" y2="95" stroke="#FFFFFF" stroke-dasharray="3 6" />
    <line x1="0" y1="205" x2="1180" y2="205" stroke="#FFFFFF" stroke-dasharray="3 6" />
    <circle cx="590" cy="205" r="90" stroke="#FFFFFF" stroke-width="0.8" stroke-dasharray="4 6" />
  </g>

  <!-- ========================================================================= -->
  <!-- TOP DISPLAY HUD: THE 5 SEQUENTIAL CHANTS (MUTUALLY EXCLUSIVE / NO OVERLAP) -->
  <!-- ========================================================================= -->
  <g class="font-sans" transform="translate(590, 52)">
    
    <!-- PHASE 1: NINE ROPES (九綱) -->
    <g class="p1" text-anchor="middle">
      <rect x="-240" y="-32" width="480" height="64" rx="32" fill="rgba(2,132,199,0.12)" stroke="rgba(56,189,248,0.5)" stroke-width="1.4" />
      <text x="0" y="-4" fill="#38BDF8" font-size="20" font-weight="900" letter-spacing="4">九 綱</text>
      <text x="0" y="18" fill="#FFFFFF" font-size="12" font-weight="700" letter-spacing="2">INCANTATION PHASE 01 : NINE ROPES</text>
    </g>

    <!-- PHASE 2: POLARIZED LIGHT (偏光) -->
    <g class="p2" text-anchor="middle">
      <rect x="-240" y="-32" width="480" height="64" rx="32" fill="rgba(225,29,72,0.12)" stroke="rgba(251,113,133,0.5)" stroke-width="1.4" />
      <text x="0" y="-4" fill="#FB7185" font-size="20" font-weight="900" letter-spacing="4">偏 光</text>
      <text x="0" y="18" fill="#FFFFFF" font-size="12" font-weight="700" letter-spacing="2">INCANTATION PHASE 02 : POLARIZED LIGHT</text>
    </g>

    <!-- PHASE 3: CROW & DECLARATION (烏と声明) -->
    <g class="p3" text-anchor="middle">
      <rect x="-260" y="-32" width="520" height="64" rx="32" fill="rgba(168,85,247,0.14)" stroke="rgba(192,132,252,0.5)" stroke-width="1.4" />
      <text x="0" y="-4" fill="#C084FC" font-size="20" font-weight="900" letter-spacing="4">烏 と 声 明</text>
      <text x="0" y="18" fill="#FFFFFF" font-size="12" font-weight="700" letter-spacing="2">INCANTATION PHASE 03 : CROW &amp; DECLARATION</text>
    </g>

    <!-- PHASE 4: BETWEEN FRONT & BACK (表裏の間) -->
    <g class="p4" text-anchor="middle">
      <rect x="-260" y="-32" width="520" height="64" rx="32" fill="rgba(147,51,234,0.16)" stroke="rgba(232,121,249,0.5)" stroke-width="1.4" />
      <text x="0" y="-4" fill="#E879F9" font-size="20" font-weight="900" letter-spacing="4">表 裏 の 間</text>
      <text x="0" y="18" fill="#FFFFFF" font-size="12" font-weight="700" letter-spacing="2">INCANTATION PHASE 04 : BETWEEN FRONT &amp; BACK</text>
    </g>

    <!-- PHASE 5: HOLLOW PURPLE CLIMAX (虚式「茈」 200%) -->
    <g class="p5" text-anchor="middle">
      <rect x="-290" y="-34" width="580" height="68" rx="34" fill="rgba(10,5,24,0.95)" stroke="#C084FC" stroke-width="2" filter="drop-shadow(0 0 18px rgba(192,132,252,0.8))" />
      <text x="0" y="-5" fill="#FFFFFF" font-size="22" font-weight="900" letter-spacing="3">虚 式 「 茈 」</text>
      <text x="0" y="19" fill="#E879F9" font-size="12.5" font-weight="800" letter-spacing="2.5">UNRESTRICTED HOLLOW PURPLE · 200% OUTPUT</text>
    </g>

  </g>

  <!-- ========================================================================= -->
  <!-- MAIN ARENA: LAPSE BLUE (LEFT) & REVERSAL RED (RIGHT)                      -->
  <!-- ========================================================================= -->
  
  <!-- Horizontal Fusion Axis Rail -->
  <line x1="90" y1="205" x2="1090" y2="205" stroke="rgba(255,255,255,0.08)" stroke-width="1.5" />
  <line x1="490" y1="205" x2="690" y2="205" stroke="rgba(192,132,252,0.3)" stroke-width="2" />

  <!-- LEFT: LAPSE BLUE (蒼) -->
  <g class="anim-blue">
    <!-- Blue Orbit Rings -->
    <g class="spin-blue">
      <ellipse cx="160" cy="205" rx="46" ry="18" stroke="#38BDF8" stroke-width="1.4" fill="none" stroke-dasharray="6 4" />
      <circle cx="114" cy="205" r="3" fill="#FFFFFF" />
    </g>
    <!-- Blue Glowing Core -->
    <circle cx="160" cy="205" r="36" fill="url(#blueGlow)" filter="url(#hyperGlow)" />
    <circle cx="160" cy="205" r="14" fill="#FFFFFF" />
    
    <!-- Technique Label -->
    <g class="font-sans" transform="translate(160, 260)" text-anchor="middle">
      <text x="0" y="0" fill="#38BDF8" font-size="13" font-weight="800" letter-spacing="1">術式順転「蒼」</text>
      <text x="0" y="16" fill="rgba(255,255,255,0.5)" font-size="10.5" font-weight="600">LAPSE: BLUE</text>
    </g>
  </g>

  <!-- RIGHT: REVERSAL RED (赫) -->
  <g class="anim-red">
    <!-- Red Orbit Rings -->
    <g class="spin-red">
      <ellipse cx="1020" cy="205" rx="46" ry="18" stroke="#FB7185" stroke-width="1.4" fill="none" stroke-dasharray="6 4" />
      <circle cx="1066" cy="205" r="3" fill="#FFFFFF" />
    </g>
    <!-- Red Glowing Core -->
    <circle cx="1020" cy="205" r="36" fill="url(#redGlow)" filter="url(#hyperGlow)" />
    <circle cx="1020" cy="205" r="14" fill="#FFFFFF" />

    <!-- Technique Label -->
    <g class="font-sans" transform="translate(1020, 260)" text-anchor="middle">
      <text x="0" y="0" fill="#FB7185" font-size="13" font-weight="800" letter-spacing="1">術式反転「赫」</text>
      <text x="0" y="16" fill="rgba(255,255,255,0.5)" font-size="10.5" font-weight="600">REVERSAL: RED</text>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- CENTER FUSION: SUPERNOVA HOLLOW PURPLE DETONATION                         -->
  <!-- ========================================================================= -->

  <!-- Shockwave Expanding Beam Surge -->
  <g class="anim-surge">
    <ellipse cx="590" cy="205" rx="480" ry="40" fill="url(#horizontalSurge)" filter="url(#hyperGlow)" />
    <line x1="120" y1="205" x2="1060" y2="205" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round" />
  </g>

  <!-- Shockwave Ring 1 -->
  <g class="anim-ring-1">
    <circle cx="590" cy="205" r="60" stroke="#E879F9" stroke-width="3" fill="none" />
    <circle cx="590" cy="205" r="90" stroke="#C084FC" stroke-width="1.5" stroke-dasharray="8 6" fill="none" />
  </g>

  <!-- Shockwave Ring 2 -->
  <g class="anim-ring-2">
    <circle cx="590" cy="205" r="80" stroke="#FFFFFF" stroke-width="2" fill="none" />
    <ellipse cx="590" cy="205" rx="140" ry="70" stroke="#A855F7" stroke-width="1.8" fill="none" />
  </g>

  <!-- Supernova Purple Singularity Core -->
  <g class="anim-nuke">
    <circle cx="590" cy="205" r="48" fill="url(#purpleNukeCore)" filter="url(#hyperGlow)" />
    <circle cx="590" cy="205" r="18" fill="#FFFFFF" />
  </g>

  <!-- Bottom Coordinates / Status Strip -->
  <g class="font-sans" transform="translate(590, 318)" text-anchor="middle" font-size="11" font-weight="600" fill="rgba(255,255,255,0.4)">
    <text x="0" y="0">DOMAIN STATUS: MAXIMUM UNRESTRICTED OUTPUT · TARGET: INFINITE HORIZON</text>
  </g>
</svg>"""

    scratch_path = os.path.join(r"C:\Users\leven\.gemini\antigravity\brain\c3fec2c6-884c-4ac6-b9ac-403ef9ea1318\scratch", "hollow_purple_wave.svg")
    with open(scratch_path, 'w', encoding='utf-8') as f:
        f.write(svg_code)
    repo_output = os.path.join(r"C:\Users\leven\.gemini\antigravity\scratch\Alceinn_repo", "hollow_purple_wave.svg")
    with open(repo_output, 'w', encoding='utf-8') as f:
        f.write(svg_code)
    
    # Strict XML Validation
    ET.parse(repo_output)
    print(f"Generated and STRICTLY VALIDATED Sukuna-climax hollow_purple_wave.svg ({os.path.getsize(repo_output)/1024:.1f} KB)")

if __name__ == "__main__":
    generate_hollow_purple_sukuna_climax()
