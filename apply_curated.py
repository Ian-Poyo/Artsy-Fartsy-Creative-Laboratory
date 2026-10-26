import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update body styling to enable smooth vertical scroll
old_body = '''body {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  background-color: var(--bg-deep);
  color: var(--text-main);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow: hidden;
}'''

new_body = '''html {
  scroll-behavior: smooth;
  width: 100%;
  min-height: 100%;
}

body {
  width: 100%;
  min-height: 100%;
  margin: 0;
  padding: 0;
  background-color: var(--bg-deep);
  color: var(--text-main);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  overflow-y: auto;
}'''

if old_body in content:
    content = content.replace(old_body, new_body, 1)
    print("1. Body styling updated to overflow-y: auto")
else:
    print("WARNING: old_body not found!")

# 2. Update #stage from position: fixed to position: absolute
old_stage = '''#stage {
  position: fixed;
  inset: 0;
  overflow: hidden;
  background: var(--bg);
  z-index: 1;
}'''

new_stage = '''#stage {
  position: absolute;
  inset: 0;
  overflow: hidden;
  background: var(--bg);
  z-index: 1;
}'''

if old_stage in content:
    content = content.replace(old_stage, new_stage, 1)
    print("2. #stage updated to position: absolute")
else:
    print("WARNING: old_stage not found!")

# 3. Add Curated button to navbar
old_nav = '''      <div class="nav-links">
        <button class="nav-link-btn" data-modal="homeModal">Home</button>
        <button class="nav-link-btn" data-modal="classesModal">Classes</button>
        <button class="nav-link-btn" data-modal="foundationModal">Foundation</button>'''

new_nav = '''      <div class="nav-links">
        <button class="nav-link-btn" data-modal="homeModal">Home</button>
        <button class="nav-link-btn" data-modal="classesModal">Classes</button>
        <button class="nav-link-btn" id="navCuratedBtn">Curated</button>
        <button class="nav-link-btn" data-modal="foundationModal">Foundation</button>'''

if old_nav in content:
    content = content.replace(old_nav, new_nav, 1)
    print("3. Curated button added to navbar")
else:
    print("WARNING: old_nav not found!")

# 4. Add Curated scroll prompt to tier-lower-left
old_tier_lower_left = '''      <div class="tier-lower-left">
        <span class="bottom-quote" id="bottomQuote">Unleash Creativity Today</span>
      </div>'''

new_tier_lower_left = '''      <div class="tier-lower-left">
        <span class="bottom-quote" id="bottomQuote">Unleash Creativity Today</span>
        <a href="#curatedSection" class="hero-curated-link" id="heroCuratedLink" aria-label="Scroll to Curated Carousels">
          <span>Curated Collection</span>
          <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
        </a>
      </div>'''

if old_tier_lower_left in content:
    content = content.replace(old_tier_lower_left, new_tier_lower_left, 1)
    print("4. Curated scroll link added to tier-lower-left")
else:
    print("WARNING: old_tier_lower_left not found!")

# Read the CSS to inject
with open('/home/user/test_curated_css.py', 'r') as f:
    css_file = f.read()
# Extract css string
css_match = re.search(r"css = '''(.*?)'''", css_file, re.DOTALL)
curated_css = css_match.group(1)

# Inject CSS before </style>
pos_style_close = content.find('</style>')
if pos_style_close != -1:
    content = content[:pos_style_close] + '\n' + curated_css + '\n' + content[pos_style_close:]
    print("5. Curated CSS injected before </style>")
else:
    print("WARNING: </style> not found!")

# Read the HTML section to inject
with open('/home/user/build_curated_section.py', 'r') as f:
    html_file = f.read()
html_match = re.search(r"html_section = '''(.*?)'''", html_file, re.DOTALL)
curated_html = html_match.group(1)

# Inject HTML section after </section> of hero
pos_hero_end = content.find('</section>')
if pos_hero_end != -1:
    content = content[:pos_hero_end + len('</section>')] + '\n' + curated_html + content[pos_hero_end + len('</section>'):]
    print("6. Curated Section 2 HTML injected after </section>")
else:
    print("WARNING: </section> not found!")

# Read the JS to inject
with open('/home/user/test_curated_js.py', 'r') as f:
    js_file = f.read()
js_match = re.search(r"js = '''(.*?)'''", js_file, re.DOTALL)
curated_js = js_match.group(1)

