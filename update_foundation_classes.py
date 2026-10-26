import re

# 1. Update Section 2 HTML
new_html = '''<!-- ============================================================
     SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE
     Inspired by Globe Express Horizontal Card Slider
     Enlarged Background Image with Mission & Classes Showcase
     ============================================================ -->
<section id="curatedSection" class="foundation-section" aria-label="Friends of Artsy Fartsy Foundation & Studio Classes">
  <!-- Active Slide Background (Enlarged to occupy the full background) -->
  <div class="foundation-stage-bg" id="foundationStageBg" style="background-image: url('/images/foundation-music-children.jpg');" aria-hidden="true"></div>
  <!-- Cinematic Scrim for Text Contrast -->
  <div class="foundation-scrim-overlay" aria-hidden="true"></div>

  <div class="foundation-container">
    
    <!-- Top Row: Left Info & Right Horizontal Cards -->
    <div class="foundation-main-row">
      
      <!-- Left Column: Mission Statement, Classes & Dynamic Actions -->
      <div class="foundation-info-col">
        <div class="foundation-eyebrow-wrap">
          <span class="foundation-eyebrow" id="foundationEyebrow">— Mission Statement</span>
        </div>

        <h2 class="foundation-title" id="foundationTitle">
          Friends of Artsy Fartsy Foundation
        </h2>

        <div class="foundation-desc" id="foundationDesc">
          <p>Our mission is to ensure accessible, inspiring space for the Artsy Fartsy Creative Laboratory; expand equitable access to the arts through scholarships for high school students and adult learners; and strengthen arts education by delivering high-quality color science professional development for elementary, middle, and high school teachers.</p>
          <p>We believe creativity is a powerful catalyst for learning, expression, and community, and we work to nurture it across ages, disciplines, and classrooms.</p>
        </div>

        <!-- Action Row: Dynamically updated per slide -->
        <div class="foundation-actions-row" id="foundationActionsRow">
          <button class="foundation-donate-btn" id="foundationDonateBtn" data-modal="donateModal" aria-label="Donate to the Foundation">
            <svg class="donate-heart" viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
            <span>DONATE</span>
          </button>
        </div>
      </div>

      <!-- Right Column: Horizontal Cards Slider Track -->
      <div class="foundation-cards-viewport" id="foundationCardsViewport">
        <div class="foundation-cards-track" id="foundationCardsTrack">
          
          <!-- Card 0: Children Music Gathering Photo -->
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

          <!-- Card 2: Teacher Development -->
          <article class="foundation-card" data-index="2" tabindex="0" role="button" aria-label="Teacher Development">
            <img class="card-bg-img" src="/images/card-birthday.webp" alt="Teacher Development" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>K-12 Educators</span>
              </div>
              <h3 class="card-main-heading">TEACHER DEVELOPMENT</h3>
            </div>
          </article>

          <!-- Card 3: Creative Lab Space -->
          <article class="foundation-card" data-index="3" tabindex="0" role="button" aria-label="Creative Lab Space">
            <img class="card-bg-img" src="/images/card-starry.webp" alt="Creative Lab Space" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Carmel Studio</span>
              </div>
              <h3 class="card-main-heading">CREATIVE LAB SPACE</h3>
            </div>
          </article>

          <!-- Card 4: Community Impact -->
          <article class="foundation-card" data-index="4" tabindex="0" role="button" aria-label="Community Impact">
            <img class="card-bg-img" src="/images/card-party.webp" alt="Community Impact" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Lifelong Creativity</span>
              </div>
              <h3 class="card-main-heading">COMMUNITY IMPACT</h3>
            </div>
          </article>

        </div>
      </div>

    </div>

    <!-- Bottom Row: Navigation Controls, Progress Bar & Big Numeral Counter -->
    <div class="foundation-controls-bar">
      <!-- Circular Navigation Buttons -->
      <div class="foundation-arrow-buttons">
        <button class="foundation-circle-btn prev" id="foundationPrevBtn" aria-label="Previous slide">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="19" y1="12" x2="5" y2="12"></line>
            <polyline points="12 19 5 12 12 5"></polyline>
          </svg>
        </button>
        <button class="foundation-circle-btn next" id="foundationNextBtn" aria-label="Next slide">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </button>
      </div>

      <!-- Center Progress Track -->
      <div class="foundation-progress-track" aria-hidden="true">
        <div class="foundation-progress-fill" id="foundationProgressFill"></div>
      </div>

      <!-- Right Large Display Numeral -->
      <div class="foundation-counter-display">
        <span class="foundation-counter-num" id="foundationCounterNum">01</span>
      </div>
    </div>

  </div>
</section>'''

