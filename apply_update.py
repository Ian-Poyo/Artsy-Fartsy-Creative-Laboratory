import re

with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Extract embedded fonts
font_matches = re.findall(r'src:\s*url\(data:font/woff2;base64,([^\)]+)\)\s*format\(\'woff2\'\);', orig)
pf_norm = font_matches[0]
pf_ital = font_matches[1]
jak_sans = font_matches[2]

# Extract authentic background WebP from Starry Sky Animation.html
with open('/home/user/uploads/Starry Sky Animation.html', 'r', encoding='utf-8') as f:
    starry_source = f.read()

bg_img = re.search(r'id=\"bg\"[^>]*src=\"(data:image/webp;base64,[^\"]+)\"', starry_source).group(1)

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Artsy Fartsy — Creative Studio</title>
<meta name="description" content="Artsy Fartsy Creative Studio — A calm interface for asking better questions and drawing thoughtful insight.">

<style>
/* Embedded Typography */
@font-face {{
  font-family: 'Playfair Display';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(data:font/woff2;base64,{pf_norm}) format('woff2');
}}

@font-face {{
  font-family: 'Playfair Display';
  font-style: italic;
  font-weight: 400;
  font-display: swap;
  src: url(data:font/woff2;base64,{pf_ital}) format('woff2');
}}

@font-face {{
  font-family: 'Plus Jakarta Sans';
  font-style: normal;
  font-weight: 400 700;
  font-display: swap;
  src: url(data:font/woff2;base64,{jak_sans}) format('woff2');
}}

:root {{
  color-scheme: dark;
  --bg: #0a3f8a;
  --text-main: #ffffff;
  --text-muted: rgba(255, 255, 255, 0.9);
  --text-dim: rgba(255, 255, 255, 0.72);
  --glass-bg: rgba(12, 18, 34, 0.45);
  --glass-border: rgba(255, 255, 255, 0.22);
  --glass-border-hover: rgba(255, 255, 255, 0.55);
  --glass-highlight: rgba(255, 255, 255, 0.28);
  --glow-warm: rgba(255, 215, 130, 0.35);
  --font-serif: 'Playfair Display', Georgia, 'Times New Roman', serif;
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}}

* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}}

html, body {{
  width: 100%;
  height: 100%;
  background: var(--bg);
  overflow: hidden;
  font-family: var(--font-sans);
  color: var(--text-main);
  user-select: none;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}}

/* ============================================================
   BACKGROUND STAGE & COSMIC ANIMATION (VIBRANT & SEEABLE)
   ============================================================ */
#stage {{
  position: fixed;
  inset: 0;
  overflow: hidden;
  background: var(--bg);
  z-index: 1;
}}

#wrap {{
  position: absolute;
  inset: 0;
  transform-origin: 50% 68%;
  animation: breathe 28s ease-in-out infinite alternate;
  will-change: transform;
}}

#wrap img#bg {{
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: 50% 70%;
  display: block;
}}

canvas#c {{
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}}

/* Interactive Stardust Cursor Layer */
canvas#cursor-canvas {{
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 2;
}}

@keyframes breathe {{
  from {{ transform: scale(1); }}
  to {{ transform: scale(1.032); }}
}}

@media (prefers-reduced-motion: reduce) {{
  #wrap {{ animation: none; }}
}}

/* ============================================================
   TOP NAVIGATION BAR
   ============================================================ */
.navbar-wrapper {{
  position: fixed;
  top: 24px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  z-index: 50;
  padding: 0 20px;
  pointer-events: none;
}}

.navbar {{
  pointer-events: auto;
  width: auto;
  max-width: 840px;
  height: 46px;
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 0 20px;
  background: var(--glass-bg);
  backdrop-filter: blur(22px) saturate(190%);
  -webkit-backdrop-filter: blur(22px) saturate(190%);
  border: 1px solid var(--glass-border);
  border-radius: 9999px;
  box-shadow: 
    0 10px 32px rgba(0, 0, 0, 0.38),
    inset 0 1px 0 var(--glass-highlight),
    inset 0 -1px 0 rgba(255, 255, 255, 0.05);
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}}

.navbar:hover {{
  border-color: rgba(255, 255, 255, 0.38);
  box-shadow: 
    0 14px 40px rgba(0, 0, 0, 0.48),
    inset 0 1px 0 rgba(255, 255, 255, 0.35),
    0 0 24px rgba(255, 215, 120, 0.12);
}}

