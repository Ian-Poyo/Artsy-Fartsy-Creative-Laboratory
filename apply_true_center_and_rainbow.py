import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Donate button SVG with Rainbow LinearGradient and Heart
old_donate_btn = re.search(r'<button class="nav-donate-btn"[^>]*>.*?</button>', content, re.DOTALL)
if not old_donate_btn:
    raise ValueError("nav-donate-btn not found")

new_donate_btn = '''<button class="nav-donate-btn" data-modal="donateModal" aria-label="Donate">
        <svg class="donate-heart-icon" width="13" height="13" viewBox="0 0 24 24" aria-hidden="true">
          <defs>
            <linearGradient id="rainbowHeart" x1="0%" y1="100%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#ff2a6d"/>
              <stop offset="20%" stop-color="#ff5e3a"/>
              <stop offset="40%" stop-color="#ffb300"/>
              <stop offset="60%" stop-color="#00e676"/>
              <stop offset="80%" stop-color="#00b0ff"/>
              <stop offset="100%" stop-color="#d500f9"/>
            </linearGradient>
          </defs>
          <path fill="url(#rainbowHeart)" d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
        </svg>
        <span>Donate</span>
      </button>'''

content = content.replace(old_donate_btn.group(0), new_donate_btn, 1)

# 2. Update CSS for nav-donate-btn and donate-heart-icon with rainbow highlighting
old_donate_css = re.search(r'\.nav-donate-btn\s*\{[^}]*\}\s*\.nav-donate-btn:hover\s*\{[^}]*\}', content, re.DOTALL)
if not old_donate_css:
    raise ValueError("nav-donate-btn CSS not found")

new_donate_css = '''.nav-donate-btn {
  background: rgba(255, 255, 255, 0.14);
  border: 1px solid rgba(255, 255, 255, 0.45);
  border-radius: 9999px;
  padding: 5px 15px;
  color: #ffffff;
  font-family: var(--font-sans);
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 
    0 2px 10px rgba(0, 0, 0, 0.25),
    inset 0 1px 0 rgba(255, 255, 255, 0.4);
  transition: all 0.25s ease;
  outline: none;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.donate-heart-icon {
  filter: drop-shadow(0 0 3px rgba(255, 42, 109, 0.55)) drop-shadow(0 0 6px rgba(0, 176, 255, 0.45));
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), filter 0.3s ease;
}

.nav-donate-btn:hover {
  background: rgba(255, 255, 255, 0.26);
  border-color: rgba(255, 255, 255, 0.85);
  box-shadow: 
    0 4px 18px rgba(0, 0, 0, 0.35),
    0 0 14px rgba(255, 42, 109, 0.35),
    0 0 22px rgba(0, 230, 118, 0.25),
    0 0 28px rgba(213, 0, 249, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.5);
  transform: translateY(-1px);
}

.nav-donate-btn:hover .donate-heart-icon {
  transform: scale(1.22);
  filter: 
    drop-shadow(0 0 5px rgba(255, 42, 109, 0.8))
    drop-shadow(0 0 10px rgba(0, 230, 118, 0.7))
    drop-shadow(0 0 16px rgba(213, 0, 249, 0.85));
}'''

content = content.replace(old_donate_css.group(0), new_donate_css, 1)

# 3. Update Editorial & Title CSS
css_marker = content.find('/* ============================================================')
css_start = content.find('DESIGNER-GRADE MINIMALIST EDITORIAL', css_marker)
if css_start == -1:
    css_start = content.find('PROFESSIONAL MINIMALIST EDITORIAL', css_marker)

css_section_start = content.rfind('/*', 0, css_start)
modals_idx = content.find('/* ============================================================', css_start)
if modals_idx == -1:
    modals_idx = content.find('</style>')

