import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Section 2 HTML
with open('/home/user/build_foundation_section.py', 'r') as f:
    txt = f.read()
m_h = re.search(r"html = '''(.*?)'''", txt, re.DOTALL)
new_html = m_h.group(1).strip()

pos_h_start = content.find('<!-- ============================================================\n     SECTION 2: EXPEDITIONS SHOWCASE')
if pos_h_start == -1:
    pos_h_start = content.find('<section id="curatedSection"')

pos_h_end = content.find('<!-- ============================================================\n     INTERACTIVE MODALS')

print("HTML positions:", pos_h_start, pos_h_end)
if pos_h_start != -1 and pos_h_end != -1:
    content = content[:pos_h_start] + new_html + '\n\n' + content[pos_h_end:]
    print("1. HTML replaced successfully!")
else:
    print("WARNING: Could not find HTML boundaries!")

# 2. Replace Section 2 CSS
with open('/home/user/test_foundation_css.py', 'r') as f:
    txt = f.read()
m_c = re.search(r"css = '''(.*?)'''", txt, re.DOTALL)
new_css = m_c.group(1).strip()

pos_c_start = content.find('/* ============================================================\n   SECTION 2: ARTSY FARTSY EXPEDITIONS SHOWCASE')
if pos_c_start == -1:
    pos_c_start = content.find('.expedition-section {')

pos_c_end = content.find('</style>')

print("CSS positions:", pos_c_start, pos_c_end)
if pos_c_start != -1 and pos_c_end != -1:
    content = content[:pos_c_start] + new_css + '\n' + content[pos_c_end:]
    print("2. CSS replaced successfully!")
else:
    print("WARNING: Could not find CSS boundaries!")

# 3. Replace Section 2 JS
with open('/home/user/test_foundation_slider.py', 'r') as f:
    txt = f.read()
m_j = re.search(r"js = '''(.*?)'''", txt, re.DOTALL)
new_js = m_j.group(1).strip()

pos_j_start = content.find('// ============================================================\n// ARTSY FARTSY EXPEDITIONS SHOWCASE CONTROLLER')
pos_j_end = content.find('// ============================================================\n// NAVIGATION & PERFORMANCE CONTROLLER (HERO + CURATED)')

print("JS positions:", pos_j_start, pos_j_end)
if pos_j_start != -1 and pos_j_end != -1:
    content = content[:pos_j_start] + new_js + '\n\n' + content[pos_j_end:]
    print("3. JS replaced successfully!")
else:
    print("WARNING: Could not find JS boundaries!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html fully updated with Friends of Artsy Fartsy Foundation Slider!")
