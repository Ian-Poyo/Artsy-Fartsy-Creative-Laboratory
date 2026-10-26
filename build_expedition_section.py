import re

# 1. HTML Markup
html = '''<!-- ============================================================
     SECTION 2: EXPEDITIONS SHOWCASE (GLOBE EXPRESS DESIGN)
     Pure White Background with Horizontal Card Slider
     ============================================================ -->
<section id="curatedSection" class="expedition-section" aria-label="Artsy Fartsy Studio Expeditions">
  <div class="expedition-container">
    
    <!-- Top Row: Left Info & Right Horizontal Cards -->
    <div class="expedition-main-row">
      
      <!-- Left Column: Active Experience Details -->
      <div class="expedition-info-col">
        <div class="expedition-eyebrow-wrap">
          <span class="eyebrow-dash">—</span>
          <span class="expedition-eyebrow" id="expeditionEyebrow">A LAB FOR THE UNCONVENTIONAL</span>
        </div>

        <h2 class="expedition-title" id="expeditionTitle">
          CREATIVE<br>LABORATORY
        </h2>

        <p class="expedition-desc" id="expeditionDesc">
          An experimental sanctuary where strange ideas take shape, materials are pushed to their breaking points, and creativity has no single direction.
        </p>

        <!-- Action Buttons Matching Pin Layout -->
        <div class="expedition-actions-row">
          <button class="expedition-bookmark-btn" id="expeditionBookmarkBtn" aria-label="Save to favorites">
            <svg class="bookmark-icon" viewBox="0 0 24 24" width="20" height="20" fill="currentColor">
              <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path>
            </svg>
          </button>

          <button class="expedition-discover-btn" id="expeditionDiscoverBtn">
            <span>DISCOVER STUDIO</span>
          </button>

          <button class="expedition-modal-btn" id="expeditionModalBtn" data-modal="homeModal">
            <span>OFFERINGS &rarr;</span>
          </button>
        </div>
      </div>

      <!-- Right Column: Horizontal Cards Slider Track -->
      <div class="expedition-cards-viewport" id="expeditionCardsViewport">
        <div class="expedition-cards-track" id="expeditionCardsTrack">
          
          <!-- Card 0: Stargazer Creative Lab -->
          <article class="expedition-card is-active" data-index="0" tabindex="0" role="button" aria-label="Creative Laboratory">
            <img class="card-bg-img" src="/images/card-starry.webp" alt="Creative Laboratory" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Stargazer Atelier</span>
              </div>
              <h3 class="card-main-heading">CREATIVE LABORATORY</h3>
            </div>
          </article>

          <!-- Card 1: Floating Classroom Workshops -->
          <article class="expedition-card" data-index="1" tabindex="0" role="button" aria-label="Floating Workshops">
            <img class="card-bg-img" src="/images/card-classroom.webp" alt="Floating Workshops" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Carmel Studio</span>
              </div>
              <h3 class="card-main-heading">FLOATING WORKSHOPS</h3>
            </div>
          </article>

          <!-- Card 2: Happy Birthday Color Magic -->
          <article class="expedition-card" data-index="2" tabindex="0" role="button" aria-label="Color Magic Celebrations">
            <img class="card-bg-img" src="/images/card-birthday.webp" alt="Color Magic Celebrations" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Milestone Parties</span>
              </div>
              <h3 class="card-main-heading">COLOR & CONFETTI</h3>
            </div>
          </article>

          <!-- Card 3: Collaborative Retreats -->
          <article class="expedition-card" data-index="3" tabindex="0" role="button" aria-label="Executive Retreats">
            <img class="card-bg-img" src="/images/card-presentation.jpg" alt="Executive Retreats" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Innovation Retreats</span>
              </div>
              <h3 class="card-main-heading">VISION IN CLOUDS</h3>
            </div>
          </article>

          <!-- Card 4: Garden Twilight Private Gatherings -->
          <article class="expedition-card" data-index="4" tabindex="0" role="button" aria-label="Garden Twilight Evenings">
            <img class="card-bg-img" src="/images/card-party.webp" alt="Garden Twilight Evenings" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Secret Garden</span>
              </div>
              <h3 class="card-main-heading">TWILIGHT SOIRÉES</h3>
            </div>
          </article>

        </div>
      </div>

    </div>

    <!-- Bottom Row: Navigation Controls, Progress Bar & Big Numeral Counter -->
    <div class="expedition-controls-bar">
      <!-- Circular Navigation Buttons -->
      <div class="expedition-arrow-buttons">
        <button class="expedition-circle-btn prev" id="expeditionPrevBtn" aria-label="Previous destination">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="19" y1="12" x2="5" y2="12"></line>
            <polyline points="12 19 5 12 12 5"></polyline>
          </svg>
        </button>
        <button class="expedition-circle-btn next" id="expeditionNextBtn" aria-label="Next destination">
          <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </button>
      </div>

      <!-- Center Progress Track -->
      <div class="expedition-progress-track" aria-hidden="true">
        <div class="expedition-progress-fill" id="expeditionProgressFill"></div>
      </div>

      <!-- Right Large Display Numeral -->
      <div class="expedition-counter-display">
        <span class="expedition-counter-num" id="expeditionCounterNum">01</span>
      </div>
    </div>

  </div>
</section>'''

print("HTML generated successfully! Length:", len(html))
