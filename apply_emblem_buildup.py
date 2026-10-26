import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('/home/user/emblem_markup.txt', 'r', encoding='utf-8') as f:
    emblem_svg = f.read()

# 1. Add emblem CSS styles
emblem_css = '''
/* ============================================================
   HEARTLIGHT HONEYBEE EMBLEM (CINEMATIC BUILD-UP INTRO LOGO)
   ============================================================ */
.emblem-stage {
  position: absolute;
  bottom: calc(100% + 16px);
  left: 50%;
  transform: translateX(-50%) scale(1);
  width: clamp(140px, 20vw, 185px);
  aspect-ratio: 1560 / 1020;
  pointer-events: none;
  opacity: 1;
  transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1), transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 50;
}

.emblem-stage.out {
  opacity: 0;
  transform: translateX(-50%) scale(0.92);
  pointer-events: none;
}

.emblem-svg {
  width: 100%;
  height: 100%;
  display: block;
  overflow: visible;
}

.emblem-svg * { --e: cubic-bezier(.22,1,.36,1); }
.emblem-svg .ln { stroke: #111; stroke-width: 14; stroke-linecap: round; stroke-linejoin: round; }

/* ---------- INTRO BUILD (0 – 2.1s) ---------- */
.emblem-svg .draw { stroke-dasharray: 1; stroke-dashoffset: 1; animation: emblemDraw var(--t,.6s) var(--e) var(--d,0s) forwards; }
.emblem-svg .fill { fill-opacity: 0; animation: emblemFillin .35s ease-out calc(var(--d,0s) + var(--t,.6s)*.55) forwards; }
.emblem-svg .pop { opacity: 0; transform-box: fill-box; transform-origin: center; animation: emblemPop .6s var(--e) var(--d,0s) forwards; }
.emblem-svg .hex { opacity: 0; transform-origin: 770px 570px; animation: emblemHex .55s var(--e) forwards; }
.emblem-svg .wing { opacity: 0; transform-origin: 680px 460px; animation: emblemWing .55s var(--e) var(--d) forwards; }
.emblem-svg .ring { opacity: 0; animation: emblemRing .4s var(--e) var(--d) forwards; }
.emblem-svg .shine { opacity: 0; animation: emblemFade .4s ease-out var(--d) forwards; }

@keyframes emblemDraw { to { stroke-dashoffset: 0; } }
@keyframes emblemFillin { to { fill-opacity: 1; } }
@keyframes emblemPop { 0% { opacity: 0; transform: scale(.55); } 60% { opacity: 1; transform: scale(1.07); } 100% { opacity: 1; transform: scale(1); } }
@keyframes emblemHex { from { opacity: 0; transform: scale(.82) rotate(-8deg); } to { opacity: 1; transform: none; } }
@keyframes emblemWing { from { opacity: 0; transform: scale(.3) rotate(14deg); } to { opacity: 1; transform: none; } }
@keyframes emblemRing { from { opacity: 0; transform: translateY(-22px); } to { opacity: 1; transform: none; } }
@keyframes emblemFade { to { opacity: 1; } }

/* ---------- ALIVE LOOP (from 2.0s, forever) ---------- */
.emblem-svg .breathe { transform-origin: 770px 570px; animation: emblemBreathe 3.2s ease-in-out 1s infinite alternate; }
.emblem-svg .bob { animation: emblemBob 1.5s ease-in-out 2s infinite alternate; }
.emblem-svg .flap { transform-origin: 680px 460px; animation: emblemFlap .22s ease-in-out 2s infinite alternate; }
.emblem-svg .flap.r { animation-delay: 2.03s; }
.emblem-svg .sway { animation: emblemSway 1.8s ease-in-out 2s infinite alternate; }
.emblem-svg .sway.a { transform-origin: 733px 245px; }
.emblem-svg .sway.b { transform-origin: 807px 245px; animation-delay: 2.25s; }
.emblem-svg .beat { transform-origin: 768px 710px; animation: emblemBeat 1.3s ease-in-out 2.1s infinite; }
.emblem-svg .glow { opacity: 0; animation: emblemGlow 1.3s ease-out 2.1s infinite; }
.emblem-svg .pulse { opacity: 0; transform-origin: 768px 710px; animation: emblemPulse 1.3s ease-out 2.1s infinite; }

@keyframes emblemBreathe { to { transform: scale(1.035); } }
@keyframes emblemBob { from { transform: translateY(8px); } to { transform: translateY(-14px); } }
@keyframes emblemFlap { from { transform: rotate(-5deg) scaleY(1); } to { transform: rotate(9deg) scaleY(.93); } }
@keyframes emblemSway { from { transform: rotate(-3.5deg); } to { transform: rotate(3.5deg); } }
@keyframes emblemBeat { 0%,100% { transform: scale(1); } 14% { transform: scale(1.12); } 28% { transform: scale(1); } 42% { transform: scale(1.07); } 70% { transform: scale(1); } }
@keyframes emblemGlow { 0% { opacity: 0; } 14% { opacity: 1; } 60%,100% { opacity: 0; } }
@keyframes emblemPulse { 0% { opacity: .55; transform: scale(.35); } 100% { opacity: 0; transform: scale(1); } }
'''

# Insert emblem CSS right before /* ============================================================ MODALS
modals_idx = content.find('/* ============================================================\n   MODALS')
if modals_idx == -1:
    modals_idx = content.find('/* ============================================================', content.find('hero-editorial-stage'))

content = content[:modals_idx] + emblem_css + '\n' + content[modals_idx:]

# 2. Add emblemStage inside #heroTitleBlock right before #heroTitleMain
target_title_block = '<div class="hero-title-block" id="heroTitleBlock" title="Click to replay title transition">\n            <h1 class="hero-title-main"'

