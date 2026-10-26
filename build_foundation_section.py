html = '''<!-- ============================================================
     SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE
     Inspired by Globe Express Horizontal Card Slider
     Enlarged Background Image with Mission & Donate CTA
     ============================================================ -->
<section id="curatedSection" class="foundation-section" aria-label="Friends of Artsy Fartsy Foundation">
  <!-- Active Slide Background (Enlarged to occupy the full background) -->
  <div class="foundation-stage-bg" id="foundationStageBg" style="background-image: url('/images/foundation-students.jpg');" aria-hidden="true"></div>
  <!-- Cinematic Scrim for Text Contrast -->
  <div class="foundation-scrim-overlay" aria-hidden="true"></div>

  <div class="foundation-container">
    
    <!-- Top Row: Left Info & Right Horizontal Cards -->
    <div class="foundation-main-row">
      
      <!-- Left Column: Mission Statement & Donate CTA -->
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

        <!-- Action Button: Donate (Bookmark and Offerings removed per user request) -->
        <div class="foundation-actions-row">
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
          
          <!-- Card 0: High School Students Classroom Photo -->
          <article class="foundation-card is-active" data-index="0" tabindex="0" role="button" aria-label="Foundation Mission">
            <img class="card-bg-img" src="/images/foundation-students.jpg" alt="Foundation Mission" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Equitable Arts Access</span>
              </div>
              <h3 class="card-main-heading">FOUNDATION MISSION</h3>
            </div>
          </article>

          <!-- Card 1: Student Scholarships -->
          <article class="foundation-card" data-index="1" tabindex="0" role="button" aria-label="Student Scholarships">
            <img class="card-bg-img" src="/images/card-classroom.webp" alt="Student Scholarships" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>High School & Adults</span>
              </div>
              <h3 class="card-main-heading">STUDENT SCHOLARSHIPS</h3>
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

print("HTML length:", len(html))
