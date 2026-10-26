import sys

# Load current index.html
with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# -------------------------------------------------------------
# 1. FIX THE CARDS BACKDROP
# Remove individual translateY entrance that caused detached backdrops
# Clean up .foundation-card CSS: remove backdrop-filter and gradient
# -------------------------------------------------------------

old_entrance_cascade = '''/* Individual card subtle entrance cascade */
.foundation-section .foundation-card {
  opacity: 0;
  transform: translateY(24px);
  transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.8s ease, border-color 0.35s ease, box-shadow 0.35s ease, background 0.35s ease;
}

.foundation-section.is-in-view .foundation-card:nth-child(1) { transition-delay: 0.20s; opacity: 1; transform: translateY(0); }
.foundation-section.is-in-view .foundation-card:nth-child(2) { transition-delay: 0.28s; opacity: 1; transform: translateY(0); }
.foundation-section.is-in-view .foundation-card:nth-child(3) { transition-delay: 0.36s; opacity: 1; transform: translateY(0); }
.foundation-section.is-in-view .foundation-card:nth-child(4) { transition-delay: 0.44s; opacity: 1; transform: translateY(0); }
.foundation-section.is-in-view .foundation-card:nth-child(5) { transition-delay: 0.52s; opacity: 1; transform: translateY(0); }'''

new_entrance_cascade = '''/* Cards track moves as a unified viewport unit (prevents backdrop detachment) */
.foundation-section .foundation-card {
  opacity: 1;
  transform: none;
  transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), border-color 0.35s ease, box-shadow 0.35s ease;
}'''

if old_entrance_cascade in html:
    html = html.replace(old_entrance_cascade, new_entrance_cascade, 1)
    print("Replaced old_entrance_cascade successfully!")
else:
    print("WARNING: old_entrance_cascade not found directly, will check alternatives")

old_card_css = '''.foundation-card {
  flex: 0 0 clamp(240px, 24vw, 290px);
  height: clamp(310px, 32vw, 360px);
  border-radius: 22px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.42);
  transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.35s ease, border-color 0.35s ease, background 0.35s ease;
  border: 1px solid rgba(255, 255, 255, 0.14);
  background: linear-gradient(160deg, rgba(255, 255, 255, 0.06) 0%, rgba(255, 255, 255, 0.02) 100%);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  outline: none;
  box-sizing: border-box;
}

.foundation-card:hover {
  transform: translateY(-6px);
  background: linear-gradient(160deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.035) 100%);
  box-shadow: 0 24px 50px rgba(0, 0, 0, 0.55), 0 0 24px rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.4);
}

/* Pure White Luminous Active Card Border */
.foundation-card.is-active {
  border: 1.5px solid #ffffff;
  background: linear-gradient(160deg, rgba(255, 255, 255, 0.15) 0%, rgba(255, 255, 255, 0.045) 100%);
  box-shadow: 
    0 22px 48px rgba(0, 0, 0, 0.58),
    0 0 32px rgba(255, 255, 255, 0.22),
    inset 0 1px 0 rgba(255, 255, 255, 0.45);
  transform: translateY(-4px);
}'''

new_card_css = '''.foundation-card {
  flex: 0 0 clamp(240px, 24vw, 290px);
  height: clamp(310px, 32vw, 360px);
  border-radius: 22px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  border: 1px solid rgba(255, 255, 255, 0.16);
  background: #050811;
  box-shadow: 0 12px 28px rgba(0, 0, 0, 0.42);
  transition: transform 0.35s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.35s ease, border-color 0.35s ease;
  outline: none;
  box-sizing: border-box;
}

.foundation-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 38px rgba(0, 0, 0, 0.55);
  border-color: rgba(255, 255, 255, 0.45);
}

/* Pure White Luminous Active Card Border (No detached backdrop glow) */
.foundation-card.is-active {
  border: 1.5px solid #ffffff;
  box-shadow: 
    0 16px 36px rgba(0, 0, 0, 0.58),
    0 0 18px rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
}'''

if old_card_css in html:
    html = html.replace(old_card_css, new_card_css, 1)
    print("Replaced old_card_css successfully!")
else:
    print("ERROR: old_card_css not found")
    sys.exit(1)

# Also add bottom blend to Section 2 for seamless transition into CTA Footer
old_sec2_end = '''  <!-- Fine Micro-Dither Overlay (Eliminates 8-bit gradient banding lines) -->
  <div class="cinematic-dither-overlay" aria-hidden="true"></div>'''

