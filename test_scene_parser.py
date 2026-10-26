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
    
    # Check all getElementById in scripts
    scripts = re.findall(r'<script(?:\s+[^>]*)?>([\s\S]*?)</script>', content)
    ids_found = set()
    for s in scripts:
        for m in re.finditer(r'getElementById\([\'"]([^\'"]+)[\'"]\)', s):
            ids_found.add(m.group(1))
    print(f"{name} uses element IDs: {ids_found}")