new_editorial_css = '''/* ============================================================
   TRUE CENTER CINEMATIC STARTUP, NO SHADOWS & 2-TIER ALIGNED LAYOUT
   ============================================================ */

/* Bottom Scrim: Velvety deep gradient for crisp contrast behind text */
.hero-bottom-scrim {
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
}

.hero-editorial-stage {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 0 clamp(24px, 5.5vw, 72px) clamp(38px, 6vh, 58px);
  z-index: 20;
  pointer-events: none;
}

/* --- Tier 1 (Above the Line): Left Title & Right Explore Button --- */
.tier-upper {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr clamp(320px, 34vw, 440px);
  align-items: flex-end;
  gap: clamp(24px, 4vw, 64px);
  margin-bottom: clamp(14px, 2vh, 18px);
  pointer-events: none;
}

.tier-upper-left {
  position: relative;
  display: flex;
  align-items: flex-end;
  pointer-events: auto;
  min-height: clamp(80px, 12vh, 120px);
}

.title-anchor {
  width: 100%;
  display: flex;
  align-items: flex-end;
}

/* --- The Title Block: Pure CSS Fixed Dead-Center in Startup Phase --- */
.hero-title-block {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  margin: 0;
  width: auto;
  max-width: 90vw;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 40;
  cursor: pointer;
  pointer-events: auto;
  will-change: transform;
}

.hero-title-block.is-centered {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  align-items: center;
  justify-content: center;
}

.hero-title-block.is-docked {
  position: relative;
  top: auto;
  left: auto;
  transform: none !important;
  width: 100%;
  max-width: 640px;
  text-align: left;
  align-items: flex-start;
  z-index: 25;
}

.hero-title-main {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: clamp(4px, 1.2vh, 10px);
  line-height: 1.04;
  user-select: none;
  align-items: center;
  text-align: center;
  transition: align-items 0.8s ease, text-align 0.8s ease;
}

.hero-title-block.is-docked .hero-title-main {
  align-items: flex-start;
  text-align: left;
}

/* Mask container for clean optical line reveals */
.title-line-mask {
  display: flex;
  justify-content: center;
  text-align: center;
  overflow: hidden;
  padding-bottom: 6px;
  width: 100%;
}

.hero-title-block.is-docked .title-line-mask {
  display: block;
  justify-content: flex-start;
  text-align: left;
}

/* ZERO SHADOWS, ZERO BLUR - PURE VECTOR CRISP TYPOGRAPHY */
.title-primary {
  display: block;
  font-family: var(--font-sans);
  font-size: clamp(3.6rem, 8vw, 6.2rem);
  font-weight: 600;
  letter-spacing: -0.035em;
  color: #ffffff;
  text-align: center;
  text-shadow: none !important;
  filter: none !important;
  transform: translateY(115%);
  opacity: 0;
  animation: titleQuickBuild 0.55s cubic-bezier(0.16, 1, 0.3, 1) 0.08s forwards;
  transition: font-size 1.25s cubic-bezier(0.16, 1, 0.3, 1), letter-spacing 1.25s ease;
}

.title-secondary {
  display: block;
  font-family: var(--font-sans);
  font-size: clamp(1.8rem, 3.6vw, 2.8rem);
  font-weight: 300;
  letter-spacing: -0.015em;
  color: rgba(255, 255, 255, 0.92);
  text-align: center;
  text-shadow: none !important;
  filter: none !important;
  transform: translateY(115%);
  opacity: 0;
  animation: titleQuickBuild 0.55s cubic-bezier(0.16, 1, 0.3, 1) 0.22s forwards;
  transition: font-size 1.25s cubic-bezier(0.16, 1, 0.3, 1), color 1.25s ease;
}

/* Docked Layout Scale */
.hero-title-block.is-docked .title-primary {
  font-size: clamp(2.4rem, 4.4vw, 3.6rem);
  letter-spacing: -0.03em;
  text-align: left;
}

.hero-title-block.is-docked .title-secondary {
  font-size: clamp(1.4rem, 2.5vw, 2.1rem);
  letter-spacing: -0.015em;
  text-align: left;
  color: rgba(255, 255, 255, 0.78);
}

/* Quick Crisp Upward Build-up (snappy & clean, NO BLUR, NO SHADOW) */
@keyframes titleQuickBuild {
  0% {
    transform: translateY(115%);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}

/* Tier Upper Right: Button aligned with subtitle, above the line */
.tier-upper-right {
  display: flex;
  align-items: flex-end;
  justify-content: flex-start;
  pointer-events: auto;
  opacity: 0;
  transform: translateY(14px);
  transition: opacity 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.3s, transform 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.3s;
  will-change: transform, opacity;
}

body.layout-active .tier-upper-right {
  opacity: 1;
  transform: translateY(0);
}

.hero-explore-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 8px 24px;
  border-radius: 9999px;
  border: 1px solid rgba(255, 255, 255, 0.42);
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  color: #ffffff;
  font-family: var(--font-sans);
  font-size: 13.5px;
  font-weight: 500;
  letter-spacing: 0.01em;
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35);
  transition: all 0.25s ease;
  outline: none;
  margin-bottom: 4px; /* Perfectly aligns with baseline of subtitle */
}

.hero-explore-btn:hover {
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.85);
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4), 0 0 20px rgba(255, 255, 255, 0.25);
}

.hero-explore-btn:active {
  transform: translateY(0);
}

/* --- THE HORIZONTAL DIVIDER LINE --- */
.hero-divider-line {
  width: 100%;
  height: 1px;
  background: linear-gradient(
    to right,
    rgba(255, 255, 255, 0.35) 0%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0.3) 100%
  );
  margin: 0 0 clamp(16px, 2.4vh, 22px) 0;
  transform-origin: left center;
  opacity: 0;
  transform: scaleX(0);
  transition: opacity 1.1s ease 0.25s, transform 1.25s cubic-bezier(0.16, 1, 0.3, 1) 0.25s;
  pointer-events: none;
}

body.layout-active .hero-divider-line {
  opacity: 1;
  transform: scaleX(1);
}

/* --- Tier 2 (Below the Line): Left Quote & Right Paragraphs --- */
.tier-lower {
  width: 100%;
  display: grid;
  grid-template-columns: 1fr clamp(320px, 34vw, 440px);
  align-items: flex-start;
  gap: clamp(20px, 4vw, 64px);
  pointer-events: none;
  opacity: 0;
  transform: translateY(14px);
  transition: opacity 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.36s, transform 0.9s cubic-bezier(0.16, 1, 0.3, 1) 0.36s;
  will-change: transform, opacity;
}

body.layout-active .tier-lower {
  opacity: 1;
  transform: translateY(0);
}

.tier-lower-left {
  display: flex;
  align-items: center;
  pointer-events: auto;
  padding-top: 4px;
}

.bottom-quote {
  font-family: var(--font-sans);
  font-size: 12.5px;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.68);
  letter-spacing: 0.015em;
  text-shadow: none;
}

/* Tier Lower Right: Paragraphs aligned with Start Exploring button */
.tier-lower-right {
  display: flex;
  flex-direction: column;
  gap: 12px;
  pointer-events: auto;
}

.editorial-p1 {
  margin: 0;
  font-family: var(--font-sans);
  font-size: clamp(12.5px, 1.05vw, 13.5px);
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.88);
  letter-spacing: 0.005em;
  text-shadow: none;
}

.editorial-p2 {
  margin: 0;
  font-family: var(--font-sans);
  font-size: clamp(12px, 0.98vw, 13px);
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.7);
  letter-spacing: 0.005em;
  text-shadow: none;
}

/* --- Dedicated Bottom Center Social Bar (PUSHED UP MORE) --- */
.hero-social-float {
  position: absolute;
  bottom: clamp(38px, 6vh, 58px); /* Elevated comfortably above bottom edge */
  left: 50%;
  transform: translateX(-50%) translateY(16px);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  z-index: 30;
  pointer-events: auto;
  opacity: 0;
  transition: opacity 1s cubic-bezier(0.16, 1, 0.3, 1) 0.45s, transform 1s cubic-bezier(0.16, 1, 0.3, 1) 0.45s;
  will-change: transform, opacity;
}

body.layout-active .hero-social-float {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}

/* Social Icon Circles */
.social-circle {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255, 255, 255, 0.22);
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.9);
  text-decoration: none;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.35);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.social-circle:hover {
  background: rgba(255, 255, 255, 0.22);
  border-color: rgba(255, 255, 255, 0.75);
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 6px 22px rgba(0, 0, 0, 0.45), 0 0 18px rgba(255, 255, 255, 0.25);
}

.social-circle::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  background: rgba(8, 14, 28, 0.94);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  color: #fff;
  font-size: 11px;
  font-family: var(--font-sans);
  font-weight: 500;
  letter-spacing: 0.04em;
  padding: 4px 8px;
  border-radius: 6px;
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.2s ease, transform 0.2s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
  z-index: 35;
}

.social-circle:hover::after {
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}

/* Responsive Overrides */
@media (max-width: 960px) {
  .tier-upper {
    grid-template-columns: 1fr;
    gap: 16px;
    margin-bottom: 14px;
  }
  .tier-upper-right {
    justify-content: flex-start;
  }
  .tier-lower {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  .hero-social-float {
    position: static;
    transform: none;
    justify-content: flex-start;
    margin-top: 14px;
  }
  body.layout-active .hero-social-float {
    transform: none;
  }
}

@media (max-width: 640px) {
  .hero-editorial-stage {
    padding: 0 20px 24px;
  }
  .editorial-p2 {
    display: none;
  }
  .hero-social-float {
    justify-content: center;
    margin-top: 16px;
  }
  .tier-lower-left {
    text-align: center;
    justify-content: center;
  }
}
'''

