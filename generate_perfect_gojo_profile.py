import os
import base64
import random
from PIL import Image, ImageEnhance, ImageOps
import io

def generate_banner(is_dark=True):
    mode_str = "dark" if is_dark else "light"
    image_path = r"C:\Users\leven\Downloads\Nah, id code.png"
    
    # Process image to crisp, ultra-clean monochrome
    img = Image.open(image_path).convert("L")
    img = ImageOps.autocontrast(img, cutoff=1)
    enhancer = ImageEnhance.Contrast(img)
    img_crisp = enhancer.enhance(1.22)
    
    target_w, target_h = 420, 520
    img_resized = img_crisp.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    buffered = io.BytesIO()
    img_resized.save(buffered, format="JPEG", quality=95, optimize=True)
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    data_uri = f"data:image/jpeg;base64,{img_base64}"
    
    # Minimalist Star Constellation System
    random.seed(112)
    stars_coords = []
    for _ in range(50):
        x = random.randint(40, 1140)
        y = random.randint(30, 470)
        stars_coords.append((x, y))
        
    # Constellation lines
    lines_svg = []
    for i in range(len(stars_coords)):
        for j in range(i + 1, len(stars_coords)):
            x1, y1 = stars_coords[i]
            x2, y2 = stars_coords[j]
            d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            if 70 < d < 130:
                lines_svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="rgba(255,255,255,0.09)" stroke-width="0.8" />')
                
    constellation_lines_str = "\n    ".join(lines_svg[:28])
    
    # Constellation Star Dots
    star_dots = []
    for x, y in stars_coords:
        r = round(random.uniform(0.8, 1.8), 1)
        dur = round(random.uniform(2.0, 5.0), 1)
        star_dots.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" opacity="0.65"><animate attributeName="opacity" values="0.8;0.25;0.8" dur="{dur}s" repeatCount="indefinite" /></circle>')
    star_dots_str = "\n    ".join(star_dots)
    
    bg_color = "#040408" if is_dark else "#F8FAFC"
    card_bg = "rgba(10, 8, 22, 0.65)" if is_dark else "rgba(255, 255, 255, 0.9)"
    border_color = "rgba(255, 255, 255, 0.12)" if is_dark else "rgba(0, 0, 0, 0.1)"
    text_main = "#FFFFFF" if is_dark else "#0F172A"
    text_sub = "rgba(255, 255, 255, 0.65)" if is_dark else "rgba(15, 23, 42, 0.65)"
    text_muted = "rgba(255, 255, 255, 0.42)" if is_dark else "rgba(15, 23, 42, 0.45)"
    chip_bg = "rgba(255, 255, 255, 0.05)" if is_dark else "rgba(0, 0, 0, 0.04)"
    quote_bg = "rgba(255, 255, 255, 0.03)" if is_dark else "rgba(0, 0, 0, 0.02)"
    
    svg_code = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1180 500" width="1180" height="500" fill="none">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&amp;display=swap');
      
      .font-sans {{ font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif; }}
      
      @keyframes float-manga {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-6px); }}
      }}
      @keyframes subtle-glow {{
        0%, 100% {{ opacity: 0.45; }}
        50% {{ opacity: 0.85; }}
      }}
      
      .anim-float {{ animation: float-manga 5s ease-in-out infinite; }}
      .anim-glow {{ animation: subtle-glow 3.5s ease-in-out infinite; }}
    </style>

    <radialGradient id="spaceGradient_{mode_str}" cx="50%" cy="50%" r="75%">
      <stop offset="0%" stop-color="{('#0D0B1F' if is_dark else '#FFFFFF')}" />
      <stop offset="50%" stop-color="{('#060512' if is_dark else '#F1F5F9')}" />
      <stop offset="100%" stop-color="{bg_color}" />
    </radialGradient>

    <!-- Subtle Violet Ambient Nebula -->
    <radialGradient id="nebulaSoft_{mode_str}" cx="30%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#9333EA" stop-opacity="{('0.22' if is_dark else '0.1')}" />
      <stop offset="70%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <!-- Sleek Card Border Gradient -->
    <linearGradient id="cardBorderGrad_{mode_str}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{('rgba(255,255,255,0.3)' if is_dark else 'rgba(0,0,0,0.15)')}" />
      <stop offset="50%" stop-color="{('rgba(192,132,252,0.25)' if is_dark else 'rgba(147,51,234,0.15)')}" />
      <stop offset="100%" stop-color="{('rgba(255,255,255,0.1)' if is_dark else 'rgba(0,0,0,0.08)')}" />
    </linearGradient>

    <clipPath id="mangaClip_{mode_str}">
      <rect x="40" y="40" width="340" height="420" rx="16" />
    </clipPath>
  </defs>

  <!-- Deep Velvet Space Canvas -->
  <rect width="1180" height="500" rx="20" fill="url(#spaceGradient_{mode_str})" />

  <!-- Ambient Light Sphere -->
  <circle cx="210" cy="250" r="320" fill="url(#nebulaSoft_{mode_str})" />

  <!-- Constellation Star Lattice -->
  <g id="star-chart">
    {constellation_lines_str}
    {star_dots_str}
  </g>

  <!-- Outer Minimalist Glass Frame -->
  <rect x="12" y="12" width="1156" height="476" rx="18" fill="{card_bg}" stroke="{border_color}" stroke-width="1" />

  <!-- ========================================================================= -->
  <!-- LEFT: HIGH-END MINIMALIST GOJO MANGA SHOWCASE                             -->
  <!-- ========================================================================= -->
  <g id="manga-frame" class="anim-float">
    <!-- Soft Back-glow -->
    <rect x="34" y="34" width="352" height="432" rx="18" fill="rgba(168,85,247,0.15)" class="anim-glow" />

    <!-- Manga Image -->
    <g clip-path="url(#mangaClip_{mode_str})">
      <image href="{data_uri}" x="40" y="40" width="340" height="420" preserveAspectRatio="xMidYMid slice" />
      <!-- Minimalist Bottom Shadow -->
      <rect x="40" y="380" width="340" height="80" fill="linear-gradient(to top, rgba(4,4,8,0.92), transparent)" />
    </g>

    <!-- Border -->
    <rect x="40" y="40" width="340" height="420" rx="16" stroke="url(#cardBorderGrad_{mode_str})" stroke-width="1.2" />

    <!-- Minimalist Caption -->
    <g transform="translate(125, 418)">
      <rect width="170" height="28" rx="6" fill="rgba(4,4,8,0.92)" stroke="rgba(255,255,255,0.25)" stroke-width="1" />
      <text x="85" y="18" fill="#FFFFFF" font-size="12" font-weight="700" letter-spacing="1" text-anchor="middle" class="font-sans">NAH, I'D CODE. 🤞</text>
    </g>
  </g>

  <!-- Thin Minimal Vertical Divider -->
  <line x1="420" y1="50" x2="420" y2="450" stroke="{border_color}" stroke-width="1" />

  <!-- ========================================================================= -->
  <!-- RIGHT: EDITORIAL LUXURY MINIMALIST HEADER & TECH PILLS                    -->
  <!-- ========================================================================= -->
  <g class="font-sans" transform="translate(465, 55)">
    
    <!-- Eyebrow Tag -->
    <g transform="translate(0, 0)">
      <circle cx="4" cy="4" r="3.5" fill="#C084FC" />
      <text x="16" y="8" fill="{text_muted}" font-size="12" font-weight="700" letter-spacing="2">LIMITLESS ARCHITECTURE // ALCEIN.COM.TR</text>
    </g>

    <!-- Headline Name -->
    <g transform="translate(0, 48)">
      <text x="0" y="0" fill="{text_main}" font-size="38" font-weight="900" letter-spacing="-1">LEVENT ARAS EREN</text>
      <text x="0" y="28" fill="{text_sub}" font-size="16" font-weight="500">Special Grade Full-Stack Architect <tspan fill="{text_muted}">(@Alceinn)</tspan></text>
    </g>

    <!-- Minimalist Tech Stack Pills (Horizontal Luxury Badges) -->
    <g transform="translate(0, 120)">
      <text x="0" y="0" fill="{text_muted}" font-size="12" font-weight="700" letter-spacing="1.5">STACK &amp; ARSENAL</text>
      
      <!-- Tech Badge Row 1 -->
      <g transform="translate(0, 15)">
        <!-- React -->
        <g transform="translate(0, 0)">
          <rect width="90" height="32" rx="8" fill="{chip_bg}" stroke="{border_color}" stroke-width="1" />
          <text x="45" y="20" fill="{text_main}" font-size="13" font-weight="600" text-anchor="middle">React</text>
        </g>
        <!-- Next.js -->
        <g transform="translate(100, 0)">
          <rect width="90" height="32" rx="8" fill="{chip_bg}" stroke="{border_color}" stroke-width="1" />
          <text x="45" y="20" fill="{text_main}" font-size="13" font-weight="600" text-anchor="middle">Next.js</text>
        </g>
        <!-- TypeScript -->
        <g transform="translate(200, 0)">
          <rect width="115" height="32" rx="8" fill="{chip_bg}" stroke="{border_color}" stroke-width="1" />
          <text x="57.5" y="20" fill="{text_main}" font-size="13" font-weight="600" text-anchor="middle">TypeScript</text>
        </g>
        <!-- Tailwind -->
        <g transform="translate(325, 0)">
          <rect width="115" height="32" rx="8" fill="{chip_bg}" stroke="{border_color}" stroke-width="1" />
          <text x="57.5" y="20" fill="{text_main}" font-size="13" font-weight="600" text-anchor="middle">Tailwind CSS</text>
        </g>
        <!-- Laravel -->
        <g transform="translate(450, 0)">
          <rect width="95" height="32" rx="8" fill="{chip_bg}" stroke="{border_color}" stroke-width="1" />
          <text x="47.5" y="20" fill="{text_main}" font-size="13" font-weight="600" text-anchor="middle">Laravel</text>
        </g>
        <!-- Python -->
        <g transform="translate(555, 0)">
          <rect width="95" height="32" rx="8" fill="{chip_bg}" stroke="{border_color}" stroke-width="1" />
          <text x="47.5" y="20" fill="{text_main}" font-size="13" font-weight="600" text-anchor="middle">Python</text>
        </g>
      </g>
    </g>

    <!-- Editorial Quote Card -->
    <g transform="translate(0, 220)">
      <rect width="650" height="74" rx="12" fill="{quote_bg}" stroke="{border_color}" stroke-width="1" />
      <text x="24" y="32" fill="{text_main}" font-size="14.5" font-weight="600">"Throughout Heaven and Earth, I alone am the honored one."</text>
      <text x="24" y="56" fill="{text_muted}" font-size="12" font-weight="500">天上天下唯我独尊 · Domain Expansion: Unlimited Void</text>
    </g>

    <!-- Clean Direct Links -->
    <g transform="translate(0, 335)" font-size="13" font-weight="500">
      <text x="0" y="0" fill="{text_muted}">CONNECT:</text>
      <text x="80" y="0" fill="{text_main}">alcein.dev@gmail.com</text>
      <text x="260" y="0" fill="{text_muted}">·</text>
      <text x="280" y="0" fill="#C084FC" font-weight="700">alcein.com.tr</text>
      <text x="390" y="0" fill="{text_muted}">·</text>
      <text x="410" y="0" fill="{text_sub}">github.com/Alceinn</text>
    </g>
  </g>