.nav-links {{
  display: flex;
  align-items: center;
  gap: 22px;
}}

.nav-link-btn {{
  background: none;
  border: none;
  font-family: var(--font-sans);
  font-size: 13px;
  font-weight: 400;
  color: var(--text-muted);
  cursor: pointer;
  padding: 4px 0;
  transition: color 0.2s ease, text-shadow 0.2s ease;
  outline: none;
  white-space: nowrap;
}}

.nav-link-btn:hover {{
  color: #ffffff;
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.7);
}}

/* Donate CTA Button in Navbar */
.nav-donate-btn {{
  background: rgba(255, 255, 255, 0.16);
  border: 1px solid rgba(255, 255, 255, 0.38);
  border-radius: 9999px;
  padding: 5px 15px;
  font-family: var(--font-sans);
  font-size: 12.5px;
  font-weight: 600;
  letter-spacing: 0.015em;
  color: #ffffff;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.3);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  white-space: nowrap;
  outline: none;
}}

.nav-donate-btn:hover {{
  background: rgba(255, 255, 255, 0.28);
  border-color: rgba(255, 255, 255, 0.75);
  box-shadow: 
    0 4px 18px rgba(0, 0, 0, 0.35),
    0 0 18px rgba(255, 220, 140, 0.35),
    inset 0 1px 0 rgba(255, 255, 255, 0.5);
  transform: translateY(-1px);
  color: #ffffff;
}}

.nav-donate-btn:active {{
  transform: translateY(0);
}}

/* Interactive Pill Button */
.cta-pill-btn {{
  background: rgba(10, 20, 38, 0.45);
  backdrop-filter: blur(20px) saturate(190%);
  -webkit-backdrop-filter: blur(20px) saturate(190%);
  border: 1px solid rgba(255, 255, 255, 0.28);
  border-radius: 9999px;
  padding: 8px 24px;
  color: #ffffff;
  font-family: var(--font-sans);
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.01em;
  cursor: pointer;
  box-shadow: 
    0 8px 24px rgba(0, 0, 0, 0.4),
    inset 0 1px 0 var(--glass-highlight);
  transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  outline: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}}

.cta-pill-btn::after {{
  content: '→';
  font-size: 13px;
  transition: transform 0.25s ease;
}}

.cta-pill-btn:hover {{
  background: rgba(255, 255, 255, 0.18);
  border-color: rgba(255, 255, 255, 0.55);
  box-shadow: 
    0 12px 32px rgba(0, 0, 0, 0.48),
    0 0 28px rgba(255, 220, 140, 0.3),
    inset 0 1px 0 rgba(255, 255, 255, 0.45);
  transform: translateY(-2px);
}}

.cta-pill-btn:hover::after {{
  transform: translateX(3px);
}}

.cta-pill-btn:active {{
  transform: translateY(0);
}}

/* ============================================================
   BOTTOM BAR: SOCIALS IN MIDDLE, COPYRIGHT ON RIGHT
   ============================================================ */
.footer-bar {{
  position: fixed;
  bottom: clamp(16px, 3vh, 26px);
  left: 0;
  right: 0;
  padding: 0 clamp(24px, 5.5vw, 68px);
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  z-index: 40;
  pointer-events: auto;
  font-size: 12px;
  font-weight: 400;
  color: var(--text-dim);
}}

.footer-left {{
  display: flex;
  align-items: center;
}}

.footer-center {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
}}

.footer-right {{
  display: flex;
  align-items: center;
  justify-content: flex-end;
}}

.footer-copyright {{
  color: rgba(255, 255, 255, 0.75);
  letter-spacing: 0.01em;
  text-shadow: 0 1px 8px rgba(0, 0, 0, 0.75);
  white-space: nowrap;
}}

/* Social Icon Bubbles */
.social-circle {{
  width: 38px;
  height: 38px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.08);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border: 1px solid rgba(255, 255, 255, 0.25);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
  color: rgba(255, 255, 255, 0.92);
  text-decoration: none;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  outline: none;
}}

.social-circle svg {{
  transition: transform 0.25s ease;
}}

.social-circle:hover {{
  background: rgba(255, 255, 255, 0.18);
  border-color: rgba(255, 255, 255, 0.55);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.45), 0 0 16px rgba(255, 255, 255, 0.25);
  transform: translateY(-2px);
  color: #ffffff;
}}

