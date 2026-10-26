import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .hero-bottom-scrim to reach solid #050811 before bottom
old_scrim = """.hero-bottom-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    transparent 32%,
    rgba(8, 24, 60, 0.22) 48%,
    rgba(5, 16, 44, 0.65) 66%,
    rgba(4, 11, 28, 0.88) 84%,
    rgba(3, 8, 20, 0.96) 100%
  );
  pointer-events: none;
  z-index: 10;
}"""

new_scrim = """.hero-bottom-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    transparent 34%,
    rgba(5, 8, 17, 0.22) 48%,
    rgba(5, 8, 17, 0.60) 65%,
    rgba(5, 8, 17, 0.90) 82%,
    rgba(5, 8, 17, 0.99) 93%,
    #050811 96%,
    #050811 100%
  );
  pointer-events: none;
  z-index: 10;
}"""

if old_scrim in content:
    content = content.replace(old_scrim, new_scrim, 1)
    print("Updated .hero-bottom-scrim successfully")
else:
    print("Warning: old_scrim exact match not found, looking with regex")
    pattern = r'\.hero-bottom-scrim\s*\{[^}]*\}'
    content = re.sub(pattern, new_scrim, content, count=1)
    print("Replaced .hero-bottom-scrim with regex")

# 2. Update .foundation-section and remove image/scrim CSS
old_sec2_css = """/* ============================================================
   SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE
   Pure White Minimalist Theme with Moving Gradient Rainbow Heart
   Seamless Transitional Blending & Smooth Slide Easing
   ============================================================ */
.foundation-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  padding: clamp(80px, 11vh, 120px) clamp(24px, 5vw, 64px) clamp(80px, 11vh, 120px);
  box-sizing: border-box;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #ffffff;
  z-index: 20;
}

/* Seamless Transitional Blend connecting Hero to Section 2 (Fixes harsh seam in image-1.png) */
.foundation-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 240px;
  background: linear-gradient(180deg, #050811 0%, rgba(5, 8, 17, 0.9) 35%, rgba(5, 8, 17, 0.45) 70%, transparent 100%);
  pointer-events: none;
  z-index: 2;
}

/* Enlarged Background Image Stage (Active Slide Image Fills Area with Pure Lighting) */
.foundation-stage-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center 30%;
  transition: opacity 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 0;
  will-change: opacity, transform;
  transform: scale(1.02);
  filter: brightness(1.02) contrast(1.04);
}

/* Luminous Ambient Contrast Scrim with Seamless Top Gradient */
.foundation-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(circle at 75% 30%, rgba(255, 255, 255, 0.07) 0%, transparent 50%),
    linear-gradient(90deg, rgba(8, 11, 18, 0.92) 0%, rgba(8, 11, 18, 0.78) 36%, rgba(8, 11, 18, 0.12) 68%, rgba(8, 11, 18, 0.28) 100%),
    linear-gradient(180deg, #050811 0%, rgba(5, 8, 17, 0.8) 15%, transparent 35%, transparent 75%, rgba(8, 11, 18, 0.85) 100%);
  pointer-events: none;
  z-index: 1;
}"""

new_sec2_css = """/* ============================================================
   SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE
   Pure White Minimalist Theme with Moving Gradient Rainbow Heart
   Seamless Cosmic Backdrop & Image-Free Glassmorphic Cards
   ============================================================ */
.foundation-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  margin-top: -1px; /* Seamless subpixel blend with Hero */
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
}"""

if old_sec2_css in content:
    content = content.replace(old_sec2_css, new_sec2_css, 1)
    print("Updated Section 2 background CSS successfully")
else:
    print("Warning: old_sec2_css exact match not found!")

