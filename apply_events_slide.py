import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Card 2 in Section 2 HTML
old_card2 = '''          <!-- Card 2: Teacher Development -->
          <article class="foundation-card" data-index="2" tabindex="0" role="button" aria-label="Teacher Development">
            <img class="card-bg-img" src="/images/card-birthday.webp" alt="Teacher Development" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>K-12 Educators</span>
              </div>
              <h3 class="card-main-heading">TEACHER DEVELOPMENT</h3>
            </div>
          </article>'''

new_card2 = '''          <!-- Card 2: Birthday Parties & Events (Gala Celebration Photo) -->
          <article class="foundation-card" data-index="2" tabindex="0" role="button" aria-label="Birthday Parties & Events">
            <img class="card-bg-img" src="/images/foundation-events-party.jpg" alt="Birthday Parties & Events" loading="lazy">
            <div class="card-gradient-scrim"></div>
            <div class="card-content-overlay">
              <div class="card-category-line">
                <span class="dash">—</span>
                <span>Milestone Gatherings</span>
              </div>
              <h3 class="card-main-heading">BIRTHDAY PARTIES & EVENTS</h3>
            </div>
          </article>'''

if old_card2 in content:
    content = content.replace(old_card2, new_card2, 1)
    print("1. Card 2 HTML updated!")
else:
    print("WARNING: Could not find old Card 2 HTML!")

# 2. Add eventsModal right before donateModal if not present
events_modal_html = '''<!-- Birthday & Private Events Modal -->
<div class="modal-overlay" id="eventsModal">
  <div class="modal-card">
    <button class="modal-close-btn" data-close aria-label="Close dialog">✕</button>
    <h2 class="modal-title">Birthday Parties & Events</h2>
    <div class="modal-subtitle">Milestone Celebrations & Private Atelier Gatherings</div>
    <div class="modal-body">
      <p>
        Celebrate life’s most cherished moments in our luminous studio atelier. We curate all-inclusive creative birthday parties, private soirées, milestone debuts, and celebratory gatherings with custom art projects, atmospheric lighting, and festive hospitality.
      </p>
      <div class="info-card">
        <h4>Color Magic Birthday Packages</h4>
        <p>Private studio access, custom color-splatter canvases, dedicated artist host, and personalized favors for all guests.</p>
      </div>
      <div class="info-card">
        <h4>Private Twilight Celebrations</h4>
        <p>Evening cocktail receptions, candlelit art soirées, curated music, and bespoke collaborative art keepsakes.</p>
      </div>
      <div class="info-card">
        <h4>Custom Event Design</h4>
        <p>Full floral arrangements, gourmet catering coordination, ambient lighting, and personalized themes tailored to your vision.</p>
      </div>
    </div>
  </div>
</div>

'''

if 'id="eventsModal"' not in content:
    pos_donate = content.find('<!-- Donate Modal -->')
    if pos_donate != -1:
        content = content[:pos_donate] + events_modal_html + content[pos_donate:]
        print("2. eventsModal added successfully!")
    else:
        print("WARNING: Could not find Donate Modal position!")
else:
    print("2. eventsModal already present.")

# 3. Replace JS controller for Section 2
with open('/home/user/test_events_slider.py', 'r') as f:
    txt = f.read()
m_j = re.search(r"js = '''(.*?)'''", txt, re.DOTALL)
new_js = m_j.group(1).strip()

pos_j_start = content.find('// ============================================================\n// FRIENDS OF ARTSY FARTSY FOUNDATION SLIDER CONTROLLER')
pos_j_end = content.find('// ============================================================\n// NAVIGATION & PERFORMANCE CONTROLLER (HERO + CURATED)')
if pos_j_start != -1 and pos_j_end != -1:
    content = content[:pos_j_start] + new_js + '\n\n' + content[pos_j_end:]
    print("3. JS updated successfully!")
else:
    print("WARNING: Could not find JS block!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS: index.html fully updated with Birthday Parties & Events slide!")
