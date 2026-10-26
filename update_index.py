import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove "Curated" from the top navbar
old_nav_curated = '      <button class="nav-link-btn" id="navCuratedBtn">Curated</button>\n'
if old_nav_curated in content:
    content = content.replace(old_nav_curated, '', 1)
    print("1. Curated button removed from navbar!")
else:
    print("WARNING: old_nav_curated not found!")

# 2. Replace Section 2 HTML
with open('/home/user/generate_full_curated.py', 'r') as f:
    gen_file = f.read()
m_html = re.search(r"curated_html = '''(.*?)'''", gen_file, re.DOTALL)
new_html = m_html.group(1).strip()

pos_sec_start = content.find('<!-- ============================================================\n     SECTION 2: CURATED CAROUSELS')
if pos_sec_start == -1:
    pos_sec_start = content.find('<section id="curatedSection"')

pos_sec_end = content.find('<!-- ============================================================\n     SECTION 2: EXPANDED BOTTOM SHOWCASE')
if pos_sec_end == -1:
    pos_sec_end = content.find('<!-- ============================================================\n     INTERACTIVE MODALS')

print("Found HTML boundaries:", pos_sec_start, pos_sec_end)
if pos_sec_start != -1 and pos_sec_end != -1:
    content = content[:pos_sec_start] + new_html + '\n\n' + content[pos_sec_end:]
    print("2. Section 2 HTML successfully replaced with themed showcase!")
else:
    print("WARNING: Could not find HTML boundaries!")

# 3. Replace Section 2 CSS
with open('/home/user/test_curated_theme_css.py', 'r') as f:
    css_file = f.read()
m_css = re.search(r"css = '''(.*?)'''", css_file, re.DOTALL)
new_css = m_css.group(1).strip()

pos_css_start = content.find('/* ============================================================\n   SECTION 2: CURATED CAROUSELS')
pos_css_end = content.find('</style>')

print("Found CSS boundaries:", pos_css_start, pos_css_end)
if pos_css_start != -1 and pos_css_end != -1:
    # Also preserve scroll prompt in hero
    hero_scroll_css = '''
/* Scroll Prompt in Hero Tier Lower Left */
.hero-curated-link {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  margin-top: 8px;
  padding: 6px 14px;
  border-radius: 100px;
  background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.14);
  color: rgba(255, 255, 255, 0.85);
  font-family: var(--font-sans);
  font-size: 11.5px;
  font-weight: 500;
  letter-spacing: 0.03em;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.25s ease;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.hero-curated-link:hover {
  background: rgba(255, 255, 255, 0.16);
  border-color: rgba(255, 255, 255, 0.28);
  color: #ffffff;
  transform: translateY(-1px);
}

.hero-curated-link svg {
  animation: bounceDownPrompt 2s ease-in-out infinite;
}

@keyframes bounceDownPrompt {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(3px); }
}
'''
    content = content[:pos_css_start] + new_css + '\n' + hero_scroll_css + '\n' + content[pos_css_end:]
    print("3. Section 2 CSS successfully replaced with themed styles!")
else:
    print("WARNING: Could not find CSS boundaries!")

# 4. Replace Section 2 JS
with open('/home/user/test_curated_theme_js.py', 'r') as f:
    js_file = f.read()
m_js = re.search(r"js = '''(.*?)'''", js_file, re.DOTALL)
new_js = m_js.group(1).strip()

pos_js_start = content.find('// ============================================================\n// CURATED CAROUSELS (FUNKY TWIST 3D SHOWCASE CONTROLLER)')
pos_js_end = content.find('// ============================================================\n// NAVIGATION & PERFORMANCE CONTROLLER (HERO + CURATED)')

print("Found JS boundaries:", pos_js_start, pos_js_end)
if pos_js_start != -1 and pos_js_end != -1:
    content = content[:pos_js_start] + new_js + '\n\n' + content[pos_js_end:]
    print("4. Section 2 JS successfully replaced with enhanced controller!")
else:
    print("WARNING: Could not find JS boundaries!")

# Write updated file
with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html fully updated!")
