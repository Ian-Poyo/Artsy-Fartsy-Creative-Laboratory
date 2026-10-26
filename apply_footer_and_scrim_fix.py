import sys

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# =============================================================
# 1. TONE DOWN HERO BOTTOM SCRIM & HIDE DURING CINEMATIC BUILDUP
# =============================================================
old_hero_scrim_css = '''/* Bottom Scrim: Continuous velvety gradient reaching 100% solid #050811 at 82% */
.hero-bottom-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    transparent 0%,
    transparent 36%,
    rgba(5, 8, 17, 0.05) 46%,
    rgba(5, 8, 17, 0.16) 54%,
    rgba(5, 8, 17, 0.35) 62%,
    rgba(5, 8, 17, 0.60) 70%,
    rgba(5, 8, 17, 0.85) 78%,
    #050811 84%,
    #050811 100%
  );
  pointer-events: none;
  z-index: 10;
}'''

new_hero_scrim_css = '''/* Bottom Scrim: Toned-down, soft cinematic gradient. 
   Hidden during buildup, revealed smoothly after buildup finishes */
.hero-bottom-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    transparent 0%,
    transparent 48%,
    rgba(5, 8, 17, 0.06) 64%,
    rgba(5, 8, 17, 0.18) 76%,
    rgba(5, 8, 17, 0.38) 86%,
    rgba(5, 8, 17, 0.65) 94%,
    #050811 100%
  );
  pointer-events: none;
  z-index: 10;
  opacity: 0;
  visibility: hidden;
  transition: opacity 1.35s cubic-bezier(0.16, 1, 0.3, 1) 0.35s, visibility 1.35s;
  will-change: opacity;
}

body.layout-active .hero-bottom-scrim {
  opacity: 1;
  visibility: visible;
}

/* Dither overlay in hero also fades in after buildup */
.hero-section .cinematic-dither-overlay {
  opacity: 0;
  visibility: hidden;
  transition: opacity 1.35s cubic-bezier(0.16, 1, 0.3, 1) 0.35s, visibility 1.35s;
}

body.layout-active .hero-section .cinematic-dither-overlay {
  opacity: 0.038;
  visibility: visible;
}'''

if old_hero_scrim_css in html:
    html = html.replace(old_hero_scrim_css, new_hero_scrim_css, 1)
    print("Updated hero-bottom-scrim CSS successfully!")
else:
    print("ERROR: old_hero_scrim_css not found")
    sys.exit(1)

# =============================================================
# 2. UPDATE FOOTER IN SECTION 3: ADD FIND US, CONTACT US, MESSAGE US
#    AND REMOVE "& Foundation" & "All rights reserved. 501(c)(3) Nonprofit."
# =============================================================