# 2. Update Section 2 CSS with Book & Offerings buttons
new_css_buttons = '''
/* Action Row & Buttons */
.foundation-actions-row {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  transition: opacity 0.25s ease;
}

.foundation-donate-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 40px;
  border-radius: 9999px;
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.35);
  font-family: var(--font-sans);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s ease;
  box-shadow: 0 8px 24px rgba(245, 158, 11, 0.38);
  outline: none;
}

.foundation-donate-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(245, 158, 11, 0.55);
  filter: brightness(1.1);
}

.foundation-donate-btn:active {
  transform: scale(0.96);
}

.foundation-donate-btn .donate-heart {
  color: #ffffff;
  animation: heartPulseMini 2s infinite;
}

@keyframes heartPulseMini {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.18); }
}

/* Book Button for Classes */
.foundation-book-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 38px;
  border-radius: 9999px;
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.35);
  font-family: var(--font-sans);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s ease;
  box-shadow: 0 8px 24px rgba(245, 158, 11, 0.38);
  outline: none;
}

.foundation-book-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(245, 158, 11, 0.55);
  filter: brightness(1.1);
}

.foundation-book-btn:active {
  transform: scale(0.96);
}

/* Offerings Button for Classes */
.foundation-offerings-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 13px 26px;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.12);
  color: #ffffff;
  border: 1.5px solid rgba(255, 255, 255, 0.35);
  font-family: var(--font-sans);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s ease;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  outline: none;
}

.foundation-offerings-btn:hover {
  background: #ffffff;
  color: #0b0f19;
  border-color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255, 255, 255, 0.3);
}

.foundation-offerings-btn:active {
  transform: scale(0.96);
}
'''

# 3. Update Section 2 JS with the exact prompt requirements
with open('/home/user/test_new_slider_setup.py', 'r') as f:
    txt = f.read()
m_j = re.search(r"js = '''(.*?)'''", txt, re.DOTALL)
new_js = m_j.group(1).strip()

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace HTML
pos_h_start = content.find('<!-- ============================================================\n     SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE')
pos_h_end = content.find('<!-- ============================================================\n     INTERACTIVE MODALS')
if pos_h_start != -1 and pos_h_end != -1:
    content = content[:pos_h_start] + new_html + '\n\n' + content[pos_h_end:]
    print("1. HTML replaced successfully!")
else:
    print("WARNING: Could not find HTML block!")

# Replace CSS actions section
old_css_actions = content.find('/* Action Row (Bookmark & Offerings removed per user instructions) */')
old_css_actions_end = content.find('/* Right Column: Horizontal Cards Slider Track */')
if old_css_actions != -1 and old_css_actions_end != -1:
    content = content[:old_css_actions] + new_css_buttons.strip() + '\n\n' + content[old_css_actions_end:]
    print("2. CSS actions replaced successfully!")
else:
    print("WARNING: Could not find CSS actions block!")

# Replace JS
pos_j_start = content.find('// ============================================================\n// FRIENDS OF ARTSY FARTSY FOUNDATION SLIDER CONTROLLER')
pos_j_end = content.find('// ============================================================\n// NAVIGATION & PERFORMANCE CONTROLLER (HERO + CURATED)')
if pos_j_start != -1 and pos_j_end != -1:
    content = content[:pos_j_start] + new_js + '\n\n' + content[pos_j_end:]
    print("3. JS replaced successfully!")
else:
    print("WARNING: Could not find JS block!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html fully updated!")
