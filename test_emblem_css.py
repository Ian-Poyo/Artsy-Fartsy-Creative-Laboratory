# Extract CSS from Heartlight Honeybee Emblem (1).html
with open('/home/user/uploads/Heartlight Honeybee Emblem (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
styles = re.findall(r'<style>([\s\S]*?)</style>', content)[0]

# Check what selectors are in the styles
selectors = re.findall(r'([^{}]+)\s*\{', styles)
print(f"Total selectors: {len(selectors)}")
for s in selectors[:15]:
    print(" ", s.strip())