</svg>"""

    scratch_path = os.path.join(r"C:\Users\leven\.gemini\antigravity\brain\c3fec2c6-884c-4ac6-b9ac-403ef9ea1318\scratch", f"{mode_str}.svg")
    with open(scratch_path, 'w', encoding='utf-8') as f:
        f.write(svg_code)
    repo_output = os.path.join(r"C:\Users\leven\.gemini\antigravity\scratch\Alceinn_repo", f"{mode_str}.svg")
    with open(repo_output, 'w', encoding='utf-8') as f:
        f.write(svg_code)
    print(f"Generated Modern Minimalist {mode_str}.svg ({os.path.getsize(repo_output)/1024:.1f} KB)")

def generate_hollow_purple_wave():
    """
    Generates an ultra-clear, high-contrast Hollow Purple 200% Incantation & Shockwave banner.
    All chants are 100% visible, bold, crystal-clear with vibrant Japanese Kanji and English labels.
    """
    svg_code = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1180 260" width="1180" height="260" fill="none">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800;900&amp;display=swap');
      
      .font-main { font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif; }

      @keyframes wave-beam {
        0% { transform: translateX(-200px) scaleX(0.3); opacity: 0; }
        25% { opacity: 0.95; }
        75% { opacity: 1; }
        100% { transform: translateX(1300px) scaleX(2.0); opacity: 0; }
      }
      @keyframes core-glow {
        0%, 100% { transform: scale(1); filter: drop-shadow(0 0 15px #A855F7); }
        50% { transform: scale(1.12); filter: drop-shadow(0 0 35px #C084FC); }
      }
      @keyframes chant-highlight-1 {
        0%, 100% { border-color: rgba(255,255,255,0.18); }
        10%, 30% { border-color: #00F0FF; filter: drop-shadow(0 0 12px rgba(0,240,255,0.8)); }
      }
      @keyframes chant-highlight-2 {
        0%, 100% { border-color: rgba(255,255,255,0.18); }
        30%, 50% { border-color: #F43F5E; filter: drop-shadow(0 0 12px rgba(244,63,94,0.8)); }
      }
      @keyframes chant-highlight-3 {
        0%, 100% { border-color: rgba(255,255,255,0.18); }
        50%, 70% { border-color: #A855F7; filter: drop-shadow(0 0 12px rgba(168,85,247,0.8)); }
      }
      @keyframes chant-highlight-4 {
        0%, 100% { border-color: rgba(255,255,255,0.18); }
        70%, 90% { border-color: #C084FC; filter: drop-shadow(0 0 16px rgba(192,132,252,0.9)); }
      }

      .anim-wave { animation: wave-beam 3.8s cubic-bezier(0.15, 0.85, 0.35, 1) infinite; }
      .anim-wave-sub { animation: wave-beam 3.8s cubic-bezier(0.15, 0.85, 0.35, 1) 0.18s infinite; }
      .anim-core { animation: core-glow 2.5s ease-in-out infinite; transform-origin: 75px 185px; }
      .card-1 { animation: chant-highlight-1 7s ease-in-out infinite; }
      .card-2 { animation: chant-highlight-2 7s ease-in-out infinite; }
      .card-3 { animation: chant-highlight-3 7s ease-in-out infinite; }
      .card-4 { animation: chant-highlight-4 7s ease-in-out infinite; }
    </style>

    <radialGradient id="cardVoid" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="#0E0924" />
      <stop offset="100%" stop-color="#030208" />
    </radialGradient>

    <!-- Hollow Purple Shockwave Beam -->
    <linearGradient id="purpleSurge" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0" />
      <stop offset="25%" stop-color="#00F0FF" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#F43F5E" stop-opacity="0.95" />
      <stop offset="75%" stop-color="#C084FC" stop-opacity="1" />
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0" />
    </linearGradient>

    <radialGradient id="purpleCoreOrb" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="30%" stop-color="#E879F9" />
      <stop offset="65%" stop-color="#9333EA" />
      <stop offset="100%" stop-color="#3B0764" stop-opacity="0" />
    </radialGradient>

    <filter id="laserGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Container -->
  <rect width="1180" height="260" rx="18" fill="url(#cardVoid)" stroke="rgba(255,255,255,0.12)" stroke-width="1.2" />

  <!-- ========================================================================= -->
  <!-- 4 BOLD & CRYSTAL-CLEAR CHANT TILES                                        -->
  <!-- ========================================================================= -->
  <g class="font-main" transform="translate(30, 25)">
    <!-- Chant 1: Nine Ropes (九綱) -->
    <g class="card-1" transform="translate(0, 0)">
      <rect width="265" height="70" rx="12" fill="rgba(255,255,255,0.06)" stroke="rgba(0,240,255,0.4)" stroke-width="1.4" />
      <text x="20" y="32" fill="#00F0FF" font-size="19" font-weight="900">九綱</text>
      <text x="75" y="31" fill="#FFFFFF" font-size="14" font-weight="700">NINE ROPES</text>
      <text x="20" y="54" fill="rgba(255,255,255,0.6)" font-size="11" font-weight="600">INCANTATION PHASE 01</text>
    </g>

    <!-- Chant 2: Polarized Light (偏光) -->
    <g class="card-2" transform="translate(285, 0)">
      <rect width="265" height="70" rx="12" fill="rgba(255,255,255,0.06)" stroke="rgba(244,63,94,0.4)" stroke-width="1.4" />
      <text x="20" y="32" fill="#F43F5E" font-size="19" font-weight="900">偏光</text>
      <text x="75" y="31" fill="#FFFFFF" font-size="14" font-weight="700">POLARIZED LIGHT</text>
      <text x="20" y="54" fill="rgba(255,255,255,0.6)" font-size="11" font-weight="600">INCANTATION PHASE 02</text>
    </g>

    <!-- Chant 3: Crow & Declaration (烏と声明) -->
    <g class="card-3" transform="translate(570, 0)">
      <rect width="265" height="70" rx="12" fill="rgba(255,255,255,0.06)" stroke="rgba(168,85,247,0.4)" stroke-width="1.4" />
      <text x="18" y="32" fill="#A855F7" font-size="19" font-weight="900">烏と声明</text>
      <text x="110" y="31" fill="#FFFFFF" font-size="14" font-weight="700">CROW &amp; RECITE</text>
      <text x="18" y="54" fill="rgba(255,255,255,0.6)" font-size="11" font-weight="600">INCANTATION PHASE 03</text>
    </g>

    <!-- Chant 4: Front & Back (表裏の間) -->
    <g class="card-4" transform="translate(855, 0)">
      <rect width="265" height="70" rx="12" fill="rgba(255,255,255,0.06)" stroke="rgba(192,132,252,0.45)" stroke-width="1.4" />
      <text x="18" y="32" fill="#C084FC" font-size="19" font-weight="900">表裏の間</text>
      <text x="110" y="31" fill="#FFFFFF" font-size="14" font-weight="700">FRONT &amp; BACK</text>
      <text x="18" y="54" fill="rgba(255,255,255,0.6)" font-size="11" font-weight="600">INCANTATION PHASE 04</text>
    </g>
  </g>

  <!-- ========================================================================= -->
  <!-- HOLLOW PURPLE 200% SHOCKWAVE CHANNEL & SURGE                              -->
  <!-- ========================================================================= -->
  <!-- Shockwave Track -->
  <rect x="30" y="115" width="1120" height="120" rx="14" fill="rgba(147,51,234,0.08)" stroke="rgba(192,132,252,0.25)" stroke-width="1" />

  <!-- Core Fusion Orb (Lapse Blue + Reversal Red -> Purple) -->
  <g class="anim-core">
    <circle cx="85" cy="175" r="38" fill="url(#purpleCoreOrb)" filter="url(#laserGlow)" />
    <circle cx="85" cy="175" r="48" stroke="#C084FC" stroke-width="1.8" stroke-dasharray="8 4" />
    <circle cx="85" cy="175" r="16" fill="#FFFFFF" />
  </g>

  <!-- Traveling Shockwave Beam 1 -->
  <g class="anim-wave">
    <ellipse cx="0" cy="175" rx="180" ry="42" fill="url(#purpleSurge)" filter="url(#laserGlow)" />
    <line x1="-140" y1="175" x2="140" y2="175" stroke="#FFFFFF" stroke-width="3.5" stroke-linecap="round" />
  </g>

  <!-- Traveling Shockwave Beam 2 (Trailing Light Pulse) -->
  <g class="anim-wave-sub">
    <ellipse cx="0" cy="175" rx="120" ry="26" fill="url(#purpleSurge)" opacity="0.8" />
  </g>

  <!-- 200% Output Unleashed Badge -->
  <g class="font-main" transform="translate(800, 155)">
    <rect width="320" height="40" rx="20" fill="rgba(8,5,22,0.95)" stroke="#C084FC" stroke-width="1.5" filter="drop-shadow(0 0 12px rgba(192,132,252,0.6))" />
    <circle cx="20" cy="20" r="6" fill="#00F0FF">
      <animate attributeName="r" values="5;8;5" dur="1.4s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="1;0.4;1" dur="1.4s" repeatCount="indefinite" />
    </circle>
    <text x="36" y="26" fill="#FFFFFF" font-size="14" font-weight="900" letter-spacing="0.5">虚式「茈」 HOLLOW PURPLE 200%</text>
  </g>

  <!-- Clean Subtext -->
  <g class="font-main" transform="translate(155, 180)" font-size="13" font-weight="700">
    <text x="0" y="0" fill="rgba(255,255,255,0.85)">TECHNIQUE UNLEASHED</text>
    <text x="0" y="20" fill="rgba(255,255,255,0.5)" font-size="11" font-weight="500">MAXIMUM CURSED ENERGY OUTPUT</text>
  </g>
</svg>"""

    scratch_path = os.path.join(r"C:\Users\leven\.gemini\antigravity\brain\c3fec2c6-884c-4ac6-b9ac-403ef9ea1318\scratch", "hollow_purple_wave.svg")
    with open(scratch_path, 'w', encoding='utf-8') as f:
        f.write(svg_code)
    repo_output = os.path.join(r"C:\Users\leven\.gemini\antigravity\scratch\Alceinn_repo", "hollow_purple_wave.svg")
    with open(repo_output, 'w', encoding='utf-8') as f:
        f.write(svg_code)
    print(f"Generated crystal clear hollow_purple_wave.svg ({os.path.getsize(repo_output)/1024:.1f} KB)")

if __name__ == "__main__":
    generate_banner(is_dark=True)
    generate_banner(is_dark=False)
    generate_hollow_purple_wave()
