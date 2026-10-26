import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero Section bottom feathering
old_hero_rule = '''.hero-section {
  position: relative;
  width: 100%;
  height: 100vh;
  min-height: 600px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
}'''

new_hero_rule = '''.hero-section {
  position: relative;
  width: 100%;
  height: 100vh;
  min-height: 600px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
}

/* Seamless Bottom Gradient Feathering into Section 2 */
.hero-section::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 160px;
  background: linear-gradient(180deg, transparent 0%, rgba(5, 8, 17, 0.75) 55%, #050811 100%);
  pointer-events: none;
  z-index: 22;
}'''

if old_hero_rule in content:
    content = content.replace(old_hero_rule, new_hero_rule, 1)
    print("1. Hero bottom feathering added successfully!")
else:
    print("WARNING: Old hero rule not found!")

# 2. Update Section 2 CSS
with open('/home/user/test_refined_transition_css.py', 'r') as f:
    txt = f.read()
m_c = re.search(r"css = '''(.*?)'''", txt, re.DOTALL)
new_css = m_c.group(1).strip()

pos_c_start = content.find('/* ============================================================\n   SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE')
pos_c_end = content.find('</style>')
if pos_c_start != -1 and pos_c_end != -1:
    content = content[:pos_c_start] + new_css + '\n' + content[pos_c_end:]
    print("2. Section 2 CSS updated successfully!")
else:
    print("WARNING: Could not find CSS block!")

# 3. Update Section 2 HTML Donate Button with Rainbow Heart
rainbow_heart_btn = '''        <!-- Action Row: Glassmorphic Buttons with Animated Rainbow Heart -->
        <div class="foundation-actions-row" id="foundationActionsRow">
          <button class="foundation-donate-btn" id="foundationDonateBtn" data-modal="donateModal" aria-label="Donate to the Foundation">
            <span class="donate-heart-wrap">
              <svg class="donate-heart-icon" width="18" height="18" viewBox="0 0 24 24" aria-hidden="true" style="overflow: visible;">
                <defs>
                  <linearGradient id="rainbowHeartSection2" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#ff0055">
                      <animate attributeName="stop-color" values="#ff0055;#ff5500;#ffcc00;#00e676;#00b0ff;#9d00ff;#ff0055" dur="3s" repeatCount="indefinite" />
                    </stop>
                    <stop offset="20%" stop-color="#ff5500">
                      <animate attributeName="stop-color" values="#ff5500;#ffcc00;#00e676;#00b0ff;#9d00ff;#ff0055;#ff5500" dur="3s" repeatCount="indefinite" />
                    </stop>
                    <stop offset="40%" stop-color="#ffcc00">
                      <animate attributeName="stop-color" values="#ffcc00;#00e676;#00b0ff;#9d00ff;#ff0055;#ff5500;#ffcc00" dur="3s" repeatCount="indefinite" />
                    </stop>
                    <stop offset="60%" stop-color="#00e676">
                      <animate attributeName="stop-color" values="#00e676;#00b0ff;#9d00ff;#ff0055;#ff5500;#ffcc00;#00e676" dur="3s" repeatCount="indefinite" />
                    </stop>
                    <stop offset="80%" stop-color="#00b0ff">
                      <animate attributeName="stop-color" values="#00b0ff;#9d00ff;#ff0055;#ff5500;#ffcc00;#00e676;#00b0ff" dur="3s" repeatCount="indefinite" />
                    </stop>
                    <stop offset="100%" stop-color="#9d00ff">
                      <animate attributeName="stop-color" values="#9d00ff;#ff0055;#ff5500;#ffcc00;#00e676;#00b0ff;#9d00ff" dur="3s" repeatCount="indefinite" />
                    </stop>
                    <animateTransform attributeName="gradientTransform" type="rotate" from="0 0.5 0.5" to="360 0.5 0.5" dur="2.8s" repeatCount="indefinite"/>
                  </linearGradient>
                </defs>
                <path fill="url(#rainbowHeartSection2)" d="M 12 21.35 l -1.45 -1.32 C 5.4 15.36 2 12.28 2 8.5 C 2 5.42 4.42 3 7.5 3 c 1.74 0 3.41 0.81 4.5 2.09 C 13.09 3.81 14.76 3 16.5 3 c 3.08 0 5.5 2.42 5.5 5.5 c 0 3.78 -3.4 6.86 -8.55 11.54 L 12 21.35 z"/>
              </svg>
            </span>
            <span>DONATE</span>
          </button>
        </div>'''

old_actions_block = re.search(r'<!-- Action Row: Glassmorphic Buttons -->\s*<div class="foundation-actions-row" id="foundationActionsRow">.*?</div>\s*</div>', content, re.DOTALL)
if old_actions_block:
    content = content[:old_actions_block.start()] + rainbow_heart_btn + '\n      </div>' + content[old_actions_block.end():]
    print("3. HTML Donate Button updated with Rainbow Heart!")
else:
    print("WARNING: Could not find old actions block in HTML!")

# 4. Update JS controller
with open('/home/user/test_rainbow_heart_and_transition.py', 'r') as f:
    txt = f.read()
m_j = re.search(r"js = '''(.*?)'''", txt, re.DOTALL)
new_js = m_j.group(1).strip()

pos_j_start = content.find('// ============================================================\n// FRIENDS OF ARTSY FARTSY FOUNDATION SLIDER CONTROLLER')
pos_j_end = content.find('// ============================================================\n// NAVIGATION & PERFORMANCE CONTROLLER (HERO + CURATED)')
if pos_j_start != -1 and pos_j_end != -1:
    content = content[:pos_j_start] + new_js + '\n\n' + content[pos_j_end:]
    print("4. JS updated successfully with Rainbow Heart & smooth slide easing!")
else:
    print("WARNING: Could not find JS block!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html fully updated!")
