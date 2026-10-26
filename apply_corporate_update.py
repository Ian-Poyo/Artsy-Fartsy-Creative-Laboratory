import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Section 2 HTML
new_html = '''<!-- ============================================================
     SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE
     Clean Editorial Layout with Glassmorphic Buttons
     5 Experiences: Mission, Classes, Birthday, Private Events, Corporate Events
     ============================================================ -->
<section id="curatedSection" class="foundation-section" aria-label="Friends of Artsy Fartsy Foundation & Studio Experiences">
  <!-- Active Slide Background (Enlarged to occupy the full background) -->
  <div class="foundation-stage-bg" id="foundationStageBg" style="background-image: url('/images/foundation-music-children.jpg');" aria-hidden="true"></div>
  <!-- Cinematic Contrast Scrim -->
  <div class="foundation-scrim-overlay" aria-hidden="true"></div>

  <div class="foundation-container">
    
    <!-- Top Row: Left Clean Editorial & Right Horizontal Cards -->
    <div class="foundation-main-row">
      
      <!-- Left Column: Clean Editorial Info (NO card wrapper) -->
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

        <!-- Action Row: Glassmorphic Buttons -->
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
                <span>Milestone Celebrations</span>
              </div>
              <h3 class="card-main-heading">BIRTHDAY EVENTS</h3>
            </div>
          </article>

          <!-- Card 3: Sunlit Luncheon Arcade Photo -> Private Events -->
          <article class="foundation-card" data-index="3" tabindex="0" role="button" aria-label="Private Events">
            <img class="card-bg-img" src="/images/foundation-private-events.jpg" alt="Private Events" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Bespoke Gatherings</span>
              </div>
              <h3 class="card-main-heading">PRIVATE EVENTS</h3>
            </div>
          </article>

          <!-- Card 4: Garden Cocktail Reception Photo -> Corporate Events -->
          <article class="foundation-card" data-index="4" tabindex="0" role="button" aria-label="Corporate Events">
            <img class="card-bg-img" src="/images/foundation-corporate-events.jpg" alt="Corporate Events" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Team &amp; Executive Retreats</span>
              </div>
              <h3 class="card-main-heading">CORPORATE EVENTS</h3>
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

# Replace HTML
pos_h_start = content.find('<!-- ============================================================\n     SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE')
pos_h_end = content.find('<!-- ============================================================\n     INTERACTIVE MODALS')
if pos_h_start != -1 and pos_h_end != -1:
    content = content[:pos_h_start] + new_html + '\n\n' + content[pos_h_end:]
    print("1. HTML replaced successfully!")
else:
    print("WARNING: Could not find HTML block!")

# 2. Update CSS with clean editorial & glassmorphic buttons
with open('/home/user/test_refined_css.py', 'r') as f:
    txt = f.read()
m_c = re.search(r"css = '''(.*?)'''", txt, re.DOTALL)
new_css = m_c.group(1).strip()

pos_c_start = content.find('/* ============================================================\n   SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE')
pos_c_end = content.find('</style>')
if pos_c_start != -1 and pos_c_end != -1:
    content = content[:pos_c_start] + new_css + '\n' + content[pos_c_end:]
    print("2. Refined CSS replaced successfully!")
else:
    print("WARNING: Could not find CSS block!")

# 3. Update eventsModal content
old_events_modal = '''<!-- Birthday & Private Events Modal -->
<div class="modal-overlay" id="eventsModal">
  <div class="modal-card">
    <button class="modal-close-btn" data-close aria-label="Close dialog">✕</button>
    <h2 class="modal-title">Birthday Parties & Events</h2>
    <div class="modal-subtitle">Milestone Celebrations & Private Atelier Gatherings</div>
    <div class="modal-body">
      <p>
        Celebrate life’s most cherished moments in our luminous studio atelier. We curate all-inclusive creative birthday parties, private soirées, milestone debuts, and celebratory gatherings with custom art projects, atmospheric lighting, and festive hospitality.
      </p>
      <div class="info-card">
        <h4>Color Magic Birthday Packages</h4>
        <p>Private studio access, custom color-splatter canvases, dedicated artist host, and personalized favors for all guests.</p>
      </div>
      <div class="info-card">
        <h4>Private Twilight Celebrations</h4>
        <p>Evening cocktail receptions, candlelit art soirées, curated music, and bespoke collaborative art keepsakes.</p>
      </div>
      <div class="info-card">
        <h4>Custom Event Design</h4>
        <p>Full floral arrangements, gourmet catering coordination, ambient lighting, and personalized themes tailored to your vision.</p>
      </div>
    </div>
  </div>
</div>'''

new_events_modal = '''<!-- Birthday, Private & Corporate Events Modal -->
<div class="modal-overlay" id="eventsModal">
  <div class="modal-card">
    <button class="modal-close-btn" data-close aria-label="Close dialog">✕</button>
    <h2 class="modal-title">Events & Celebrations</h2>
    <div class="modal-subtitle">Milestone Birthdays, Private Soirées & Corporate Retreats</div>
    <div class="modal-body">
      <p>
        Celebrate life’s most cherished moments and inspire your team in our luminous studio atelier. We curate all-inclusive creative events, bespoke private soirées, milestone celebrations, and collaborative corporate experiences tailored to your vision.
      </p>
      <div class="info-card">
        <h4>Color Magic Birthday Packages</h4>
        <p>Private studio access, custom color-splatter canvases, dedicated artist host, and personalized favors for all guests.</p>
      </div>
      <div class="info-card">
        <h4>Private Gatherings & Soirées</h4>
        <p>Evening cocktail receptions, sunlit arcade luncheons, candlelit art soirées, and bespoke collaborative keepsakes.</p>
      </div>
      <div class="info-card">
        <h4>Corporate Retreats & Team Building</h4>
        <p>Guided creative problem solving, collaborative large-scale murals, executive retreats, and festive holiday team celebrations.</p>
      </div>
    </div>
  </div>
</div>'''

if old_events_modal in content:
    content = content.replace(old_events_modal, new_events_modal, 1)
    print("3. eventsModal updated successfully!")
else:
    print("Note: old eventsModal format differed or already updated.")

# 4. Update JS controller
with open('/home/user/test_corporate_slider.py', 'r') as f:
    txt = f.read()
m_j = re.search(r"js = '''(.*?)'''", txt, re.DOTALL)
new_js = m_j.group(1).strip()

pos_j_start = content.find('// ============================================================\n// FRIENDS OF ARTSY FARTSY FOUNDATION SLIDER CONTROLLER')
pos_j_end = content.find('// ============================================================\n// NAVIGATION & PERFORMANCE CONTROLLER (HERO + CURATED)')
if pos_j_start != -1 and pos_j_end != -1:
    content = content[:pos_j_start] + new_js + '\n\n' + content[pos_j_end:]
    print("4. JS replaced successfully!")
else:
    print("WARNING: Could not find JS block!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html fully updated!")
