import sys

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update .hero-bottom-scrim CSS
old_hero_scrim = '''.hero-bottom-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    transparent 42%,
    rgba(5, 8, 17, 0.18) 58%,
    rgba(5, 8, 17, 0.55) 75%,
    rgba(5, 8, 17, 0.88) 92%,
    #050811 100%
  );
  pointer-events: none;
  z-index: 10;
}'''

new_hero_scrim = '''/* Bottom Scrim: Continuous velvety gradient reaching 100% solid #050811 at 82% */
.hero-bottom-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    transparent 0%,
    transparent 36%,
    rgba(5, 8, 17, 0.05) 46%,
    rgba(5, 8, 17, 0.16) 54%,
    rgba(5, 8, 17, 0.35) 62%,
    rgba(5, 8, 17, 0.60) 70%,
    rgba(5, 8, 17, 0.85) 78%,
    #050811 84%,
    #050811 100%
  );
  pointer-events: none;
  z-index: 10;
}

/* Micro-Dither Film Grain Overlay (Eliminates 8-bit gradient quantization & Mach banding) */
.cinematic-dither-overlay {
  position: absolute;
  inset: 0;
  pointer-events: none;
  z-index: 11;
  opacity: 0.038;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  mix-blend-mode: overlay;
}'''

if old_hero_scrim not in html:
    print('ERROR: old_hero_scrim not found in index.html')
    sys.exit(1)
html = html.replace(old_hero_scrim, new_hero_scrim, 1)

# 2. Update Section 2 CSS
old_section2_css = '''.foundation-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  margin-top: -1px; /* Seamless subpixel bridge with Hero */
  padding: clamp(90px, 12vh, 130px) clamp(24px, 5vw, 64px) clamp(80px, 11vh, 120px);
  box-sizing: border-box;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #ffffff;
  z-index: 20;
  background: #050811;
}

/* Dynamic Slide Background Stage (Continuous 200px Atmospheric Fade) */
.foundation-stage-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center 38%;
  opacity: 1;
  transition: opacity 0.75s cubic-bezier(0.4, 0, 0.2, 1), transform 1.4s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 0;
  will-change: opacity, transform;
  transform: scale(1.02);
  filter: brightness(1.0) contrast(1.02);
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.04) 40px, rgba(0, 0, 0, 0.22) 80px, rgba(0, 0, 0, 0.55) 125px, rgba(0, 0, 0, 0.88) 165px, #000 200px);
  mask-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.04) 40px, rgba(0, 0, 0, 0.22) 80px, rgba(0, 0, 0, 0.55) 125px, rgba(0, 0, 0, 0.88) 165px, #000 200px);
}

/* Luminous Ambient Contrast Scrim with Seamless Left Legibility & Top Vignette */
.foundation-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(circle at 80% 30%, rgba(255, 255, 255, 0.08) 0%, transparent 50%),
    linear-gradient(90deg, rgba(5, 8, 17, 0.92) 0%, rgba(5, 8, 17, 0.78) 36%, rgba(5, 8, 17, 0.14) 68%, rgba(5, 8, 17, 0.22) 100%),
    linear-gradient(180deg, #050811 0%, rgba(5, 8, 17, 0.70) 50px, rgba(5, 8, 17, 0.25) 120px, transparent 180px);
  pointer-events: none;
  z-index: 1;
}'''

