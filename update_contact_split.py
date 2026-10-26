import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace contact CSS with exact image-2.png match
new_contact_css = """/* --- CTA Footer Contact Section (Faithful 1:1 match to image-2.png) --- */
.footer-contact-grid {
  width: 100%;
  max-width: 1200px;
  margin: 40px auto 56px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  border-radius: 24px;
  overflow: hidden;
  position: relative;
  z-index: 10;
  box-sizing: border-box;
  box-shadow: 0 24px 64px rgba(0, 0, 0, 0.45), 0 2px 8px rgba(0, 0, 0, 0.2);
}

/* Left Pane: Soft Sky Blue (#8ab8db) */
.footer-find-pane {
  background: #8ab8db;
  color: #111827;
  padding: clamp(32px, 4vw, 56px);
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

/* Right Pane: Warm Clean Grey (#e2e2e2) */
.footer-message-pane {
  background: #e2e2e2;
  color: #111827;
  padding: clamp(32px, 4vw, 56px);
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  gap: 36px;
}

/* Section Titles with Organic Yellow Squiggle */
.contact-header-wrap {
  position: relative;
  display: inline-block;
  margin-bottom: 14px;
}

.contact-pane-title {
  margin: 0;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(1.9rem, 2.5vw, 2.3rem);
  font-weight: 500;
  letter-spacing: -0.01em;
  color: #111827;
  line-height: 1.15;
}

.yellow-squiggle {
  display: block;
  margin-top: 3px;
  height: 7px;
}
.yellow-squiggle-find { width: 100px; }
.yellow-squiggle-contact { width: 135px; }
.yellow-squiggle-message { width: 145px; }

/* Left Pane: Address Details */
.find-details-block {
  margin-bottom: 24px;
}

.building-note {
  margin: 0 0 6px 0;
  font-family: var(--font-sans);
  font-size: 15px;
  font-weight: 500;
  color: #1f2937;
}

.street-address {
  margin: 0;
  font-family: var(--font-sans);
  font-size: 15px;
  line-height: 1.5;
  color: #111827;
  font-weight: 500;
}

/* Embedded Google Map */
.footer-map-container {
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
  background: #ffffff;
}

.footer-map-frame {
  width: 100%;
  height: 260px;
  border: 0;
  display: block;
}

/* Right Pane: Contact Links */
.contact-links-stack {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 4px;
}

.contact-clean-link {
  font-family: var(--font-sans);
  font-size: 17px;
  color: #111827;
  font-weight: 500;
  text-decoration: underline;
  text-decoration-color: #111827;
  text-underline-offset: 4px;
  transition: color 0.2s ease, text-decoration-color 0.2s ease;
  display: inline-block;
  width: fit-content;
}

.contact-clean-link:hover {
  color: #b45309;
  text-decoration-color: #b45309;
}

/* Message Us Form */
.message-form-block {
  display: flex;
  flex-direction: column;
}

.footer-clean-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 100%;
}

.form-duo-fields {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.form-input-field {
  display: flex;
  flex-direction: column;
  gap: 4px;
  text-align: left;
}

.form-input-field label {
  font-family: var(--font-sans);
  font-size: 13px;
  color: #374151;
  font-weight: 400;
}

.form-input-field input,
.form-input-field textarea {
  background: transparent;
  border: none;
  border-bottom: 1.5px solid #4b5563;
  border-radius: 0;
  padding: 6px 0;
  font-family: var(--font-sans);
  font-size: 14.5px;
  color: #111827;
  outline: none;
  transition: border-bottom-color 0.2s ease;
  box-sizing: border-box;
}

.form-input-field input:focus,
.form-input-field textarea:focus {
  border-bottom: 2px solid #000000;
}

.form-submit-centered {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-top: 10px;
}

.clean-send-btn {
  background: #000000;
  color: #ffffff;
  border: none;
  border-radius: 9999px;
  padding: 10px 38px;
  font-family: var(--font-sans);
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.02em;
  cursor: pointer;
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), background-color 0.2s ease, box-shadow 0.2s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.clean-send-btn:hover {
  background: #27272a;
  transform: translateY(-1px);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.25);
}

.clean-send-btn:active {
  transform: scale(0.97);
}

.form-status-msg {
  font-family: var(--font-sans);
  font-size: 13px;
  color: #059669;
  font-weight: 500;
  min-height: 18px;
}

@media (max-width: 900px) {
  .footer-contact-grid {
    grid-template-columns: 1fr;
    margin: 32px 16px 48px;
  }
}

@media (max-width: 540px) {
  .form-duo-fields {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  .footer-find-pane,
  .footer-message-pane {
    padding: 28px 20px;
  }
}
"""

