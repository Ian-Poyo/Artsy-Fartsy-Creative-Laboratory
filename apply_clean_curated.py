import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean Section 2 HTML
clean_html = '''<!-- ============================================================
     SECTION 2: CURATED CAROUSELS (FUNKY TWIST 3D SHOWCASE)
     Clean, Pure 3D Carousel matching Pinterest Reference
     ============================================================ -->
<section id="curatedSection" class="curated-section" aria-label="Curated Carousels Showcase">
  <div class="curated-ambient-glow" aria-hidden="true"></div>

  <div class="curated-container">
    <!-- Left-aligned Editorial Title from Reference Image -->
    <div class="curated-title-group">
      <h2 class="curated-title">
        <span class="curated-word-italic">Curated</span>
        <span class="curated-word-main">Carousels</span>
      </h2>
    </div>

    <!-- The 3D Funky Twist Viewport -->
    <div class="funky-viewport" id="funkyViewport" role="region" aria-roledescription="carousel" aria-label="Curated Carousels">
      <div class="funky-cards-stage" id="funkyCardsStage">
        
        <!-- Card 01: Funky Twist -->
        <article class="funky-card card-01" data-index="0" data-slot="0" tabindex="0" role="group" aria-roledescription="slide" aria-label="1 of 5: Funky Twist">
          <div class="card-glass-specular" aria-hidden="true"></div>
          <div class="card-inner">
            <div class="card-titles">
              <span class="card-title">Funky Twist</span>
              <span class="card-subtitle">Desktop</span>
            </div>
            <div class="card-footer">
              <span class="card-badge">108™</span>
              <span class="card-num">01</span>
            </div>
          </div>
        </article>

        <!-- Card 02: Floating Studio -->
        <article class="funky-card card-02" data-index="1" data-slot="1" tabindex="0" role="group" aria-roledescription="slide" aria-label="2 of 5: Floating Studio">
          <div class="card-glass-specular" aria-hidden="true"></div>
          <div class="card-inner">
            <div class="card-titles">
              <span class="card-title">Floating Studio</span>
              <span class="card-subtitle">Workshops</span>
            </div>
            <div class="card-footer">
              <span class="card-badge">108™</span>
              <span class="card-num">02</span>
            </div>
          </div>
        </article>

        <!-- Card 03: Color Magic -->
        <article class="funky-card card-03" data-index="2" data-slot="deep" tabindex="0" role="group" aria-roledescription="slide" aria-label="3 of 5: Color Magic">
          <div class="card-glass-specular" aria-hidden="true"></div>
          <div class="card-inner">
            <div class="card-titles">
              <span class="card-title">Color Magic</span>
              <span class="card-subtitle">Celebrations</span>
            </div>
            <div class="card-footer">
              <span class="card-badge">108™</span>
              <span class="card-num">03</span>
            </div>
          </div>
        </article>

        <!-- Card 04: Cloud Vision -->
        <article class="funky-card card-04" data-index="3" data-slot="deep" tabindex="0" role="group" aria-roledescription="slide" aria-label="4 of 5: Cloud Vision">
          <div class="card-glass-specular" aria-hidden="true"></div>
          <div class="card-inner">
            <div class="card-titles">
              <span class="card-title">Cloud Vision</span>
              <span class="card-subtitle">Retreats</span>
            </div>
            <div class="card-footer">
              <span class="card-badge">108™</span>
              <span class="card-num">04</span>
            </div>
          </div>
        </article>

        <!-- Card 05: Garden Twilight -->
        <article class="funky-card card-05" data-index="4" data-slot="-1" tabindex="0" role="group" aria-roledescription="slide" aria-label="5 of 5: Garden Twilight">
          <div class="card-glass-specular" aria-hidden="true"></div>
          <div class="card-inner">
            <div class="card-titles">
              <span class="card-title">Garden Twilight</span>
              <span class="card-subtitle">Evenings</span>
            </div>
            <div class="card-footer">
              <span class="card-badge">108™</span>
              <span class="card-num">05</span>
            </div>
          </div>
        </article>

      </div>
    </div>

    <!-- Controls Row (Left Buttons & Right Title) -->
    <div class="funky-controls-row">
      <div class="funky-buttons-wrap">
        <button class="funky-nav-btn prev" id="funkyPrevBtn" aria-label="Previous card">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="19" y1="12" x2="5" y2="12"></line>
            <polyline points="12 19 5 12 12 5"></polyline>
          </svg>
        </button>
        <button class="funky-nav-btn next active" id="funkyNextBtn" aria-label="Next card">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
          
          <!-- Illustrated Hand Cursor Pointer from Reference Image -->
          <span class="funky-hand-cursor" id="funkyHandCursor" aria-hidden="true">
            <svg width="28" height="32" viewBox="0 0 28 32" fill="none">
              <path d="M10 2 C10 0.9 10.9 0 12 0 C13.1 0 14 0.9 14 2 L14 13 L15.5 13 C16.6 13 17.5 13.9 17.5 15 L17.5 16 C18.3 16 19 16.7 19 17.5 L19 19 C19.8 19 20.5 19.7 20.5 20.5 L20.5 24 C20.5 28.1 17.1 31.5 13 31.5 L10.5 31.5 C7.5 31.5 4.7 29.8 3.3 27.2 L0.8 22.3 C0.3 21.3 0.6 20.1 1.5 19.5 C2.4 18.9 3.6 19.2 4.2 20.1 L6 22.8 L6 8 C6 6.9 6.9 6 8 6 C9.1 6 10 6.9 10 8 Z" fill="rgba(0,0,0,0.4)" transform="translate(1, 2)"/>
              <path d="M10 2 C10 0.9 10.9 0 12 0 C13.1 0 14 0.9 14 2 L14 13 L15.5 13 C16.6 13 17.5 13.9 17.5 15 L17.5 16 C18.3 16 19 16.7 19 17.5 L19 19 C19.8 19 20.5 19.7 20.5 20.5 L20.5 24 C20.5 28.1 17.1 31.5 13 31.5 L10.5 31.5 C7.5 31.5 4.7 29.8 3.3 27.2 L0.8 22.3 C0.3 21.3 0.6 20.1 1.5 19.5 C2.4 18.9 3.6 19.2 4.2 20.1 L6 22.8 L6 8 C6 6.9 6.9 6 8 6 C9.1 6 10 6.9 10 8 Z" fill="#ffffff" stroke="#181818" stroke-width="1.8" stroke-linejoin="round"/>
              <path d="M14 16 L14 21 M17.5 18 L17.5 22 M19 21 L19 24" stroke="#181818" stroke-width="1.4" stroke-linecap="round"/>
            </svg>
          </span>
        </button>
      </div>

      <!-- Right Active Title from Reference Image -->
      <div class="funky-label-display">
        <span class="funky-active-title" id="funkyActiveTitle">Funky Twist</span>
      </div>
    </div>

  </div>
</section>'''

