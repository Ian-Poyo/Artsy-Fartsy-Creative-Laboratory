css = '''
/* ============================================================
   SECTION 2: CURATED CAROUSELS (FUNKY TWIST 3D SHOWCASE)
   Warm Caramel Ambient Background & 3D Depth Viewport
   ============================================================ */
.curated-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  padding: clamp(80px, 11vh, 130px) clamp(20px, 4.5vw, 48px) clamp(80px, 12vh, 140px);
  box-sizing: border-box;
  background-color: #120c09;
  background-image: 
    radial-gradient(ellipse 65% 50% at 75% 25%, rgba(194, 114, 54, 0.45) 0%, rgba(122, 60, 24, 0.22) 50%, transparent 80%),
    radial-gradient(ellipse 60% 45% at 20% 75%, rgba(160, 88, 38, 0.38) 0%, rgba(75, 32, 12, 0.18) 55%, transparent 80%),
    radial-gradient(circle at 50% 45%, rgba(95, 45, 18, 0.32) 0%, transparent 70%);
  color: #ffffff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  z-index: 20;
}

.curated-section::before {
  content: '';
  position: absolute;
  top: 10%;
  right: 5%;
  width: clamp(260px, 45vw, 550px);
  height: clamp(260px, 45vw, 550px);
  border-radius: 50%;
  background: radial-gradient(circle, rgba(212, 128, 62, 0.25) 0%, rgba(142, 68, 26, 0.1) 45%, transparent 70%);
  filter: blur(60px);
  pointer-events: none;
  z-index: 0;
}

.curated-section::after {
  content: '';
  position: absolute;
  bottom: 8%;
  left: 6%;
  width: clamp(240px, 40vw, 480px);
  height: clamp(240px, 40vw, 480px);
  border-radius: 50%;
  background: radial-gradient(circle, rgba(175, 88, 38, 0.22) 0%, rgba(85, 38, 14, 0.08) 50%, transparent 75%);
  filter: blur(55px);
  pointer-events: none;
  z-index: 0;
}

.funky-container {
  width: 100%;
  max-width: 640px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  position: relative;
  z-index: 10;
}

/* Curated Carousels Editorial Title Group (From Reference Image) */
.curated-title-group {
  width: 100%;
  margin-bottom: clamp(20px, 3vh, 32px);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
}

.curated-title {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.curated-word-italic {
  font-family: 'Playfair Display', Georgia, serif;
  font-style: italic;
  font-weight: 400;
  font-size: clamp(48px, 6.8vw, 76px);
  line-height: 0.95;
  color: #ede4d8;
  letter-spacing: -0.015em;
  display: block;
}

.curated-word-main {
  font-family: 'Playfair Display', Georgia, serif;
  font-style: normal;
  font-weight: 400;
  font-size: clamp(48px, 6.8vw, 76px);
  line-height: 0.95;
  color: #ffffff;
  letter-spacing: -0.025em;
  display: block;
  margin-top: -0.04em;
}

/* The Black Viewport Box */
.funky-viewport {
  position: relative;
  width: 100%;
  aspect-ratio: 1.25 / 1;
  min-height: 380px;
  max-height: 520px;
  background: #000000;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 45px 95px -20px rgba(0, 0, 0, 0.95), 0 0 0 1px rgba(255, 255, 255, 0.08);
  perspective: 1200px;
  transform-style: preserve-3d;
  display: flex;
  align-items: center;
  justify-content: center;
  user-select: none;
  cursor: grab;
}

.funky-viewport:active {
  cursor: grabbing;
}

.funky-cards-stage {
  position: relative;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  transform-style: preserve-3d;
}

/* 3D Funky Cards */
.funky-card {
  position: absolute;
  width: clamp(240px, 58%, 340px);
  aspect-ratio: 16 / 10.5;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 24px 60px -10px rgba(0, 0, 0, 0.75), 0 0 0 1px rgba(255, 255, 255, 0.12);
  will-change: transform, filter, opacity;
  transition: transform 0.8s cubic-bezier(0.2, 0.85, 0.25, 1), 
              filter 0.8s cubic-bezier(0.2, 0.85, 0.25, 1), 
              opacity 0.8s cubic-bezier(0.2, 0.85, 0.25, 1);
  outline: none;
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  padding: clamp(14px, 2.8vw, 22px);
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-header {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.card-title {
  font-family: var(--font-sans);
  font-size: clamp(15px, 1.8vw, 19px);
  font-weight: 600;
  color: #ffffff;
  letter-spacing: -0.02em;
  line-height: 1.1;
}

.card-subtitle {
  font-family: 'Playfair Display', Georgia, serif;
  font-style: italic;
  font-size: clamp(12px, 1.2vw, 14.5px);
  color: rgba(255, 255, 255, 0.68);
  line-height: 1.2;
}

.card-footer {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
}

.card-badge {
  font-family: var(--font-sans);
  font-size: clamp(11.5px, 1.1vw, 13px);
  font-weight: 800;
  letter-spacing: 0.06em;
  color: rgba(255, 255, 255, 0.85);
}

.card-num {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(38px, 4.6vw, 52px);
  font-weight: 400;
  line-height: 0.85;
  color: #faf5ee;
  letter-spacing: -0.04em;
}

/* Card Themes & Authentic Gradients */
.card-01 {
  background: linear-gradient(175deg, #18100b 0%, #2a1910 32%, #824722 65%, #c07742 85%, #b46833 100%);
}
.card-02 {
  background: linear-gradient(175deg, #180c12 0%, #351622 32%, #8e3f4e 65%, #cf6c6c 85%, #d48270 100%);
}
.card-03 {
  background: linear-gradient(175deg, #140718 0%, #2e0f39 32%, #822b82 65%, #c64fa8 85%, #e06fa6 100%);
}
.card-04 {
  background: linear-gradient(175deg, #070e1b 0%, #0f223f 32%, #225596 65%, #3d88cf 85%, #5aa5e6 100%);
}
.card-05 {
  background: linear-gradient(175deg, #09120c 0%, #172719 32%, #4e6328 65%, #9fa13c 85%, #d8b248 100%);
}

/* 3D Card Slots */
.funky-card[data-slot="0"] {
  transform: translate3d(0, 0, 50px) rotate(-11deg);
  filter: blur(0px);
  opacity: 1;
  z-index: 10;
  pointer-events: auto;
  cursor: grab;
}
.funky-card[data-slot="0"]:hover {
  transform: translate3d(0, -3px, 55px) rotate(-10deg);
}

.funky-card[data-slot="-1"] {
  transform: translate3d(28px, -148px, -60px) rotate(14deg);
  filter: blur(12px);
  opacity: 0.58;
  z-index: 5;
  pointer-events: auto;
  cursor: pointer;
}
.funky-card[data-slot="-1"]:hover {
  filter: blur(8px);
  opacity: 0.75;
}

.funky-card[data-slot="1"] {
  transform: translate3d(-32px, 150px, -70px) rotate(-16deg);
  filter: blur(14px);
  opacity: 0.48;
  z-index: 4;
  pointer-events: auto;
  cursor: pointer;
}
.funky-card[data-slot="1"]:hover {
  filter: blur(9px);
  opacity: 0.68;
}

.funky-card[data-slot="deep"] {
  transform: translate3d(0, 240px, -200px) rotate(-22deg);
  filter: blur(24px);
  opacity: 0;
  z-index: 1;
  pointer-events: none;
}

/* Controls Bar Below Viewport (From Reference Image) */
.funky-controls-row {
  width: 100%;
  margin-top: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 2px;
  box-sizing: border-box;
}

.funky-buttons-wrap {
  display: flex;
  align-items: center;
  gap: 10px;
  position: relative;
}

.funky-nav-btn {
  width: 44px;
  height: 44px;
  border-radius: 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s ease;
  position: relative;
  outline: none;
}

.funky-nav-btn.prev {
  background: rgba(255, 255, 255, 0.18);
  border: none;
  color: #ffffff;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

.funky-nav-btn.prev:hover {
  background: rgba(255, 255, 255, 0.28);
  transform: translateY(-1px);
}

.funky-nav-btn.next {
  background: #000000;
  border: 1px solid rgba(255, 255, 255, 0.16);
  color: #ffffff;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.5);
}

.funky-nav-btn.next:hover {
  background: #181818;
  border-color: rgba(255, 255, 255, 0.28);
  transform: translateY(-1px);
}

/* Hand Cursor Prompt from Reference Image */
.funky-hand-cursor {
  position: absolute;
  bottom: -18px;
  right: -12px;
  pointer-events: none;
  z-index: 20;
  animation: handClickPulse 2.4s ease-in-out infinite;
  transition: opacity 0.35s ease, transform 0.35s ease;
}

.funky-hand-cursor.is-dismissed {
  opacity: 0;
  transform: scale(0.85);
  pointer-events: none;
}

@keyframes handClickPulse {
  0%, 100% {
    transform: translate(0, 0);
  }
  50% {
    transform: translate(2px, -3px) scale(1.06);
  }
}

/* Right Active Label from Reference Image */
.funky-label-display {
  display: flex;
  align-items: center;
}

.funky-active-title {
  font-family: var(--font-sans);
  font-size: clamp(16px, 1.4vw, 19px);
  font-weight: 500;
  color: #ffffff;
  letter-spacing: -0.015em;
  transition: opacity 0.25s ease, transform 0.25s ease;
}

/* Experience Details Drawer */
.funky-details-card {
  width: 100%;
  margin-top: 24px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.09);
  border-radius: 16px;
  padding: clamp(20px, 3vw, 28px);
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  gap: 12px;
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  transition: border-color 0.3s ease;
}

.funky-details-card:hover {
  border-color: rgba(212, 128, 62, 0.35);
}

.funky-details-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.funky-badge-pill {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #e59d68;
}

.funky-index-pill {
  font-family: var(--font-mono, monospace);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.12em;
  color: rgba(255, 255, 255, 0.5);
}

.funky-headline {
  margin: 0;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(19px, 2vw, 24px);
  font-weight: 400;
  line-height: 1.3;
  color: #ffffff;
}

.funky-desc {
  margin: 0;
  font-family: var(--font-sans);
  font-size: clamp(13px, 1vw, 14.5px);
  line-height: 1.62;
  color: rgba(255, 255, 255, 0.72);
}

.funky-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 8px;
}

.funky-action-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 100px;
  font-family: var(--font-sans);
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.25s ease;
  outline: none;
}

.funky-action-btn.primary {
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.18);
}

.funky-action-btn.primary:hover {
  background: rgba(255, 255, 255, 0.2);
  transform: translateY(-2px);
}

.funky-action-btn.secondary {
  background: linear-gradient(135deg, #c27236 0%, #8e441c 100%);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.funky-action-btn.secondary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 22px rgba(194, 114, 54, 0.4);
}

/* Scroll Prompt in Hero Tier Lower Left */
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
}
'''
print("CSS length:", len(css))
