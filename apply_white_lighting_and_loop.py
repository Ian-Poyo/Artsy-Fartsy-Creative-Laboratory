import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
with open('/home/user/test_white_lighting_css.py', 'r') as f:
    txt = f.read()
m_c = re.search(r"css = '''(.*?)'''", txt, re.DOTALL)
new_css = m_c.group(1).strip()

pos_c_start = content.find('/* ============================================================\n   SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE')
pos_c_end = content.find('</style>')
if pos_c_start != -1 and pos_c_end != -1:
    content = content[:pos_c_start] + new_css + '\n' + content[pos_c_end:]
    print("1. CSS updated successfully!")
else:
    print("WARNING: Could not find CSS block!")

# 2. Update JS (3-second auto loop)
with open('/home/user/test_3s_loop.py', 'r') as f:
    txt = f.read()
m_j = re.search(r"js = '''(.*?)'''", txt, re.DOTALL)
new_js = m_j.group(1).strip()

pos_j_start = content.find('// ============================================================\n// FRIENDS OF ARTSY FARTSY FOUNDATION SLIDER CONTROLLER')
pos_j_end = content.find('// ============================================================\n// NAVIGATION & PERFORMANCE CONTROLLER (HERO + CURATED)')
if pos_j_start != -1 and pos_j_end != -1:
    content = content[:pos_j_start] + new_js + '\n\n' + content[pos_j_end:]
    print("2. JS updated successfully with 3s loop!")
else:
    print("WARNING: Could not find JS block!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html fully updated with pure white styling, enhanced lighting, and 3-second auto loop!")
