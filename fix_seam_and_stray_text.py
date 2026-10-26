with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove stray text after </html>
if "</html>bgImage: '/images/foundation-slide-1.jpg'," in content:
    content = content.replace("</html>bgImage: '/images/foundation-slide-1.jpg',", "</html>")
    print("1. Removed stray text after </html> successfully")
else:
    # Check general trailing text after </html>
    pos_html = content.find("</html>")
    if pos_html != -1:
        trailing = content[pos_html + len("</html>"):].strip()
        if trailing:
            print(f"Found trailing text: {repr(trailing)}")
            content = content[:pos_html + len("</html>")] + "\n"
            print("1. Cleaned trailing text after </html>")

# 2. Update .hero-bottom-scrim in CSS to eliminate the 75px flat black shelf
old_hero_scrim = """.hero-bottom-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    transparent 34%,
    rgba(5, 8, 17, 0.22) 48%,
    rgba(5, 8, 17, 0.60) 65%,
    rgba(5, 8, 17, 0.90) 82%,
    rgba(5, 8, 17, 0.99) 93%,
    #050811 96%,
    #050811 100%
  );
  pointer-events: none;
  z-index: 10;
}"""

new_hero_scrim = """.hero-bottom-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    transparent 42%,
    rgba(5, 8, 17, 0.18) 58%,
    rgba(5, 8, 17, 0.55) 75%,
    rgba(5, 8, 17, 0.88) 92%,
    #050811 100%
  );
  pointer-events: none;
  z-index: 10;
}"""

if old_hero_scrim in content:
    content = content.replace(old_hero_scrim, new_hero_scrim, 1)
    print("2. Updated .hero-bottom-scrim successfully")
else:
    print("2. Warning: old_hero_scrim not found exactly")

# 3. Update .foundation-stage-bg and .foundation-scrim-overlay to eliminate the 110px mask & dark 180deg scrim
old_stage_css = """.foundation-stage-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center 42%;
  opacity: 1;
  transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 0;
  will-change: opacity;
  transform: scale(1.02);
  filter: brightness(0.96) contrast(1.04);
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.4) 50px, #000 110px);
  mask-image: linear-gradient(to bottom, transparent 0%, rgba(0, 0, 0, 0.4) 50px, #000 110px);
}

/* Luminous Ambient Contrast Scrim with Seamless Left Legibility & Visible Kids */
.foundation-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(circle at 80% 30%, rgba(255, 255, 255, 0.08) 0%, transparent 50%),
    linear-gradient(90deg, rgba(5, 8, 17, 0.92) 0%, rgba(5, 8, 17, 0.78) 36%, rgba(5, 8, 17, 0.12) 68%, rgba(5, 8, 17, 0.25) 100%),
    linear-gradient(180deg, #050811 0%, rgba(5, 8, 17, 0.3) 12%, transparent 30%, transparent 80%, rgba(5, 8, 17, 0.65) 100%);
  pointer-events: none;
  z-index: 1;
}"""

new_stage_css = """.foundation-stage-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center 42%;
  opacity: 1;
  transition: opacity 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 0;
  will-change: opacity;
  transform: scale(1.02);
  filter: brightness(1.0) contrast(1.02);
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, #000 30px);
  mask-image: linear-gradient(to bottom, transparent 0%, #000 30px);
}

/* Luminous Ambient Contrast Scrim with Seamless Left Legibility & Visible Kids */
.foundation-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(circle at 80% 30%, rgba(255, 255, 255, 0.08) 0%, transparent 50%),
    linear-gradient(90deg, rgba(5, 8, 17, 0.90) 0%, rgba(5, 8, 17, 0.75) 36%, rgba(5, 8, 17, 0.12) 68%, rgba(5, 8, 17, 0.20) 100%);
  pointer-events: none;
  z-index: 1;
}"""

if old_stage_css in content:
    content = content.replace(old_stage_css, new_stage_css, 1)
    print("3. Updated .foundation-stage-bg & .foundation-scrim-overlay successfully")
else:
    print("3. Warning: old_stage_css not found exactly")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html successfully")
