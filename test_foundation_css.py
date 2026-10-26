css = '''
/* ============================================================
   SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE
   Inspired by Globe Express Horizontal Card Slider
   Enlarged Active Image Background & Mission Donate CTA
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
  background-position: center 30%;
  transition: opacity 0.45s ease;
  z-index: 0;
  will-change: opacity, transform;
  transform: scale(1.02);
}

/* Cinematic Contrast Scrim Matching Pin Reference */
.foundation-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    linear-gradient(90deg, rgba(8, 12, 22, 0.94) 0%, rgba(8, 12, 22, 0.82) 42%, rgba(8, 12, 22, 0.3) 72%, rgba(8, 12, 22, 0.55) 100%),
    linear-gradient(180deg, rgba(8, 12, 22, 0.45) 0%, transparent 35%, rgba(8, 12, 22, 0.9) 100%);
  pointer-events: none;
  z-index: 1;
}

.foundation-container {
  width: 100%;
  max-width: 1360px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: clamp(32px, 5vh, 48px);
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

/* Left Column: Active Experience Details */
.foundation-info-col {
  flex: 0 0 clamp(320px, 38%, 480px);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
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
  margin: 10px 0 20px;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(2.4rem, 4.2vw, 3.8rem);
  font-weight: 600;
  line-height: 1.08;
  letter-spacing: -0.02em;
  color: #ffffff;
  transition: opacity 0.25s ease;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

.foundation-desc {
  font-family: var(--font-sans);
  font-size: clamp(13.5px, 1vw, 15px);
  line-height: 1.68;
  color: rgba(255, 255, 255, 0.88);
  transition: opacity 0.25s ease;
  margin-bottom: 28px;
}

.foundation-desc p {
  margin: 0 0 14px;
}

.foundation-desc p:last-child {
  margin-bottom: 0;
}

/* Action Row (Bookmark & Offerings removed per user instructions) */
.foundation-actions-row {
  display: flex;
  align-items: center;
  gap: 14px;
}

.foundation-donate-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 40px;
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

/* Right Column: Horizontal Cards Slider Track */
.foundation-cards-viewport {
  flex: 1;
  overflow: hidden;
  padding: 12px 0 24px;
  position: relative;
  mask-image: linear-gradient(90deg, #000 78%, transparent 100%);
  -webkit-mask-image: linear-gradient(90deg, #000 78%, transparent 100%);
}

.foundation-cards-track {
  display: flex;
  gap: 20px;
  transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
  will-change: transform;
}

/* Cards Matching Pin Design */
.foundation-card {
  flex: 0 0 clamp(190px, 20vw, 230px);
  height: clamp(280px, 30vw, 340px);
  border-radius: 20px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4);
  transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
  border: 2.5px solid rgba(255, 255, 255, 0.15);
  background: #0b0f19;
  outline: none;
}

.foundation-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 24px 50px rgba(0, 0, 0, 0.55);
  border-color: rgba(255, 255, 255, 0.35);
}

.foundation-card.is-active {
  border-color: #f59e0b;
  box-shadow: 0 20px 48px rgba(245, 158, 11, 0.4);
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
  background: linear-gradient(180deg, transparent 35%, rgba(0, 0, 0, 0.85) 100%);
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

/* Bottom Controls Bar Matching Pin Layout */
.foundation-controls-bar {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.foundation-arrow-buttons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.foundation-circle-btn {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 1.5px solid rgba(255, 255, 255, 0.3);
  background: rgba(255, 255, 255, 0.08);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s ease;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
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
  background: rgba(255, 255, 255, 0.2);
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
  font-size: 52px;
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
  .foundation-card {
    flex: 0 0 180px;
    height: 260px;
  }
  .foundation-title {
    font-size: 2.2rem;
  }
  .foundation-circle-btn {
    width: 44px;
    height: 44px;
  }
  .foundation-counter-num {
    font-size: 42px;
  }
}
'''
print("CSS valid, len:", len(css))