# 3. Update Card CSS (remove card-bg-img and scrim, add modern typography and glassmorphism)
old_card_css = """/* Cards with Bright Luminous Lighting */
.foundation-card {
  flex: 0 0 clamp(190px, 20vw, 230px);
  height: clamp(280px, 30vw, 340px);
  border-radius: 20px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
  transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
  border: 2px solid rgba(255, 255, 255, 0.22);
  background: #0b0f19;
  outline: none;
}

.foundation-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 24px 50px rgba(0, 0, 0, 0.6), 0 0 20px rgba(255, 255, 255, 0.25);
  border-color: rgba(255, 255, 255, 0.6);
}

/* Pure White Luminous Active Card Border (Yellow Removed) */
.foundation-card.is-active {
  border: 2.5px solid #ffffff;
  box-shadow: 
    0 20px 48px rgba(0, 0, 0, 0.55),
    0 0 26px rgba(255, 255, 255, 0.4),
    inset 0 0 15px rgba(255, 255, 255, 0.12);
  transform: translateY(-4px);
}

.card-bg-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  filter: brightness(1.05) contrast(1.04);
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), filter 0.6s ease;
}

.foundation-card:hover .card-bg-img {
  transform: scale(1.06);
  filter: brightness(1.08) contrast(1.06);
}

/* Refined Scrim letting natural light pour in */
.card-gradient-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 48%, rgba(6, 8, 14, 0.85) 100%);
  pointer-events: none;
}

.card-content-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 20px 18px;
  color: #ffffff;
  z-index: 2;
  pointer-events: none;
}

/* Pure White Category Line (Yellow Removed) */
.card-category-line {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #ffffff;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.card-category-line .dash {
  color: #ffffff;
  opacity: 0.9;
}

.card-main-heading {
  font-family: var(--font-sans);
  font-size: 1.15rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #ffffff;
  margin: 0;
  line-height: 1.25;
}"""

new_card_css = """/* Cards with Clean Glassmorphism & Elegant Typography (No Images) */
.foundation-card {
  flex: 0 0 clamp(240px, 24vw, 290px);
  height: clamp(310px, 32vw, 360px);
  border-radius: 22px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.42);
  transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.35s ease, border-color 0.35s ease, background 0.35s ease;
  border: 1px solid rgba(255, 255, 255, 0.14);
  background: linear-gradient(160deg, rgba(255, 255, 255, 0.06) 0%, rgba(255, 255, 255, 0.02) 100%);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  outline: none;
  box-sizing: border-box;
}

.foundation-card:hover {
  transform: translateY(-6px);
  background: linear-gradient(160deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.035) 100%);
  box-shadow: 0 24px 50px rgba(0, 0, 0, 0.55), 0 0 24px rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.4);
}

/* Pure White Luminous Active Card Border */
.foundation-card.is-active {
  border: 1.5px solid #ffffff;
  background: linear-gradient(160deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.045) 100%);
  box-shadow: 
    0 22px 48px rgba(0, 0, 0, 0.58),
    0 0 32px rgba(255, 255, 255, 0.22),
    inset 0 1px 0 rgba(255, 255, 255, 0.45);
  transform: translateY(-4px);
}

.card-inner {
  width: 100%;
  height: 100%;
  padding: clamp(20px, 2.2vw, 26px);
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: left;
}

.card-top-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
}

.card-number-tag {
  font-family: var(--font-mono, monospace);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #ffffff;
  padding: 3px 9px;
  border-radius: 6px;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.16);
}

.card-status-pill {
  font-family: var(--font-sans);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.72);
}

.card-main-body {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin: auto 0;
}

.card-category-line {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.75);
  display: flex;
  align-items: center;
  gap: 6px;
}

.card-category-line .dash {
  color: #ffffff;
  opacity: 0.85;
}

.card-main-heading {
  font-family: var(--font-sans);
  font-size: clamp(1.1rem, 1.4vw, 1.3rem);
  font-weight: 800;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #ffffff;
  margin: 0;
  line-height: 1.22;
}

.card-snippet {
  font-family: var(--font-sans);
  font-size: 13px;
  line-height: 1.55;
  color: rgba(255, 255, 255, 0.82);
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-footer-action {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.card-cta-label {
  font-family: var(--font-sans);
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.06em;
  color: #ffffff;
}

.card-cta-arrow {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.12);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  transition: transform 0.25s ease, background 0.25s ease;
}

.foundation-card:hover .card-cta-arrow {
  transform: translateX(4px);
  background: rgba(255, 255, 255, 0.28);
}"""

if old_card_css in content:
    content = content.replace(old_card_css, new_card_css, 1)
    print("Updated Card CSS successfully")
else:
    print("Warning: old_card_css exact match not found!")