new_sec2_end = '''  <!-- Fine Micro-Dither Overlay (Eliminates 8-bit gradient banding lines) -->
  <div class="cinematic-dither-overlay" aria-hidden="true"></div>
  <!-- Dedicated Bottom Transition Corridor into Section 3 (Seamless #050811 Blend) -->
  <div class="foundation-bottom-blend" aria-hidden="true"></div>'''

if old_sec2_end in html:
    html = html.replace(old_sec2_end, new_sec2_end, 1)
    print("Added foundation-bottom-blend successfully!")

# -------------------------------------------------------------
# 2. ADD CTA FOOTER STYLES (CSS)
# -------------------------------------------------------------

cta_css = '''
/* ============================================================
   SECTION 3: CTA FOOTER WITH ANIMATED MEADOW DAY
   Seamless Blend, WebGL Wind & Floating Flower Petals Engine
   ============================================================ */
.foundation-bottom-blend {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 240px;
  background: linear-gradient(
    180deg,
    transparent 0px,
    rgba(5, 8, 17, 0.4) 70px,
    rgba(5, 8, 17, 0.82) 140px,
    #050811 200px,
    #050811 240px
  );
  pointer-events: none;
  z-index: 5;
}

.cta-footer-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  margin-top: 0;
  padding: clamp(90px, 12vh, 140px) clamp(24px, 5vw, 64px) clamp(36px, 5vh, 56px);
  box-sizing: border-box;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  color: #ffffff;
  z-index: 20;
  background: #050811;
}

/* Animated Meadow Stage Canvas Wrap */
.meadow-stage {
  position: absolute;
  inset: 0;
  overflow: hidden;
  z-index: 0;
}

.meadow-stage canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center bottom;
  display: block;
}

/* Top Seamless Blend from Section 2 into Meadow */
.meadow-top-blend {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 280px;
  background: linear-gradient(
    180deg,
    #050811 0px,
    #050811 70px,
    rgba(5, 8, 17, 0.94) 120px,
    rgba(5, 8, 17, 0.75) 170px,
    rgba(5, 8, 17, 0.35) 230px,
    transparent 280px
  );
  pointer-events: none;
  z-index: 4;
}

/* Luminous Ambient Contrast Scrim over Meadow for Editorial Crispness */
.meadow-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(ellipse 75% 65% at 50% 45%, rgba(5, 8, 17, 0.45) 0%, rgba(5, 8, 17, 0.88) 100%),
    linear-gradient(180deg, rgba(5, 8, 17, 0.6) 0%, rgba(5, 8, 17, 0.25) 45%, rgba(5, 8, 17, 0.72) 80%, rgba(5, 8, 17, 0.96) 100%);
  pointer-events: none;
  z-index: 2;
}

/* Main CTA Editorial Container */
.cta-main-container {
  width: 100%;
  max-width: 980px;
  margin: auto auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  position: relative;
  z-index: 10;
  padding: 20px 0;
}

.cta-eyebrow-wrap {
  display: inline-flex;
  align-items: center;
  margin-bottom: 14px;
}

.cta-eyebrow {
  font-family: var(--font-sans);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #ffffff;
  opacity: 0.95;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.7);
}

.cta-headline {
  margin: 10px 0 22px;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(2.8rem, 5.2vw, 4.6rem);
  font-weight: 600;
  line-height: 1.08;
  letter-spacing: -0.02em;
  color: #ffffff;
  text-shadow: 0 4px 28px rgba(0, 0, 0, 0.75);
}

.cta-headline-italic {
  font-style: italic;
  font-weight: 400;
  opacity: 0.96;
}

.cta-description {
  font-family: var(--font-sans);
  font-size: clamp(14px, 1.15vw, 16.5px);
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.94);
  max-width: 720px;
  margin: 0 auto 36px;
  text-shadow: 0 2px 12px rgba(0, 0, 0, 0.75);
}

.cta-actions-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
}

/* Footer Bottom Tier */
.cta-footer-bottom {
  width: 100%;
  max-width: 1360px;
  margin: 0 auto;
  position: relative;
  z-index: 10;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.footer-top-divider {
  width: 100%;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(255, 255, 255, 0.22) 20%,
    rgba(255, 255, 255, 0.35) 50%,
    rgba(255, 255, 255, 0.22) 80%,
    transparent 100%
  );
}

.footer-inner-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 24px;
}

.footer-brand-col {
  display: flex;
  flex-direction: column;
  gap: 6px;
  text-align: left;
}

.footer-brand-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 19px;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: #ffffff;
}

.footer-tagline {
  margin: 0;
  font-family: var(--font-sans);
  font-size: 13px;
  color: rgba(255, 255, 255, 0.75);
}

.footer-legal {
  font-family: var(--font-sans);
  font-size: 12px;
  color: rgba(255, 255, 255, 0.55);
}

.footer-links-col {
  display: flex;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
}

.footer-link,
.footer-link-btn {
  font-family: var(--font-sans);
  font-size: 13px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.82);
  text-decoration: none;
  background: none;
  border: none;
  padding: 0;
  cursor: pointer;
  transition: color 0.2s ease, transform 0.2s ease;
}

.footer-link:hover,
.footer-link-btn:hover {
  color: #ffffff;
  transform: translateY(-1px);
}

.footer-social-col {
  display: flex;
  align-items: center;
  gap: 16px;
}

.footer-social-title {
  font-family: var(--font-sans);
  font-size: 12.5px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.75);
}

.footer-social-icons {
  display: flex;
  align-items: center;
  gap: 10px;
}

@media (max-width: 860px) {
  .footer-inner-row {
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  .footer-brand-col {
    align-items: center;
    text-align: center;
  }
  .footer-links-col {
    justify-content: center;
  }
}
'''

