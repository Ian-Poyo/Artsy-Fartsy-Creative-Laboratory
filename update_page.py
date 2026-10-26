import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update body / html overflow in CSS
content = re.sub(
    r'body\s*\{[^}]*overflow-x:\s*hidden;\s*overflow-y:\s*auto;\s*\}',
    '''body {
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
  background-color: var(--bg-deep);
  color: var(--text-main);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow: hidden;
}''',
    content
)

# 2. Hide or remove .hero-bottom-blend so centered woman is fully seeable
content = re.sub(
    r'\.hero-bottom-blend\s*\{[^}]*\}',
    '''.hero-bottom-blend {
  display: none;
}''',
    content
)

# 3. In HTML: Remove explore expeditions from hero-bottom-bar and remove .hero-bottom-blend div
old_hero_bottom = re.search(
    r'(<div class="hero-bottom-blend"></div>\s*)?<div class="hero-bottom-bar".*?</div>\s*</div>\s*</div>\s*</section>',
    content,
    re.DOTALL
)

if not old_hero_bottom:
    print("Trying alternative pattern for hero-bottom-bar")
    # Let's inspect where hero-section ends
    hero_end = content.find('</section>')
    hero_bottom_bar_start = content.find('<div class="hero-bottom-bar"')
    print("Found hero_bottom_bar_start at", hero_bottom_bar_start, "hero_end at", hero_end)

new_hero_bottom_html = '''  <!-- Bottom Bar in Hero: Socials in Middle, Copyright on Right -->
  <div class="hero-bottom-bar" aria-label="Hero Footer Navigation">
    <div class="hero-bar-left"></div>

    <div class="hero-bar-center">
      <!-- Socials: Instagram, Facebook -->
      <a href="https://instagram.com/artsyfartsystudio" target="_blank" rel="noopener noreferrer" class="social-circle" data-tooltip="Instagram" aria-label="Instagram">
        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
          <circle cx="12" cy="12" r="4"></circle>
          <circle cx="17.5" cy="6.5" r="1" fill="currentColor"></circle>
        </svg>
      </a>
      <a href="https://facebook.com/artsyfartsystudio" target="_blank" rel="noopener noreferrer" class="social-circle" data-tooltip="Facebook" aria-label="Facebook">
        <svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor">
          <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
        </svg>
      </a>
    </div>

    <div class="hero-bar-right">
      <span class="footer-copyright">© 2026 Artsy Fartsy Creative Laboratory.</span>
    </div>
  </div>
</section>'''

# Replace from hero-bottom-blend (or hero-bottom-bar) to </section>
hero_blend_idx = content.find('<div class="hero-bottom-blend">')
if hero_blend_idx != -1:
    hero_section_close = content.find('</section>', hero_blend_idx) + len('</section>')
    content = content[:hero_blend_idx] + new_hero_bottom_html + content[hero_section_close:]
    print("Replaced hero bottom bar successfully!")
else:
    hero_bar_idx = content.find('<div class="hero-bottom-bar"')
    hero_section_close = content.find('</section>', hero_bar_idx) + len('</section>')
    content = content[:hero_bar_idx] + new_hero_bottom_html + content[hero_section_close:]
    print("Replaced hero bottom bar successfully without blend div!")

# 4. Remove Section 2 (#showcase-section) and footer (.site-footer) and destinationModal
# Find showcase-section to modals
showcase_idx = content.find('<section id="showcase-section"')
home_modal_idx = content.find('<div class="modal-overlay" id="homeModal">')

if showcase_idx != -1 and home_modal_idx != -1:
    modals_comment = '''<!-- ============================================================
     INTERACTIVE MODALS
     ============================================================ -->\n'''
    content = content[:showcase_idx] + modals_comment + content[home_modal_idx:]
    print("Removed showcase section, footer, and destination modal!")

# 5. Clean up JavaScript: Remove destination data and showcase carousel listeners
script_idx = content.find('<script>')
script_close = content.find('</script>')
old_script = content[script_idx:script_close]

# Let's find cosmic particles canvas engine in script
cosmic_idx = content.find('// COSMIC PARTICLES CANVAS ENGINE', script_idx)
if cosmic_idx != -1:
    clean_script_start = '''<script>
// ============================================================
// COSMIC PARTICLES CANVAS ENGINE
// ============================================================'''
    content = content[:script_idx] + clean_script_start + content[cosmic_idx + len('// COSMIC PARTICLES CANVAS ENGINE'):]
    print("Cleaned up showcase script!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully!")
