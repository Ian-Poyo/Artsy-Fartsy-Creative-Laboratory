import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS: Remove hero-title-docked completely (no dual DOM element needed!)
# Clean up title styles to be pure, crisp, inline-block with smooth GPU transform
old_css_part = re.search(r'/\* --- Docked Title in Grid[\s\S]*?/\* Quick Crisp Upward Build-up', content)
if not old_css_part:
    raise ValueError("old_css_part not found")

new_css_part = '''/* --- Title Anchor (Defines editorial baseline in grid) --- */
.title-anchor {
  width: 100%;
  height: clamp(55px, 8.5vh, 76px);
  display: flex;
  align-items: flex-end;
  pointer-events: none;
}

/* --- THE CINEMATIC STARTUP TITLE BLOCK (100% PURE CSS TRUE DEAD CENTER) --- */
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
  transform-origin: center center;
}

.hero-title-main {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: clamp(3px, 0.8vh, 6px);
  line-height: 1.05;
  user-select: none;
  align-items: center;
  text-align: center;
}

.title-line-mask {
  display: inline-flex;
  justify-content: center;
  text-align: center;
  overflow: hidden;
  padding-bottom: 4px;
}

.title-line-inner {
  display: inline-block;
  transform: translateY(115%);
  opacity: 0;
  animation: titleQuickBuild 0.55s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

#titleLineInner1 {
  animation-delay: 0.08s;
}

#titleLineInner2 {
  animation-delay: 0.22s;
}

/* ZERO SHADOWS, ZERO BLUR - PURE VECTOR CRISP TYPOGRAPHY */
.title-primary {
  display: inline-block;
  font-family: var(--font-sans);
  font-size: clamp(3.2rem, 6.8vw, 5.2rem);
  font-weight: 600;
  letter-spacing: -0.03em;
  color: #ffffff;
  text-align: center;
  text-shadow: none !important;
  filter: none !important;
  will-change: transform;
}

.title-secondary {
  display: inline-block;
  font-family: var(--font-sans);
  font-size: clamp(1.35rem, 2.1vw, 1.85rem);
  font-weight: 400;
  letter-spacing: -0.01em;
  color: rgba(255, 255, 255, 0.82);
  text-align: center;
  text-shadow: none !important;
  filter: none !important;
  will-change: transform;
}

/* Quick Crisp Upward Build-up'''

content = content[:old_css_part.start()] + new_css_part + content[old_css_part.end():]

# 2. Update HTML in .tier-upper-left: titleAnchor is a clean anchor slot (no docked duplicate!)
old_upper_left = re.search(r'<div class="tier-upper-left" id="tierUpperLeft">[\s\S]*?</div>\s*</div>\s*(?=<div class="tier-upper-right")', content)
if not old_upper_left:
    raise ValueError("old_upper_left not found")

new_upper_left = '''<div class="tier-upper-left" id="tierUpperLeft">
        <div class="title-anchor" id="titleAnchor"></div>
      </div>
    </div>
    '''

content = content[:old_upper_left.start()] + new_upper_left + content[old_upper_left.end():]

# 3. Update the JavaScript orchestration: Single element, pure Bezier glide, zero handoff pop
old_js_part = re.search(r'// TITLE SCREEN CENTER-TO-LAYOUT SHIFT CHOREOGRAPHY[\s\S]*?window\.replayIntro = replayTitleScreen;\s*\}\)\(\);', content)
if not old_js_part:
    raise ValueError("old_js_part not found")