pos_h_start = content.find('<!-- ============================================================\n     SECTION 2: CURATED CAROUSELS')
pos_h_end = content.find('<!-- ============================================================\n     SECTION 2: EXPANDED BOTTOM SHOWCASE')

if pos_h_start != -1 and pos_h_end != -1:
    content = content[:pos_h_start] + clean_html + '\n\n' + content[pos_h_end:]
    print("1. Clean Section 2 HTML inserted without extra boxes!")
else:
    print("WARNING: pos_h_start or pos_h_end not found!")

# 2. Clean Section 2 CSS
clean_css = '''/* ============================================================
   SECTION 2: CURATED CAROUSELS (FUNKY TWIST 3D SHOWCASE)
   Pure, Elegant 3D Carousel matching Pinterest Reference
   ============================================================ */
.curated-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  padding: clamp(80px, 11vh, 130px) clamp(20px, 4.5vw, 48px) clamp(80px, 12vh, 140px);
  box-sizing: border-box;
  background-color: #070912;
  background-image: 
    radial-gradient(ellipse 75% 55% at 50% 0%, rgba(10, 63, 138, 0.38) 0%, transparent 70%),
    radial-gradient(ellipse 65% 50% at 85% 40%, rgba(217, 119, 6, 0.14) 0%, transparent 65%),
    radial-gradient(ellipse 60% 45% at 15% 75%, rgba(139, 92, 246, 0.16) 0%, transparent 60%);
  color: #ffffff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  z-index: 20;
}

/* Seamless Top Scrim Transition from Hero to Section 2 */
.curated-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 140px;
  background: linear-gradient(180deg, #070509 0%, transparent 100%);
  pointer-events: none;
  z-index: 1;
}

.curated-container {
  width: 100%;
  max-width: 640px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: relative;
  z-index: 10;
}

/* Left-Aligned Curated Carousels Title (From Reference Image) */
.curated-title-group {
  width: 100%;
  margin-bottom: clamp(20px, 3.2vh, 32px);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
}

.curated-title {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.curated-word-italic {
  font-family: 'Playfair Display', Georgia, serif;
  font-style: italic;
  font-weight: 400;
  font-size: clamp(48px, 6.8vw, 76px);
  line-height: 0.95;
  color: #ede4d8;
  letter-spacing: -0.015em;
  display: block;
}

.curated-word-main {
  font-family: 'Playfair Display', Georgia, serif;
  font-style: normal;
  font-weight: 400;
  font-size: clamp(48px, 6.8vw, 76px);
  line-height: 0.95;
  color: #ffffff;
  letter-spacing: -0.025em;
  display: block;
  margin-top: -0.04em;
}

/* The Black Viewport Box (From Reference Image) */
.funky-viewport {
  position: relative;
  width: 100%;
  aspect-ratio: 1.25 / 1;
  min-height: 380px;
  max-height: 520px;
  background: #000000;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 
    0 45px 95px -20px rgba(0, 0, 0, 0.95), 
    0 0 0 1px rgba(255, 255, 255, 0.1),
    0 0 35px rgba(10, 63, 138, 0.15);
  perspective: 1200px;
  transform-style: preserve-3d;
  display: flex;
  align-items: center;
  justify-content: center;
  user-select: none;
  cursor: grab;
}

.funky-viewport:active {
  cursor: grabbing;
}

.funky-cards-stage {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  transform-style: preserve-3d;
}

/* 3D Funky Cards */
.funky-card {
  position: absolute;
  width: clamp(240px, 58%, 340px);
  aspect-ratio: 16 / 10.5;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 
    0 24px 60px -10px rgba(0, 0, 0, 0.85), 
    0 0 0 1px rgba(255, 255, 255, 0.15);
  will-change: transform, filter, opacity;
  transition: transform 0.8s cubic-bezier(0.2, 0.85, 0.25, 1), 
              filter 0.8s cubic-bezier(0.2, 0.85, 0.25, 1), 
              opacity 0.8s cubic-bezier(0.2, 0.85, 0.25, 1);
  outline: none;
}

.card-glass-specular {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.18) 0%, rgba(255, 255, 255, 0.03) 40%, transparent 70%);
  pointer-events: none;
  z-index: 2;
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  padding: clamp(14px, 2.8vw, 22px);
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  z-index: 3;
}

.card-titles {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.card-title {
  font-family: var(--font-sans);
  font-size: clamp(15px, 1.8vw, 19px);
  font-weight: 600;
  color: #ffffff;
  letter-spacing: -0.02em;
  line-height: 1.1;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
}

.card-subtitle {
  font-family: 'Playfair Display', Georgia, serif;
  font-style: italic;
  font-size: clamp(12px, 1.2vw, 14.5px);
  color: rgba(255, 255, 255, 0.72);
  line-height: 1.2;
}

.card-footer {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
}

.card-badge {
  font-family: var(--font-sans);
  font-size: clamp(11.5px, 1.1vw, 13px);
  font-weight: 800;
  letter-spacing: 0.06em;
  color: rgba(255, 255, 255, 0.85);
}

.card-num {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(38px, 4.6vw, 52px);
  font-weight: 400;
  line-height: 0.85;
  color: #ffffff;
  letter-spacing: -0.04em;
  text-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
}

/* Card Themes & Authentic Gradients Matching Website Theme */
.card-01 {
  background: linear-gradient(165deg, #090e1a 0%, #1a1e34 38%, #783818 70%, #d97706 100%);
}
.card-02 {
  background: linear-gradient(165deg, #090e1a 0%, #20131b 38%, #883244 70%, #f43f5e 100%);
}
.card-03 {
  background: linear-gradient(165deg, #090918 0%, #1e102e 38%, #6d28d9 70%, #ec4899 100%);
}
.card-04 {
  background: linear-gradient(165deg, #050b16 0%, #0b1e38 38%, #1d4ed8 70%, #38bdf8 100%);
}
.card-05 {
  background: linear-gradient(165deg, #050e09 0%, #0f2214 38%, #15803d 70%, #eab308 100%);
}

/* 3D Card Slots */
.funky-card[data-slot="0"] {
  transform: translate3d(0, 0, 50px) rotate(-11deg);
  filter: blur(0px);
  opacity: 1;
  z-index: 10;
  pointer-events: auto;
  cursor: grab;
}
.funky-card[data-slot="0"]:hover {
  transform: translate3d(0, -3px, 55px) rotate(-10deg);
}

.funky-card[data-slot="-1"] {
  transform: translate3d(28px, -148px, -60px) rotate(14deg);
  filter: blur(12px);
  opacity: 0.58;
  z-index: 5;
  pointer-events: auto;
  cursor: pointer;
}
.funky-card[data-slot="-1"]:hover {
  filter: blur(8px);
  opacity: 0.75;
}

.funky-card[data-slot="1"] {
  transform: translate3d(-32px, 150px, -70px) rotate(-16deg);
  filter: blur(14px);
  opacity: 0.48;
  z-index: 4;
  pointer-events: auto;
  cursor: pointer;
}
.funky-card[data-slot="1"]:hover {
  filter: blur(9px);
  opacity: 0.68;
}

.funky-card[data-slot="deep"] {
  transform: translate3d(0, 240px, -200px) rotate(-22deg);
  filter: blur(24px);
  opacity: 0;
  z-index: 1;
  pointer-events: none;
}

/* Controls Row Below Viewport (From Reference Image) */
.funky-controls-row {
  width: 100%;
  margin-top: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 2px;
  box-sizing: border-box;
}

.funky-buttons-wrap {
  display: flex;
  align-items: center;
  gap: 10px;
  position: relative;
}

.funky-nav-btn {
  width: 44px;
  height: 44px;
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s ease;
  position: relative;
  outline: none;
}

.funky-nav-btn.prev {
  background: rgba(255, 255, 255, 0.14);
  border: 1px solid rgba(255, 255, 255, 0.18);
  color: #ffffff;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.funky-nav-btn.prev:hover {
  background: rgba(255, 255, 255, 0.24);
  transform: translateY(-1px);
}

.funky-nav-btn.next {
  background: #000000;
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #ffffff;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.5);
}

.funky-nav-btn.next:hover {
  background: #141414;
  border-color: rgba(255, 255, 255, 0.35);
  transform: translateY(-1px);
}

.funky-nav-btn:active {
  transform: scale(0.92) !important;
}

/* Hand Cursor Prompt from Reference Image */
.funky-hand-cursor {
  position: absolute;
  bottom: -18px;
  right: -12px;
  pointer-events: none;
  z-index: 20;
  animation: handClickPulse 2.4s ease-in-out infinite;
  transition: opacity 0.35s ease, transform 0.35s ease;
}

.funky-hand-cursor.is-dismissed {
  opacity: 0;
  transform: scale(0.85);
  pointer-events: none;
}

@keyframes handClickPulse {
  0%, 100% {
    transform: translate(0, 0);
  }
  50% {
    transform: translate(2px, -3px) scale(1.06);
  }
}

/* Right Active Label from Reference Image */
.funky-label-display {
  display: flex;
  align-items: center;
}

.funky-active-title {
  font-family: var(--font-sans);
  font-size: clamp(16px, 1.4vw, 19px);
  font-weight: 500;
  color: #ffffff;
  letter-spacing: -0.015em;
  transition: opacity 0.25s ease, transform 0.25s ease;
}

/* Mobile Responsiveness */
@media (max-width: 640px) {
  .curated-section {
    padding: 70px 16px 90px;
  }
  .funky-viewport {
    aspect-ratio: 1.1 / 1;
    min-height: 320px;
  }
  .funky-card {
    width: clamp(210px, 74%, 290px);
  }
  .funky-card[data-slot="-1"] {
    transform: translate3d(20px, -118px, -50px) rotate(14deg);
    filter: blur(10px);
  }
  .funky-card[data-slot="1"] {
    transform: translate3d(-20px, 122px, -60px) rotate(-16deg);
    filter: blur(12px);
  }
}'''

