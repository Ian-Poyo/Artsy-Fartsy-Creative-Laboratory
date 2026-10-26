with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove HTML link from tier-lower-left
old_html = '''      <div class="tier-lower-left">
        <span class="bottom-quote" id="bottomQuote">Unleash Creativity Today</span>
        <a href="#curatedSection" class="hero-curated-link" id="heroCuratedLink" aria-label="Scroll to Curated Carousels">
          <span>Curated Collection</span>
          <svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 5v14M19 12l-7 7-7-7"/></svg>
        </a>
      </div>'''

new_html = '''      <div class="tier-lower-left">
        <span class="bottom-quote" id="bottomQuote">Unleash Creativity Today</span>
      </div>'''

if old_html in text:
    text = text.replace(old_html, new_html, 1)
    print("1. Curated Collection button removed from HTML!")
else:
    print("WARNING: old_html not found!")

# 2. Remove CSS rules for .hero-curated-link
old_css = '''/* Scroll Prompt in Hero Tier Lower Left */
.hero-curated-link {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  margin-top: 8px;
  padding: 6px 14px;
  border-radius: 100px;
  background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.14);
  color: rgba(255, 255, 255, 0.85);
  font-family: var(--font-sans);
  font-size: 11.5px;
  font-weight: 500;
  letter-spacing: 0.03em;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.25s ease;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.hero-curated-link:hover {
  background: rgba(255, 255, 255, 0.16);
  border-color: rgba(255, 255, 255, 0.28);
  color: #ffffff;
  transform: translateY(-1px);
}

.hero-curated-link svg {
  animation: bounceDownPrompt 2s ease-in-out infinite;
}

@keyframes bounceDownPrompt {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(3px); }
}'''

if old_css in text:
    text = text.replace(old_css, '', 1)
    print("2. Curated Collection CSS removed!")
else:
    print("WARNING: old_css not found!")

# 3. Clean JS reference
old_js_line = '  var heroLink = document.getElementById(\'heroCuratedLink\');\n'
if old_js_line in text:
    text = text.replace(old_js_line, '', 1)
    print("3. heroLink variable removed from JS!")

old_js_listener = '  if (heroLink) heroLink.addEventListener(\'click\', scrollToCurated);\n'
if old_js_listener in text:
    text = text.replace(old_js_listener, '', 1)
    print("4. heroLink listener removed from JS!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: Curated Collection button completely removed!")
