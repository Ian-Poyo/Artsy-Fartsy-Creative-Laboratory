import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Section 2 CSS:
# - Smooth 200px mask-image feather for zero-seam transition
# - Left-side contrast scrim + top atmospheric blend
# - Professional entrance animation CSS (staggered fade-in & glide)
# - Slide morphing text animation
# - Card cascade transitions

sec2_css_marker = "/* ============================================================\n   SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE"
sec2_css_pos = content.find(sec2_css_marker)
end_of_sec_css = content.find(".foundation-container {", sec2_css_pos)

if sec2_css_pos != -1 and end_of_sec_css != -1:
    new_sec2_css = """/* ============================================================
   SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE
   Pure White Minimalist Theme with Moving Gradient Rainbow Heart
   Seamless Cinematic Blend & Professional Staggered Entrance Animations
   ============================================================ */
.foundation-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  margin-top: -1px; /* Seamless subpixel bridge with Hero */
  padding: clamp(90px, 12vh, 130px) clamp(24px, 5vw, 64px) clamp(80px, 11vh, 120px);
  box-sizing: border-box;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #ffffff;
  z-index: 20;
  background: #050811;
}

/* Dynamic Slide Background Stage (Continuous 200px Atmospheric Fade) */
.foundation-stage-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center 38%;
  opacity: 1;
  transition: opacity 0.75s cubic-bezier(0.4, 0, 0.2, 1), transform 1.4s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 0;
  will-change: opacity, transform;
  transform: scale(1.02);
  filter: brightness(1.0) contrast(1.02);
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.04) 40px, rgba(0, 0, 0, 0.22) 80px, rgba(0, 0, 0, 0.55) 125px, rgba(0, 0, 0, 0.88) 165px, #000 200px);
  mask-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.04) 40px, rgba(0, 0, 0, 0.22) 80px, rgba(0, 0, 0, 0.55) 125px, rgba(0, 0, 0, 0.88) 165px, #000 200px);
}

/* Luminous Ambient Contrast Scrim with Seamless Left Legibility & Top Vignette */
.foundation-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(circle at 80% 30%, rgba(255, 255, 255, 0.08) 0%, transparent 50%),
    linear-gradient(90deg, rgba(5, 8, 17, 0.92) 0%, rgba(5, 8, 17, 0.78) 36%, rgba(5, 8, 17, 0.14) 68%, rgba(5, 8, 17, 0.22) 100%),
    linear-gradient(180deg, #050811 0%, rgba(5, 8, 17, 0.70) 50px, rgba(5, 8, 17, 0.25) 120px, transparent 180px);
  pointer-events: none;
  z-index: 1;
}

"""
    content = content[:sec2_css_pos] + new_sec2_css + content[end_of_sec_css:]
    print("1. Updated Section 2 base CSS with smooth 200px mask feathering")
else:
    print("1. ERROR: sec2_css_pos or end_of_sec_css not found")

# 2. Add professional scroll entrance animations and slide morphing styles
anim_css_marker = "/* Main Content Row */"
pos_main_row = content.find(anim_css_marker)

if pos_main_row != -1:
    entrance_css = """/* Professional Content Entrance Animations (Awwwards Style) */
.foundation-info-col {
  opacity: 0;
  transform: translateY(32px);
  transition: opacity 1.0s cubic-bezier(0.16, 1, 0.3, 1), transform 1.0s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform;
}

.foundation-cards-viewport {
  opacity: 0;
  transform: translateX(45px);
  transition: opacity 1.1s cubic-bezier(0.16, 1, 0.3, 1) 0.15s, transform 1.1s cubic-bezier(0.16, 1, 0.3, 1) 0.15s;
  will-change: opacity, transform;
}

.foundation-controls-bar {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.28s, transform 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.28s;
  will-change: opacity, transform;
}

/* Activated when section scrolls into view */
.foundation-section.is-in-view .foundation-info-col {
  opacity: 1;
  transform: translateY(0);
}

.foundation-section.is-in-view .foundation-cards-viewport {
  opacity: 1;
  transform: translateX(0);
}

.foundation-section.is-in-view .foundation-controls-bar {
  opacity: 1;
  transform: translateY(0);
}

/* Individual card subtle entrance cascade */
.foundation-section .foundation-card {
  opacity: 0;
  transform: translateY(24px);
  transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.8s ease, border-color 0.35s ease, box-shadow 0.35s ease, background 0.35s ease;
}

.foundation-section.is-in-view .foundation-card:nth-child(1) { transition-delay: 0.20s; opacity: 1; transform: translateY(0); }
.foundation-section.is-in-view .foundation-card:nth-child(2) { transition-delay: 0.28s; opacity: 1; transform: translateY(0); }
.foundation-section.is-in-view .foundation-card:nth-child(3) { transition-delay: 0.36s; opacity: 1; transform: translateY(0); }
.foundation-section.is-in-view .foundation-card:nth-child(4) { transition-delay: 0.44s; opacity: 1; transform: translateY(0); }
.foundation-section.is-in-view .foundation-card:nth-child(5) { transition-delay: 0.52s; opacity: 1; transform: translateY(0); }

/* Slide Text Morphing Animation (When Switching Slides) */
.foundation-eyebrow,
.foundation-title,
.foundation-desc,
.foundation-actions-row {
  transition: opacity 0.35s cubic-bezier(0.4, 0, 0.2, 1), transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform;
}

/* Counter Numeral Flip Animation */
.foundation-counter-num {
  display: inline-block;
  transition: opacity 0.28s ease, transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform;
}

"""
    content = content[:pos_main_row] + entrance_css + content[pos_main_row:]
    print("2. Added professional entrance animations & slide morphing CSS")
