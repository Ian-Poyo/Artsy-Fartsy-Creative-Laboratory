with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix CSS for .foundation-stage-bg and .foundation-scrim-overlay
old_css_block = """.foundation-stage-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center 30%;
  opacity: 0;
  transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 0;
  will-change: opacity;
  transform: scale(1.02);
  filter: brightness(0.96) contrast(1.04);
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.4) 60px, #000 130px);
  mask-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.4) 60px, #000 130px);
}

/* Luminous Ambient Contrast Scrim with Seamless Left Legibility */
.foundation-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(circle at 75% 30%, rgba(255, 255, 255, 0.06) 0%, transparent 50%),
    linear-gradient(90deg, rgba(5, 8, 17, 0.94) 0%, rgba(5, 8, 17, 0.82) 36%, rgba(5, 8, 17, 0.16) 68%, rgba(5, 8, 17, 0.32) 100%),
    linear-gradient(180deg, #050811 0%, rgba(5, 8, 17, 0.4) 15%, transparent 35%, transparent 75%, rgba(5, 8, 17, 0.85) 100%);
  pointer-events: none;
  z-index: 1;
}"""

new_css_block = """.foundation-stage-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center 42%;
  opacity: 1;
  transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 0;
  will-change: opacity;
  transform: scale(1.02);
  filter: brightness(0.96) contrast(1.04);
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.4) 50px, #000 110px);
  mask-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.4) 50px, #000 110px);
}

/* Luminous Ambient Contrast Scrim with Seamless Left Legibility & Visible Kids */
.foundation-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(circle at 80% 30%, rgba(255, 255, 255, 0.08) 0%, transparent 50%),
    linear-gradient(90deg, rgba(5, 8, 17, 0.92) 0%, rgba(5, 8, 17, 0.78) 36%, rgba(5, 8, 17, 0.12) 68%, rgba(5, 8, 17, 0.25) 100%),
    linear-gradient(180deg, #050811 0%, rgba(5, 8, 17, 0.3) 12%, transparent 30%, transparent 80%, rgba(5, 8, 17, 0.65) 100%);
  pointer-events: none;
  z-index: 1;
}"""

if old_css_block in content:
    content = content.replace(old_css_block, new_css_block, 1)
    print("1. Replaced CSS block successfully")
else:
    print("1. Warning: old_css_block not found exactly!")

# 2. Add bgImage to Slide 0 in JS
old_mission_slide = """    {
      id: 'mission',
      eyebrow: '— Mission Statement',
      title: 'Friends of Artsy Fartsy Foundation',
      descHtml: '<p>Our mission is to ensure accessible, inspiring space for the Artsy Fartsy Creative Laboratory; expand equitable access to the arts through scholarships for high school students and adult learners; and strengthen arts education by delivering high-quality color science professional development for elementary, middle, and high school teachers.</p><p>We believe creativity is a powerful catalyst for learning, expression, and community, and we work to nurture it across ages, disciplines, and classrooms.</p>',
      actionsHtml: '<button class=\\"foundation-donate-btn\\" data-modal=\\"donateModal\\" aria-label=\\"Donate to the Foundation\\">' + rainbowHeartSvg + '<span>DONATE</span></button>'
    },"""

new_mission_slide = """    {
      id: 'mission',
      eyebrow: '— Mission Statement',
      title: 'Friends of Artsy Fartsy Foundation',
      descHtml: '<p>Our mission is to ensure accessible, inspiring space for the Artsy Fartsy Creative Laboratory; expand equitable access to the arts through scholarships for high school students and adult learners; and strengthen arts education by delivering high-quality color science professional development for elementary, middle, and high school teachers.</p><p>We believe creativity is a powerful catalyst for learning, expression, and community, and we work to nurture it across ages, disciplines, and classrooms.</p>',
      bgImage: '/images/foundation-slide-1.jpg',
      actionsHtml: '<button class=\\"foundation-donate-btn\\" data-modal=\\"donateModal\\" aria-label=\\"Donate to the Foundation\\">' + rainbowHeartSvg + '<span>DONATE</span></button>'
    },"""

if old_mission_slide in content:
    content = content.replace(old_mission_slide, new_mission_slide, 1)
    print("2. Added bgImage to slide 0 in JS")
else:
    print("2. Warning: old_mission_slide not found exactly!")

# 3. Update updateSlide() in JS so the background image persists and doesn't fade to black
old_js_update = """    // 1. Dynamic Slide Background Update with smooth crossfade
    if (bgEl) {
      if (s.bgImage) {
        bgEl.style.opacity = '0';
        setTimeout(function() {
          bgEl.style.backgroundImage = 'url(\"' + s.bgImage + '\")';
          bgEl.style.opacity = '1';
        }, 180);
      } else {
        bgEl.style.opacity = '0';
      }
    }"""

new_js_update = """    // 1. Dynamic Slide Background Update: Kid image persists across section
    if (bgEl) {
      var targetBg = s.bgImage || '/images/foundation-slide-1.jpg';
      var currentBg = bgEl.style.backgroundImage || '';
      if (currentBg.indexOf(targetBg) === -1) {
        bgEl.style.opacity = '0.35';
        setTimeout(function() {
          bgEl.style.backgroundImage = 'url(\"' + targetBg + '\")';
          bgEl.style.opacity = '1';
        }, 180);
      } else {
        bgEl.style.opacity = '1';
      }
    }"""

if old_js_update in content:
    content = content.replace(old_js_update, new_js_update, 1)
    print("3. Updated updateSlide() background persistence logic in JS")
else:
    print("3. Warning: old_js_update not found exactly!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html successfully")
