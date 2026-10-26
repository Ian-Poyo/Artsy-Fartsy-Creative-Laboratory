import re
from build_showcase_scenes import scenes_data

transformed_scripts = []

for name, data in scenes_data.items():
    scripts = data["scripts"]
    for i, s in enumerate(scripts):
        # Scoped element IDs
        s_mod = s.replace("document.getElementById('c')", f"document.getElementById('c-{name}')")
        s_mod = s_mod.replace('document.getElementById("c")', f"document.getElementById('c-{name}')")
        s_mod = s_mod.replace("document.getElementById('bg')", f"document.getElementById('bg-{name}')")
        s_mod = s_mod.replace('document.getElementById("bg")', f"document.getElementById('bg-{name}')")
        s_mod = s_mod.replace("document.getElementById('gl')", f"document.getElementById('gl-{name}')")
        s_mod = s_mod.replace('document.getElementById("gl")', f"document.getElementById('gl-{name}')")
        
        # Add inactive throttle to frame loop
        # Check if 'function frame(' is present
        if 'function frame(now){' in s_mod:
            s_mod = s_mod.replace(
                'function frame(now){',
                f'function frame(now){{var sc=document.getElementById("scene-{name}");if(sc&&!sc.classList.contains("is-active")){{requestAnimationFrame(frame);return;}}'
            )
        elif 'function frame(){' in s_mod:
            s_mod = s_mod.replace(
                'function frame(){',
                f'function frame(){{var sc=document.getElementById("scene-{name}");if(sc&&!sc.classList.contains("is-active")){{requestAnimationFrame(frame);return;}}'
            )
        
        transformed_scripts.append((name, i, s_mod))

print(f"Transformed {len(transformed_scripts)} scripts successfully.")