# Replace the previous contact CSS block
pattern_css = r'/\* --- CTA Footer Contact Grid \(Find Us, Contact Us, Message Us from image-2\.png\) ---\*/.*?(?=@media \(max-width: 540px\) \{\s*\.form-row-duo \{\s*grid-template-columns: 1fr;\s*\}\s*\})'
# Let's do a more robust string replacement
old_css_start = content.find('/* --- CTA Footer Contact Grid (Find Us, Contact Us, Message Us from image-2.png) --- */')
old_css_end = content.find('/* ============================================================', old_css_start)

if old_css_start != -1 and old_css_end != -1:
    content = content[:old_css_start] + new_contact_css + '\n' + content[old_css_end:]
    print("Replaced CSS successfully!")
else:
    print(f"Could not find CSS boundaries: {old_css_start}, {old_css_end}")

# Now replace the HTML of the contact section
new_html = """  <!-- Interactive Contact & Location Section (1:1 with image-2.png) -->
  <div class="footer-contact-grid">
    
    <!-- Left Pane: Find Us (#8ab8db) -->
    <div class="footer-find-pane">
      <div>
        <div class="contact-header-wrap">
          <h3 class="contact-pane-title">Find Us</h3>
          <svg class="yellow-squiggle yellow-squiggle-find" viewBox="0 0 100 8" preserveAspectRatio="none">
            <path d="M 0 4 Q 25 1 50 4 T 100 4" stroke="#edbd4a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
          </svg>
        </div>
        
        <div class="find-details-block">
          <p class="building-note">(In the Turner Jeffrey Building)</p>
          <p class="street-address">1030 South Rangeline Road, Suite #220<br>Carmel, IN 46032</p>
        </div>
      </div>

      <!-- Google Map Container -->
      <div class="footer-map-container">
        <iframe 
          class="footer-map-frame"
          src="https://maps.google.com/maps?q=1030+South+Rangeline+Road,+Suite+220,+Carmel,+IN+46032&t=&z=15&ie=UTF8&iwloc=&output=embed" 
          allowfullscreen="" 
          loading="lazy" 
          referrerpolicy="no-referrer-when-downgrade"
          title="Artsy Fartsy Studio Location in Carmel, IN">
        </iframe>
      </div>
    </div>

    <!-- Right Pane: Contact Us & Message Us (#e2e2e2) -->
    <div class="footer-message-pane">
      <!-- Contact Us Block -->
      <div>
        <div class="contact-header-wrap">
          <h3 class="contact-pane-title">Contact Us</h3>
          <svg class="yellow-squiggle yellow-squiggle-contact" viewBox="0 0 100 8" preserveAspectRatio="none">
            <path d="M 0 4 Q 25 1 50 4 T 100 4" stroke="#edbd4a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
          </svg>
        </div>
        <div class="contact-links-stack">
          <a href="tel:3176909435" class="contact-clean-link">(317) 690-9435</a>
          <a href="mailto:artsyfartsycreativelab@gmail.com" class="contact-clean-link">artsyfartsycreativelab@gmail.com</a>
        </div>
      </div>

      <!-- Message Us Block -->
      <div class="message-form-block">
        <div class="contact-header-wrap">
          <h3 class="contact-pane-title">Message Us</h3>
          <svg class="yellow-squiggle yellow-squiggle-message" viewBox="0 0 100 8" preserveAspectRatio="none">
            <path d="M 0 4 Q 25 1 50 4 T 100 4" stroke="#edbd4a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
          </svg>
        </div>
        
        <form class="footer-clean-form" id="footerContactForm">
          <div class="form-duo-fields">
            <div class="form-input-field">
              <label for="contactFirstName">First Name (required)</label>
              <input type="text" id="contactFirstName" name="firstName" required autocomplete="given-name" />
            </div>
            <div class="form-input-field">
              <label for="contactLastName">Last Name (required)</label>
              <input type="text" id="contactLastName" name="lastName" required autocomplete="family-name" />
            </div>
          </div>
          
          <div class="form-input-field">
            <label for="contactEmail">Email (required)</label>
            <input type="email" id="contactEmail" name="email" required autocomplete="email" />
          </div>
          
          <div class="form-input-field">
            <label for="contactMessage">Message</label>
            <textarea id="contactMessage" name="message" rows="2"></textarea>
          </div>
          
          <div class="form-submit-centered">
            <button type="submit" class="clean-send-btn" id="contactSendBtn">Send</button>
            <div class="form-status-msg" id="contactFormFeedback"></div>
          </div>
        </form>
      </div>

    </div>

  </div>"""

old_html_start = content.find('<!-- Interactive Contact & Location Grid (Find Us, Contact Us, Message Us from image-2.png) -->')
old_html_end = content.find('<!-- Polished Footer Bottom Tier -->')

if old_html_start != -1 and old_html_end != -1:
    content = content[:old_html_start] + new_html + '\n\n  ' + content[old_html_end:]
    print("Replaced HTML successfully!")
else:
    print(f"Could not find HTML boundaries: {old_html_start}, {old_html_end}")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated index.html!")