new_js_part = '''// TITLE SCREEN CENTER-TO-LAYOUT SHIFT CHOREOGRAPHY (SINGLE-ELEMENT SILKY-SMOOTH GLIDE)
// ============================================================
(function(){
  var titleBlock = document.getElementById('heroTitleBlock');
  var titlePrimary = document.getElementById('titlePrimary');
  var titleSecondary = document.getElementById('titleSecondary');
  var anchor = document.getElementById('titleAnchor');
  var hasShifted = false;
  var shiftTimeout = null;

  if(!titleBlock || !titlePrimary || !titleSecondary || !anchor) return;

  function calculateTargetTransform(){
    var startRect = titleBlock.getBoundingClientRect();
    var anchorRect = anchor.getBoundingClientRect();
    var p1Rect = titlePrimary.getBoundingClientRect();
    var p2Rect = titleSecondary.getBoundingClientRect();

    // Scale from poster typography to editorial layout size
    // Responsive scale: 0.62 on desktop, slightly larger on mobile
    var scale = window.innerWidth < 640 ? 0.72 : (window.innerWidth < 1024 ? 0.66 : 0.62);
    var scaledW = startRect.width * scale;
    var scaledH = startRect.height * scale;

    var startCX = window.innerWidth / 2;
    var startCY = window.innerHeight / 2;

    // Anchor baseline: align bottom of scaled title with bottom of anchor slot
    var targetLeft = anchorRect.left;
    var targetTop = anchorRect.bottom - scaledH;

    var targetCX = targetLeft + scaledW / 2;
    var targetCY = targetTop + scaledH / 2;

    var dx = targetCX - startCX;
    var dy = targetCY - startCY;

    // Line 1 centering offset:
    // In centered state, p1 is centered above p2.
    // Width difference between p2 and p1 determines the shift to left-align:
    var lineShift = (p2Rect.width - p1Rect.width) / 2;

    return {
      dx: dx,
      dy: dy,
      scale: scale,
      lineShift: lineShift
    };
  }

  function shiftToLayout(){
    if(hasShifted) return;
    hasShifted = true;
    if(shiftTimeout) clearTimeout(shiftTimeout);

    var t = calculateTargetTransform();

    // Single uninterrupted GPU transform with silky Bezier deceleration
    titleBlock.style.transition = 'transform 1.35s cubic-bezier(0.16, 1, 0.3, 1)';
    titlePrimary.style.transition = 'transform 1.35s cubic-bezier(0.16, 1, 0.3, 1)';

    titleBlock.style.transform = 'translate(calc(-50% + ' + t.dx + 'px), calc(-50% + ' + t.dy + 'px)) scale(' + t.scale + ')';
    titlePrimary.style.transform = 'translateX(-' + t.lineShift + 'px)';

    // Reveal divider line, explore button, quote, and socials
    document.body.classList.add('layout-active');

    // ZERO HANDOFF SWAP: titleBlock simply coasts to rest and stays there!
  }

  function replayTitleScreen(){
    hasShifted = false;
    document.body.classList.remove('layout-active');

    // Restore centered block instantly
    titleBlock.style.transition = 'none';
    titlePrimary.style.transition = 'none';
    titleBlock.style.transform = 'translate(-50%, -50%) scale(1)';
    titlePrimary.style.transform = 'translateX(0)';

    // Replay crisp upward build-up
    var inner1 = document.getElementById('titleLineInner1');
    var inner2 = document.getElementById('titleLineInner2');
    if(inner1 && inner2){
      inner1.style.animation = 'none';
      inner2.style.animation = 'none';
      void inner1.offsetWidth; // Force reflow
      inner1.style.animation = '';
      inner2.style.animation = '';
    }

    if(shiftTimeout) clearTimeout(shiftTimeout);
    shiftTimeout = setTimeout(shiftToLayout, 1800);
  }

  // Handle window resizing smoothly if already shifted
  window.addEventListener('resize', function(){
    if(hasShifted){
      var t = calculateTargetTransform();
      titleBlock.style.transition = 'none';
      titlePrimary.style.transition = 'none';
      titleBlock.style.transform = 'translate(calc(-50% + ' + t.dx + 'px), calc(-50% + ' + t.dy + 'px)) scale(' + t.scale + ')';
      titlePrimary.style.transform = 'translateX(-' + t.lineShift + 'px)';
    }
  });

  // Hold centered for cinematic build-up (~1.65s), then smoothly glide to layout
  shiftTimeout = setTimeout(shiftToLayout, 1650);

  // User interactions trigger immediate smooth transition
  ['wheel', 'touchmove', 'keydown', 'click'].forEach(function(evt){
    window.addEventListener(evt, function(){
      if(!hasShifted) shiftToLayout();
    }, { passive: true });
  });

  // Clicking title block replays the transition
  titleBlock.addEventListener('click', function(e){
    e.stopPropagation();
    if(!hasShifted) shiftToLayout();
    else replayTitleScreen();
  });

  window.replayIntro = replayTitleScreen;
})();'''

content = content[:old_js_part.start()] + new_js_part + content[old_js_part.end():]

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied single-element silky-smooth glide with zero DOM swap and zero snapping!")