pos_c_start = content.find('/* ============================================================\n   SECTION 2: CURATED CAROUSELS')
pos_c_end = content.find('/* Scroll Prompt in Hero Tier Lower Left */')

if pos_c_start != -1 and pos_c_end != -1:
    content = content[:pos_c_start] + clean_css + '\n\n' + content[pos_c_end:]
    print("2. Clean Section 2 CSS inserted!")
else:
    print("WARNING: pos_c_start or pos_c_end not found!")

# 3. Clean Section 2 JS
clean_js = '''// ============================================================
// CURATED CAROUSELS (FUNKY TWIST 3D SHOWCASE CONTROLLER)
// ============================================================
(function(){
  var chapterTitles = [
    'Funky Twist',
    'Floating Studio',
    'Color Magic',
    'Cloud Vision',
    'Garden Twilight'
  ];

  var currentIndex = 0;
  var isInteracted = false;

  var cards = document.querySelectorAll('.funky-card');
  var prevBtn = document.getElementById('funkyPrevBtn');
  var nextBtn = document.getElementById('funkyNextBtn');
  var handCursor = document.getElementById('funkyHandCursor');
  var activeTitle = document.getElementById('funkyActiveTitle');
  var viewport = document.getElementById('funkyViewport');

  function updateSlots() {
    cards.forEach(function(card) {
      card.style.transform = '';
      var cardIdx = parseInt(card.getAttribute('data-index'), 10);
      var diff = (cardIdx - currentIndex + chapterTitles.length) % chapterTitles.length;
      if (diff === 0) {
        card.setAttribute('data-slot', '0');
        card.setAttribute('aria-hidden', 'false');
      } else if (diff === 1) {
        card.setAttribute('data-slot', '1');
        card.setAttribute('aria-hidden', 'true');
      } else if (diff === chapterTitles.length - 1) {
        card.setAttribute('data-slot', '-1');
        card.setAttribute('aria-hidden', 'true');
      } else {
        card.setAttribute('data-slot', 'deep');
        card.setAttribute('aria-hidden', 'true');
      }
    });

    // Update Title with smooth fade
    if (activeTitle) {
      activeTitle.style.opacity = '0';
      activeTitle.style.transform = 'translateY(4px)';
      setTimeout(function() {
        activeTitle.textContent = chapterTitles[currentIndex];
        activeTitle.style.opacity = '1';
        activeTitle.style.transform = 'translateY(0)';
      }, 180);
    }
  }

  function dismissHandPrompt() {
    if (!isInteracted && handCursor) {
      isInteracted = true;
      handCursor.classList.add('is-dismissed');
    }
  }

  function goToIndex(newIdx) {
    dismissHandPrompt();
    currentIndex = (newIdx + chapterTitles.length) % chapterTitles.length;
    updateSlots();
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', function(e) {
      e.preventDefault();
      goToIndex(currentIndex + 1);
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', function(e) {
      e.preventDefault();
      goToIndex(currentIndex - 1);
    });
  }

  // Click on cards to bring them into center
  cards.forEach(function(card) {
    card.addEventListener('click', function() {
      var slot = card.getAttribute('data-slot');
      if (slot === '1') {
        goToIndex(currentIndex + 1);
      } else if (slot === '-1') {
        goToIndex(currentIndex - 1);
      } else if (slot === '0') {
        // Clicking active card jumps to hero scene
        if (window.jumpToHeroTopic) {
          window.jumpToHeroTopic(currentIndex);
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
      }
    });
  });

  // Interactive 3D micro-tilt on mousemove
  if (viewport) {
    viewport.addEventListener('mousemove', function(e) {
      var rect = viewport.getBoundingClientRect();
      var x = (e.clientX - rect.left) / rect.width - 0.5;
      var y = (e.clientY - rect.top) / rect.height - 0.5;
      var activeCard = document.querySelector('.funky-card[data-slot="0"]');
      if (activeCard) {
        var rx = -y * 7;
        var ry = x * 7;
        activeCard.style.transform = 'translate3d(' + (x * 12) + 'px, ' + (y * 8) + 'px, 50px) rotate(' + (-11 + rx) + 'deg) rotateY(' + ry + 'deg)';
      }
    });

    viewport.addEventListener('mouseleave', function() {
      var activeCard = document.querySelector('.funky-card[data-slot="0"]');
      if (activeCard) {
        activeCard.style.transform = '';
      }
    });
  }

  // Touch Swipe support
  var touchStartX = 0;
  var touchStartY = 0;
  if (viewport) {
    viewport.addEventListener('touchstart', function(e) {
      if (e.changedTouches && e.changedTouches[0]) {
        touchStartX = e.changedTouches[0].screenX;
        touchStartY = e.changedTouches[0].screenY;
      }
    }, { passive: true });

    viewport.addEventListener('touchend', function(e) {
      if (e.changedTouches && e.changedTouches[0]) {
        var dx = e.changedTouches[0].screenX - touchStartX;
        var dy = e.changedTouches[0].screenY - touchStartY;
        if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 35) {
          if (dx < 0) goToIndex(currentIndex + 1);
          else goToIndex(currentIndex - 1);
        }
      }
    }, { passive: true });
  }

  // Keyboard navigation
  window.addEventListener('keydown', function(e) {
    var curSection = document.getElementById('curatedSection');
    if (!curSection) return;
    var rect = curSection.getBoundingClientRect();
    var isVisible = (rect.top < window.innerHeight && rect.bottom > 0);
    if (!isVisible) return;

    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
      goToIndex(currentIndex + 1);
    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
      goToIndex(currentIndex - 1);
    }
  });

  // Initial slot assignment
  updateSlots();
})();'''

pos_j_start = content.find('// ============================================================\n// CURATED CAROUSELS (FUNKY TWIST 3D SHOWCASE CONTROLLER)')
pos_j_end = content.find('// ============================================================\n// NAVIGATION & PERFORMANCE CONTROLLER (HERO + CURATED)')

if pos_j_start != -1 and pos_j_end != -1:
    content = content[:pos_j_start] + clean_js + '\n\n' + content[pos_j_end:]
    print("3. Clean Section 2 JS inserted!")
else:
    print("WARNING: pos_j_start or pos_j_end not found!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html fully updated with clean carousel!")
