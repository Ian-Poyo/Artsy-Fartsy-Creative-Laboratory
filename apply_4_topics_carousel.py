import re
from build_showcase_scenes import scenes_data

# Read existing index.html
with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update #stage with the 4 scenes
stage_match = re.search(r'<div id="stage">[\s\S]*?</div>\s*</div>\s*(?=<!-- Cinematic Bottom Scrim)', html)
if not stage_match:
    raise ValueError("stage div not found")
stage_s = stage_match.start()
stage_e = stage_match.end()

new_stage_html = f'''<div id="stage">
    <!-- Scene 0: Classroom (Starts active) -->
    <div class="hero-scene is-active" id="scene-classroom" data-scene="0">
      <div class="scene-wrap">
        <img id="bg-classroom" alt="Floating Classroom in the clouds" src="{scenes_data['classroom']['src']}">
        <canvas id="gl-classroom"></canvas>
        <canvas id="c-classroom"></canvas>
      </div>
    </div>

    <!-- Scene 1: Happy Birthday -->
    <div class="hero-scene" id="scene-birthday" data-scene="1">
      <div class="scene-wrap">
        <img id="bg-birthday" alt="Happy Birthday Celebration" src="{scenes_data['birthday']['src']}">
        <canvas id="gl-birthday"></canvas>
        <canvas id="c-birthday"></canvas>
      </div>
    </div>

    <!-- Scene 2: Presentation -->
    <div class="hero-scene" id="scene-presentation" data-scene="2">
      <div class="scene-wrap">
        <img id="bg-presentation" alt="Animated Presentation Graph" src="{scenes_data['presentation']['src']}">
        <canvas id="c-presentation"></canvas>
      </div>
    </div>

    <!-- Scene 3: Private Party -->
    <div class="hero-scene" id="scene-party" data-scene="3">
      <div class="scene-wrap">
        <img id="bg-party" alt="Private Party with Floating Music Notes" src="{scenes_data['party']['src']}">
        <canvas id="gl-party"></canvas>
        <canvas id="c-party"></canvas>
      </div>
    </div>
  </div>'''

html = html[:stage_s] + new_stage_html + html[stage_e:]

# 2. Update CSS for stage and scenes
old_stage_css = re.search(r'#stage\s*\{[\s\S]*?canvas#c\s*\{[^}]*\}', html)
if not old_stage_css:
    raise ValueError("old_stage_css not found")

new_stage_css = '''#stage {
  position: fixed;
  inset: 0;
  overflow: hidden;
  background: #0a3f8a;
  z-index: 1;
}

.hero-scene {
  position: absolute;
  inset: 0;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.8s ease-in-out;
  will-change: opacity;
}

.hero-scene.is-active {
  opacity: 1;
  pointer-events: auto;
}

.scene-wrap {
  position: absolute;
  inset: 0;
  transform-origin: 50% 55%;
  animation: breathe 28s ease-in-out infinite alternate;
  will-change: transform;
}

@keyframes breathe {
  0% { transform: scale(1); }
  100% { transform: scale(1.045); }
}

.hero-scene img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.hero-scene canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: block;
  pointer-events: none;
}'''

html = html[:old_stage_css.start()] + new_stage_css + html[old_stage_css.end():]

# 3. Update divider line CSS to include loading track, fill, and glowing bead
old_line_css = re.search(r'/\* --- THE HORIZONTAL DIVIDER LINE --- \*/[\s\S]*?body\.layout-active \.hero-divider-line\s*\{[^}]*\}', html)
if not old_line_css:
    raise ValueError("old_line_css not found")

new_line_css = '''/* --- THE HORIZONTAL DIVIDER LINE WITH ANIMATED LOADING INDICATOR (image-1.png) --- */
.hero-divider-line {
  position: relative;
  width: 100%;
  height: 2px;
  margin: 0 0 clamp(16px, 2.4vh, 22px) 0;
  pointer-events: none;
  overflow: visible;
  opacity: 0;
  transform: scaleX(0);
  transform-origin: left center;
  transition: opacity 1.1s ease 0.25s, transform 1.25s cubic-bezier(0.16, 1, 0.3, 1) 0.25s;
}

body.layout-active .hero-divider-line {
  opacity: 1;
  transform: scaleX(1);
}

.line-base-track {
  position: absolute;
  left: 0;
  right: 0;
  top: 0.5px;
  height: 1px;
  background: rgba(255, 255, 255, 0.22);
}

.line-progress-fill {
  position: absolute;
  left: 0;
  top: 0;
  height: 1.5px;
  width: 0%;
  background: linear-gradient(
    to right,
    rgba(255, 255, 255, 0.2) 0%,
    rgba(255, 255, 255, 0.7) 70%,
    #ffffff 100%
  );
  box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);
  will-change: width;
}

.line-progress-bead {
  position: absolute;
  left: 0%;
  top: 1px;
  transform: translate(-50%, -50%);
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #ffffff;
  box-shadow: 
    0 0 5px #ffffff,
    0 0 12px rgba(255, 255, 255, 0.95),
    0 0 20px rgba(120, 210, 255, 0.85);
  pointer-events: none;
  will-change: left;
}'''