.social-circle:hover svg {{
  transform: scale(1.12);
}}

.social-circle:active {{
  transform: translateY(0);
}}

/* Tooltip for Socials */
.social-circle::before {{
  content: attr(data-tooltip);
  position: absolute;
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%) translateY(4px);
  padding: 4px 8px;
  background: rgba(10, 16, 28, 0.92);
  color: #ffffff;
  font-size: 10px;
  font-weight: 500;
  letter-spacing: 0.02em;
  border-radius: 6px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: all 0.2s ease;
}}

.social-circle:hover::before {{
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}}

/* ============================================================
   MODALS SYSTEM
   ============================================================ */
.modal-overlay {{
  position: fixed;
  inset: 0;
  background: rgba(4, 8, 18, 0.65);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}}

.modal-overlay.active {{
  opacity: 1;
  pointer-events: auto;
}}

.modal-card {{
  position: relative;
  width: min(92vw, 540px);
  background: rgba(14, 22, 38, 0.88);
  backdrop-filter: blur(28px) saturate(190%);
  -webkit-backdrop-filter: blur(28px) saturate(190%);
  border: 1px solid rgba(255, 255, 255, 0.22);
  border-radius: 22px;
  padding: clamp(24px, 4vw, 36px);
  box-shadow: 
    0 24px 60px rgba(0, 0, 0, 0.65),
    inset 0 1px 0 rgba(255, 255, 255, 0.25);
  transform: translateY(20px) scale(0.96);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}}

.modal-overlay.active .modal-card {{
  transform: translateY(0) scale(1);
}}

.modal-close-btn {{
  position: absolute;
  top: 18px;
  right: 18px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.16);
  color: rgba(255, 255, 255, 0.8);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
  transition: all 0.2s ease;
  outline: none;
}}

.modal-close-btn:hover {{
  background: rgba(255, 255, 255, 0.2);
  color: #fff;
  transform: scale(1.08);
}}

.modal-title {{
  font-family: var(--font-serif);
  font-size: 1.6rem;
  font-weight: 500;
  color: #ffffff;
  margin-bottom: 6px;
}}

.modal-desc {{
  font-family: var(--font-sans);
  font-size: 13.5px;
  line-height: 1.5;
  color: rgba(255, 255, 255, 0.78);
  margin-bottom: 20px;
}}

.modal-badge {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 3px 10px;
  background: rgba(255, 215, 120, 0.14);
  border: 1px solid rgba(255, 215, 120, 0.35);
  border-radius: 9999px;
  color: #ffe699;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  margin-bottom: 12px;
}}

.modal-badge-dot {{
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #ffe082;
  box-shadow: 0 0 6px #ffe082;
}}

.modal-input-wrapper {{
  display: flex;
  align-items: center;
  gap: 10px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.22);
  border-radius: 12px;
  padding: 10px 14px;
  margin-bottom: 16px;
  transition: border-color 0.2s ease, background 0.2s ease;
}}

.modal-input-wrapper:focus-within {{
  border-color: rgba(255, 255, 255, 0.55);
  background: rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 16px rgba(255, 255, 255, 0.12);
}}

.modal-input {{
  background: transparent;
  border: none;
  outline: none;
  color: #ffffff;
  font-family: var(--font-sans);
  font-size: 14px;
  width: 100%;
}}

.modal-input::placeholder {{
  color: rgba(255, 255, 255, 0.45);
}}

.quick-chips {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}}

.chip-btn {{
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 9999px;
  padding: 5px 12px;
  font-family: var(--font-sans);
  font-size: 12px;
  color: rgba(255, 255, 255, 0.85);
  cursor: pointer;
  transition: all 0.2s ease;
}}

.chip-btn:hover {{
  background: rgba(255, 255, 255, 0.16);
  border-color: rgba(255, 255, 255, 0.4);
  color: #ffffff;
  transform: translateY(-1px);
}}

.grid-cards {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 12px;
  margin-top: 12px;
}}

.grid-card {{
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 12px;
  padding: 14px;
  transition: border-color 0.2s ease, background 0.2s ease;
}}

.grid-card:hover {{
  background: rgba(255, 255, 255, 0.08);
  border-color: rgba(255, 255, 255, 0.28);
}}

.grid-card-title {{
  font-size: 13.5px;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}}

.grid-card-tag {{
  font-size: 10px;
  padding: 2px 7px;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.8);
}}