# Insert cta_css before </style>
style_end_tag = '</style>'
idx_style = html.find(style_end_tag)
if idx_style == -1:
    print('ERROR: </style> not found')
    sys.exit(1)

html = html[:idx_style] + cta_css + '\n' + html[idx_style:]
print('Inserted CTA CSS successfully!')

# -------------------------------------------------------------
# 3. ADD CTA FOOTER HTML (SECTION 3)
# -------------------------------------------------------------

cta_html = '''
<!-- ============================================================
     SECTION 3: CTA FOOTER WITH ANIMATED MEADOW DAY
     Interactive WebGL Wind & Floating Petals Engine
     ============================================================ -->
<section id="ctaFooterSection" class="cta-footer-section" aria-label="Join Our Creative Movement">
  <!-- Animated Meadow Stage (WebGL Wind Distortion & 2D Floating Flower Petals) -->
  <div class="meadow-stage" id="meadowStage">
    <img id="meadow-img" alt="Children playing in a flower meadow" src="/images/meadow-day.jpg" style="display:none;" />
    <canvas id="gl-meadow" width="1671" height="941"></canvas>
    <canvas id="c-meadow" width="1671" height="941" class="meadow-petals-canvas" style="pointer-events:none;"></canvas>
  </div>
  
  <!-- Atmospheric Scrim & Top Blend from Section 2 -->
  <div class="meadow-top-blend" aria-hidden="true"></div>
  <div class="meadow-scrim-overlay" aria-hidden="true"></div>
  <div class="cinematic-dither-overlay" aria-hidden="true"></div>

  <!-- Main Hero CTA Content (Centered, Awwwards High-Impact Layout) -->
  <div class="cta-main-container">
    <div class="cta-eyebrow-wrap">
      <span class="cta-eyebrow">— Step Into The Creative Laboratory</span>
    </div>
    
    <h2 class="cta-headline">
      Where Imagination<br>
      <span class="cta-headline-italic">Finds Its Natural Home.</span>
    </h2>

    <p class="cta-description">
      From immersive art classes and private gatherings to equitable scholarships expanding arts education for our schools — join us in celebrating the joy of unconventional creativity.
    </p>

    <!-- Glassmorphic Button Suite -->
    <div class="cta-actions-row">
      <button class="foundation-book-btn" data-modal="eventsModal" aria-label="Book a celebration or event">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
          <line x1="16" y1="2" x2="16" y2="6"></line>
          <line x1="8" y1="2" x2="8" y2="6"></line>
          <line x1="3" y1="10" x2="21" y2="10"></line>
        </svg>
        <span>BOOK AN EXPERIENCE</span>
      </button>

      <button class="foundation-donate-btn" data-modal="donateModal" aria-label="Donate to the Foundation">
        <span class="donate-heart-wrap">
          <svg class="donate-heart-icon" viewBox="0 0 24 24" width="18" height="18">
            <path fill="url(#rainbowHeartSection2)" d="M 12 21.35 l -1.45 -1.32 C 5.4 15.36 2 12.28 2 8.5 C 2 5.42 4.42 3 7.5 3 c 1.74 0 3.41 0.81 4.5 2.09 C 13.09 3.81 14.76 3 16.5 3 c 3.08 0 5.5 2.42 5.5 5.5 c 0 3.78 -3.4 6.86 -8.55 11.54 L 12 21.35 z"/>
          </svg>
        </span>
        <span>DONATE &amp; SUPPORT</span>
      </button>

      <button class="foundation-offerings-btn" data-modal="classesModal" aria-label="Explore studio workshops">
        <span>EXPLORE CLASSES &rarr;</span>
      </button>
    </div>
  </div>

  <!-- Polished Footer Bottom Tier (Branding, Legal, Links & Socials) -->
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
  </footer>
</section>
'''

