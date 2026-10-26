import os, re

files = [
    ("classroom", "Floating Classroom Animation.html"),
    ("birthday", "Happy Birthday Animation.html"),
    ("presentation", "Animated Presentation Graph 3.html"),
    ("party", "Private Party – Music Notes.html")
]

for name, fname in files:
    path = os.path.join("/home/user/uploads", fname)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract image src
    img_m = re.search(r'<img[^>]+src="([^"]+)"', content)
    src = img_m.group(1) if img_m else ""
    
    # Extract scripts
    scripts = re.findall(r'<script(?:\s+[^>]*)?>([\s\S]*?)</script>', content)
    
    print(f"Scene: {name}")
    print(f"  Image src len: {len(src)}")
    print(f"  Scripts count: {len(scripts)}")
    for i, s in enumerate(scripts):
        print(f"    Script {i} len: {len(s)}")