# Also expose window.jumpToHeroTopic and IntersectionObserver
helper_js = '''
  // Expose jumpToHeroTopic globally for Curated Carousel
  window.jumpToHeroTopic = function(topicIndex) {
    if (typeof loopTimeout !== 'undefined' && loopTimeout) clearTimeout(loopTimeout);
    if (typeof TOPICS !== 'undefined') {
      currentTopicIndex = topicIndex % TOPICS.length;
      var targetTopic = TOPICS[currentTopicIndex];
      if (typeof switchScene === 'function') switchScene(targetTopic.sceneId);
      if (typeof updateEditorialText === 'function') updateEditorialText(targetTopic);
      if (typeof isLoopRunning !== 'undefined' && isLoopRunning && typeof runNextLoopStep === 'function') {
        runNextLoopStep();
      }
    }
  };
'''

# Add helper_js right after function runNextLoopStep in hero script
pos_loop_step = content.find('function runNextLoopStep()')
if pos_loop_step != -1:
    content = content[:pos_loop_step] + helper_js + '\n  ' + content[pos_loop_step:]
    print("7. window.jumpToHeroTopic hooked into hero loop")
else:
    print("WARNING: runNextLoopStep not found!")

# Add scroll interaction for Explore Button and Nav links + IntersectionObserver
scroll_and_perf_js = '''
// ============================================================
// NAVIGATION & PERFORMANCE CONTROLLER (HERO + CURATED)
// ============================================================
(function(){
  var navCurated = document.getElementById('navCuratedBtn');
  var heroLink = document.getElementById('heroCuratedLink');
  var exploreBtn = document.getElementById('heroExploreBtn');
  var navHome = document.querySelector('.nav-link-btn[data-modal="homeModal"]');
  var curatedSection = document.getElementById('curatedSection');
  var heroSection = document.getElementById('hero-section');

  function scrollToCurated(e) {
    if (e) e.preventDefault();
    if (curatedSection) {
      curatedSection.scrollIntoView({ behavior: 'smooth' });
    }
  }

  if (navCurated) navCurated.addEventListener('click', scrollToCurated);
  if (heroLink) heroLink.addEventListener('click', scrollToCurated);
  if (exploreBtn) exploreBtn.addEventListener('click', scrollToCurated);

  if (navHome) {
    navHome.addEventListener('click', function(e) {
      if (window.scrollY > 80) {
        e.stopPropagation();
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    });
  }

  // IntersectionObserver: Pause heavy background canvases when hero is offscreen
  if ('IntersectionObserver' in window && heroSection) {
    var heroObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (!entry.isIntersecting) {
          // Offscreen: pause background canvas loops to save 100% GPU
          if (window.starryEngine && typeof window.starryEngine.stop === 'function') window.starryEngine.stop();
          if (window.classroomEngine && typeof window.classroomEngine.stop === 'function') window.classroomEngine.stop();
          if (window.birthdayEngine && typeof window.birthdayEngine.stop === 'function') window.birthdayEngine.stop();
          if (window.presentationEngine && typeof window.presentationEngine.stop === 'function') window.presentationEngine.stop();
          if (window.partyEngine && typeof window.partyEngine.stop === 'function') window.partyEngine.stop();
        } else {
          // Onscreen: resume active scene
          var activeScene = document.querySelector('.hero-scene.is-active');
          if (activeScene) {
            if (activeScene.id === 'scene-starry' && window.starryEngine) window.starryEngine.start();
            else if (activeScene.id === 'scene-classroom' && window.classroomEngine) window.classroomEngine.start();
            else if (activeScene.id === 'scene-birthday' && window.birthdayEngine) window.birthdayEngine.start();
            else if (activeScene.id === 'scene-presentation' && window.presentationEngine) window.presentationEngine.start();
            else if (activeScene.id === 'scene-party' && window.partyEngine) window.partyEngine.start();
          }
        }
      });
    }, { threshold: 0.1 });
    heroObserver.observe(heroSection);
  }
})();
'''

# Inject curated_js and scroll_and_perf_js before </body>
pos_body_close = content.find('</body>')
if pos_body_close != -1:
    full_script = '<script>\n' + curated_js + '\n' + scroll_and_perf_js + '\n</script>\n'
    content = content[:pos_body_close] + full_script + content[pos_body_close:]
    print("8. Curated Carousel JS & Navigation Controller injected before </body>")
else:
    print("WARNING: </body> not found!")

# Save to index.html
with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html updated successfully!")