.grid-card-desc {{
  font-size: 12px;
  line-height: 1.45;
  color: rgba(255, 255, 255, 0.7);
}}

.donate-chip {{
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 9999px;
  padding: 8px 16px;
  color: rgba(255, 255, 255, 0.85);
  font-family: var(--font-sans);
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s ease;
  outline: none;
}}

.donate-chip:hover, .donate-chip.active {{
  background: rgba(255, 255, 255, 0.2);
  border-color: rgba(255, 255, 255, 0.6);
  color: #ffffff;
  box-shadow: 0 0 14px rgba(255, 255, 255, 0.25);
}}

/* Dynamic Toast Notification */
.toast {{
  position: fixed;
  bottom: 84px;
  left: 50%;
  transform: translateX(-50%) translateY(20px);
  background: rgba(14, 20, 34, 0.92);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.28);
  padding: 8px 18px;
  font-size: 12.5px;
  color: #ffffff;
  border-radius: 9999px;
  z-index: 120;
  pointer-events: none;
  opacity: 0;
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  align-items: center;
  gap: 8px;
}}

.toast.show {{
  opacity: 1;
  transform: translateX(-50%) translateY(0);
}}

/* ============================================================
   RESPONSIVE DESIGN
   ============================================================ */
@media (max-width: 680px) {{
  .navbar {{
    gap: 12px;
    padding: 0 14px;
    height: 42px;
  }}
  .nav-links {{
    gap: 12px;
  }}
  .nav-link-btn {{
    font-size: 12px;
  }}
  .nav-donate-btn {{
    padding: 4px 11px;
    font-size: 11.5px;
  }}
  .footer-bar {{
    display: flex;
    flex-direction: column-reverse;
    align-items: center;
    gap: 12px;
    bottom: 14px;
  }}
  .footer-left {{
    display: none;
  }}
}}

@media (max-width: 480px) {{
  .navbar {{
    padding: 0 10px;
    gap: 8px;
  }}
  .nav-links {{
    gap: 8px;
  }}
  .nav-link-btn {{
    font-size: 11px;
  }}
  .nav-donate-btn {{
    padding: 3px 9px;
    font-size: 11px;
  }}
}}
</style>
</head>

<body>

<!-- Background Stage with Woman Stargazer & Authentic Cosmic Particle Engine -->
<div id="stage">
  <div id="wrap">
    <img id="bg" alt="Woman gazing at a starry sky" src="{bg_img}">
    <canvas id="c"></canvas>
  </div>
</div>

<!-- Interactive Cursor Stardust Layer -->
<canvas id="cursor-canvas"></canvas>

<!-- Top Capsule Navbar (Centered, Clean Menu & Donate) -->
<header class="navbar-wrapper">
  <nav class="navbar" aria-label="Primary Navigation">
    <div class="nav-links">
      <button class="nav-link-btn" data-modal="homeModal">Home</button>
      <button class="nav-link-btn" data-modal="classesModal">Classes</button>
      <button class="nav-link-btn" data-modal="foundationModal">Foundation</button>
      <button class="nav-donate-btn" data-modal="donateModal" aria-label="Donate">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" style="opacity:0.9; margin-right:5px;" aria-hidden="true">
          <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
        </svg>
        Donate
      </button>
    </div>
  </nav>
</header>

<!-- Bottom Footer Row: Socials in Middle, Copyright on Right -->
<footer class="footer-bar" aria-label="Page Footer">
  <div class="footer-left"></div>
  <div class="footer-center">
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
  <div class="footer-right">
    <span class="footer-copyright">© 2026 Artsy Fartsy Creative Laboratory.</span>
  </div>
</footer>

<!-- ============================================================
     INTERACTIVE MODALS
     ============================================================ -->

<!-- Explore Modal -->
<div class="modal-overlay" id="exploreModal">
  <div class="modal-card">
    <button class="modal-close-btn" data-close aria-label="Close dialog">✕</button>
    <span class="modal-badge"><span class="modal-badge-dot"></span> Interactive Search & Synthesis</span>
    <h3 class="modal-title" style="margin-bottom:8px;">Start Exploring</h3>
    <p class="modal-desc">Ask questions, synthesize research, and draw thoughtful connections.</p>
    
    <div class="modal-input-wrapper">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="opacity:0.6;">
        <circle cx="11" cy="11" r="8"></circle>
        <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
      </svg>
      <input type="text" class="modal-input" placeholder="What are you curious about today?" id="exploreSearchInput" autofocus>
    </div>

    <div class="quick-chips">
      <button class="chip-btn" onclick="searchTopic('Celestial cartography')">Celestial cartography</button>
      <button class="chip-btn" onclick="searchTopic('Philosophy of wonder')">Philosophy of wonder</button>
      <button class="chip-btn" onclick="searchTopic('Cosmic soundscapes')">Cosmic soundscapes</button>
      <button class="chip-btn" onclick="searchTopic('Quantum optics')">Quantum optics</button>
    </div>

    <div style="display:flex; justify-content:flex-end;">
      <button class="cta-pill-btn" onclick="submitSearch()">Synthesize Insights</button>
    </div>
  </div>
