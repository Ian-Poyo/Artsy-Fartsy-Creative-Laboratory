import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS: add .foundation-stage-bg, .foundation-scrim-overlay, and .foundation-card .card-bg-img
sec2_css_marker = "/* ============================================================\n   SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE"
sec2_css_pos = content.find(sec2_css_marker)

if sec2_css_pos != -1:
    end_of_sec_css = content.find(".foundation-container {", sec2_css_pos)
    new_sec2_css = """/* ============================================================
   SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE
   Pure White Minimalist Theme with Moving Gradient Rainbow Heart
   Seamless Cosmic Backdrop & Dynamic Slide Visuals
   ============================================================ */
.foundation-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  margin-top: -1px; /* Seamless subpixel bridge with Hero */
  padding: clamp(80px, 11vh, 120px) clamp(24px, 5vw, 64px) clamp(80px, 11vh, 120px);
  box-sizing: border-box;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #ffffff;
  z-index: 20;
  background: 
    radial-gradient(circle at 82% 28%, rgba(55, 85, 160, 0.10) 0%, transparent 55%),
    radial-gradient(circle at 18% 72%, rgba(40, 65, 120, 0.08) 0%, transparent 50%),
    #050811;
}

/* Dynamic Slide Background Stage (Seamless Top Mask for Zero Seam) */
.foundation-stage-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center 30%;
  opacity: 0;
  transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 0;
  will-change: opacity;
  transform: scale(1.02);
  filter: brightness(0.96) contrast(1.04);
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.4) 60px, #000 130px);
  mask-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.4) 60px, #000 130px);
}

/* Luminous Ambient Contrast Scrim with Seamless Left Legibility */
.foundation-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(circle at 75% 30%, rgba(255, 255, 255, 0.06) 0%, transparent 50%),
    linear-gradient(90deg, rgba(5, 8, 17, 0.94) 0%, rgba(5, 8, 17, 0.82) 36%, rgba(5, 8, 17, 0.16) 68%, rgba(5, 8, 17, 0.32) 100%),
    linear-gradient(180deg, #050811 0%, rgba(5, 8, 17, 0.4) 15%, transparent 35%, transparent 75%, rgba(5, 8, 17, 0.85) 100%);
  pointer-events: none;
  z-index: 1;
}

"""
    content = content[:sec2_css_pos] + new_sec2_css + content[end_of_sec_css:]
    print("1. Updated Section 2 base CSS with stage-bg and scrim-overlay")
else:
    print("1. ERROR: sec2_css_marker not found")

# 2. Add card image styles
card_css_marker = ".foundation-card.is-active {"
pos_active = content.find(card_css_marker)
if pos_active != -1:
    pos_active_end = content.find("}", pos_active) + 1
    card_img_css = """

/* Card Image & Scrim Styling for Slide Visuals */
.foundation-card .card-bg-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  z-index: 0;
  filter: brightness(0.92) contrast(1.06);
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), filter 0.6s ease;
}

.foundation-card:hover .card-bg-img {
  transform: scale(1.06);
  filter: brightness(1.0) contrast(1.08);
}

.foundation-card .card-gradient-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg, 
    rgba(5, 8, 17, 0.45) 0%, 
    rgba(5, 8, 17, 0.15) 30%, 
    rgba(5, 8, 17, 0.70) 65%, 
    rgba(5, 8, 17, 0.96) 100%
  );
  z-index: 1;
  pointer-events: none;
}"""
    content = content[:pos_active_end] + card_img_css + content[pos_active_end:]
    print("2. Added card-bg-img & card-gradient-scrim CSS")
else:
    print("2. ERROR: card_css_marker not found")

# 3. Update HTML for curatedSection header to add foundationStageBg and scrim overlay
sec2_html_marker = '<section id="curatedSection" class="foundation-section" aria-label="Friends of Artsy Fartsy Foundation & Studio Experiences">'
new_sec2_html_header = """<section id="curatedSection" class="foundation-section" aria-label="Friends of Artsy Fartsy Foundation & Studio Experiences">
  <!-- Dynamic Slide Background Stage (Active Slide Image with Seamless Top Fade) -->
  <div class="foundation-stage-bg" id="foundationStageBg" style="background-image: url('/images/foundation-slide-1.jpg'); opacity: 1;" aria-hidden="true"></div>
  <!-- Cinematic Contrast Scrim -->
  <div class="foundation-scrim-overlay" aria-hidden="true"></div>"""

