with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_tier_lower = '''<div class="tier-lower" id="tierLower">
      <div class="tier-lower-left">
        <span class="bottom-quote">Clarity begins with a good question.</span>
      </div>

      <div class="tier-lower-right">
        <p class="editorial-p1">
          Discovery doesn't always begin with knowing — it starts with questions. Context that guides understanding forward.
        </p>
        <p class="editorial-p2">
          Artsy Fartsy is your companion for deeper insight. A calm space for asking better questions and drawing thoughtful insight. Less noise. More meaning.
        </p>
      </div>
    </div>'''

new_tier_lower = '''<div class="tier-lower" id="tierLower">
      <div class="tier-lower-left">
        <span class="bottom-quote">Unleash Creativity Today</span>
      </div>

      <div class="tier-lower-right">
        <h3 class="editorial-eyebrow">A LAB FOR THE UNCONVENTIONAL</h3>
        <p class="editorial-lead">For ideas that refuse to stay inside the lines.</p>
        <p class="editorial-body">
          An experimental space where imagination runs wild, strange ideas take shape, and creativity has no single direction.
        </p>
        <p class="editorial-tagline">Make a mess. Find the magic.</p>
      </div>
    </div>'''

if old_tier_lower not in content:
    raise ValueError("old_tier_lower not matched")

content = content.replace(old_tier_lower, new_tier_lower, 1)

# Update CSS for tier-lower-right
old_css_frag = '''.bottom-quote {
  font-family: var(--font-sans);
  font-size: 12.5px;
  font-weight: 400;
  color: rgba(255, 255, 255, 0.68);
  letter-spacing: 0.015em;
  text-shadow: none;
}

/* Tier Lower Right: Paragraphs aligned with Start Exploring button */
.tier-lower-right {
  display: flex;
  flex-direction: column;
  gap: 12px;
  pointer-events: auto;
}

.editorial-p1 {
  margin: 0;
  font-family: var(--font-sans);
  font-size: clamp(12.5px, 1.05vw, 13.5px);
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.88);
  letter-spacing: 0.005em;
  text-shadow: none;
}

.editorial-p2 {
  margin: 0;
  font-family: var(--font-sans);
  font-size: clamp(12px, 0.98vw, 13px);
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.7);
  letter-spacing: 0.005em;
  text-shadow: none;
}'''

new_css_frag = '''.bottom-quote {
  font-family: var(--font-sans);
  font-size: 13px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.88);
  letter-spacing: 0.015em;
  text-shadow: none;
}

/* Tier Lower Right: Laboratory Manifesto Copy */
.tier-lower-right {
  display: flex;
  flex-direction: column;
  gap: 8px;
  pointer-events: auto;
}

.editorial-eyebrow {
  margin: 0;
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.09em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.96);
  text-shadow: none;
}

.editorial-lead {
  margin: 0;
  font-family: var(--font-sans);
  font-size: clamp(12.5px, 1.05vw, 13.5px);
  font-weight: 400;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.88);
  letter-spacing: 0.005em;
  text-shadow: none;
}

.editorial-body {
  margin: 0;
  font-family: var(--font-sans);
  font-size: clamp(12px, 0.98vw, 13px);
  font-weight: 300;
  line-height: 1.55;
  color: rgba(255, 255, 255, 0.74);
  letter-spacing: 0.005em;
  text-shadow: none;
}

.editorial-tagline {
  margin: 2px 0 0 0;
  font-family: var(--font-sans);
  font-size: clamp(12px, 0.98vw, 13px);
  font-weight: 600;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.94);
  letter-spacing: 0.015em;
  text-shadow: none;
}'''

if old_css_frag not in content:
    raise ValueError("old_css_frag not matched")

content = content.replace(old_css_frag, new_css_frag, 1)

# Clean up mobile media query
content = content.replace('.editorial-p2 {\n    display: none;\n  }', '')

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated manifesto copy and quote successfully!")
