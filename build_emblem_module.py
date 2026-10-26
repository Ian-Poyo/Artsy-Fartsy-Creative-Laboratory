import re, subprocess

with open('/home/user/uploads/Heartlight Honeybee Emblem (1).html', 'r', encoding='utf-8') as f:
    emblem_file = f.read()

# Extract only wing, BULB, markup definitions
pattern = r'(const wing = [\s\S]*?const markup = \(\) => `[\s\S]*?`;)'
m = re.search(pattern, emblem_file)
if not m:
    raise ValueError("Markup generator not found")

code = m.group(1)
test_node = f"""
{code}
console.log(markup());
"""

res = subprocess.run(['node', '-e', test_node], capture_output=True, text=True)
if res.returncode != 0:
    print("Node error:", res.stderr)
else:
    svg_markup = res.stdout.strip()
    # Namespace IDs
    svg_markup = svg_markup.replace('id="g"', 'id="emblem-g"')
    svg_markup = svg_markup.replace('url(#g)', 'url(#emblem-g)')
    svg_markup = svg_markup.replace('id="bc"', 'id="emblem-bc"')
    svg_markup = svg_markup.replace('url(#bc)', 'url(#emblem-bc)')
    svg_markup = svg_markup.replace('<svg ', '<svg class="emblem-svg" ')
    
    with open('/home/user/emblem_markup.txt', 'w', encoding='utf-8') as f:
        f.write(svg_markup)
    print("SVG generated successfully, length:", len(svg_markup))