if sec2_html_marker in content:
    content = content.replace(sec2_html_marker, new_sec2_html_header, 1)
    print("3. Added foundationStageBg and scrim overlay to Section 2 HTML")
else:
    print("3. ERROR: sec2_html_marker not found")

# 4. Update Card 0 HTML to include Kids.png
card0_marker = '<!-- Card 0: Foundation Mission -->'
pos_card0 = content.find(card0_marker)
if pos_card0 != -1:
    pos_card0_end = content.find('<!-- Card 1: Studio Classes -->', pos_card0)
    new_card0_html = """<!-- Card 0: Foundation Mission (with Kids.png) -->
          <article class="foundation-card is-active has-img" data-index="0" tabindex="0" role="button" aria-label="Foundation Mission">
            <img class="card-bg-img" src="/images/foundation-slide-1.jpg" alt="Foundation Mission - Kids with Guitar in Sunlight" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-inner">
              <div class="card-top-meta">
                <span class="card-number-tag">01</span>
                <span class="card-status-pill">EQUITABLE ACCESS</span>
              </div>
              <div class="card-main-body">
                <div class="card-category-line">
                  <span class="dash">—</span>
                  <span>Nonprofit Mission</span>
                </div>
                <h3 class="card-main-heading">FOUNDATION MISSION</h3>
                <p class="card-snippet">Expanding access to the arts through high school scholarships, teacher training, and inspiring laboratory spaces.</p>
              </div>
              <div class="card-footer-action">
                <span class="card-cta-label">Explore Mission</span>
                <span class="card-cta-arrow">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                  </svg>
                </span>
              </div>
            </div>
          </article>

          """
    content = content[:pos_card0] + new_card0_html + content[pos_card0_end:]
    print("4. Updated Card 0 HTML with Kids.png")
else:
    print("4. ERROR: card0_marker not found")

# 5. Update JavaScript slides array and updateSlide logic
slides_marker = "var slides = ["
pos_slides = content.find(slides_marker)
if pos_slides != -1:
    pos_desc = content.find("id: 'foundation-mission',", pos_slides)
    pos_actions = content.find("actionsHtml:", pos_desc)
    # Insert bgImage: '/images/foundation-slide-1.jpg',
    bg_prop = "bgImage: '/images/foundation-slide-1.jpg',\n      "
    content = content[:pos_actions] + bg_prop + content[pos_actions:]
    print("5. Added bgImage to Slide 0 in JS")

# Add bgEl and updateSlide logic in JS
js_update_marker = "// 1. Background image removed per user request (clean cosmic background preserved)"
if js_update_marker in content:
    new_js_update = """// 1. Dynamic Slide Background Update with smooth crossfade
    if (bgEl) {
      if (s.bgImage) {
        bgEl.style.opacity = '0';
        setTimeout(function() {
          bgEl.style.backgroundImage = 'url(\"' + s.bgImage + '\")';
          bgEl.style.opacity = '1';
        }, 180);
      } else {
        bgEl.style.opacity = '0';
      }
    }"""
    content = content.replace(js_update_marker, new_js_update, 1)
    print("6. Updated updateSlide() background crossfade logic in JS")
else:
    print("6. Note: js_update_marker not found directly")

# Ensure var bgEl = document.getElementById('foundationStageBg'); is declared before updateSlide()
if "var bgEl = document.getElementById('foundationStageBg');" not in content:
    decl_marker = "var currentIndex = 0;"
    if decl_marker in content:
        content = content.replace(decl_marker, "var currentIndex = 0;\n  var bgEl = document.getElementById('foundationStageBg');", 1)
        print("7. Declared bgEl in JS controller")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html successfully")