html = html[:old_line_css.start()] + new_line_css + html[old_line_css.end():]

# 4. Update the horizontal divider line HTML to include the track, fill, and bead
old_line_html = '<div class="hero-divider-line" id="heroDividerLine"></div>'
new_line_html = '''<div class="hero-divider-line" id="heroDividerLine">
      <div class="line-base-track"></div>
      <div class="line-progress-fill" id="lineProgressFill"></div>
      <div class="line-progress-bead" id="lineProgressBead"></div>
    </div>'''

if old_line_html not in html:
    raise ValueError("old_line_html not matched")
html = html.replace(old_line_html, new_line_html, 1)

# 5. Update .tier-lower-right to wrap the text in #editorialTextWrap
old_tier_right = '''<div class="tier-lower-right">
        <h3 class="editorial-eyebrow">A LAB FOR THE UNCONVENTIONAL</h3>
        <p class="editorial-lead">For ideas that refuse to stay inside the lines.</p>
        <p class="editorial-body">
          An experimental space where imagination runs wild, strange ideas take shape, and creativity has no single direction.
        </p>
        <p class="editorial-tagline">Make a mess. Find the magic.</p>
      </div>'''

new_tier_right = '''<div class="tier-lower-right" id="tierLowerRight">
        <div class="editorial-text-wrap" id="editorialTextWrap">
          <h3 class="editorial-eyebrow" id="editorialEyebrow">A LAB FOR THE UNCONVENTIONAL</h3>
          <p class="editorial-lead" id="editorialLead">For ideas that refuse to stay inside the lines.</p>
          <p class="editorial-body" id="editorialBody">
            An experimental space where imagination runs wild, strange ideas take shape, and creativity has no single direction.
          </p>
          <p class="editorial-tagline" id="editorialTagline">Make a mess. Find the magic.</p>
        </div>
      </div>'''

if old_tier_right not in html:
    raise ValueError("old_tier_right not matched")
html = html.replace(old_tier_right, new_tier_right, 1)

# 6. Append all 7 scene scripts before the orchestration script
from test_transform_scripts import transformed_scripts

scene_scripts_block = '\n<!-- ================= 4 TOPIC SCENE CANVAS ANIMATION ENGINES ================= -->\n'
for name, i, s in transformed_scripts:
    scene_scripts_block += f'\n<!-- Scene {name} Script {i} -->\n<script>\n{s}\n</script>\n'

# Find the orchestration script marker
script_marker = '// TITLE SCREEN CENTER-TO-LAYOUT SHIFT CHOREOGRAPHY'
script_start = html.find(script_marker)
if script_start == -1:
    raise ValueError("script_marker not found")

