import os, re

# 1. Load the 4 uploaded scene files
scene_files = {
    "classroom": "/home/user/uploads/Floating Classroom Animation.html",
    "birthday": "/home/user/uploads/Happy Birthday Animation.html",
    "presentation": "/home/user/uploads/Animated Presentation Graph 3.html",
    "party": "/home/user/uploads/Private Party – Music Notes.html"
}

scenes_data = {}

for name, fpath in scene_files.items():
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Extract image src
    img_m = re.search(r'<img[^>]+src="([^"]+)"', html)
    src = img_m.group(1) if img_m else ""
    
    # Extract scripts
    scripts = re.findall(r'<script(?:\s+[^>]*)?>([\s\S]*?)</script>', html)
    
    scenes_data[name] = {
        "src": src,
        "scripts": scripts
    }
    print(f"Loaded {name}: img src len {len(src)}, {len(scripts)} scripts")

print("All 4 scenes successfully parsed.")
