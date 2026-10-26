css = '''
/* ============================================================
   SECTION 2: CURATED CAROUSELS (FUNKY TWIST 3D SHOWCASE)
   Harmonized with Artsy Fartsy Creative Laboratory Theme
   ============================================================ */
.curated-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  padding: clamp(90px, 12vh, 150px) clamp(20px, 4.5vw, 48px) clamp(90px, 12vh, 150px);
  box-sizing: border-box;
  background-color: #070912;
  background-image: 
    radial-gradient(ellipse 75% 60% at 50% -10%, rgba(10, 63, 138, 0.42) 0%, transparent 70%),
    radial-gradient(ellipse 65% 50% at 85% 35%, rgba(217, 119, 6, 0.16) 0%, transparent 65%),
    radial-gradient(ellipse 60% 45% at 15% 75%, rgba(139, 92, 246, 0.18) 0%, transparent 60%);
  color: #ffffff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  z-index: 20;
}

/* Seamless Top Scrim Transition from Hero to Section 2 */
.curated-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 140px;
  background: linear-gradient(180deg, #070509 0%, transparent 100%);
  pointer-events: none;
  z-index: 1;
}

/* Ambient Cosmic Glow Orbs */
.curated-ambient-mesh {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
  z-index: 0;
}

.mesh-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(70px);
  opacity: 0.65;
  will-change: transform;
}

.orb-sapphire {
  top: 15%;
  left: 5%;
  width: clamp(280px, 40vw, 550px);
  height: clamp(280px, 40vw, 550px);
  background: radial-gradient(circle, rgba(14, 80, 180, 0.3) 0%, rgba(10, 40, 100, 0.1) 50%, transparent 70%);
}

.orb-amber {
  top: 35%;
  right: 8%;
  width: clamp(260px, 38vw, 500px);
  height: clamp(260px, 38vw, 500px);
  background: radial-gradient(circle, rgba(229, 169, 60, 0.22) 0%, rgba(162, 85, 25, 0.08) 55%, transparent 70%);
}

.orb-violet {
  bottom: 10%;
  left: 20%;
  width: clamp(300px, 42vw, 580px);
  height: clamp(300px, 42vw, 580px);
  background: radial-gradient(circle, rgba(139, 92, 246, 0.2) 0%, rgba(88, 28, 135, 0.06) 50%, transparent 75%);
}

.curated-content-wrapper {
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  z-index: 10;
}

/* Section Header */
.curated-header-group {
  width: 100%;
  margin-bottom: clamp(24px, 3.5vh, 36px);
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.curated-badge-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 18px;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.16);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.16em;
  color: rgba(229, 169, 60, 0.95);
  margin-bottom: 16px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.35);
}

.eyebrow-sparkle {
  color: #e5a93c;
  font-size: 10px;
  animation: sparkleTwinkle 2.5s ease-in-out infinite;
}

@keyframes sparkleTwinkle {
  0%, 100% { opacity: 0.6; transform: scale(0.9); }
  50% { opacity: 1; transform: scale(1.2); }
}

.eyebrow-sep {
  opacity: 0.4;
}

.curated-hero-title {
  margin: 0;
  padding: 0;
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
}

.curated-title-script {
  font-family: 'Playfair Display', Georgia, serif;
  font-style: italic;
  font-weight: 400;
  font-size: clamp(48px, 6.8vw, 82px);
  line-height: 0.95;
  color: #fbf5ec;
  letter-spacing: -0.015em;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.45);
}

.curated-title-lead {
  font-family: 'Playfair Display', Georgia, serif;
  font-style: normal;
  font-weight: 400;
  font-size: clamp(48px, 6.8vw, 82px);
  line-height: 0.95;
  color: #ffffff;
  letter-spacing: -0.025em;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.45);
}

.curated-hero-sub {
  margin: 14px 0 24px;
  font-family: var(--font-sans);
  font-size: clamp(14px, 1.1vw, 16.5px);
  color: rgba(255, 255, 255, 0.72);
  line-height: 1.6;
  max-width: 580px;
  text-align: center;
}

/* Chapter Navigation Tabs (UX Pill Switcher) */
.chapter-tabs-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 6px;
  padding: 5px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 9999px;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
}

.chapter-tab {
  background: transparent;
  border: 1px solid transparent;
  border-radius: 9999px;
  padding: 7px 16px;
  font-family: var(--font-sans);
  font-size: 12.5px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.68);
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
  display: inline-flex;
  align-items: center;
  gap: 8px;
  outline: none;
}

.chapter-tab:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.08);
}

.chapter-tab.is-active {
  color: #ffffff;
  background: rgba(229, 169, 60, 0.18);
  border-color: rgba(229, 169, 60, 0.5);
  box-shadow: 0 0 16px rgba(229, 169, 60, 0.25), inset 0 1px 0 rgba(255, 255, 255, 0.2);
  font-weight: 600;
}

.tab-index {
  font-family: var(--font-mono, monospace);
  font-size: 10px;
  opacity: 0.65;
  letter-spacing: 0.05em;
}

.chapter-tab.is-active .tab-index {
  color: #e5a93c;
  opacity: 1;
}

/* Luxury Frosted Showcase Frame */
.curated-showcase-frame {
  width: 100%;
  background: rgba(14, 21, 36, 0.82);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 24px;
  overflow: hidden;
  box-shadow: 
    0 35px 80px -15px rgba(0, 0, 0, 0.85),
    inset 0 1px 0 rgba(255, 255, 255, 0.25),
    0 0 30px rgba(10, 63, 138, 0.15);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
}

/* Studio macOS Top Bar */
.viewport-header-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 20px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(255, 255, 255, 0.03);
  user-select: none;
}

.viewport-window-dots {
  display: flex;
  align-items: center;
  gap: 6px;
}

.window-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  opacity: 0.8;
}

.window-dot.red { background: #ef4444; }
.window-dot.yellow { background: #f59e0b; }
.window-dot.green { background: #10b981; }

.viewport-suite-badge {
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.12em;
  color: rgba(255, 255, 255, 0.65);
}

.viewport-suite-badge .suite-icon {
  color: #e5a93c;
}

.viewport-mode-indicator {
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: var(--font-mono, monospace);
  font-size: 10px;
  letter-spacing: 0.1em;
  color: #10b981;
}

.mode-pulse {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 8px #10b981;
  animation: pulseGreen 2s infinite;
}

@keyframes pulseGreen {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.8); }
}

/* The 3D Viewport Box */
.funky-viewport {
  position: relative;
  width: 100%;
  aspect-ratio: 16 / 10.8;
  min-height: 380px;
  max-height: 500px;
  background: radial-gradient(circle at 50% 50%, rgba(18, 27, 46, 0.5) 0%, rgba(6, 10, 18, 0.95) 100%);
  overflow: hidden;
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
  width: clamp(250px, 56%, 350px);
  aspect-ratio: 16 / 10.5;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 
    0 24px 60px -10px rgba(0, 0, 0, 0.85),
    0 0 0 1px rgba(255, 255, 255, 0.16);
  will-change: transform, filter, opacity;
  transition: transform 0.8s cubic-bezier(0.2, 0.85, 0.25, 1), 
              filter 0.8s cubic-bezier(0.2, 0.85, 0.25, 1), 
              opacity 0.8s cubic-bezier(0.2, 0.85, 0.25, 1);
  outline: none;
}

.card-glass-specular {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.2) 0%, rgba(255, 255, 255, 0.04) 40%, transparent 70%);
  pointer-events: none;
  z-index: 2;
}

.card-motif-art {
  position: absolute;
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
  opacity: 0.25;
  pointer-events: none;
  z-index: 1;
  transition: opacity 0.3s ease, transform 0.4s ease;
}

.funky-card:hover .card-motif-art {
  opacity: 0.45;
  transform: translateY(-50%) rotate(15deg);
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  padding: clamp(16px, 2.8vw, 24px);
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  z-index: 3;
}

.card-top-row {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
}

.card-titles {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.card-title {
  font-family: var(--font-sans);
  font-size: clamp(16px, 1.8vw, 20px);
  font-weight: 600;
  color: #ffffff;
  letter-spacing: -0.02em;
  line-height: 1.1;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
}

.card-subtitle {
  font-family: 'Playfair Display', Georgia, serif;
  font-style: italic;
  font-size: clamp(12px, 1.2vw, 14.5px);
  color: rgba(255, 255, 255, 0.75);
  line-height: 1.2;
}

.card-status-pill {
  font-family: var(--font-mono, monospace);
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.12em;
  color: rgba(255, 255, 255, 0.9);
  padding: 3px 8px;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.14);
  border: 1px solid rgba(255, 255, 255, 0.25);
  backdrop-filter: blur(8px);
}

.card-footer-row {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
}

.card-brand-box {
  display: flex;
  flex-direction: column;
  line-height: 1;
}

.brand-sub {
  font-family: var(--font-sans);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: rgba(255, 255, 255, 0.65);
}

.brand-code {
  font-family: var(--font-sans);
  font-size: clamp(13px, 1.2vw, 15px);
  font-weight: 800;
  letter-spacing: 0.08em;
  color: #ffffff;
}

.card-num-display {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(40px, 4.8vw, 56px);
  font-weight: 400;
  line-height: 0.82;
  color: #ffffff;
  letter-spacing: -0.04em;
  text-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
}

/* Card Themes & Jewel Tone Gradients */
.card-01 {
  background: linear-gradient(145deg, #090e1a 0%, #1a1e34 38%, #783818 72%, #d97706 100%);
}
.card-02 {
  background: linear-gradient(145deg, #090e1a 0%, #20131b 38%, #883244 72%, #f43f5e 100%);
}
.card-03 {
  background: linear-gradient(145deg, #090918 0%, #1e102e 38%, #6d28d9 72%, #ec4899 100%);
}
.card-04 {
  background: linear-gradient(145deg, #050b16 0%, #0b1e38 38%, #1d4ed8 72%, #38bdf8 100%);
}
.card-05 {
  background: linear-gradient(145deg, #050e09 0%, #0f2214 38%, #15803d 72%, #eab308 100%);
}

/* 3D Card Slots */
.funky-card[data-slot="0"] {
  transform: translate3d(0, 0, 50px) rotate(-10deg);
  filter: blur(0px);
  opacity: 1;
  z-index: 10;
  pointer-events: auto;
  cursor: grab;
}
.funky-card[data-slot="0"]:hover {
  transform: translate3d(0, -3px, 55px) rotate(-9deg);
}

.funky-card[data-slot="-1"] {
  transform: translate3d(26px, -145px, -60px) rotate(14deg);
  filter: blur(10px);
  opacity: 0.58;
  z-index: 5;
  pointer-events: auto;
  cursor: pointer;
}
.funky-card[data-slot="-1"]:hover {
  filter: blur(6px);
  opacity: 0.78;
}

.funky-card[data-slot="1"] {
  transform: translate3d(-30px, 145px, -70px) rotate(-16deg);
  filter: blur(12px);
  opacity: 0.48;
  z-index: 4;
  pointer-events: auto;
  cursor: pointer;
}
.funky-card[data-slot="1"]:hover {
  filter: blur(7px);
  opacity: 0.72;
}

.funky-card[data-slot="deep"] {
  transform: translate3d(0, 240px, -200px) rotate(-22deg);
  filter: blur(24px);
  opacity: 0;
  z-index: 1;
  pointer-events: none;
}

/* Controls Row */
.funky-controls-row {
  width: 100%;
  margin-top: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 4px;
  box-sizing: border-box;
}

.funky-nav-controls {
  display: flex;
  align-items: center;
  gap: 10px;
  position: relative;
}

.funky-nav-btn {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s ease;
  position: relative;
  outline: none;
}

.funky-nav-btn.prev {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.16);
  color: #ffffff;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

.funky-nav-btn.prev:hover {
  background: rgba(255, 255, 255, 0.18);
  border-color: rgba(255, 255, 255, 0.28);
  transform: translateY(-1px);
}

.funky-nav-btn.next {
  background: rgba(14, 23, 42, 0.95);
  border: 1px solid rgba(229, 169, 60, 0.5);
  color: #ffffff;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5), 0 0 16px rgba(229, 169, 60, 0.2);
}

.funky-nav-btn.next:hover {
  background: rgba(24, 36, 62, 0.98);
  border-color: rgba(229, 169, 60, 0.75);
  transform: translateY(-1px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6), 0 0 22px rgba(229, 169, 60, 0.35);
}

.funky-nav-btn:active {
  transform: scale(0.92) !important;
}

/* Illustrated Hand Cursor Prompt from Reference Image */
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

/* Center Progress Dots */
.funky-progress-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
}

.progress-dots {
  display: flex;
  align-items: center;
  gap: 6px;
}

.p-dot {
  width: 6px;
  height: 6px;
  border-radius: 3px;
  background: rgba(255, 255, 255, 0.22);
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.p-dot.is-active {
  width: 20px;
  background: #e5a93c;
  box-shadow: 0 0 12px rgba(229, 169, 60, 0.6);
}

.progress-counter {
  font-family: var(--font-mono, monospace);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.1em;
  color: rgba(255, 255, 255, 0.6);
}

/* Right Active Chapter Display */
.funky-label-display {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  line-height: 1.2;
}

.funky-active-title {
  font-family: var(--font-sans);
  font-size: clamp(15px, 1.3vw, 18px);
  font-weight: 600;
  color: #ffffff;
  letter-spacing: -0.01em;
  transition: opacity 0.25s ease, transform 0.25s ease;
}

.funky-active-sub {
  font-family: 'Playfair Display', serif;
  font-style: italic;
  font-size: 12px;
  color: rgba(229, 169, 60, 0.9);
  transition: opacity 0.25s ease;
}

/* Chapter Story & Studio Action Drawer */
.curated-story-drawer {
  width: 100%;
  margin-top: 24px;
  background: rgba(14, 21, 36, 0.82);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 20px;
  padding: clamp(24px, 3.2vw, 32px);
  box-sizing: border-box;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  display: grid;
  grid-template-columns: 1.35fr 1fr;
  gap: 28px;
  align-items: center;
  box-shadow: 
    0 24px 60px rgba(0, 0, 0, 0.6),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  transition: border-color 0.3s ease;
}

.curated-story-drawer:hover {
  border-color: rgba(229, 169, 60, 0.35);
}

.story-left-col {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.story-meta-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 8px;
}

.story-badge-pill {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #e5a93c;
}

.story-index-tag {
  font-family: var(--font-mono, monospace);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.12em;
  color: rgba(255, 255, 255, 0.5);
}

.story-headline {
  margin: 0;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(20px, 2.2vw, 25px);
  font-weight: 400;
  line-height: 1.3;
  color: #ffffff;
}

.story-desc {
  margin: 0;
  font-family: var(--font-sans);
  font-size: clamp(13px, 1vw, 14.5px);
  line-height: 1.62;
  color: rgba(255, 255, 255, 0.75);
}

.story-tags-list {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 4px;
}

.story-tag {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.7);
}

/* Action Card (Right Col) */
.story-right-col {
  height: 100%;
}

.story-action-card {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 12px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  box-sizing: border-box;
}

.action-card-label {
  font-family: var(--font-sans);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.14em;
  color: rgba(255, 255, 255, 0.5);
}

.story-action-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 20px;
  border-radius: 100px;
  font-family: var(--font-sans);
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.25s ease;
  outline: none;
  width: 100%;
  box-sizing: border-box;
}

.story-action-btn.primary {
  background: linear-gradient(135deg, rgba(229, 169, 60, 0.9) 0%, rgba(180, 100, 25, 0.9) 100%);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 8px 24px rgba(229, 169, 60, 0.35);
}

.story-action-btn.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(229, 169, 60, 0.5);
  background: linear-gradient(135deg, rgba(245, 185, 80, 0.95) 0%, rgba(200, 115, 30, 0.95) 100%);
}

.story-action-btn.secondary {
  background: rgba(255, 255, 255, 0.08);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.18);
}

.story-action-btn.secondary:hover {
  background: rgba(255, 255, 255, 0.16);
  border-color: rgba(255, 255, 255, 0.3);
  transform: translateY(-1px);
}

.action-hint-note {
  margin: 0;
  font-family: var(--font-sans);
  font-size: 11px;
  color: rgba(255, 255, 255, 0.45);
  text-align: center;
  line-height: 1.4;
}

/* Mobile Responsiveness */
@media (max-width: 768px) {
  .curated-section {
    padding: 70px 16px 90px;
  }
  .curated-hero-title {
    gap: 8px;
  }
  .chapter-tabs-bar {
    width: 100%;
  }
  .chapter-tab {
    padding: 6px 12px;
    font-size: 11.5px;
  }
  .funky-viewport {
    aspect-ratio: 1.1 / 1;
    min-height: 330px;
  }
  .funky-card {
    width: clamp(210px, 72%, 290px);
  }
  .funky-card[data-slot="-1"] {
    transform: translate3d(18px, -118px, -50px) rotate(14deg);
    filter: blur(8px);
  }
  .funky-card[data-slot="1"] {
    transform: translate3d(-18px, 122px, -60px) rotate(-16deg);
    filter: blur(10px);
  }
  .curated-story-drawer {
    grid-template-columns: 1fr;
    gap: 20px;
    padding: 20px;
  }
}
'''
print("Theme CSS valid, length:", len(css))
