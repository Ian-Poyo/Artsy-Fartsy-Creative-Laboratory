with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Card CSS
css_start_marker = "/* Cards with Bright Luminous Lighting */"
css_end_marker = "/* Bottom Controls Bar */"

pos1 = content.find(css_start_marker)
pos2 = content.find(css_end_marker, pos1)

if pos1 != -1 and pos2 != -1:
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
}

"""
    content = content[:pos1] + new_card_css + content[pos2:]
    print("1. Successfully updated card CSS")
else:
    print("1. ERROR: CSS markers not found")

# 2. Update HTML Cards Track
html_start_marker = '<div class="foundation-cards-viewport" id="foundationCardsViewport">'
html_end_marker = '<!-- Bottom Row: Navigation Controls, Progress Bar & Big Numeral Counter -->'

pos1 = content.find(html_start_marker)
pos2 = content.find(html_end_marker, pos1)

if pos1 != -1 and pos2 != -1:
    # Find the closing </div>\n      </div>\n\n    </div>
    inner_block = content[pos1:pos2]
    new_cards_html = """<div class="foundation-cards-viewport" id="foundationCardsViewport">
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
      </div>

    </div>

    """
    content = content[:pos1] + new_cards_html + content[pos2:]
    print("2. Successfully updated HTML cards track")
else:
    print("2. ERROR: HTML markers not found")

# 3. Update JavaScript: remove bgEl logic
js_marker_start = "// 1. Update Background with smooth transition"
pos_bg = content.find(js_marker_start)
if pos_bg != -1:
    pos_bg_end = content.find("// 2. Update Left Column Text", pos_bg)
    new_bg_js = "// 1. Background image removed per user request (clean cosmic background preserved)\n\n    "
    content = content[:pos_bg] + new_bg_js + content[pos_bg_end:]
    print("3. Successfully updated JS updateSlide() background logic")
else:
    print("3. JS background update marker not found")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html")