content = content[:css_section_start] + new_editorial_css + content[modals_idx:]

# 4. Update HTML in #hero-section:
# The title block is rendered in pure CSS fixed center during startup, with titleAnchor in .tier-upper-left
hero_s = content.find('<section id="hero-section"')
wrap_e = content.find('</div>\n  </div>', hero_s) + len('</div>\n  </div>')
hero_e = content.find('</section>', wrap_e)

new_hero_body = '''

  <!-- Cinematic Bottom Scrim Gradient (Dims lower background for crystal-clear text readability) -->
  <div class="hero-bottom-scrim" aria-hidden="true"></div>

  <!-- Pure CSS Fixed Dead-Center Cinematic Startup Title Block -->
  <div class="hero-title-block is-centered" id="heroTitleBlock" title="Click to replay title transition">
    <h1 class="hero-title-main" id="heroTitleMain">
      <span class="title-line-mask">
        <span class="title-primary" id="titlePrimary">Artsy Fartsy</span>
      </span>
      <span class="title-line-mask">
        <span class="title-secondary" id="titleSecondary">Creative Laboratory.</span>
      </span>
    </h1>
  </div>

  <!-- Editorial 2-Tier Layout with Divider Line (from image-1.png) -->
  <div class="hero-editorial-stage" id="heroEditorialStage">
    
    <!-- Tier 1 (Above the Line): Left Title Anchor & Right Explore Button -->
    <div class="tier-upper">
      <div class="tier-upper-left" id="tierUpperLeft">
        <div class="title-anchor" id="titleAnchor"></div>
      </div>

      <div class="tier-upper-right" id="tierUpperRight">
        <button class="hero-explore-btn" id="heroExploreBtn" data-modal="homeModal" aria-label="Start Exploring Artsy Fartsy">
          <span>Start Exploring</span>
        </button>
      </div>
    </div>

    <!-- The Horizontal Divider Line -->
    <div class="hero-divider-line" id="heroDividerLine"></div>

    <!-- Tier 2 (Below the Line): Left Quote & Right Paragraphs -->
    <div class="tier-lower" id="tierLower">
      <div class="tier-lower-left">
        <span class="bottom-quote">Clarity begins with a good question.</span>
      </div>

      <div class="tier-lower-right">
        <p class="editorial-p1">
          Discovery doesn't always begin with knowing — it starts with questions. Context that guides understanding forward.
        </p>
        <p class="editorial-p2">
          Artsy Fartsy is your companion for deeper insight. A calm space for asking better questions and drawing thoughtful insight. Less noise. More meaning.
        </p>
      </div>
    </div>

    <!-- Dedicated Bottom Center Social Bar (PUSHED UP MORE) -->
    <div class="hero-social-float" id="heroSocialFloat" aria-label="Social Links">
      <a href="https://instagram.com/artsyfartsystudio" target="_blank" rel="noopener noreferrer" class="social-circle" data-tooltip="Instagram" aria-label="Instagram">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
          <circle cx="12" cy="12" r="4"></circle>
          <circle cx="17.5" cy="6.5" r="1" fill="currentColor"></circle>
        </svg>
      </a>
      <a href="https://facebook.com/artsyfartsystudio" target="_blank" rel="noopener noreferrer" class="social-circle" data-tooltip="Facebook" aria-label="Facebook">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
          <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
        </svg>
      </a>
    </div>

  </div>
'''

