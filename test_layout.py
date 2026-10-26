import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect current CSS and structure around tier-upper-left and heroTitleBlock
print("Has heroTitleBlock:", 'heroTitleBlock' in content)
print("Has titleAnchor:", 'titleAnchor' in content)
print("Has rainbowHeart:", 'rainbowHeart' in content)
