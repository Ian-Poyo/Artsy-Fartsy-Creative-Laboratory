import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the donate button SVG with the fully formed, uncompacted, symmetric heart vector
old_donate_btn = re.search(r'<button class="nav-donate-btn"[^>]*>.*?</button>', content, re.DOTALL)
if not old_donate_btn:
    raise ValueError("nav-donate-btn not found")

new_donate_btn = '''<button class="nav-donate-btn" data-modal="donateModal" aria-label="Donate">
        <span class="donate-heart-wrap">
          <svg class="donate-heart-icon" width="14" height="14" viewBox="0 0 24 24" aria-hidden="true" style="overflow: visible;">
            <defs>
              <linearGradient id="rainbowHeart" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ff0055">
                  <animate attributeName="stop-color" 
                    values="#ff0055;#ff5500;#ffcc00;#00e676;#00b0ff;#9d00ff;#ff0055" 
                    dur="3s" repeatCount="indefinite" />
                </stop>
                <stop offset="20%" stop-color="#ff5500">
                  <animate attributeName="stop-color" 
                    values="#ff5500;#ffcc00;#00e676;#00b0ff;#9d00ff;#ff0055;#ff5500" 
                    dur="3s" repeatCount="indefinite" />
                </stop>
                <stop offset="40%" stop-color="#ffcc00">
                  <animate attributeName="stop-color" 
                    values="#ffcc00;#00e676;#00b0ff;#9d00ff;#ff0055;#ff5500;#ffcc00" 
                    dur="3s" repeatCount="indefinite" />
                </stop>
                <stop offset="60%" stop-color="#00e676">
                  <animate attributeName="stop-color" 
                    values="#00e676;#00b0ff;#9d00ff;#ff0055;#ff5500;#ffcc00;#00e676" 
                    dur="3s" repeatCount="indefinite" />
                </stop>
                <stop offset="80%" stop-color="#00b0ff">
                  <animate attributeName="stop-color" 
                    values="#00b0ff;#9d00ff;#ff0055;#ff5500;#ffcc00;#00e676;#00b0ff" 
                    dur="3s" repeatCount="indefinite" />
                </stop>
                <stop offset="100%" stop-color="#9d00ff">
                  <animate attributeName="stop-color" 
                    values="#9d00ff;#ff0055;#ff5500;#ffcc00;#00e676;#00b0ff;#9d00ff" 
                    dur="3s" repeatCount="indefinite" />
                </stop>
                <animateTransform 
                  attributeName="gradientTransform" 
                  type="rotate" 
                  from="0 0.5 0.5" 
                  to="360 0.5 0.5" 
                  dur="2.8s" 
                  repeatCount="indefinite"/>
              </linearGradient>
            </defs>
            <path fill="url(#rainbowHeart)" d="M 12 21.35 l -1.45 -1.32 C 5.4 15.36 2 12.28 2 8.5 C 2 5.42 4.42 3 7.5 3 c 1.74 0 3.41 0.81 4.5 2.09 C 13.09 3.81 14.76 3 16.5 3 c 3.08 0 5.5 2.42 5.5 5.5 c 0 3.78 -3.4 6.86 -8.55 11.54 L 12 21.35 z"/>
          </svg>
        </span>
        <span>Donate</span>
      </button>'''

content = content.replace(old_donate_btn.group(0), new_donate_btn, 1)

# 2. Update CSS for donate button and heart to guarantee overflow: visible and prevent clipping
old_donate_css = re.search(r'\.nav-donate-btn\s*\{.*?(?=\.nav-capsule|\.nav-brand|\/\*|\Z)', content, re.DOTALL)
if not old_donate_css:
    raise ValueError("nav-donate-btn CSS not found")

new_donate_css = '''.nav-donate-btn {
  background: rgba(255, 255, 255, 0.14);
  border: 1px solid rgba(255, 255, 255, 0.45);
  border-radius: 9999px;
  padding: 5px 15px;
  color: #ffffff;
  font-family: var(--font-sans);
  font-size: 12.5px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 
    0 2px 10px rgba(0, 0, 0, 0.25),
    inset 0 1px 0 rgba(255, 255, 255, 0.4);
  transition: all 0.25s ease;
  outline: none;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  overflow: visible;
}

.donate-heart-wrap {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 14px;
  height: 14px;
  overflow: visible;
  line-height: 0;
}

.donate-heart-icon {
  display: block;
  width: 14px;
  height: 14px;
  overflow: visible !important;
  filter: drop-shadow(0 0 3px rgba(255, 0, 85, 0.8)) drop-shadow(0 0 6px rgba(0, 176, 255, 0.6));
  animation: rainbowHeartGlow 3s ease-in-out infinite alternate;
  transform-origin: center center;
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@keyframes rainbowHeartGlow {
  0% {
    filter: drop-shadow(0 0 3px rgba(255, 0, 85, 0.85)) drop-shadow(0 0 6px rgba(255, 204, 0, 0.6));
    transform: scale(1);
  }
  50% {
    filter: drop-shadow(0 0 4px rgba(0, 230, 118, 0.85)) drop-shadow(0 0 8px rgba(0, 176, 255, 0.7));
    transform: scale(1.08);
  }
  100% {
    filter: drop-shadow(0 0 4px rgba(157, 0, 255, 0.9)) drop-shadow(0 0 9px rgba(255, 0, 85, 0.75));
    transform: scale(1);
  }
}

.nav-donate-btn:hover {
  background: rgba(255, 255, 255, 0.26);
  border-color: rgba(255, 255, 255, 0.85);
  box-shadow: 
    0 4px 18px rgba(0, 0, 0, 0.35),
    0 0 16px rgba(255, 0, 85, 0.35),
    0 0 24px rgba(0, 230, 118, 0.25),
    0 0 30px rgba(157, 0, 255, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.5);
  transform: translateY(-1px);
}

.nav-donate-btn:hover .donate-heart-icon {
  transform: scale(1.22);
  filter: 
    drop-shadow(0 0 5px rgba(255, 0, 85, 0.95))
    drop-shadow(0 0 11px rgba(0, 230, 118, 0.85))
    drop-shadow(0 0 16px rgba(157, 0, 255, 0.9));
}
'''

content = content[:old_donate_css.start()] + new_donate_css + content[old_donate_css.end():]

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated heart vector with pristine SVG path and unclipped styling!")