# Add CSS for Contact / Location Grid
contact_css = '''
/* --- CTA Footer Contact Grid (Find Us, Contact Us, Message Us from image-2.png) --- */
.footer-contact-grid {
  width: 100%;
  max-width: 1240px;
  margin: 32px auto 48px;
  display: grid;
  grid-template-columns: 1fr 1.15fr;
  gap: clamp(24px, 4vw, 48px);
  position: relative;
  z-index: 10;
  box-sizing: border-box;
}

.footer-contact-card {
  background: rgba(5, 10, 24, 0.72);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 24px;
  padding: clamp(28px, 3.5vw, 42px);
  box-sizing: border-box;
  text-align: left;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
  display: flex;
  flex-direction: column;
}

/* Card Section Header with Hand-Drawn Yellow Squiggle */
.contact-card-header {
  position: relative;
  display: inline-block;
  margin-bottom: 16px;
}

.contact-section-title {
  margin: 0;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(1.8rem, 2.5vw, 2.2rem);
  font-weight: 600;
  letter-spacing: -0.01em;
  color: #ffffff;
  display: inline-block;
}

.yellow-squiggle {
  display: block;
  width: 100%;
  height: 8px;
  margin-top: 4px;
}

/* Find Us Card Details */
.contact-card-details {
  margin-bottom: 24px;
}

.building-note {
  margin: 0 0 6px 0;
  font-family: var(--font-sans);
  font-size: 15px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.88);
}

.street-address {
  margin: 0;
  font-family: var(--font-sans);
  font-size: 15px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.95);
  font-weight: 600;
}

/* Map Embed Container */
.footer-map-embed {
  margin-top: auto;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.16);
  background: rgba(0, 0, 0, 0.35);
  position: relative;
}

.map-direct-link {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px 16px;
  background: rgba(255, 255, 255, 0.08);
  color: #ffffff;
  font-family: var(--font-sans);
  font-size: 12.5px;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-decoration: none;
  transition: background 0.2s ease, color 0.2s ease;
}

.map-direct-link:hover {
  background: rgba(255, 255, 255, 0.18);
  color: #f59e0b;
}

/* Contact Us & Message Us Card */
.footer-message-card {
  gap: 28px;
}

.contact-links-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.contact-info-link {
  font-family: var(--font-sans);
  font-size: clamp(15px, 1.2vw, 17px);
  color: #ffffff;
  font-weight: 600;
  text-decoration: underline;
  text-decoration-color: rgba(255, 255, 255, 0.45);
  text-underline-offset: 4px;
  transition: color 0.2s ease, text-decoration-color 0.2s ease;
}

.contact-info-link:hover {
  color: #f59e0b;
  text-decoration-color: #f59e0b;
}

/* Message Us Form */
.footer-contact-form {
  display: flex;
  flex-direction: column;
  gap: 18px;
  width: 100%;
}

.form-row-duo {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 18px;
}

.form-field-wrap {
  display: flex;
  flex-direction: column;
  gap: 6px;
  text-align: left;
}

.form-field-wrap label {
  font-family: var(--font-sans);
  font-size: 13px;
  color: rgba(255, 255, 255, 0.88);
  font-weight: 500;
}

.form-field-wrap label .req {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.55);
}

.form-field-wrap input,
.form-field-wrap textarea {
  background: rgba(255, 255, 255, 0.05);
  border: none;
  border-bottom: 1.5px solid rgba(255, 255, 255, 0.35);
  border-radius: 4px 4px 0 0;
  padding: 8px 10px;
  font-family: var(--font-sans);
  font-size: 14px;
  color: #ffffff;
  outline: none;
  transition: border-bottom-color 0.25s ease, background 0.25s ease;
  box-sizing: border-box;
}

.form-field-wrap input:focus,
.form-field-wrap textarea:focus {
  border-bottom-color: #f59e0b;
  background: rgba(255, 255, 255, 0.1);
}

.form-submit-row {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 16px;
  margin-top: 6px;
}

.contact-send-btn {
  background: #000000;
  color: #ffffff;
  border: 1.5px solid rgba(255, 255, 255, 0.35);
  border-radius: 9999px;
  padding: 10px 32px;
  font-family: var(--font-sans);
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.05em;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
}

.contact-send-btn:hover {
  background: #ffffff;
  color: #000000;
  border-color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255, 255, 255, 0.25);
}

.contact-send-btn:active {
  transform: scale(0.96);
}

.contact-form-feedback {
  font-family: var(--font-sans);
  font-size: 13px;
  color: #10b981;
  font-weight: 500;
}

@media (max-width: 900px) {
  .footer-contact-grid {
    grid-template-columns: 1fr;
  }
}
@media (max-width: 540px) {
  .form-row-duo {
    grid-template-columns: 1fr;
  }
}
'''

# Insert contact_css into <style>
idx_style = html.find('</style>')
if idx_style == -1:
    print('ERROR: </style> not found')
    sys.exit(1)

html = html[:idx_style] + contact_css + '\n' + html[idx_style:]
print("Inserted contact_css successfully!")

# Replace the footer HTML inside Section 3
old_footer_html = '''  <!-- Polished Footer Bottom Tier (Branding, Legal, Links & Socials) -->
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
  </footer>'''

