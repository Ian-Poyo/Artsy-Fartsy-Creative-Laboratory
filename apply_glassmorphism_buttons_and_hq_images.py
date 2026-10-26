import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the buttons CSS in Section 2
old_buttons_css = '''/* Pure White Glassmorphism Donate Button with Animated Rainbow Heart */
.foundation-donate-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 40px;
  border-radius: 9999px;
  background: #ffffff;
  color: #0b0f19;
  border: 1.5px solid #ffffff;
  font-family: var(--font-sans);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
  box-shadow: 
    0 10px 30px rgba(0, 0, 0, 0.35),
    0 0 20px rgba(255, 255, 255, 0.3),
    inset 0 1px 1px #ffffff;
  outline: none;
}

.foundation-donate-btn:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.92);
  color: #000000;
  box-shadow: 
    0 14px 36px rgba(0, 0, 0, 0.45),
    0 0 30px rgba(255, 255, 255, 0.55);
}

.foundation-donate-btn:active {
  transform: scale(0.96);
}

/* Rainbow Moving Gradient Heart Icon (Matching Navbar) */
.foundation-donate-btn .donate-heart-wrap {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 18px;
  height: 18px;
  overflow: visible;
  line-height: 0;
}

.foundation-donate-btn .donate-heart-icon {
  display: block;
  width: 18px;
  height: 18px;
  overflow: visible !important;
  filter: drop-shadow(0 0 3px rgba(255, 0, 85, 0.8)) drop-shadow(0 0 6px rgba(0, 176, 255, 0.6));
  animation: rainbowHeartGlow 3s ease-in-out infinite alternate;
  transform-origin: center center;
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.foundation-donate-btn:hover .donate-heart-icon {
  transform: scale(1.15);
}

/* Pure White Glassmorphism Book Button (Yellow Removed) */
.foundation-book-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 38px;
  border-radius: 9999px;
  background: #ffffff;
  color: #0b0f19;
  border: 1.5px solid #ffffff;
  font-family: var(--font-sans);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
  box-shadow: 
    0 10px 30px rgba(0, 0, 0, 0.35),
    0 0 20px rgba(255, 255, 255, 0.3),
    inset 0 1px 1px #ffffff;
  outline: none;
}

.foundation-book-btn:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.92);
  color: #000000;
  box-shadow: 
    0 14px 36px rgba(0, 0, 0, 0.45),
    0 0 30px rgba(255, 255, 255, 0.55);
}

.foundation-book-btn:active {
  transform: scale(0.96);
}'''

new_buttons_css = '''/* True Glassmorphism Donate Button with Animated Rainbow Heart */
.foundation-donate-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 40px;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(24px) saturate(200%);
  -webkit-backdrop-filter: blur(24px) saturate(200%);
  color: #ffffff;
  border: 1.5px solid rgba(255, 255, 255, 0.45);
  font-family: var(--font-sans);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
  box-shadow: 
    0 10px 30px rgba(0, 0, 0, 0.35),
    inset 0 1px 1.5px rgba(255, 255, 255, 0.6),
    inset 0 -1px 1px rgba(0, 0, 0, 0.2);
  outline: none;
}

.foundation-donate-btn:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.28);
  border-color: rgba(255, 255, 255, 0.8);
  color: #ffffff;
  box-shadow: 
    0 14px 40px rgba(0, 0, 0, 0.45),
    0 0 25px rgba(255, 255, 255, 0.4),
    inset 0 1px 2px rgba(255, 255, 255, 0.8);
}

.foundation-donate-btn:active {
  transform: scale(0.96);
}

/* Rainbow Moving Gradient Heart Icon inside Glassmorphism Donate Button */
.foundation-donate-btn .donate-heart-wrap {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 18px;
  height: 18px;
  overflow: visible;
  line-height: 0;
}

.foundation-donate-btn .donate-heart-icon {
  display: block;
  width: 18px;
  height: 18px;
  overflow: visible !important;
  filter: drop-shadow(0 0 3px rgba(255, 0, 85, 0.8)) drop-shadow(0 0 6px rgba(0, 176, 255, 0.6));
  animation: rainbowHeartGlow 3s ease-in-out infinite alternate;
  transform-origin: center center;
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.foundation-donate-btn:hover .donate-heart-icon {
  transform: scale(1.15);
}

/* True Glassmorphism Book Button */
.foundation-book-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 38px;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(24px) saturate(200%);
  -webkit-backdrop-filter: blur(24px) saturate(200%);
  color: #ffffff;
  border: 1.5px solid rgba(255, 255, 255, 0.45);
  font-family: var(--font-sans);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
  box-shadow: 
    0 10px 30px rgba(0, 0, 0, 0.35),
    inset 0 1px 1.5px rgba(255, 255, 255, 0.6),
    inset 0 -1px 1px rgba(0, 0, 0, 0.2);
  outline: none;
}

.foundation-book-btn:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.28);
  border-color: rgba(255, 255, 255, 0.8);
  color: #ffffff;
  box-shadow: 
    0 14px 40px rgba(0, 0, 0, 0.45),
    0 0 25px rgba(255, 255, 255, 0.4),
    inset 0 1px 2px rgba(255, 255, 255, 0.8);
}

.foundation-book-btn:active {
  transform: scale(0.96);
}'''

if old_buttons_css in content:
    content = content.replace(old_buttons_css, new_buttons_css, 1)
    print("1. Buttons CSS updated to true Glassmorphism!")
else:
    print("WARNING: Old buttons CSS not found!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html updated with true Glassmorphism for donate and book buttons!")