# 4. Remove Section 2 background stage & scrim from HTML
old_sec2_html_header = """<section id="curatedSection" class="foundation-section" aria-label="Friends of Artsy Fartsy Foundation & Studio Experiences">
  <!-- Active Slide Background (Enlarged to occupy the full background) -->
  <div class="foundation-stage-bg" id="foundationStageBg" style="background-image: url('/images/foundation-music-children.jpg');" aria-hidden="true"></div>
  <!-- Cinematic Contrast Scrim -->
  <div class="foundation-scrim-overlay" aria-hidden="true"></div>"""

new_sec2_html_header = """<section id="curatedSection" class="foundation-section" aria-label="Friends of Artsy Fartsy Foundation & Studio Experiences">"""

if old_sec2_html_header in content:
    content = content.replace(old_sec2_html_header, new_sec2_html_header, 1)
    print("Removed foundationStageBg and scrim overlay from HTML")
else:
    print("Warning: old_sec2_html_header exact match not found!")

# 5. Replace the 5 cards in HTML with clean image-free cards
old_cards_track = """      <!-- Right Column: Horizontal Cards Slider Track -->
      <div class="foundation-cards-viewport" id="foundationCardsViewport">
        <div class="foundation-cards-track" id="foundationCardsTrack">
          
          <!-- Card 0: Children Music Gathering Photo -> Foundation Mission -->
          <article class="foundation-card is-active" data-index="0" tabindex="0" role="button" aria-label="Foundation Mission">
            <img class="card-bg-img" src="/images/foundation-music-children.jpg" alt="Foundation Mission" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Equitable Arts Access</span>
              </div>
              <h3 class="card-main-heading">FOUNDATION MISSION</h3>
            </div>
          </article>

          <!-- Card 1: High School Students Classroom Photo -> Studio Classes -->
          <article class="foundation-card" data-index="1" tabindex="0" role="button" aria-label="Studio Classes">
            <img class="card-bg-img" src="/images/foundation-students.jpg" alt="Studio Classes" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Hands-On Discovery</span>
              </div>
              <h3 class="card-main-heading">STUDIO CLASSES</h3>
            </div>
          </article>

          <!-- Card 2: Gala Celebration Photo -> Birthday Events -->
          <article class="foundation-card" data-index="2" tabindex="0" role="button" aria-label="Birthday Events">
            <img class="card-bg-img" src="/images/foundation-events-party.jpg" alt="Birthday Events" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Milestone Gatherings</span>
              </div>
              <h3 class="card-main-heading">BIRTHDAY EVENTS</h3>
            </div>
          </article>

          <!-- Card 3: Creative Workshop Photo -> Private Events -->
          <article class="foundation-card" data-index="3" tabindex="0" role="button" aria-label="Private Events">
            <img class="card-bg-img" src="/images/foundation-workshop.jpg" alt="Private Events" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Intimate Occasions</span>
              </div>
              <h3 class="card-main-heading">PRIVATE EVENTS</h3>
            </div>
          </article>

          <!-- Card 4: Corporate Gathering Photo -> Corporate Events -->
          <article class="foundation-card" data-index="4" tabindex="0" role="button" aria-label="Corporate Events">
            <img class="card-bg-img" src="/images/foundation-gala.jpg" alt="Corporate Events" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Creative Team Building</span>
              </div>
              <h3 class="card-main-heading">CORPORATE EVENTS</h3>
            </div>
          </article>

        </div>
      </div>"""

