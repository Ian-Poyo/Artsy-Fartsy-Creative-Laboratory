import sys

# Generate the complete HTML markup for Section 2
html_section = '''
<!-- ============================================================
     SECTION 2: CURATED CAROUSELS (FUNKY TWIST 3D SHOWCASE)
     Inspired by 108™ Motion Templates Curated Carousels
     ============================================================ -->
<section id="curatedSection" class="curated-section" aria-label="Curated Carousels Showcase">
  <div class="funky-ambient-glow glow-top" aria-hidden="true"></div>
  <div class="funky-ambient-glow glow-bottom" aria-hidden="true"></div>

  <div class="funky-container">
    <!-- Left-Aligned Editorial Title from Reference Image -->
    <div class="curated-title-group">
      <h2 class="curated-title">
        <span class="curated-word-italic">Curated</span>
        <span class="curated-word-main">Carousels</span>
      </h2>
    </div>

    <!-- The Black Viewport Box with 3D Funky Twist Cards -->
    <div class="funky-viewport" id="funkyViewport" role="region" aria-roledescription="carousel" aria-label="Creative Studio Chapters">
      <div class="funky-cards-stage" id="funkyCardsStage">
        
        <!-- Card 01: Funky Twist -->
        <article class="funky-card card-01" data-index="0" data-slot="0" tabindex="0" role="group" aria-roledescription="slide" aria-label="1 of 5: Funky Twist">
          <div class="card-inner">
            <div class="card-header">
              <span class="card-title">Funky Twist</span>
              <span class="card-subtitle">Desktop</span>
            </div>
            <div class="card-art-accent" aria-hidden="true"></div>
            <div class="card-footer">
              <span class="card-badge">108™</span>
              <span class="card-num">01</span>
            </div>
          </div>
        </article>

        <!-- Card 02: Floating Studio -->
        <article class="funky-card card-02" data-index="1" data-slot="1" tabindex="0" role="group" aria-roledescription="slide" aria-label="2 of 5: Floating Studio">
          <div class="card-inner">
            <div class="card-header">
              <span class="card-title">Floating Studio</span>
              <span class="card-subtitle">Workshops</span>
            </div>
            <div class="card-art-accent" aria-hidden="true"></div>
            <div class="card-footer">
              <span class="card-badge">108™</span>
              <span class="card-num">02</span>
            </div>
          </div>
        </article>

        <!-- Card 03: Color Magic -->
        <article class="funky-card card-03" data-index="2" data-slot="deep" tabindex="0" role="group" aria-roledescription="slide" aria-label="3 of 5: Color Magic">
          <div class="card-inner">
            <div class="card-header">
              <span class="card-title">Color Magic</span>
              <span class="card-subtitle">Celebrations</span>
            </div>
            <div class="card-art-accent" aria-hidden="true"></div>
            <div class="card-footer">
              <span class="card-badge">108™</span>
              <span class="card-num">03</span>
            </div>
          </div>
        </article>

        <!-- Card 04: Cloud Vision -->
        <article class="funky-card card-04" data-index="3" data-slot="deep" tabindex="0" role="group" aria-roledescription="slide" aria-label="4 of 5: Cloud Vision">
          <div class="card-inner">
            <div class="card-header">
              <span class="card-title">Cloud Vision</span>
              <span class="card-subtitle">Retreats</span>
            </div>
            <div class="card-art-accent" aria-hidden="true"></div>
            <div class="card-footer">
              <span class="card-badge">108™</span>
              <span class="card-num">04</span>
            </div>
          </div>
        </article>

        <!-- Card 05: Garden Twilight -->
        <article class="funky-card card-05" data-index="4" data-slot="-1" tabindex="0" role="group" aria-roledescription="slide" aria-label="5 of 5: Garden Twilight">
          <div class="card-inner">
            <div class="card-header">
              <span class="card-title">Garden Twilight</span>
              <span class="card-subtitle">Evenings</span>
            </div>
            <div class="card-art-accent" aria-hidden="true"></div>
            <div class="card-footer">
              <span class="card-badge">108™</span>
              <span class="card-num">05</span>
            </div>
          </div>
        </article>

      </div>
    </div>

    <!-- Controls Row (Directly below viewport, matching reference) -->
    <div class="funky-controls-row">
      <div class="funky-buttons-wrap">
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

      <!-- Right Active Title from Reference Image -->
      <div class="funky-label-display">
        <span class="funky-active-title" id="funkyActiveTitle">Funky Twist</span>
      </div>
    </div>

    <!-- Interactive Experience Details Drawer -->
    <div class="funky-details-card" id="funkyDetailsCard">
      <div class="funky-details-meta">
        <span class="funky-badge-pill" id="funkyCategoryTag">A LAB FOR THE UNCONVENTIONAL</span>
        <span class="funky-index-pill" id="funkyMetaIndex">01 / 05</span>
      </div>
      <h3 class="funky-headline" id="funkyHeadline">For ideas that refuse to stay inside the lines.</h3>
      <p class="funky-desc" id="funkyDesc">
        An experimental sanctuary where strange ideas take shape, materials are pushed to their breaking points, and creativity has no single direction.
      </p>
      <div class="funky-actions">
        <button class="funky-action-btn primary" id="funkyHeroJumpBtn" aria-label="Experience this chapter in the hero stage">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
          <span>Experience in Hero Stage</span>
        </button>
        <button class="funky-action-btn secondary" id="funkyModalBtn" data-modal="homeModal" aria-label="Open Studio details modal">
          <span>Studio Overview &rarr;</span>
        </button>
      </div>
    </div>

  </div>
</section>
'''

print("Generated Section 2 HTML len:", len(html_section))