replacement_title_block = f'''<div class="hero-title-block" id="heroTitleBlock" title="Click to replay title transition">
            <!-- Heartlight Honeybee Emblem (Animated build-up at top of Artsy Fartsy, then fades out) -->
            <div class="emblem-stage" id="emblemStage">
              {emblem_svg}
            </div>
            <h1 class="hero-title-main"'''

if target_title_block not in content:
    raise ValueError("target_title_block not matched")

content = content.replace(target_title_block, replacement_title_block, 1)

# 3. Update the orchestration script: Let the emblem play out (2.8s), fade out (0.6s), then glide into place!
script_marker = '// TITLE SCREEN CENTER-TO-LAYOUT SHIFT CHOREOGRAPHY'
script_start = content.find(script_marker)
script_end = content.find('</script>', script_start)

new_orchestration_script = '''// TITLE SCREEN CENTER-TO-LAYOUT SHIFT CHOREOGRAPHY (EMBLEM PLAYOUT & FADE OUT -> GLIDE)
// ============================================================
(function(){
  var tb = document.getElementById('heroTitleBlock');
  var emblem = document.getElementById('emblemStage');
  var hasShifted = false;
  var shiftTimeout = null;
  var fadeTimeout = null;

  if(!tb) return;

  function calculateTargetTransform(){
    var prevTransition = tb.style.transition;
    var prevTransform = tb.style.transform;

    tb.style.transition = 'none';
    tb.style.transform = 'none';

    var r = tb.getBoundingClientRect();

    tb.style.transform = prevTransform;
    tb.style.transition = prevTransition;

    var scale = window.innerWidth < 640 ? 1.35 : (window.innerWidth < 1024 ? 1.45 : 1.55);
    var startX = (window.innerWidth / 2) - (r.width * scale) / 2;
    var startY = (window.innerHeight / 2) - (r.height * scale) / 2;

    var tx = startX - r.left;
    var ty = startY - r.top;

    return {
      tx: tx,
      ty: ty,
      scale: scale
    };
  }

  function applyCenteredPosition(immediate){
    var t = calculateTargetTransform();
    if(immediate){
      tb.style.transition = 'none';
    }
    tb.style.transformOrigin = '0 0';
    tb.style.transform = 'translate3d(' + t.tx + 'px, ' + t.ty + 'px, 0) scale(' + t.scale + ')';
  }

  function shiftToLayout(){
    if(hasShifted) return;
    hasShifted = true;
    if(shiftTimeout) clearTimeout(shiftTimeout);
    if(fadeTimeout) clearTimeout(fadeTimeout);

    // Fade out emblem if not already fading out
    if(emblem) emblem.classList.add('out');

    // Smooth single-element GPU glide directly to identity resting position
    tb.style.transition = 'transform 1.35s cubic-bezier(0.16, 1, 0.3, 1)';
    tb.style.transform = 'translate3d(0px, 0px, 0px) scale(1)';

    // Reveal divider line, explore button, quote, and socials
    document.body.classList.add('layout-active');
  }

  function replayTitleScreen(){
    hasShifted = false;
    if(shiftTimeout) clearTimeout(shiftTimeout);
    if(fadeTimeout) clearTimeout(fadeTimeout);
    document.body.classList.remove('layout-active');

    // Restore emblem visibility and replay animations
    if(emblem){
      emblem.classList.remove('out');
      // Clone and replace SVG to re-trigger drawing and pop animations
      var oldSvg = emblem.querySelector('svg');
      if(oldSvg){
        var newSvg = oldSvg.cloneNode(true);
        emblem.replaceChild(newSvg, oldSvg);
      }
    }

    applyCenteredPosition(true);

    // Replay crisp upward build-up on title text
    var inner1 = document.getElementById('titleLineInner1');
    var inner2 = document.getElementById('titleLineInner2');
    if(inner1 && inner2){
      inner1.style.animation = 'none';
      inner2.style.animation = 'none';
      void inner1.offsetWidth; // Force reflow
      inner1.style.animation = '';
      inner2.style.animation = '';
    }

    // Schedule: Emblem plays out for 2.8s, triggers fade out, then at 3.4s shifts into place
    fadeTimeout = setTimeout(function(){
      if(emblem) emblem.classList.add('out');
    }, 2800);

    shiftTimeout = setTimeout(shiftToLayout, 3400);
  }

  // Set centered position immediately
  applyCenteredPosition(true);

  if(document.fonts && document.fonts.ready){
    document.fonts.ready.then(function(){
      if(!hasShifted) applyCenteredPosition(true);
    });
  }

  window.addEventListener('resize', function(){
    if(!hasShifted) applyCenteredPosition(true);
  });

  // INITIAL RUN: Let the emblem play out its intro assembly & alive loop (2.8s)
  // Then trigger emblem fade-out animation (0.6s)
  fadeTimeout = setTimeout(function(){
    if(emblem) emblem.classList.add('out');
  }, 2800);

  // Then at 3.4s, once the emblem has faded out, smoothly glide into layout position
  shiftTimeout = setTimeout(shiftToLayout, 3400);

  // User interactions trigger immediate smooth transition
  ['wheel', 'touchmove', 'keydown', 'click'].forEach(function(evt){
    window.addEventListener(evt, function(){
      if(!hasShifted) shiftToLayout();
    }, { passive: true });
  });

  // Clicking title block replays the transition
  tb.addEventListener('click', function(e){
    e.stopPropagation();
    if(!hasShifted) shiftToLayout();
    else replayTitleScreen();
  });

  window.replayIntro = replayTitleScreen;
})();
'''

content = content[:script_start] + new_orchestration_script + content[script_end:]

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Heartlight Honeybee Emblem build-up, playout, fade-out, and smooth glide successfully!")