else:
    print("2. ERROR: anim_css_marker not found")

# 3. Update the 5 Cards in HTML with all 5 new images
html_start_marker = '<div class="foundation-cards-viewport" id="foundationCardsViewport">'
html_end_marker = '<!-- Bottom Row: Navigation Controls, Progress Bar & Big Numeral Counter -->'

pos1 = content.find(html_start_marker)
pos2 = content.find(html_end_marker, pos1)

if pos1 != -1 and pos2 != -1:
    new_cards_html = """<div class="foundation-cards-viewport" id="foundationCardsViewport">
        <div class="foundation-cards-track" id="foundationCardsTrack">
          
          <!-- Card 0: Foundation Mission (Kids with Guitar in Sunlight) -->
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

          <!-- Card 1: Studio Classes (Classroom Collaborative Discovery) -->
          <article class="foundation-card has-img" data-index="1" tabindex="0" role="button" aria-label="Studio Classes">
            <img class="card-bg-img" src="/images/foundation-slide-2.jpg" alt="Studio Classes - Classroom Collaborative Discovery" loading="lazy">
            <div class="card-gradient-scrim"></div>
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

          <!-- Card 2: Birthday Events (Magical Celebration Ballroom) -->
          <article class="foundation-card has-img" data-index="2" tabindex="0" role="button" aria-label="Birthday Events">
            <img class="card-bg-img" src="/images/foundation-slide-3.jpg" alt="Birthday Events - Magical Celebration Ballroom" loading="lazy">
            <div class="card-gradient-scrim"></div>
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

          <!-- Card 3: Private Events (Sunlit Luncheon Soiree) -->
          <article class="foundation-card has-img" data-index="3" tabindex="0" role="button" aria-label="Private Events">
            <img class="card-bg-img" src="/images/foundation-slide-4.jpg" alt="Private Events - Sunlit Luncheon Soiree" loading="lazy">
            <div class="card-gradient-scrim"></div>
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

          <!-- Card 4: Corporate Events (Gilded Banquet Hall Retreat) -->
          <article class="foundation-card has-img" data-index="4" tabindex="0" role="button" aria-label="Corporate Events">
            <img class="card-bg-img" src="/images/foundation-slide-5.jpg" alt="Corporate Events - Gilded Banquet Hall Retreat" loading="lazy">
            <div class="card-gradient-scrim"></div>
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
    print("3. Updated all 5 Cards with real images and rich metadata")
else:
    print("3. ERROR: Cards viewport HTML markers not found")

# 4. Update the JavaScript slides array with all 5 bgImage paths
slides_start = "var slides = ["
pos_slides = content.find(slides_start)
pos_slides_end = content.find("var currentIndex = 0;", pos_slides)

if pos_slides != -1 and pos_slides_end != -1:
    new_slides_js = """var slides = [
    {
      id: 'mission',
      eyebrow: '— Mission Statement',
      title: 'Friends of Artsy Fartsy Foundation',
      descHtml: '<p>Our mission is to ensure accessible, inspiring space for the Artsy Fartsy Creative Laboratory; expand equitable access to the arts through scholarships for high school students and adult learners; and strengthen arts education by delivering high-quality color science professional development for elementary, middle, and high school teachers.</p><p>We believe creativity is a powerful catalyst for learning, expression, and community, and we work to nurture it across ages, disciplines, and classrooms.</p>',
      bgImage: '/images/foundation-slide-1.jpg',
      actionsHtml: '<button class=\"foundation-donate-btn\" data-modal=\"donateModal\" aria-label=\"Donate to the Foundation\">' + rainbowHeartSvg + '<span>DONATE</span></button>'
    },
    {
      id: 'classes',
      eyebrow: '— Weekly Offerings',
      title: 'Studio Classes & Workshops',
      descHtml: '<p>Join us at our Carmel studio for fun-filled weekly classes, adult workshops, special events, and more! Hands-on playful art exploration thoughtfully designed by educators to spark open-ended, process based discovery.</p>',
      bgImage: '/images/foundation-slide-2.jpg',
      actionsHtml: '<button class=\"foundation-book-btn\" data-modal=\"classesModal\" aria-label=\"Book a class\"><svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"3\" y=\"4\" width=\"18\" height=\"18\" rx=\"2\" ry=\"2\"></rect><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"6\"></line><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"6\"></line><line x1=\"3\" y1=\"10\" x2=\"21\" y2=\"10\"></line></svg><span>BOOK</span></button><button class=\"foundation-offerings-btn\" data-modal=\"classesModal\" aria-label=\"View Class Offerings\"><span>OFFERINGS &rarr;</span></button>'
    },
    {
      id: 'birthday',
      eyebrow: '— Milestone Celebrations',
      title: 'Birthday Parties & Celebrations',
      descHtml: '<p>Celebrate your milestone birthdays with pure color, wonder, and joy! Our signature birthday packages include dedicated artist hosts, vibrant color-splatter canvases, guided painting adventures, and custom party favors designed for all ages.</p>',
      bgImage: '/images/foundation-slide-3.jpg',
      actionsHtml: '<button class=\"foundation-book-btn\" data-modal=\"eventsModal\" aria-label=\"Book a birthday party\"><svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"3\" y=\"4\" width=\"18\" height=\"18\" rx=\"2\" ry=\"2\"></rect><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"6\"></line><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"6\"></line><line x1=\"3\" y1=\"10\" x2=\"21\" y2=\"10\"></line></svg><span>BOOK</span></button><button class=\"foundation-offerings-btn\" data-modal=\"eventsModal\" aria-label=\"View Birthday Packages\"><span>OFFERINGS &rarr;</span></button>'
    },
    {
      id: 'private-events',
      eyebrow: '— Bespoke Gatherings',
      title: 'Private Events & Soirées',
      descHtml: '<p>Host an extraordinary private soirée, intimate celebration, bridal gathering, or celebratory luncheon in our sunlit ateliers. Enjoy tailored creative experiences, curated table scapes, atmospheric lighting, and bespoke artistic keepsakes.</p>',
      bgImage: '/images/foundation-slide-4.jpg',
      actionsHtml: '<button class=\"foundation-book-btn\" data-modal=\"eventsModal\" aria-label=\"Book a private event\"><svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"3\" y=\"4\" width=\"18\" height=\"18\" rx=\"2\" ry=\"2\"></rect><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"6\"></line><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"6\"></line><line x1=\"3\" y1=\"10\" x2=\"21\" y2=\"10\"></line></svg><span>BOOK</span></button><button class=\"foundation-offerings-btn\" data-modal=\"eventsModal\" aria-label=\"View Private Event Offerings\"><span>OFFERINGS &rarr;</span></button>'
    },
    {
      id: 'corporate-events',
      eyebrow: '— Corporate Retreats',
      title: 'Corporate Events & Retreats',
      descHtml: '<p>Inspire innovation, camaraderie, and creative problem-solving with tailored corporate retreats and team-building events at Artsy Fartsy Studio. From collaborative group canvas projects and color theory workshops to elegant cocktail networking soirées, we curate elevated experiences that bring teams together.</p>',
      bgImage: '/images/foundation-slide-5.jpg',
      actionsHtml: '<button class=\"foundation-book-btn\" data-modal=\"eventsModal\" aria-label=\"Book a corporate event\"><svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"3\" y=\"4\" width=\"18\" height=\"18\" rx=\"2\" ry=\"2\"></rect><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"6\"></line><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"6\"></line><line x1=\"3\" y1=\"10\" x2=\"21\" y2=\"10\"></line></svg><span>BOOK</span></button><button class=\"foundation-offerings-btn\" data-modal=\"eventsModal\" aria-label=\"View Corporate Offerings\"><span>OFFERINGS &rarr;</span></button>'
    }
  ];

  """
    content = content[:pos_slides] + new_slides_js + content[pos_slides_end:]
    print("4. Updated slides array with all 5 bgImage mappings")
else:
    print("4. ERROR: slides array JS markers not found")

# 5. Update updateSlide() in JS with smooth crossfades and text morphing animations
old_update_fn_marker = "function updateSlide() {"
pos_fn = content.find(old_update_fn_marker)
pos_fn_end = content.find("function goToIndex(newIdx) {", pos_fn)

if pos_fn != -1 and pos_fn_end != -1:
    new_update_fn = """function updateSlide() {
    var s = slides[currentIndex];

    // 1. Dynamic Slide Background Crossfade with subtle zoom
    if (bgEl && s.bgImage) {
      bgEl.style.opacity = '0.35';
      bgEl.style.transform = 'scale(1.04)';
      setTimeout(function() {
        bgEl.style.backgroundImage = 'url(\"' + s.bgImage + '\")';
        bgEl.style.opacity = '1';
        bgEl.style.transform = 'scale(1.02)';
      }, 160);
    }

    // 2. Smooth Slide Text Morphing: glide down slightly, update, glide smoothly back up
    if (eyebrowEl && titleEl && descEl) {
      eyebrowEl.style.opacity = '0';
      eyebrowEl.style.transform = 'translateY(8px)';
      titleEl.style.opacity = '0';
      titleEl.style.transform = 'translateY(8px)';
      descEl.style.opacity = '0';
      descEl.style.transform = 'translateY(8px)';
      if (actionsEl) {
        actionsEl.style.opacity = '0';
        actionsEl.style.transform = 'translateY(8px)';
      }

      setTimeout(function() {
        eyebrowEl.textContent = s.eyebrow;
        titleEl.textContent = s.title;
        descEl.innerHTML = s.descHtml;
        if (actionsEl) {
          actionsEl.innerHTML = s.actionsHtml;
          actionsEl.style.opacity = '1';
          actionsEl.style.transform = 'translateY(0)';
        }
        eyebrowEl.style.opacity = '1';
        eyebrowEl.style.transform = 'translateY(0)';
        titleEl.style.opacity = '1';
        titleEl.style.transform = 'translateY(0)';
        descEl.style.opacity = '1';
        descEl.style.transform = 'translateY(0)';
      }, 160);
    }

    // 3. Update Cards Track Translation & Active Class
    cards.forEach(function(card, idx) {
      if (idx === currentIndex) {
        card.classList.add('is-active');
        card.setAttribute('aria-selected', 'true');
      } else {
        card.classList.remove('is-active');
        card.setAttribute('aria-selected', 'false');
      }
    });

    if (track && cards.length > 0) {
      var cardW = cards[0].offsetWidth || 250;
      var gap = 20;
      var offset = currentIndex * (cardW + gap);
      track.style.transform = 'translate3d(-' + offset + 'px, 0, 0)';
    }

    // 4. Update Progress Fill & Animated Counter Numeral
    if (progressFill) {
      var pct = ((currentIndex + 1) / slides.length) * 100;
      progressFill.style.width = pct + '%';
    }
    if (counterNum) {
      counterNum.style.opacity = '0';
      counterNum.style.transform = 'translateY(-8px)';
      setTimeout(function() {
        counterNum.textContent = '0' + (currentIndex + 1);
        counterNum.style.opacity = '1';
        counterNum.style.transform = 'translateY(0)';
      }, 140);
    }
  }

  """
    content = content[:pos_fn] + new_update_fn + content[pos_fn_end:]
    print("5. Updated updateSlide() with smooth crossfade and text morphing animations")
else:
    print("5. ERROR: updateSlide markers not found")

# 6. Add IntersectionObserver for Section 2 to trigger is-in-view scroll entrance animation
obs_marker = "  // Initialize and start 3-second loop\n  updateSlide();\n  startAutoLoop();\n})();"
pos_obs = content.find(obs_marker)

if pos_obs != -1:
    new_obs_code = """  // Preload all 5 slide backgrounds for instant butter-smooth transitions
  slides.forEach(function(s) {
    if (s.bgImage) {
      var pre = new Image();
      pre.src = s.bgImage;
    }
  });

  // IntersectionObserver for Section 2: Trigger smooth scroll entrance animations
  var sec2El = document.getElementById('curatedSection');
  if ('IntersectionObserver' in window && sec2El) {
    var sec2Observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          sec2El.classList.add('is-in-view');
        }
      });
    }, { threshold: 0.12 });
    sec2Observer.observe(sec2El);
  } else if (sec2El) {
    sec2El.classList.add('is-in-view');
  }

  // Initialize and start 3-second loop
  updateSlide();
  startAutoLoop();
})();"""
    content = content[:pos_obs] + new_obs_code + content[pos_obs + len(obs_marker):]
    print("6. Added image preloading and Section 2 scroll entrance IntersectionObserver")
else:
    print("6. ERROR: obs_marker not found")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html successfully")