</div>

<!-- Home Modal -->
<div class="modal-overlay" id="homeModal">
  <div class="modal-card">
    <button class="modal-close-btn" data-close aria-label="Close dialog">✕</button>
    <span class="modal-badge"><span class="modal-badge-dot"></span> Studio Overview</span>
    <h3 class="modal-title" style="margin-bottom:8px;">Welcome to Artsy Fartsy</h3>
    <p class="modal-desc">A contemplative creative laboratory designing next-generation interfaces for human curiosity and intellectual clarity.</p>
    
    <div class="grid-cards">
      <div class="grid-card">
        <div class="grid-card-title">
          <span>Inquiry as a Practice</span>
          <span class="grid-card-tag">Philosophy</span>
        </div>
        <p class="grid-card-desc">Moving beyond rapid answers to cultivate deeper, richer perspectives.</p>
      </div>
      <div class="grid-card">
        <div class="grid-card-title">
          <span>Clarity over Chaos</span>
          <span class="grid-card-tag">Aesthetic</span>
        </div>
        <p class="grid-card-desc">Cutting through the deluge of web noise to present synthesized, verifiable understanding.</p>
      </div>
    </div>
  </div>
</div>

<!-- Classes Modal -->
<div class="modal-overlay" id="classesModal">
  <div class="modal-card">
    <button class="modal-close-btn" data-close aria-label="Close dialog">✕</button>
    <span class="modal-badge"><span class="modal-badge-dot"></span> Curriculum</span>
    <h3 class="modal-title" style="margin-bottom:8px;">Classes & Learning Programs</h3>
    <p class="modal-desc">Deep-dive sessions on knowledge architecture, prompt engineering, and inquiry-driven research.</p>
    
    <div class="grid-cards">
      <div class="grid-card">
        <div class="grid-card-title">
          <span>The Art of Inquiry</span>
          <span class="grid-card-tag">Fundamental</span>
        </div>
        <p class="grid-card-desc">Formulating high-dimensional questions that extract precise, non-obvious insights from complex systems.</p>
      </div>
      <div class="grid-card">
        <div class="grid-card-title">
          <span>Synthetic Reasoning & Logic</span>
          <span class="grid-card-tag">Advanced</span>
        </div>
        <p class="grid-card-desc">Structuring mental models alongside AI agents to cross-verify facts and synthesize multi-source data.</p>
      </div>
    </div>
  </div>
</div>

<!-- Foundation Modal -->
<div class="modal-overlay" id="foundationModal">
  <div class="modal-card">
    <button class="modal-close-btn" data-close aria-label="Close dialog">✕</button>
    <span class="modal-badge"><span class="modal-badge-dot"></span> Mission</span>
    <h3 class="modal-title" style="margin-bottom:8px;">The Knowledge Foundation</h3>
    <p class="modal-desc" style="margin-bottom: 16px;">
      Dedicated to democratizing open research, cultivating curiosity, and providing free inquiry tools to schools and students worldwide.
    </p>
    <div class="grid-cards">
      <div class="grid-card">
        <div class="grid-card-title">
          <span>Open Knowledge Grant</span>
          <span class="grid-card-tag">Grants</span>
        </div>
        <p class="grid-card-desc">Funding independent researchers and educators building open scientific exploration tools.</p>
      </div>
    </div>
  </div>
</div>