new_footer_html = '''  <!-- Interactive Contact & Location Grid (Find Us, Contact Us, Message Us from image-2.png) -->
  <div class="footer-contact-grid">
    
    <!-- Left Card: Find Us & Map -->
    <div class="footer-contact-card footer-find-card">
      <div class="contact-card-header">
        <h3 class="contact-section-title">Find Us</h3>
        <svg class="yellow-squiggle" viewBox="0 0 100 12" preserveAspectRatio="none">
          <path d="M 0 6 Q 25 1 50 6 T 100 6" stroke="#f59e0b" stroke-width="3" fill="none" stroke-linecap="round"/>
        </svg>
      </div>
      <div class="contact-card-details">
        <p class="building-note">(In the Turner Jeffrey Building)</p>
        <p class="street-address">1030 South Rangeline Road, Suite #220<br>Carmel, IN 46032</p>
      </div>

      <!-- Map Embed (Interactive Carmel, IN location) -->
      <div class="footer-map-embed">
        <iframe 
          src="https://maps.google.com/maps?q=1030+South+Rangeline+Road,+Suite+220,+Carmel,+IN+46032&t=&z=15&ie=UTF8&iwloc=&output=embed" 
          width="100%" 
          height="200" 
          style="border:0; display:block;" 
          allowfullscreen="" 
          loading="lazy" 
          referrerpolicy="no-referrer-when-downgrade"
          title="Artsy Fartsy Location in Carmel, IN">
        </iframe>
        <a href="https://maps.google.com/?q=1030+South+Rangeline+Road,+Suite+220,+Carmel,+IN+46032" target="_blank" rel="noopener noreferrer" class="map-direct-link">
          <span>Open in Google Maps &rarr;</span>
        </a>
      </div>
    </div>

    <!-- Right Card: Contact Us & Message Us Form -->
    <div class="footer-contact-card footer-message-card">
      <!-- Contact Info -->
      <div class="contact-block">
        <div class="contact-card-header">
          <h3 class="contact-section-title">Contact Us</h3>
          <svg class="yellow-squiggle" viewBox="0 0 100 12" preserveAspectRatio="none">
            <path d="M 0 6 Q 25 1 50 6 T 100 6" stroke="#f59e0b" stroke-width="3" fill="none" stroke-linecap="round"/>
          </svg>
        </div>
        <div class="contact-links-list">
          <a href="tel:3176909435" class="contact-info-link">(317) 690-9435</a>
          <a href="mailto:artsyfartsycreativelab@gmail.com" class="contact-info-link">artsyfartsycreativelab@gmail.com</a>
        </div>
      </div>

      <!-- Message Us Form -->
      <div class="message-block">
        <div class="contact-card-header">
          <h3 class="contact-section-title">Message Us</h3>
          <svg class="yellow-squiggle" viewBox="0 0 100 12" preserveAspectRatio="none">
            <path d="M 0 6 Q 25 1 50 6 T 100 6" stroke="#f59e0b" stroke-width="3" fill="none" stroke-linecap="round"/>
          </svg>
        </div>
        <form class="footer-contact-form" id="footerContactForm">
          <div class="form-row-duo">
            <div class="form-field-wrap">
              <label for="contactFirstName">First Name <span class="req">(required)</span></label>
              <input type="text" id="contactFirstName" name="firstName" required autocomplete="given-name" />
            </div>
            <div class="form-field-wrap">
              <label for="contactLastName">Last Name <span class="req">(required)</span></label>
              <input type="text" id="contactLastName" name="lastName" required autocomplete="family-name" />
            </div>
          </div>
          <div class="form-field-wrap">
            <label for="contactEmail">Email <span class="req">(required)</span></label>
            <input type="email" id="contactEmail" name="email" required autocomplete="email" />
          </div>
          <div class="form-field-wrap">
            <label for="contactMessage">Message</label>
            <textarea id="contactMessage" name="message" rows="3"></textarea>
          </div>
          <div class="form-submit-row">
            <div class="contact-form-feedback" id="contactFormFeedback"></div>
            <button type="submit" class="contact-send-btn" id="contactSendBtn">
              <span>Send</span>
            </button>
          </div>
        </form>
      </div>
    </div>

  </div>

  <!-- Polished Footer Bottom Tier (Clean Brand & Navigation without 501(c)(3) or & Foundation) -->
  <footer class="cta-footer-bottom">
    <div class="footer-top-divider"></div>
    <div class="footer-inner-row">
      <!-- Left: Logo & Clean Copyright (Removed & Foundation and 501(c)(3)) -->
      <div class="footer-brand-col">
        <div class="footer-brand-title">Artsy Fartsy Studio</div>
        <p class="footer-tagline">An experimental laboratory where curiosity leads and everyone creates.</p>
        <span class="footer-legal">© 2026 Artsy Fartsy Studio.</span>
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
  </footer>'''

if old_footer_html in html:
    html = html.replace(old_footer_html, new_footer_html, 1)
    print("Replaced footer HTML successfully!")
else:
    print("ERROR: old_footer_html not found")
    sys.exit(1)

# Add contact form submission JS handler
form_js = '''
  // Interactive Message Us Form Submission Handler
  var contactForm = document.getElementById('footerContactForm');
  var formFeedback = document.getElementById('contactFormFeedback');
  if (contactForm && formFeedback) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      var fName = document.getElementById('contactFirstName').value.trim();
      var email = document.getElementById('contactEmail').value.trim();
      if (!fName || !email) {
        formFeedback.style.color = '#f59e0b';
        formFeedback.textContent = 'Please fill out all required fields.';
        return;
      }
      var sendBtn = document.getElementById('contactSendBtn');
      if (sendBtn) {
        sendBtn.disabled = true;
        sendBtn.innerHTML = '<span>Sending...</span>';
      }
      setTimeout(function() {
        formFeedback.style.color = '#10b981';
        formFeedback.textContent = 'Message sent! Thank you, ' + fName + '. We will be in touch soon.';
        contactForm.reset();
        if (sendBtn) {
          sendBtn.disabled = false;
          sendBtn.innerHTML = '<span>Send</span>';
        }
      }, 700);
    });
  }
'''

idx_script_end = html.rfind('})();\n</script>')
if idx_script_end != -1:
    html = html[:idx_script_end] + form_js + '\n' + html[idx_script_end:]
    print("Inserted form JS handler successfully!")
else:
    print("WARNING: ()( );</script> anchor not found, inserting before </body>")
    idx_b = html.rfind('</body>')
    html = html[:idx_b] + '<script>' + form_js + '</script>\n' + html[idx_b:]

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated /home/user/index.html successfully!")
