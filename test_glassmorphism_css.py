css = '''
/* ============================================================
   SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE
   Ultra-Refined Glassmorphism Design System
   Enlarged Active Image Background & Frosted Glass Panels
   ============================================================ */
.foundation-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  padding: clamp(80px, 11vh, 120px) clamp(24px, 5vw, 64px) clamp(80px, 11vh, 120px);
  box-sizing: border-box;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #ffffff;
  z-index: 20;
}

/* Enlarged Background Image Stage (Active Slide Image Fills Area) */
.foundation-stage-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center 35%;
  transition: opacity 0.45s ease;
  z-index: 0;
  will-change: opacity, transform;
  transform: scale(1.02);
}

/* Atmospheric Ambient Tint Overlay */
.foundation-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(circle at 20% 50%, rgba(8, 12, 22, 0.6) 0%, transparent 65%),
    linear-gradient(90deg, rgba(8, 12, 22, 0.85) 0%, rgba(8, 12, 22, 0.4) 50%, rgba(8, 12, 22, 0.3) 100%),
    linear-gradient(180deg, rgba(8, 12, 22, 0.4) 0%, transparent 40%, rgba(8, 12, 22, 0.85) 100%);
  pointer-events: none;
  z-index: 1;
}

.foundation-container {
  width: 100%;
  max-width: 1360px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: clamp(28px, 4.5vh, 44px);
  position: relative;
  z-index: 10;
}

/* Main Content Row */
.foundation-main-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: clamp(32px, 4vw, 56px);
  width: 100%;
}

/* Left Column: Glassmorphism Floating Editorial Card */
.foundation-info-col {
  flex: 0 0 clamp(340px, 40%, 500px);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
  background: rgba(14, 20, 32, 0.58);
  backdrop-filter: blur(28px) saturate(190%);
  -webkit-backdrop-filter: blur(28px) saturate(190%);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 28px;
  padding: clamp(30px, 3.8vw, 44px);
  box-shadow: 
    0 24px 60px rgba(0, 0, 0, 0.5), 
    inset 0 1px 1.5px rgba(255, 255, 255, 0.35), 
    inset 0 -1px 1px rgba(0, 0, 0, 0.25);
  transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.foundation-info-col:hover {
  box-shadow: 
    0 30px 70px rgba(0, 0, 0, 0.6), 
    inset 0 1px 2px rgba(255, 255, 255, 0.45);
}

.foundation-eyebrow-wrap {
  display: inline-flex;
  align-items: center;
  margin-bottom: 8px;
}

.foundation-eyebrow {
  font-family: var(--font-sans);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #f59e0b;
  transition: opacity 0.25s ease;
}

.foundation-title {
  margin: 8px 0 18px;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(2.2rem, 3.6vw, 3.2rem);
  font-weight: 600;
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: #ffffff;
  transition: opacity 0.25s ease;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

.foundation-desc {
  font-family: var(--font-sans);
  font-size: clamp(13.5px, 0.98vw, 15px);
  line-height: 1.68;
  color: rgba(255, 255, 255, 0.9);
  transition: opacity 0.25s ease;
  margin-bottom: 26px;
}

.foundation-desc p {
  margin: 0 0 14px;
}

.foundation-desc p:last-child {
  margin-bottom: 0;
}

/* Action Row & Glassmorphic Buttons */
.foundation-actions-row {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  transition: opacity 0.25s ease;
}

.foundation-donate-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 38px;
  border-radius: 9999px;
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.35);
  font-family: var(--font-sans);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s ease;
  box-shadow: 0 8px 24px rgba(245, 158, 11, 0.38);
  outline: none;
}

.foundation-donate-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(245, 158, 11, 0.55);
  filter: brightness(1.1);
}

.foundation-donate-btn:active {
  transform: scale(0.96);
}

.foundation-donate-btn .donate-heart {
  color: #ffffff;
  animation: heartPulseMini 2s infinite;
}

@keyframes heartPulseMini {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.18); }
}

/* Book Button for Classes, Birthday & Private Events */
.foundation-book-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 38px;
  border-radius: 9999px;
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.35);
  font-family: var(--font-sans);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s ease;
  box-shadow: 0 8px 24px rgba(245, 158, 11, 0.38);
  outline: none;
}

.foundation-book-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(245, 158, 11, 0.55);
  filter: brightness(1.1);
}

.foundation-book-btn:active {
  transform: scale(0.96);
}

/* Offerings Button (Glassmorphism Frosted Outline) */
.foundation-offerings-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 13px 26px;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.12);
  color: #ffffff;
  border: 1.5px solid rgba(255, 255, 255, 0.32);
  font-family: var(--font-sans);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s ease;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  outline: none;
}

.foundation-offerings-btn:hover {
  background: #ffffff;
  color: #0b0f19;
  border-color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(255, 255, 255, 0.3);
}

.foundation-offerings-btn:active {
  transform: scale(0.96);
}

/* Right Column: Horizontal Cards Slider Track */
.foundation-cards-viewport {
  flex: 1;
  overflow: hidden;
  padding: 12px 0 24px;
  position: relative;
  mask-image: linear-gradient(90deg, #000 80%, transparent 100%);
  -webkit-mask-image: linear-gradient(90deg, #000 80%, transparent 100%);
}

.foundation-cards-track {
  display: flex;
  gap: 20px;
  transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
  will-change: transform;
}

/* Glassmorphism Cards */
.foundation-card {
  flex: 0 0 clamp(190px, 20vw, 230px);
  height: clamp(280px, 30vw, 340px);
  border-radius: 22px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
  transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
  border: 2px solid rgba(255, 255, 255, 0.2);
  background: #0b0f19;
  outline: none;
}

.foundation-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 24px 50px rgba(0, 0, 0, 0.6);
  border-color: rgba(255, 255, 255, 0.45);
}

.foundation-card.is-active {
  border-color: #f59e0b;
  box-shadow: 0 20px 48px rgba(245, 158, 11, 0.45), inset 0 0 15px rgba(245, 158, 11, 0.2);
  transform: translateY(-4px);
}

.card-bg-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s ease;
}

.foundation-card:hover .card-bg-img {
  transform: scale(1.06);
}

.card-gradient-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 35%, rgba(8, 12, 22, 0.88) 100%);
  pointer-events: none;
}

.card-content-overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 20px 18px;
  color: #ffffff;
  z-index: 2;
  pointer-events: none;
  background: linear-gradient(180deg, transparent 0%, rgba(8, 12, 22, 0.65) 40%, rgba(8, 12, 22, 0.92) 100%);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
}

.card-category-line {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.85);
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
}

.card-category-line .dash {
  color: #f59e0b;
  font-weight: 700;
}

.card-main-heading {
  font-family: 'Bebas Neue', var(--font-condensed), sans-serif;
  font-size: 24px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  line-height: 1.05;
  color: #ffffff;
  margin: 0;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
}

/* Bottom Controls Bar: Glassmorphic Dock */
.foundation-controls-bar {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: rgba(14, 20, 32, 0.55);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.16);
  border-radius: 9999px;
  padding: 10px 24px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35), inset 0 1px 1px rgba(255, 255, 255, 0.2);
}

.foundation-arrow-buttons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.foundation-circle-btn {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: 1.5px solid rgba(255, 255, 255, 0.28);
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s ease;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  outline: none;
}

.foundation-circle-btn:hover {
  border-color: #ffffff;
  background: #ffffff;
  color: #0b0f19;
  transform: scale(1.05);
}

.foundation-progress-track {
  flex: 1;
  margin: 0 clamp(24px, 4vw, 56px);
  height: 2px;
  background: rgba(255, 255, 255, 0.22);
  position: relative;
  border-radius: 2px;
  overflow: hidden;
}

.foundation-progress-fill {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 20%;
  background: #f59e0b;
  box-shadow: 0 0 10px rgba(245, 158, 11, 0.5);
  transition: width 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.foundation-counter-display {
  min-width: 60px;
  text-align: right;
}

.foundation-counter-num {
  font-family: 'Bebas Neue', var(--font-condensed), sans-serif;
  font-size: 48px;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: 0.04em;
  line-height: 1;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
}

/* Responsive Breakpoints */
@media (max-width: 960px) {
  .foundation-main-row {
    flex-direction: column;
    align-items: flex-start;
  }
  .foundation-info-col {
    flex: none;
    width: 100%;
    max-width: 640px;
  }
  .foundation-cards-viewport {
    width: 100%;
    mask-image: none;
    -webkit-mask-image: none;
  }
}

@media (max-width: 640px) {
  .foundation-section {
    padding: 70px 18px 80px;
  }
  .foundation-info-col {
    padding: 24px;
    border-radius: 20px;
  }
  .foundation-card {
    flex: 0 0 180px;
    height: 260px;
  }
  .foundation-title {
    font-size: 2rem;
  }
  .foundation-circle-btn {
    width: 42px;
    height: 42px;
  }
  .foundation-counter-num {
    font-size: 40px;
  }
  .foundation-controls-bar {
    padding: 8px 16px;
  }
}
'''
print("Glassmorphism CSS length:", len(css))