<!-- Donate Modal -->
<div class="modal-overlay" id="donateModal">
  <div class="modal-card">
    <button class="modal-close-btn" data-close aria-label="Close dialog">✕</button>
    <span class="modal-badge"><span class="modal-badge-dot"></span> Support The Laboratory</span>
    <h3 class="modal-title" style="margin-bottom:8px;">Support Artsy Fartsy</h3>
    <p class="modal-desc">Your generosity fuels independent creative experiments, interactive astronomical art, and educational classes.</p>
    
    <div style="display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; margin: 20px 0 14px 0;">
      <button class="donate-chip" onclick="selectTier(this, '$10')">$10 &middot; Spark</button>
      <button class="donate-chip active" onclick="selectTier(this, '$25')">$25 &middot; Stargazer</button>
      <button class="donate-chip" onclick="selectTier(this, '$50')">$50 &middot; Patron</button>
      <button class="donate-chip" onclick="selectTier(this, '$100')">$100 &middot; Benefactor</button>
    </div>

    <div style="display:flex; justify-content:center; margin-top: 14px;">
      <button class="cta-pill-btn" style="padding: 10px 28px;" onclick="completeDonation()">
        Donate with Love
      </button>
    </div>
  </div>
</div>

<!-- Toast -->
<div class="toast" id="toast">
  <span id="toastIcon">✨</span>
  <span id="toastMessage">Welcome!</span>
</div>

<!-- ============================================================
     AUTHENTIC STARRY SKY ENGINE (SPARKS, SHOOTING STARS & GLOW)
     ============================================================ -->
