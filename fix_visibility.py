with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove .hero-section::after (which covered the text with z-index 22)
old_hero_after = '''/* Seamless Bottom Gradient Feathering into Section 2 */
.hero-section::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 160px;
  background: linear-gradient(180deg, transparent 0%, rgba(5, 8, 17, 0.75) 55%, #050811 100%);
  pointer-events: none;
  z-index: 22;
}'''

if old_hero_after in content:
    content = content.replace(old_hero_after, '/* Bottom feathering moved to section 2 top to prevent text occlusion */', 1)
    print("1. Removed .hero-section::after overlay that occluded text!")
else:
    print("Note: old hero after not found or already removed.")

# 2. Update .editorial-body, .editorial-tagline, and .social-circle for crystal-clear readability
old_editorial = '''.editorial-body {
  margin: 0;
  font-family: var(--font-sans);
  font-size: clamp(12.5px, 0.96vw, 13.5px);
  font-weight: 400;
  line-height: 1.62;
  color: rgba(255, 255, 255, 0.78);
  letter-spacing: 0.005em;
  text-shadow: none;
}

.editorial-tagline {
  margin: 0;
  font-family: var(--font-sans);
  font-size: clamp(13px, 1.0vw, 14.5px);
  font-weight: 700;
  line-height: 1.48;
  color: #ffffff;
  letter-spacing: 0.01em;
  text-shadow: none;
}'''

new_editorial = '''.editorial-body {
  margin: 0;
  font-family: var(--font-sans);
  font-size: clamp(13px, 1.0vw, 14.5px);
  font-weight: 400;
  line-height: 1.62;
  color: #ffffff;
  opacity: 0.95;
  letter-spacing: 0.005em;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.85);
}

.editorial-tagline {
  margin: 0;
  font-family: var(--font-sans);
  font-size: clamp(13px, 1.0vw, 14.5px);
  font-weight: 700;
  line-height: 1.48;
  color: #ffffff;
  letter-spacing: 0.01em;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.85);
}'''

if old_editorial in content:
    content = content.replace(old_editorial, new_editorial, 1)
    print("2. Editorial text contrast upgraded to pure brilliant white!")
else:
    print("Note: old editorial text not found or already upgraded.")

# 3. Brighten social circles
old_social = '''.social-circle {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255, 255, 255, 0.22);
  display: flex;
  align-items: center;
  justify-content: center;
  color: rgba(255, 255, 255, 0.9);
  text-decoration: none;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.35);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}'''

new_social = '''.social-circle {
  position: relative;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.16);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1.5px solid rgba(255, 255, 255, 0.45);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  text-decoration: none;
  box-shadow: 0 4px 18px rgba(0, 0, 0, 0.5), 0 0 12px rgba(255, 255, 255, 0.25);
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}'''

if old_social in content:
    content = content.replace(old_social, new_social, 1)
    print("3. Social circles brightened with crisp glassmorphic contrast!")
else:
    print("Note: old social circle not found.")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Visibility fix applied successfully!")
