import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update docked title CSS: Refined, elegant subtitle scale that never goes large
old_docked_css = re.search(r'\.hero-title-docked\s*\{[\s\S]*?\.docked-secondary\s*\{[^}]*\}', content)
if not old_docked_css:
    raise ValueError("old_docked_css not found")

new_docked_css = '''.hero-title-docked {
  position: relative;
  margin: 0;
  padding: 0;
  width: 100%;
  max-width: 640px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
  cursor: pointer;
  pointer-events: auto;
  opacity: 0;
}

.docked-title-main {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: clamp(3px, 0.8vh, 6px);
  line-height: 1.05;
  user-select: none;
  align-items: flex-start;
  text-align: left;
}

.docked-primary {
  display: block;
  font-family: var(--font-sans);
  font-size: clamp(2.2rem, 3.8vw, 3.2rem);
  font-weight: 600;
  letter-spacing: -0.03em;
  color: #ffffff;
  text-align: left;
  text-shadow: none !important;
  filter: none !important;
}

.docked-secondary {
  display: block;
  font-family: var(--font-sans);
  font-size: clamp(0.95rem, 1.2vw, 1.15rem);
  font-weight: 400;
  letter-spacing: -0.01em;
  color: rgba(255, 255, 255, 0.78);
  text-align: left;
  text-shadow: none !important;
  filter: none !important;
}'''

content = content[:old_docked_css.start()] + new_docked_css + content[old_docked_css.end():]

# 2. Update centered title typography CSS: Match proportions so it scales seamlessly
old_title_css = re.search(r'\.title-primary\s*\{[\s\S]*?\.title-secondary\s*\{[^}]*\}', content)
if not old_title_css:
    raise ValueError("old_title_css not found")

new_title_css = '''.title-primary {
  display: block;
  font-family: var(--font-sans);
  font-size: clamp(3.2rem, 6.8vw, 5.2rem);
  font-weight: 600;
  letter-spacing: -0.03em;
  color: #ffffff;
  text-align: center;
  text-shadow: none !important;
  filter: none !important;
  will-change: transform;
}

.title-secondary {
  display: block;
  font-family: var(--font-sans);
  font-size: clamp(1.35rem, 2.1vw, 1.85rem);
  font-weight: 400;
  letter-spacing: -0.01em;
  color: rgba(255, 255, 255, 0.88);
  text-align: center;
  text-shadow: none !important;
  filter: none !important;
  will-change: transform;
}'''

content = content[:old_title_css.start()] + new_title_css + content[old_title_css.end():]

# 3. Update gap in .hero-title-main
content = content.replace('gap: clamp(4px, 1.2vh, 10px);', 'gap: clamp(3px, 0.8vh, 6px);')

# 4. Update the transition in shiftToLayout and replayTitleScreen
old_handoff = re.search(r'// At exact completion, hand off invisibly with zero pixel jump[\s\S]*?}, 1380\);', content)
if not old_handoff:
    raise ValueError("old_handoff not found")

new_handoff = '''// At exact completion, seamless 200ms crossfade with zero font jump
    setTimeout(function(){
      dockedBlock.style.visibility = 'visible';
      dockedBlock.style.transition = 'opacity 0.22s ease';
      titleBlock.style.transition = 'opacity 0.22s ease';

      requestAnimationFrame(function(){
        dockedBlock.style.opacity = '1';
        titleBlock.style.opacity = '0';
      });

      setTimeout(function(){
        titleBlock.style.pointerEvents = 'none';
      }, 230);
    }, 1350);'''

content = content[:old_handoff.start()] + new_handoff + content[old_handoff.end():]

# 5. Update replayTitleScreen to reset opacity
old_replay = re.search(r'function replayTitleScreen\(\)\{[\s\S]*?dockedBlock\.style\.visibility = \'hidden\';', content)
if not old_replay:
    raise ValueError("old_replay not found")

new_replay = '''function replayTitleScreen(){
    hasShifted = false;
    document.body.classList.remove('layout-active');

    // Hide docked target and restore centered block
    dockedBlock.style.opacity = '0';
    dockedBlock.style.visibility = 'hidden';
    dockedBlock.style.transition = 'none';
'''

content = content[:old_replay.start()] + new_replay + content[old_replay.end():]

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated typography and handoff: Creative Laboratory font size stays perfectly refined and never goes large!")