content = content[:wrap_e] + new_hero_body + content[hero_e:]

# 5. Update the Orchestration Script: True Dead Center & Smooth Docking
script_marker = '// TITLE SCREEN CENTER-TO-LAYOUT SHIFT CHOREOGRAPHY'
script_start = content.find(script_marker)
script_end = content.find('</script>', script_start)

new_orchestration_script = '''// TITLE SCREEN CENTER-TO-LAYOUT SHIFT CHOREOGRAPHY (TRUE DEAD CENTER & CLEAN SHIFT)
// ============================================================
(function(){
  var titleBlock = document.getElementById('heroTitleBlock');
  var hasShifted = false;
  var shiftTimeout = null;

  if(!titleBlock) return;

  function shiftToLayout(){
    if(hasShifted) return;
    hasShifted = true;
    if(shiftTimeout) clearTimeout(shiftTimeout);

    var anchor = document.getElementById('titleAnchor');
    if(!anchor) return;

    // Get current bounding box of the centered title and destination anchor
    var currentRect = titleBlock.getBoundingClientRect();
    var targetRect = anchor.getBoundingClientRect();

    // Mathematical translation delta from fixed center to target anchor
    var dx = targetRect.left - currentRect.left;
    var dy = targetRect.top - currentRect.top;

    titleBlock.style.transition = 'transform 1.35s cubic-bezier(0.16, 1, 0.3, 1)';
    titleBlock.style.transform = 'translate(calc(-50% + ' + dx + 'px), calc(-50% + ' + dy + 'px))';
    titleBlock.classList.remove('is-centered');
    document.body.classList.add('layout-active');

    setTimeout(function(){
      // Cleanly dock into anchor container so layout is 100% fluid & responsive
      anchor.appendChild(titleBlock);
      titleBlock.classList.add('is-docked');
      titleBlock.style.transform = '';
      titleBlock.style.transition = '';
    }, 1400);
  }

  function replayTitleScreen(){
    var anchor = document.getElementById('titleAnchor');
    var stage = document.getElementById('heroEditorialStage');
    if(!titleBlock || !stage) return;

    hasShifted = false;
    document.body.classList.remove('layout-active');

    // Move back to root stage with pure fixed centering
    titleBlock.classList.remove('is-docked');
    titleBlock.classList.add('is-centered');
    stage.parentNode.insertBefore(titleBlock, stage);
    titleBlock.style.transform = '';
    titleBlock.style.transition = '';

    // Re-trigger quick build-up animation
    var p1 = document.getElementById('titlePrimary');
    var p2 = document.getElementById('titleSecondary');
    if(p1 && p2){
      p1.style.animation = 'none';
      p2.style.animation = 'none';
      void p1.offsetWidth; // trigger reflow
      p1.style.animation = '';
      p2.style.animation = '';
    }

    if(shiftTimeout) clearTimeout(shiftTimeout);
    shiftTimeout = setTimeout(shiftToLayout, 1800);
  }

  // Quick cinematic build-up finishes at ~0.65s, holds in dead center, then shifts cleanly at 1.65s
  shiftTimeout = setTimeout(shiftToLayout, 1650);

  // User interaction triggers immediate smooth transition
  ['wheel', 'touchmove', 'keydown', 'click'].forEach(function(evt){
    window.addEventListener(evt, function(){
      if(!hasShifted) shiftToLayout();
    }, { passive: true });
  });

  // Clicking the title replays the transition
  titleBlock.addEventListener('click', function(e){
    e.stopPropagation();
    if(!hasShifted) shiftToLayout();
    else replayTitleScreen();
  });

  // Expose replay function globally
  window.replayIntro = replayTitleScreen;
})();
'''

content = content[:script_start] + new_orchestration_script + content[script_end:]

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied true fixed dead-center and rainbow heart highlight successfully!")