<script>
// --- AUTHENTIC STARRY SKY ENGINE ---
(function(){{
  var W = 1672, H = 941, cv = document.getElementById('c'), ctx = cv.getContext('2d');
  var vw, vh, s, ox, oy, dpr;

  function resize(){{
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    vw = innerWidth;
    vh = innerHeight;
    cv.width = vw * dpr;
    cv.height = vh * dpr;
    s = Math.max(vw / W, vh / H);
    ox = (vw - W * s) * 0.5;
    // Align vertically with object-position: 50% 70% so the woman is always seeable & centered
    oy = (vh - H * s) * 0.70;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }}
  addEventListener('resize', resize);
  resize();

  // Sprites
  function mk(n, f){{
    var c = document.createElement('canvas');
    c.width = c.height = n;
    f(c.getContext('2d'), n);
    return c;
  }}

  var glow = mk(64, function(g, n){{
    var r = g.createRadialGradient(n/2, n/2, 0, n/2, n/2, n/2);
    r.addColorStop(0, 'rgba(255,248,220,1)');
    r.addColorStop(.25, 'rgba(255,220,130,.55)');
    r.addColorStop(1, 'rgba(255,200,90,0)');
    g.fillStyle = r;
    g.fillRect(0, 0, n, n);
  }});

  var spark = mk(128, function(g, n){{
    var h = n / 2;
    g.drawImage(glow, h - 32, h - 32);
    [[1, .16], [.16, 1]].forEach(function(a){{
      g.save();
      g.translate(h, h);
      g.scale(a[0], a[1]);
      var r = g.createRadialGradient(0, 0, 0, 0, 0, h);
      r.addColorStop(0, 'rgba(255,255,240,1)');
      r.addColorStop(.3, 'rgba(255,236,170,.6)');
      r.addColorStop(1, 'rgba(255,220,130,0)');
      g.fillStyle = r;
      g.beginPath();
      g.arc(0, 0, h, 0, 7);
      g.fill();
      g.restore();
    }});
  }});

  // Big sparkle stars (image coordinates)
  var P = [
    [759, 20, 1], [640, 56, .9], [747, 73, .8], [471, 110, .7], [328, 157, .9],
    [1171, 17, .7], [852, 44, .5], [220, 98, .5], [806, 296, 1], [1147, 378, .9],
    [360, 385, .8], [764, 390, .8], [1052, 413, .6], [1010, 355, .4], [503, 158, .5],
    [594, 307, .4], [1090, 120, .5], [960, 200, .5], [130, 230, .4], [1380, 150, .5],
    [1500, 300, .4], [300, 60, .4], [1250, 260, .5], [560, 420, .5]
  ];
  var stars = P.map(function(p){{
    return {{
      x: p[0],
      y: p[1],
      z: p[2],
      ph: Math.random() * 6.28,
      sp: .8 + Math.random() * 1.8,
      rot: (Math.random() - .5) * .5
    }};
  }});

  // Ambient twinkling dust
  var dust = [];
  for(var i=0; i<150; i++){{
    dust.push({{
      x: Math.random() * W,
      y: Math.random() * 520,
      z: .08 + Math.random() * .16,
      ph: Math.random() * 6.28,
      sp: 1 + Math.random() * 3,
      vx: (Math.random() - .5) * 4,
      vy: -Math.random() * 3
    }});
  }}

  // Stream of sparks rising from the head into the sky
  var N = 110, st = [];
  function reset(p, init){{
    p.t = init ? Math.random() : 0;
    p.d = 7 + Math.random() * 9;
    p.x0 = 830 + Math.random() * 130;
    p.y0 = 560 + Math.random() * 50;
    p.tx = p.x0 + (Math.random() - .5) * 900;
    p.ty = 60 + Math.random() * 320;
    p.w = Math.random() * 6.28;
    p.wa = 10 + Math.random() * 30;
    p.z = .12 + Math.random() * .22;
  }}
  for(i=0; i<N; i++){{
    var q = {{}};
    reset(q, true);
    st.push(q);
  }}

  var shoot = null, nextShoot = 3;
  function draw(img, x, y, sz, a, rot){{
    ctx.globalAlpha = a;
    if(rot){{
      ctx.save();
      ctx.translate(x, y);
      ctx.rotate(rot);
      ctx.drawImage(img, -sz/2, -sz/2, sz, sz);
      ctx.restore();
    }} else {{
      ctx.drawImage(img, x - sz/2, y - sz/2, sz, sz);
    }}
  }}

  var last = performance.now(), T = 0, run = true;
  function frame(now){{
    if(!run) return;
    requestAnimationFrame(frame);
    var dt = Math.min((now - last) / 1000, .05);
    last = now;
    T += dt;
    ctx.clearRect(0, 0, vw, vh);
    ctx.globalCompositeOperation = 'lighter';

    // Ambient dust
    for(var i=0; i<dust.length; i++){{
      var d = dust[i];
      d.x += d.vx * dt;
      d.y += d.vy * dt;
      if(d.y < -10) d.y = 520;
      if(d.x < -10) d.x = W;
      if(d.x > W + 10) d.x = -10;
      var a = .5 + .5 * Math.sin(T * d.sp + d.ph);
      a *= a;
      draw(glow, ox + d.x * s, oy + d.y * s, (10 + d.z * 60) * s, .15 + a * .7, 0);
    }}

    // Stream of sparks rising from head
    for(i=0; i<N; i++){{
      var p = st[i];
      p.t += dt / p.d;
      if(p.t >= 1){{ reset(p, false); }}
      var u = p.t, e = u * u * (3 - 2 * u),
          x = p.x0 + (p.tx - p.x0) * e + Math.sin(T * .9 + p.w) * p.wa * Math.sin(u * 3.14),
          y = p.y0 + (p.ty - p.y0) * e;
      var al = Math.sin(u * 3.14159);
      al *= .55 + .45 * Math.sin(T * 3 + p.w);
      draw(glow, ox + x * s, oy + y * s, (14 + p.z * 70) * s * (1 - u * .4), al * .9, 0);
    }}

    // Sparkle stars
    for(i=0; i<stars.length; i++){{
      var t = stars[i], k = .5 + .5 * Math.sin(T * t.sp + t.ph);
      var sz = (34 + 70 * t.z) * s * (.55 + .7 * k);
      draw(spark, ox + t.x * s, oy + t.y * s, sz, .35 + .65 * k, t.rot + Math.sin(T * .4 + t.ph) * .15);
    }}

    // Shooting stars
    if(!shoot && T > nextShoot){{
      shoot = {{ t: 0, x: 200 + Math.random() * 1000, y: 20 + Math.random() * 120, a: .35 + Math.random() * .3 }};
    }}
    if(shoot){{
      shoot.t += dt / 1.1;
      var u2 = shoot.t;
      if(u2 >= 1){{
        shoot = null;
        nextShoot = T + 5 + Math.random() * 7;
      }} else {{
        var L = 260, dx = Math.cos(shoot.a), dy = Math.sin(shoot.a),
            hx = shoot.x + dx * L * u2 * 2.2, hy = shoot.y + dy * L * u2 * 2.2,
            fade = Math.sin(u2 * 3.14159);
        for(var j=0; j<14; j++){{
          var f = j / 14;
          draw(glow, ox + (hx - dx * L * f * .5) * s, oy + (hy - dy * L * f * .5) * s, (34 - f * 26) * s, fade * (1 - f) * .8, 0);
        }}
      }}
    }}

    ctx.globalAlpha = 1;
    ctx.globalCompositeOperation = 'source-over';
  }}
  requestAnimationFrame(frame);

  document.addEventListener('visibilitychange', function(){{
    if(document.hidden) run = false;
    else if(!run){{ run = true; last = performance.now(); requestAnimationFrame(frame); }}
  }});

  if(matchMedia('(prefers-reduced-motion:reduce)').matches){{ N = 30; }}
}})();