# Insert cta_html after </section> of curatedSection
curated_end_tag = '</section>'
idx_curated = html.find('id="curatedSection"')
if idx_curated == -1:
    print('ERROR: id="curatedSection" not found')
    sys.exit(1)

idx_curated_close = html.find(curated_end_tag, idx_curated)
if idx_curated_close == -1:
    print('ERROR: curatedSection close tag not found')
    sys.exit(1)

idx_insert_html = idx_curated_close + len(curated_end_tag)
html = html[:idx_insert_html] + '\n' + cta_html + '\n' + html[idx_insert_html:]
print('Inserted CTA HTML successfully!')

# -------------------------------------------------------------
# 4. ADD MEADOW DAY ENGINE SCRIPT (WEBGL + FLOATING PETALS)
# -------------------------------------------------------------

meadow_js = '''
// ============================================================
// SECTION 3: MEADOW DAY ANIMATED ENGINE (WEBGL WIND & PETALS)
// ============================================================
(function(){
  var img = document.getElementById('meadow-img');
  var glCanvas = document.getElementById('gl-meadow');
  var petalsCanvas = document.getElementById('c-meadow');
  var isRunning = false;
  var isInitialized = false;
  var rafId = null;

  var gl = null;
  var ut = null;
  var ctx2d = null;
  var ps = [];
  var t0 = 0;
  var last = 0;

  function initGL() {
    if (!glCanvas || !img) return false;
    gl = glCanvas.getContext('webgl', { alpha: false, depth: false, antialias: false, powerPreference: 'low-power' });
    if (!gl) return false;

    var vs = 'attribute vec2 a;varying vec2 v;void main(){v=vec2(a.x*.5+.5,.5-a.y*.5);gl_Position=vec4(a,0.,1.);}';
    var fs = 'precision highp float;uniform sampler2D u;uniform float t;varying vec2 v;' +
      'float B(vec2 p,vec2 c,vec2 r){vec2 d=(p-c)/r;return exp(-dot(d,d));}' +
      'void main(){vec2 p=v,o=vec2(0.);' +
      'float sky=smoothstep(.75,.35,p.y);' +
      'o.x+=(sin(p.y*9.+t*.35+p.x*4.)*.0035+sin(t*.15)*.004)*sky;' +
      'o.y+=cos(p.x*7.+t*.3)*.0025*sky;' +
      'float fl=smoothstep(.76,1.,p.y);' +
      'o.x+=sin(p.x*18.+t*1.5+p.y*12.)*.0045*fl;' +
      'o.y+=sin(p.x*14.-t*1.2)*.002*fl;' +
      'float k=B(p,vec2(.197,.457),vec2(.07,.065));' +
      'o+=vec2(sin(t*1.1),cos(t*1.5))*.007*k;' +
      'float b=B(p,vec2(.694,.579),vec2(.035,.07));' +
      'o+=vec2(sin(t*1.1)*.003,sin(t*1.6)*.007)*b;' +
      'float m=0.;' +
      'vec2 K[8];K[0]=vec2(.21,.7);K[1]=vec2(.326,.7);K[2]=vec2(.422,.7);K[3]=vec2(.506,.71);K[4]=vec2(.568,.73);K[5]=vec2(.727,.71);K[6]=vec2(.799,.71);K[7]=vec2(.9,.76);' +
      'for(int i=0;i<8;i++){vec2 d=(p-K[i])/vec2(.034,.085);m=max(m,exp(-dot(d,d)*1.5));}' +
      'o*=1.-clamp(m*1.3,0.,1.);' +
      'vec4 col=texture2D(u,p+o);' +
      'col.rgb+=.05*sky*(sin(p.x*5.-t*.4+p.y*3.)*.5+.5)*vec3(1.,.95,.85);' +
      'col.rgb+=.07*fl*pow(sin(p.x*60.+t*2.)*sin(p.y*50.-t*1.7)*.5+.5,8.);' +
      'gl_FragColor=col;}';

    function compileSh(type, src) {
      var s = gl.createShader(type);
      gl.shaderSource(s, src);
      gl.compileShader(s);
      return s;
    }

    var pr = gl.createProgram();
    gl.attachShader(pr, compileSh(gl.VERTEX_SHADER, vs));
    gl.attachShader(pr, compileSh(gl.FRAGMENT_SHADER, fs));
    gl.linkProgram(pr);
    gl.useProgram(pr);

    var bf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, bf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);

    var al = gl.getAttribLocation(pr, 'a');
    gl.enableVertexAttribArray(al);
    gl.vertexAttribPointer(al, 2, gl.FLOAT, false, 0, 0);

    var tx = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, tx);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, img);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);

    ut = gl.getUniformLocation(pr, 't');

    // Setup 2D Petals Canvas
    if (petalsCanvas) {
      ctx2d = petalsCanvas.getContext('2d');
      var cols = ['#ffd6e7', '#fff3b0', '#ffffff', '#ffc9a8'];
      ps = [];
      for (var i = 0; i < 45; i++) {
        ps.push({
          x: Math.random() * 1671,
          y: 280 + Math.random() * 650,
          s: 3 + Math.random() * 4,
          v: 20 + Math.random() * 40,
          ph: Math.random() * 6.28,
          c: cols[i % 4],
          r: Math.random() * 6
        });
      }
    }

    t0 = performance.now();
    last = t0;
    isInitialized = true;
    return true;
  }

  function render(now) {
    if (!isRunning || !gl) return;
    var t = (now - t0) / 1000;
    var dt = Math.min(0.05, (now - last) / 1000);
    last = now;

    // Render WebGL Wind Distortion
    gl.viewport(0, 0, 1671, 941);
    gl.uniform1f(ut, t);
    gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);

    // Render 2D Floating Petals
    if (ctx2d) {
      ctx2d.clearRect(0, 0, 1671, 941);
      for (var j = 0; j < ps.length; j++) {
        var q = ps[j];
        q.x += q.v * dt;
        q.y += Math.sin(t * 1.2 + q.ph) * 14 * dt - 4 * dt;
        if (q.x > 1700) {
          q.x = -10;
          q.y = 280 + Math.random() * 650;
        }
        ctx2d.save();
        ctx2d.translate(q.x, q.y);
        ctx2d.rotate(q.r + t * 1.5);
        ctx2d.globalAlpha = 0.8;
        ctx2d.fillStyle = q.c;
        ctx2d.beginPath();
        ctx2d.ellipse(0, 0, q.s, q.s * 0.5, 0, 0, 6.283);
        ctx2d.fill();
        ctx2d.restore();
      }
    }

    rafId = requestAnimationFrame(render);
  }

  function start() {
    if (!isInitialized) {
      if (!img.complete) {
        img.onload = function() {
          if (initGL()) start();
        };
        return;
      }
      if (!initGL()) return;
    }
    if (!isRunning) {
      isRunning = true;
      last = performance.now();
      rafId = requestAnimationFrame(render);
    }
  }

  function stop() {
    if (isRunning) {
      isRunning = false;
      if (rafId) {
        cancelAnimationFrame(rafId);
        rafId = null;
      }
    }
  }

  window.meadowEngine = {
    start: start,
    stop: stop
  };

  // IntersectionObserver: automatically start WebGL loop when Section 3 scrolls into view
  var ctaSec = document.getElementById('ctaFooterSection');
  if (ctaSec && 'IntersectionObserver' in window) {
    var ctaObserver = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          start();
        } else {
          stop();
        }
      });
    }, { threshold: 0.05 });
    ctaObserver.observe(ctaSec);
  } else {
    start();
  }

  // Smooth scroll links inside footer
  var fHome = document.getElementById('footerLinkHome');
  var fCurated = document.getElementById('footerLinkCurated');
  if (fHome) {
    fHome.addEventListener('click', function(e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }
  if (fCurated) {
    fCurated.addEventListener('click', function(e) {
      e.preventDefault();
      var cur = document.getElementById('curatedSection');
      if (cur) cur.scrollIntoView({ behavior: 'smooth' });
    });
  }
})();
'''

# Insert meadow_js before </body>
body_end_tag = '</body>'
idx_body = html.rfind(body_end_tag)
if idx_body == -1:
    print('ERROR: </body> not found')
    sys.exit(1)

html = html[:idx_body] + '<script>\n' + meadow_js + '\n</script>\n' + html[idx_body:]
print('Inserted Meadow JS successfully!')

# Write back to index.html
with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Full update successfully written to /home/user/index.html!')