new_cards_track = """      <!-- Right Column: Horizontal Cards Slider Track -->
      <div class="foundation-cards-viewport" id="foundationCardsViewport">
        <div class="foundation-cards-track" id="foundationCardsTrack">
          
          <!-- Card 0: Foundation Mission -->
          <article class="foundation-card is-active" data-index="0" tabindex="0" role="button" aria-label="Foundation Mission">
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

          <!-- Card 1: Studio Classes -->
          <article class="foundation-card" data-index="1" tabindex="0" role="button" aria-label="Studio Classes">
            <div class="card-inner">
              <div class="card-top-meta">
                <span class="card-number-tag">02</span>
                <span class="card-status-pill">WEEKLY WORKSHOPS</span>
              </div>
              <div class="card-main-body">
                <div class="card-category-line">
                  <span class="dash">—</span>
                  <span>Hands-On Discovery</span>
                </div>
                <h3 class="card-main-heading">STUDIO CLASSES</h3>
                <p class="card-snippet">Fun-filled weekly classes, adult masterclasses, and hands-on color science exploration designed to spark open-ended discovery.</p>
              </div>
              <div class="card-footer-action">
                <span class="card-cta-label">View Classes</span>
                <span class="card-cta-arrow">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                  </svg>
                </span>
              </div>
            </div>
          </article>

          <!-- Card 2: Birthday Events -->
          <article class="foundation-card" data-index="2" tabindex="0" role="button" aria-label="Birthday Events">
            <div class="card-inner">
              <div class="card-top-meta">
                <span class="card-number-tag">03</span>
                <span class="card-status-pill">CELEBRATIONS</span>
              </div>
              <div class="card-main-body">
                <div class="card-category-line">
                  <span class="dash">—</span>
                  <span>Milestone Moments</span>
                </div>
                <h3 class="card-main-heading">BIRTHDAY EVENTS</h3>
                <p class="card-snippet">Unforgettable birthday experiences featuring dedicated artist hosts, color splatter canvases, and custom creative party packages.</p>
              </div>
              <div class="card-footer-action">
                <span class="card-cta-label">View Packages</span>
                <span class="card-cta-arrow">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                  </svg>
                </span>
              </div>
            </div>
          </article>

          <!-- Card 3: Private Events -->
          <article class="foundation-card" data-index="3" tabindex="0" role="button" aria-label="Private Events">
            <div class="card-inner">
              <div class="card-top-meta">
                <span class="card-number-tag">04</span>
                <span class="card-status-pill">INTIMATE GATHERINGS</span>
              </div>
              <div class="card-main-body">
                <div class="card-category-line">
                  <span class="dash">—</span>
                  <span>Bespoke Soirées</span>
                </div>
                <h3 class="card-main-heading">PRIVATE EVENTS</h3>
                <p class="card-snippet">Custom celebratory gatherings, bridal luncheons, and intimate soirees with bespoke creative experiences and curated tablescapes.</p>
              </div>
              <div class="card-footer-action">
                <span class="card-cta-label">Book Soirée</span>
                <span class="card-cta-arrow">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                  </svg>
                </span>
              </div>
            </div>
          </article>

          <!-- Card 4: Corporate Events -->
          <article class="foundation-card" data-index="4" tabindex="0" role="button" aria-label="Corporate Events">
            <div class="card-inner">
              <div class="card-top-meta">
                <span class="card-number-tag">05</span>
                <span class="card-status-pill">EXECUTIVE RETREATS</span>
              </div>
              <div class="card-main-body">
                <div class="card-category-line">
                  <span class="dash">—</span>
                  <span>Team Innovation</span>
                </div>
                <h3 class="card-main-heading">CORPORATE EVENTS</h3>
                <p class="card-snippet">Tailored retreats, collaborative team canvas sessions, and color theory workshops that inspire camaraderie and fresh thinking.</p>
              </div>
              <div class="card-footer-action">
                <span class="card-cta-label">Plan Retreat</span>
                <span class="card-cta-arrow">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M5 12h14M12 5l7 7-7 7"/>
                  </svg>
                </span>
              </div>
            </div>
          </article>

        </div>
      </div>"""

if old_cards_track in content:
    content = content.replace(old_cards_track, new_cards_track, 1)
    print("Replaced cards with image-free clean glassmorphic cards in HTML")
else:
    print("Warning: old_cards_track exact match not found!")

# 6. Update JavaScript: clean up bgEl and bgImage
old_js_bg = """    // 1. Update Background with smooth transition
    if (bgEl) {
      bgEl.style.opacity = '0.35';
      setTimeout(function() {
        bgEl.style.backgroundImage = 'url(\"' + s.bgImage + '\")';
        bgEl.style.opacity = '1';
      }, 180);
    }"""

new_js_bg = """    // 1. Background image removed per user request (clean cosmic background preserved)"""

if old_js_bg in content:
    content = content.replace(old_js_bg, new_js_bg, 1)
    print("Updated JS updateSlide() background logic")
else:
    print("Warning: old_js_bg exact match not found!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html")
