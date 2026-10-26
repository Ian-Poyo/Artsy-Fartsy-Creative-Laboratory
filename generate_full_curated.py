import re

# 1. New HTML for Section 2
curated_html = '''
<!-- ============================================================
     SECTION 2: CURATED CAROUSELS (FUNKY TWIST 3D SHOWCASE)
     Re-imagined for Artsy Fartsy Luxury Creative Laboratory Theme
     ============================================================ -->
<section id="curatedSection" class="curated-section" aria-label="Curated Carousels Showcase">
  <!-- Ambient Cosmic Aura Glows (Seamless continuation of Stargazer theme) -->
  <div class="curated-ambient-mesh" aria-hidden="true">
    <div class="mesh-orb orb-sapphire"></div>
    <div class="mesh-orb orb-amber"></div>
    <div class="mesh-orb orb-violet"></div>
  </div>

  <div class="curated-content-wrapper">
    
    <!-- Section Header (Editorial & Sophisticated) -->
    <header class="curated-header-group">
      <div class="curated-badge-eyebrow">
        <span class="eyebrow-sparkle">✦</span>
        <span>ATMOSPHERIC CHAPTERS</span>
        <span class="eyebrow-sep">•</span>
        <span>ARTSY FARTSY CREATIVE LAB</span>
      </div>
      <h2 class="curated-hero-title">
        <span class="curated-title-script">Curated</span>
        <span class="curated-title-lead">Carousels</span>
      </h2>
      <p class="curated-hero-sub">
        Five interactive sensory chapters crafted for tactile discovery, vivid pigments, and open-ended curiosity.
      </p>

      <!-- Chapter Navigation Tabs (Instant UX Switcher) -->
      <div class="chapter-tabs-bar" role="tablist" aria-label="Curated Chapter Tabs">
        <button class="chapter-tab is-active" data-index="0" role="tab" aria-selected="true">
          <span class="tab-index">01</span>
          <span class="tab-name">The Lab</span>
        </button>
        <button class="chapter-tab" data-index="1" role="tab" aria-selected="false">
          <span class="tab-index">02</span>
          <span class="tab-name">Workshops</span>
        </button>
        <button class="chapter-tab" data-index="2" role="tab" aria-selected="false">
          <span class="tab-index">03</span>
          <span class="tab-name">Celebrations</span>
        </button>
        <button class="chapter-tab" data-index="3" role="tab" aria-selected="false">
          <span class="tab-index">04</span>
          <span class="tab-name">Retreats</span>
        </button>
        <button class="chapter-tab" data-index="4" role="tab" aria-selected="false">
          <span class="tab-index">05</span>
          <span class="tab-name">Twilight</span>
        </button>
      </div>
    </header>

    <!-- The Luxury Frosted Showcase Frame (Elevated from plain black box) -->
    <div class="curated-showcase-frame">
      <!-- Frame macOS / Studio Top Bar -->
      <div class="viewport-header-bar" aria-hidden="true">
        <div class="viewport-window-dots">
          <span class="window-dot red"></span>
          <span class="window-dot yellow"></span>
          <span class="window-dot green"></span>
        </div>
        <div class="viewport-suite-badge">
          <span class="suite-icon">✦</span>
          <span>AF™ MOTION SUITE • 3D CAROUSEL</span>
        </div>
        <div class="viewport-mode-indicator">
          <span class="mode-pulse"></span>
          <span>INTERACTIVE</span>
        </div>
      </div>

      <!-- 3D Perspective Funky Twist Viewport -->
      <div class="funky-viewport" id="funkyViewport" role="region" aria-roledescription="carousel" aria-label="Chapter Cards Carousel">
        <div class="funky-cards-stage" id="funkyCardsStage">
          
          <!-- Card 01: Funky Twist (Creative Lab) -->
          <article class="funky-card card-01" data-index="0" data-slot="0" tabindex="0" role="group" aria-roledescription="slide" aria-label="1 of 5: Funky Twist">
            <div class="card-glass-specular" aria-hidden="true"></div>
            <div class="card-inner">
              <div class="card-top-row">
                <div class="card-titles">
                  <span class="card-title">Funky Twist</span>
                  <span class="card-subtitle">Desktop • Creative Lab</span>
                </div>
                <span class="card-status-pill">CHAPTER 01</span>
              </div>
              <div class="card-motif-art" aria-hidden="true">
                <svg viewBox="0 0 100 100" width="70" height="70" fill="none">
                  <circle cx="50" cy="50" r="40" stroke="#ffffff" stroke-width="1.2" stroke-dasharray="3 3"/>
                  <circle cx="50" cy="50" r="26" stroke="#ffffff" stroke-width="1.4"/>
                  <circle cx="50" cy="50" r="12" stroke="#ffffff" stroke-width="1"/>
                  <circle cx="50" cy="50" r="2.5" fill="#ffffff"/>
                </svg>
              </div>
              <div class="card-footer-row">
                <div class="card-brand-box">
                  <span class="brand-sub">AF™</span>
                  <span class="brand-code">108</span>
                </div>
                <span class="card-num-display">01</span>
              </div>
            </div>
          </article>

          <!-- Card 02: Floating Studio (Workshops & Atelier) -->
          <article class="funky-card card-02" data-index="1" data-slot="1" tabindex="0" role="group" aria-roledescription="slide" aria-label="2 of 5: Floating Studio">
            <div class="card-glass-specular" aria-hidden="true"></div>
            <div class="card-inner">
              <div class="card-top-row">
                <div class="card-titles">
                  <span class="card-title">Floating Studio</span>
                  <span class="card-subtitle">Workshops & Atelier</span>
                </div>
                <span class="card-status-pill">CHAPTER 02</span>
              </div>
              <div class="card-motif-art" aria-hidden="true">
                <svg viewBox="0 0 100 100" width="70" height="70" fill="none">
                  <polygon points="50,15 82,75 18,75" stroke="#ffffff" stroke-width="1.2" stroke-dasharray="3 3"/>
                  <circle cx="50" cy="55" r="18" stroke="#ffffff" stroke-width="1.4"/>
                  <line x1="50" y1="25" x2="50" y2="75" stroke="#ffffff" stroke-width="1"/>
                </svg>
              </div>
              <div class="card-footer-row">
                <div class="card-brand-box">
                  <span class="brand-sub">AF™</span>
                  <span class="brand-code">108</span>
                </div>
                <span class="card-num-display">02</span>
              </div>
            </div>
          </article>

          <!-- Card 03: Color Magic (Celebrations & Birthdays) -->
          <article class="funky-card card-03" data-index="2" data-slot="deep" tabindex="0" role="group" aria-roledescription="slide" aria-label="3 of 5: Color Magic">
            <div class="card-glass-specular" aria-hidden="true"></div>
            <div class="card-inner">
              <div class="card-top-row">
                <div class="card-titles">
                  <span class="card-title">Color Magic</span>
                  <span class="card-subtitle">Celebrations & Joy</span>
                </div>
                <span class="card-status-pill">CHAPTER 03</span>
              </div>
              <div class="card-motif-art" aria-hidden="true">
                <svg viewBox="0 0 100 100" width="70" height="70" fill="none">
                  <path d="M50 15 Q75 35 65 65 Q50 85 35 65 Q25 35 50 15Z" stroke="#ffffff" stroke-width="1.4"/>
                  <circle cx="50" cy="50" r="15" stroke="#ffffff" stroke-width="1.2" stroke-dasharray="2 2"/>
                  <circle cx="50" cy="50" r="3" fill="#ffffff"/>
                </svg>
              </div>
              <div class="card-footer-row">
                <div class="card-brand-box">
                  <span class="brand-sub">AF™</span>
                  <span class="brand-code">108</span>
                </div>
                <span class="card-num-display">03</span>
              </div>
            </div>
          </article>

          <!-- Card 04: Cloud Vision (Collaborative Retreats) -->
          <article class="funky-card card-04" data-index="3" data-slot="deep" tabindex="0" role="group" aria-roledescription="slide" aria-label="4 of 5: Cloud Vision">
            <div class="card-glass-specular" aria-hidden="true"></div>
            <div class="card-inner">
              <div class="card-top-row">
                <div class="card-titles">
                  <span class="card-title">Cloud Vision</span>
                  <span class="card-subtitle">Retreats & Innovation</span>
                </div>
                <span class="card-status-pill">CHAPTER 04</span>
              </div>
              <div class="card-motif-art" aria-hidden="true">
                <svg viewBox="0 0 100 100" width="70" height="70" fill="none">
                  <path d="M25 60 A15 15 0 0 1 50 45 A20 20 0 0 1 80 55 A12 12 0 0 1 75 72 L25 72 Z" stroke="#ffffff" stroke-width="1.4"/>
                  <circle cx="50" cy="30" r="8" stroke="#ffffff" stroke-width="1" stroke-dasharray="2 2"/>
                </svg>
              </div>
              <div class="card-footer-row">
                <div class="card-brand-box">
                  <span class="brand-sub">AF™</span>
                  <span class="brand-code">108</span>
                </div>
                <span class="card-num-display">04</span>
              </div>
            </div>
          </article>

          <!-- Card 05: Garden Twilight (Private Gatherings) -->
          <article class="funky-card card-05" data-index="4" data-slot="-1" tabindex="0" role="group" aria-roledescription="slide" aria-label="5 of 5: Garden Twilight">
            <div class="card-glass-specular" aria-hidden="true"></div>
            <div class="card-inner">
              <div class="card-top-row">
                <div class="card-titles">
                  <span class="card-title">Garden Twilight</span>
                  <span class="card-subtitle">Private Gatherings</span>
                </div>
                <span class="card-status-pill">CHAPTER 05</span>
              </div>
              <div class="card-motif-art" aria-hidden="true">
                <svg viewBox="0 0 100 100" width="70" height="70" fill="none">
                  <path d="M50 20 C65 35 75 55 50 80 C25 55 35 35 50 20 Z" stroke="#ffffff" stroke-width="1.4"/>
                  <line x1="50" y1="20" x2="50" y2="80" stroke="#ffffff" stroke-width="1.2"/>
                  <path d="M40 45 Q50 50 60 45" stroke="#ffffff" stroke-width="1"/>
                </svg>
              </div>
              <div class="card-footer-row">
                <div class="card-brand-box">
                  <span class="brand-sub">AF™</span>
                  <span class="brand-code">108</span>
                </div>
                <span class="card-num-display">05</span>
              </div>
            </div>
          </article>

        </div>
      </div>
    </div>

    <!-- Controls Row (Directly below viewport, matching reference composition) -->
    <div class="funky-controls-row">
      <div class="funky-nav-controls">
        <button class="funky-nav-btn prev" id="funkyPrevBtn" aria-label="Previous chapter">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="19" y1="12" x2="5" y2="12"></line>
            <polyline points="12 19 5 12 12 5"></polyline>
          </svg>
        </button>
        <button class="funky-nav-btn next active" id="funkyNextBtn" aria-label="Next chapter">
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

      <!-- Center Progress Dots & Counter -->
      <div class="funky-progress-wrap" aria-hidden="true">
        <div class="progress-dots">
          <span class="p-dot is-active" data-index="0"></span>
          <span class="p-dot" data-index="1"></span>
          <span class="p-dot" data-index="2"></span>
          <span class="p-dot" data-index="3"></span>
          <span class="p-dot" data-index="4"></span>
        </div>
        <span class="progress-counter" id="funkyProgressCounter">01 / 05</span>
      </div>

      <!-- Right Active Chapter Label (from Reference Image) -->
      <div class="funky-label-display">
        <span class="funky-active-title" id="funkyActiveTitle">Funky Twist</span>
        <span class="funky-active-sub" id="funkyActiveSub">Creative Laboratory</span>
      </div>
    </div>

    <!-- Interactive Chapter Story & Studio Action Drawer -->
    <div class="curated-story-drawer" id="curatedStoryDrawer">
      <div class="story-left-col">
        <div class="story-meta-row">
          <span class="story-badge-pill" id="storyCategoryTag">A LAB FOR THE UNCONVENTIONAL</span>
          <span class="story-index-tag" id="storyIndexTag">CHAPTER 01 OF 05</span>
        </div>
        <h3 class="story-headline" id="storyHeadline">For ideas that refuse to stay inside the lines.</h3>
        <p class="story-desc" id="storyDesc">
          An experimental sanctuary where strange ideas take shape, materials are pushed to their breaking points, and creativity has no single direction.
        </p>
        <div class="story-tags-list" id="storyTagsList">
          <span class="story-tag">✦ Process-Based Discovery</span>
          <span class="story-tag">✦ Raw Pigments & Clay</span>
          <span class="story-tag">✦ Carmel Studio</span>
          <span class="story-tag">✦ All Skill Levels</span>
        </div>
      </div>

      <div class="story-right-col">
        <div class="story-action-card">
          <span class="action-card-label">STAGE INTEGRATION</span>
          <button class="story-action-btn primary" id="storyHeroJumpBtn" aria-label="Experience this chapter in the hero background stage">
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="7" y1="17" x2="17" y2="7"></line>
              <polyline points="7 7 17 7 17 17"></polyline>
            </svg>
            <span>Experience in Hero Stage</span>
          </button>
          <button class="story-action-btn secondary" id="storyModalBtn" data-modal="homeModal" aria-label="Open Studio details modal">
            <span>Explore Studio Offerings &rarr;</span>
          </button>
          <p class="action-hint-note">Use arrow keys, swipe, or click cards to browse chapters.</p>
        </div>
      </div>
    </div>

  </div>
</section>
'''

print("Refined Curated HTML ready, length:", len(curated_html))