new_section2_css = '''.foundation-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  margin-top: 0;
  padding: clamp(90px, 12vh, 130px) clamp(24px, 5vw, 64px) clamp(80px, 11vh, 120px);
  box-sizing: border-box;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #ffffff;
  z-index: 20;
  background: #050811;
}

/* Dynamic Slide Background Stage (Guaranteed 90px Pure Black-Navy Buffer at Top) */
.foundation-stage-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center 38%;
  opacity: 1;
  transition: opacity 0.75s cubic-bezier(0.4, 0, 0.2, 1), transform 1.4s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 0;
  will-change: opacity, transform;
  transform: scale(1.02);
  filter: brightness(1.0) contrast(1.02);
  -webkit-mask-image: linear-gradient(180deg, transparent 0px, transparent 90px, rgba(0, 0, 0, 0.12) 150px, rgba(0, 0, 0, 0.45) 210px, rgba(0, 0, 0, 0.82) 270px, #000000 340px);
  mask-image: linear-gradient(180deg, transparent 0px, transparent 90px, rgba(0, 0, 0, 0.12) 150px, rgba(0, 0, 0, 0.45) 210px, rgba(0, 0, 0, 0.82) 270px, #000000 340px);
}

/* Luminous Ambient Contrast Scrim with Smooth Lower Fill & Zero Top Light */
.foundation-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(ellipse 70% 55% at 80% 65%, rgba(255, 255, 255, 0.05) 0%, transparent 70%),
    linear-gradient(90deg, rgba(5, 8, 17, 0.94) 0%, rgba(5, 8, 17, 0.82) 38%, rgba(5, 8, 17, 0.20) 70%, rgba(5, 8, 17, 0.28) 100%),
    linear-gradient(180deg, #050811 0px, #050811 90px, rgba(5, 8, 17, 0.85) 160px, rgba(5, 8, 17, 0.35) 240px, transparent 330px);
  pointer-events: none;
  z-index: 1;
}

/* Dedicated Top Transition Shield (Solid #050811 Bridge, 0.000 RGB Jump Across Seam) */
.foundation-top-blend {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 340px;
  background: linear-gradient(
    180deg,
    #050811 0px,
    #050811 90px,
    rgba(5, 8, 17, 0.985) 130px,
    rgba(5, 8, 17, 0.92) 170px,
    rgba(5, 8, 17, 0.78) 210px,
    rgba(5, 8, 17, 0.52) 255px,
    rgba(5, 8, 17, 0.22) 295px,
    transparent 340px
  );
  pointer-events: none;
  z-index: 5;
}'''

if old_section2_css not in html:
    print('ERROR: old_section2_css not found in index.html')
    sys.exit(1)
html = html.replace(old_section2_css, new_section2_css, 1)

# 3. Add dither overlay to Hero HTML
old_hero_scrim_html = '<div class="hero-bottom-scrim" aria-hidden="true"></div>'
new_hero_scrim_html = '<div class="hero-bottom-scrim" aria-hidden="true"></div>\n  <div class="cinematic-dither-overlay" aria-hidden="true"></div>'
if old_hero_scrim_html not in html:
    print('ERROR: old_hero_scrim_html not found in index.html')
    sys.exit(1)
html = html.replace(old_hero_scrim_html, new_hero_scrim_html, 1)

# 4. Add top blend shield and dither overlay to Section 2 HTML
old_sec2_bg_html = '''  <!-- Dynamic Slide Background Stage (Active Slide Image with Seamless Top Fade) -->
  <div class="foundation-stage-bg" id="foundationStageBg" style="background-image: url('/images/foundation-slide-1.jpg'); opacity: 1;" aria-hidden="true"></div>
  <!-- Cinematic Contrast Scrim -->
  <div class="foundation-scrim-overlay" aria-hidden="true"></div>'''

new_sec2_bg_html = '''  <!-- Dynamic Slide Background Stage (Active Slide Image with Seamless Top Fade) -->
  <div class="foundation-stage-bg" id="foundationStageBg" style="background-image: url('/images/foundation-slide-1.jpg'); opacity: 1;" aria-hidden="true"></div>
  <!-- Cinematic Contrast Scrim -->
  <div class="foundation-scrim-overlay" aria-hidden="true"></div>
  <!-- Dedicated Top Transition Shield (Guarantees flawless seamless bridge, zero lines) -->
  <div class="foundation-top-blend" aria-hidden="true"></div>
  <!-- Fine Micro-Dither Overlay (Eliminates 8-bit gradient banding lines) -->
  <div class="cinematic-dither-overlay" aria-hidden="true"></div>'''

if old_sec2_bg_html not in html:
    print('ERROR: old_sec2_bg_html not found in index.html')
    sys.exit(1)
html = html.replace(old_sec2_bg_html, new_sec2_bg_html, 1)

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Update successfully applied to /home/user/index.html!')
