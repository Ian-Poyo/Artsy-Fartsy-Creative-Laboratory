with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove Contact CSS
css_start = content.find('/* --- CTA Footer Contact Section (Faithful 1:1 match to image-2.png) --- */')
if css_start == -1:
    css_start = content.find('/* --- CTA Footer Contact Grid')

css_end = content.find('</style>', css_start) if css_start != -1 else -1

if css_start != -1 and css_end != -1:
    content = content[:css_start] + content[css_end:]
    print("Removed contact CSS successfully!")
else:
    print(f"Could not find contact CSS: {css_start}, {css_end}")

# 2. Revert Footer HTML inside Section 3
old_footer_exact = """  <!-- Polished Footer Bottom Tier (Branding, Legal, Links & Socials) -->
  <footer class="cta-footer-bottom">
    <div class="footer-top-divider"></div>
    <div class="footer-inner-row">
      <!-- Left: Logo & Legal -->
      <div class="footer-brand-col">
        <div class="footer-brand-title">Artsy Fartsy Studio &amp; Foundation</div>
        <p class="footer-tagline">An experimental laboratory where curiosity leads and everyone creates.</p>
        <span class="footer-legal">© 2026 Friends of Artsy Fartsy Foundation. All rights reserved. 501(c)(3) Nonprofit.</span>
      </div>

      <!-- Center: Quick Nav Links -->
      <div class="footer-links-col">
        <a href="#hero-section" class="footer-link" id="footerLinkHome">Home</a>
        <a href="#curatedSection" class="footer-link" id="footerLinkCurated">Experiences</a>
        <button type="button" class="footer-link-btn" data-modal="classesModal">Studio Classes</button>
        <button type="button" class="footer-link-btn" data-modal="eventsModal">Private Events</button>
        <button type="button" class="footer-link-btn" data-modal="donateModal">Support Mission</button>
      </div>

      <!-- Right: Social Circle Links -->
      <div class="footer-social-col">
        <div class="footer-social-title">Follow the Magic</div>
        <div class="footer-social-icons">
          <a href="https://instagram.com/artsyfartsystudio" target="_blank" rel="noopener noreferrer" class="social-circle" data-tooltip="Instagram" aria-label="Instagram">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
              <circle cx="12" cy="12" r="4"></circle>
              <circle cx="17.5" cy="6.5" r="1" fill="currentColor"></circle>
            </svg>
          </a>
          <a href="https://facebook.com/artsyfartsystudio" target="_blank" rel="noopener noreferrer" class="social-circle" data-tooltip="Facebook" aria-label="Facebook">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
            </svg>
          </a>
        </div>
      </div>
    </div>
  </footer>"""

# Target start of contact section or footer in Section 3
pos_grid = content.find('<!-- Interactive Contact & Location Section (1:1 with image-2.png) -->')
if pos_grid == -1:
    pos_grid = content.find('<div class="footer-contact-grid">')

pos_sec_end = content.find('</section>', pos_grid)

if pos_grid != -1 and pos_sec_end != -1:
    content = content[:pos_grid] + old_footer_exact + '\n' + content[pos_sec_end:]
    print("Reverted footer HTML successfully!")
else:
    print(f"Could not find footer HTML boundaries: {pos_grid}, {pos_sec_end}")

# 3. Remove Footer Message Form Script Handler if present
js_marker = '// Footer Message Us Form Submission Handler'
pos_js = content.find(js_marker)
if pos_js != -1:
    pos_js_end = content.find('})();', pos_js)
    if pos_js_end != -1:
        content = content[:pos_js] + content[pos_js_end:]
        print("Removed footer form JS handler successfully!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html!")