// --- INTERACTIVE CURSOR STARDUST TRAIL ---
(function(){{
  var c = document.getElementById('cursor-canvas'), ctx = c.getContext('2d');
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var particles = [];

  function resize(){{
    c.width = window.innerWidth * dpr;
    c.height = window.innerHeight * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }}
  window.addEventListener('resize', resize);
  resize();

  window.addEventListener('pointermove', function(e){{
    if(particles.length < 35){{
      for(var i=0; i<2; i++){{
        particles.push({{
          x: e.clientX + (Math.random() - .5) * 8,
          y: e.clientY + (Math.random() - .5) * 8,
          vx: (Math.random() - .5) * 1.5,
          vy: (Math.random() - .5) * 1.5 - 0.4,
          life: 1,
          decay: 0.025 + Math.random() * 0.03,
          size: 1.5 + Math.random() * 2.5
        }});
      }}
    }}
  }});

  function loop(){{
    ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
    for(var i=particles.length - 1; i>=0; i--){{
      var p = particles[i];
      p.x += p.vx;
      p.y += p.vy;
      p.life -= p.decay;
      if(p.life <= 0){{
        particles.splice(i, 1);
        continue;
      }}
      ctx.fillStyle = 'rgba(255, 235, 170, ' + (p.life * 0.75) + ')';
      ctx.shadowColor = 'rgba(255, 210, 100, 0.8)';
      ctx.shadowBlur = 8;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.size * p.life, 0, Math.PI * 2);
      ctx.fill();
    }}
    requestAnimationFrame(loop);
  }}
  loop();
}})();

// --- UI INTERACTIONS & MODALS ---
function showToast(msg, icon){{
  var toast = document.getElementById('toast');
  var toastMsg = document.getElementById('toastMessage');
  var toastIco = document.getElementById('toastIcon');
  toastMsg.textContent = msg;
  if(icon) toastIco.textContent = icon;
  toast.classList.add('show');
  setTimeout(function(){{
    toast.classList.remove('show');
  }}, 3500);
}}

// Modal Handlers
var openButtons = document.querySelectorAll('[data-modal]');
var modals = document.querySelectorAll('.modal-overlay');

function openModal(id){{
  var target = document.getElementById(id);
  if(target){{
    modals.forEach(function(m){{ m.classList.remove('active'); }});
    target.classList.add('active');
  }}
}}

function closeAllModals(){{
  modals.forEach(function(m){{ m.classList.remove('active'); }});
}}

openButtons.forEach(function(btn){{
  btn.addEventListener('click', function(e){{
    e.preventDefault();
    var id = btn.getAttribute('data-modal');
    openModal(id);
  }});
}});

document.querySelectorAll('[data-close]').forEach(function(btn){{
  btn.addEventListener('click', closeAllModals);
}});

modals.forEach(function(modal){{
  modal.addEventListener('click', function(e){{
    if(e.target === modal) closeAllModals();
  }});
}});

document.addEventListener('keydown', function(e){{
  if(e.key === 'Escape') closeAllModals();
}});


// Search interactive handler
function searchTopic(query){{
  var input = document.getElementById('exploreSearchInput');
  if(input){{
    input.value = query;
    input.focus();
  }}
}}

function submitSearch(){{
  var input = document.getElementById('exploreSearchInput');
  var val = input ? input.value.trim() : '';
  if(!val) val = 'Celestial Cartography';
  closeAllModals();
  showToast('Exploring "' + val + '"...', '✦');
}}

// Donation Tier Selection & Flow
var selectedDonation = '$25';
function selectTier(btn, amt){{
  document.querySelectorAll('.donate-chip').forEach(function(c){{ c.classList.remove('active'); }});
  btn.classList.add('active');
  selectedDonation = amt;
}}

function completeDonation(){{
  closeAllModals();
  showToast('Thank you for supporting Artsy Fartsy with ' + selectedDonation + '!', '💖');
}}
</script>
</body>
</html>
'''

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Updated index.html: Authentic starry background, woman centered & seeable, text centered in celestial sky!')