# Replace orchestration script with updated version that starts the carousel after cinematic shift
orchestration_script = '''// TITLE SCREEN CENTER-TO-LAYOUT SHIFT CHOREOGRAPHY & 4-TOPIC BACKGROUND CAROUSEL
// ============================================================
(function(){
  var titleBlock = document.getElementById('heroTitleBlock');
  var dockedBlock = document.getElementById('heroTitleDocked');
  var titlePrimary = document.getElementById('titlePrimary');
  var titleSecondary = document.getElementById('titleSecondary');
  var hasShifted = false;
  var shiftTimeout = null;

  if(!titleBlock || !dockedBlock || !titlePrimary || !titleSecondary) return;

  // The 4 topics with their specific copy and display timing
  // Topic 0: Classroom (3 seconds)
  // Subsequent topics: 1.5 seconds each
  var TOPICS = [
    {
      id: 'classroom',
      duration: 3000,
      quote: 'Unleash Creativity Today',
      eyebrow: 'A LAB FOR THE UNCONVENTIONAL',
      lead: 'For ideas that refuse to stay inside the lines.',
      body: 'An experimental space where imagination runs wild, strange ideas take shape, and creativity has no single direction.',
      tagline: 'Make a mess. Find the magic.'
    },
    {
      id: 'birthday',
      duration: 1500,
      quote: 'Celebrate The Magic Of Color',
      eyebrow: 'BIRTHDAYS & MILESTONE CELEBRATIONS',
      lead: 'Unforgettable celebrations dipped in color, joy, and confetti.',
      body: 'Custom creative birthday parties filled with art making, vibrant mess, and personalized magic you take home.',
      tagline: 'Celebrate vividly. Make lasting memories.'
    },
    {
      id: 'presentation',
      duration: 1500,
      quote: 'Where Bold Vision Meets Execution',
      eyebrow: 'PRESENTATIONS & BRAND SHOWCASES',
      lead: 'Elevate ideas with bold, creative visual storytelling.',
      body: 'An inspiring, tech-forward canvas for dynamic presentations, product launches, and interactive visionary gatherings.',
      tagline: 'Transform concepts into captivating experiences.'
    },
    {
      id: 'party',
      duration: 1500,
      quote: 'Every Great Night Has A Melody',
      eyebrow: 'PRIVATE PARTIES & MUSIC NIGHTS',
      lead: 'Intimate gatherings enveloped in sound, art, and soul.',
      body: 'Exclusive celebrations with curated music, ambient lighting, and tailored creative atmospheres crafted for your circle.',
      tagline: 'Your sanctuary for music, magic, and connection.'
    }
  ];

  var currentTopicIndex = 0;
  var isCarouselRunning = false;
  var progressRafId = null;

  function switchScene(sceneId) {
    var scenes = document.querySelectorAll('.hero-scene');
    scenes.forEach(function(sc) {
      if(sc.id === 'scene-' + sceneId) {
        sc.classList.add('is-active');
      } else {
        sc.classList.remove('is-active');
      }
    });
  }

  function updateTopicText(topic) {
    var wrap = document.getElementById('editorialTextWrap');
    var quote = document.getElementById('bottomQuote');
    if(!wrap) return;

    wrap.style.transition = 'opacity 0.25s ease, transform 0.25s ease';
    if(quote) quote.style.transition = 'opacity 0.25s ease';
    wrap.style.opacity = '0';
    wrap.style.transform = 'translateY(-6px)';
    if(quote) quote.style.opacity = '0';

    setTimeout(function() {
      var eyebrow = document.getElementById('editorialEyebrow');
      var lead = document.getElementById('editorialLead');
      var body = document.getElementById('editorialBody');
      var tagline = document.getElementById('editorialTagline');
      
      if(eyebrow) eyebrow.textContent = topic.eyebrow;
      if(lead) lead.textContent = topic.lead;
      if(body) body.textContent = topic.body;
      if(tagline) tagline.textContent = topic.tagline;
      if(quote) quote.textContent = topic.quote;

      wrap.style.transform = 'translateY(6px)';
      void wrap.offsetWidth; // Force reflow

      wrap.style.opacity = '1';
      wrap.style.transform = 'translateY(0)';
      if(quote) quote.style.opacity = '1';
    }, 250);
  }

  function runSlide(index) {
    if(!isCarouselRunning) return;
    currentTopicIndex = index % TOPICS.length;
    var topic = TOPICS[currentTopicIndex];

    // 1. Switch background scene
    switchScene(topic.id);

    // 2. Update text smoothly
    updateTopicText(topic);

    // 3. Animate loading line progress
    var fill = document.getElementById('lineProgressFill');
    var bead = document.getElementById('lineProgressBead');
    if(fill) fill.style.width = '0%';
    if(bead) bead.style.left = '0%';

    var startTime = performance.now();
    var duration = topic.duration;

    if(progressRafId) cancelAnimationFrame(progressRafId);

    function progressLoop(now) {
      if(!isCarouselRunning) return;
      var elapsed = now - startTime;
      var pct = Math.min(1, elapsed / duration);

      if(fill) fill.style.width = (pct * 100) + '%';
      if(bead) bead.style.left = (pct * 100) + '%';

      if(pct < 1) {
        progressRafId = requestAnimationFrame(progressLoop);
      } else {
        // Completed loading progress: proceed to next slide
        setTimeout(function() {
          if(isCarouselRunning) {
            runSlide(currentTopicIndex + 1);
          }
        }, 40);
      }
    }

    progressRafId = requestAnimationFrame(progressLoop);
  }

  function shiftToLayout(){
    if(hasShifted) return;
    hasShifted = true;
    if(shiftTimeout) clearTimeout(shiftTimeout);

    // Measure exact start rect (center) and target rect (docked layout)
    var startRect = titleBlock.getBoundingClientRect();
    var targetRect = dockedBlock.getBoundingClientRect();
    var p1Rect = titlePrimary.getBoundingClientRect();
    var p2Rect = titleSecondary.getBoundingClientRect();

    var scale = targetRect.height / startRect.height;
    var scaledW = startRect.width * scale;

    var startCX = window.innerWidth / 2;
    var startCY = window.innerHeight / 2;

    var targetCX = targetRect.left + scaledW / 2;
    var targetCY = targetRect.top + targetRect.height / 2;

    var dx = targetCX - startCX;
    var dy = targetCY - startCY;

    var lineShift = (p2Rect.width - p1Rect.width) / 2;

    titleBlock.style.transition = 'transform 1.35s cubic-bezier(0.16, 1, 0.3, 1)';
    titlePrimary.style.transition = 'transform 1.35s cubic-bezier(0.16, 1, 0.3, 1)';

    titleBlock.style.transform = 'translate(calc(-50% + ' + dx + 'px), calc(-50% + ' + dy + 'px)) scale(' + scale + ')';
    titlePrimary.style.transform = 'translateX(-' + lineShift + 'px)';

    // Reveal divider line, explore button, quote, and socials
    document.body.classList.add('layout-active');

    // At exact completion, hand off invisibly with zero pixel jump and start carousel
    setTimeout(function(){
      dockedBlock.style.visibility = 'visible';
      titleBlock.style.opacity = '0';
      titleBlock.style.pointerEvents = 'none';

      // Start the 4-topic background & loading line carousel
      isCarouselRunning = true;
      runSlide(0);
    }, 1380);
  }

  function replayTitleScreen(){
    hasShifted = false;
    isCarouselRunning = false;
    if(progressRafId) cancelAnimationFrame(progressRafId);
    document.body.classList.remove('layout-active');

    // Reset to classroom scene
    switchScene('classroom');
    var fill = document.getElementById('lineProgressFill');
    var bead = document.getElementById('lineProgressBead');
    if(fill) fill.style.width = '0%';
    if(bead) bead.style.left = '0%';

    // Hide docked target and restore centered block
    dockedBlock.style.visibility = 'hidden';
    titleBlock.style.transition = 'none';
    titlePrimary.style.transition = 'none';
    titleBlock.style.transform = 'translate(-50%, -50%) scale(1)';
    titlePrimary.style.transform = 'translateX(0)';
    titleBlock.style.opacity = '1';
    titleBlock.style.pointerEvents = 'auto';

    // Replay crisp upward build-up
    var inner1 = document.getElementById('titleLineInner1');
    var inner2 = document.getElementById('titleLineInner2');
    if(inner1 && inner2){
      inner1.style.animation = 'none';
      inner2.style.animation = 'none';
      void inner1.offsetWidth;
      inner1.style.animation = '';
      inner2.style.animation = '';
    }

    if(shiftTimeout) clearTimeout(shiftTimeout);
    shiftTimeout = setTimeout(shiftToLayout, 1800);
  }

  // Hold centered for cinematic build-up (~1.65s), then smoothly glide to layout
  shiftTimeout = setTimeout(shiftToLayout, 1650);

  // User interactions trigger immediate smooth transition
  ['wheel', 'touchmove', 'keydown', 'click'].forEach(function(evt){
    window.addEventListener(evt, function(){
      if(!hasShifted) shiftToLayout();
    }, { passive: true });
  });

  // Clicking either title block replays the transition
  titleBlock.addEventListener('click', function(e){
    e.stopPropagation();
    if(!hasShifted) shiftToLayout();
    else replayTitleScreen();
  });

  dockedBlock.addEventListener('click', function(e){
    e.stopPropagation();
    replayTitleScreen();
  });

  window.replayIntro = replayTitleScreen;
})();
'''

# Find the end of script tag
script_tag_end = html.find('</script>', script_start)
html = html[:script_start] + orchestration_script + html[script_tag_end:]

# Insert the scene_scripts_block right before </body>
body_end = html.rfind('</body>')
html = html[:body_end] + scene_scripts_block + html[body_end:]

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully applied 4-topic background slideshow with animated line progress loader!")
