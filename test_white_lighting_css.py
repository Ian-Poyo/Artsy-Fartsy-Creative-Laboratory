css = '''
/* ============================================================
   SECTION 2: FRIENDS OF ARTSY FARTSY FOUNDATION SHOWCASE
   Pure White Minimalist Theme with Glassmorphic Buttons
   Enhanced Lighting & Automatic 3-Second Loop
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

/* Enlarged Background Image Stage (Active Slide Image Fills Area with Pure Lighting) */
.foundation-stage-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center 30%;
  transition: opacity 0.45s ease;
  z-index: 0;
  will-change: opacity, transform;
  transform: scale(1.02);
  filter: brightness(1.02) contrast(1.04);
}

/* Luminous Ambient Contrast Scrim (Clear, Vibrant & Bright Lighting) */
.foundation-scrim-overlay {
  position: absolute;
  inset: 0;
  background: 
    radial-gradient(circle at 75% 30%, rgba(255, 255, 255, 0.07) 0%, transparent 50%),
    linear-gradient(90deg, rgba(8, 11, 18, 0.92) 0%, rgba(8, 11, 18, 0.78) 36%, rgba(8, 11, 18, 0.12) 68%, rgba(8, 11, 18, 0.28) 100%),
    linear-gradient(180deg, rgba(8, 11, 18, 0.35) 0%, transparent 25%, transparent 75%, rgba(8, 11, 18, 0.85) 100%);
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

/* Left Column: Clean Editorial Floating Content (NO card wrapper) */
.foundation-info-col {
  flex: 0 0 clamp(320px, 38%, 480px);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
  background: transparent;
  border: none;
  box-shadow: none;
  padding: 0;
}

.foundation-eyebrow-wrap {
  display: inline-flex;
  align-items: center;
  margin-bottom: 8px;
}

/* Pure White Eyebrow Text (Yellow Removed) */
.foundation-eyebrow {
  font-family: var(--font-sans);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #ffffff;
  opacity: 0.95;
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
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
}

.foundation-desc {
  font-family: var(--font-sans);
  font-size: clamp(13.5px, 1vw, 15px);
  line-height: 1.68;
  color: rgba(255, 255, 255, 0.92);
  transition: opacity 0.25s ease;
  margin-bottom: 28px;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
}

.foundation-desc p {
  margin: 0 0 14px;
}

.foundation-desc p:last-child {
  margin-bottom: 0;
}

/* Action Row & Glassmorphic White Buttons */
.foundation-actions-row {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  transition: opacity 0.25s ease;
}

/* Pure White Glassmorphism Donate Button (Yellow Removed) */
.foundation-donate-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 40px;
  border-radius: 9999px;
  background: #ffffff;
  color: #0b0f19;
  border: 1.5px solid #ffffff;
  font-family: var(--font-sans);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
  box-shadow: 
    0 10px 30px rgba(0, 0, 0, 0.35),
    0 0 20px rgba(255, 255, 255, 0.3),
    inset 0 1px 1px #ffffff;
  outline: none;
}

.foundation-donate-btn:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.92);
  color: #000000;
  box-shadow: 
    0 14px 36px rgba(0, 0, 0, 0.45),
    0 0 30px rgba(255, 255, 255, 0.55);
}

.foundation-donate-btn:active {
  transform: scale(0.96);
}

.foundation-donate-btn .donate-heart {
  color: #e11d48;
  animation: heartPulseMini 2s infinite;
}

@keyframes heartPulseMini {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.18); }
}

/* Pure White Glassmorphism Book Button (Yellow Removed) */
.foundation-book-btn {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 14px 38px;
  border-radius: 9999px;
  background: #ffffff;
  color: #0b0f19;
  border: 1.5px solid #ffffff;
  font-family: var(--font-sans);
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
  box-shadow: 
    0 10px 30px rgba(0, 0, 0, 0.35),
    0 0 20px rgba(255, 255, 255, 0.3),
    inset 0 1px 1px #ffffff;
  outline: none;
}

.foundation-book-btn:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.92);
  color: #000000;
  box-shadow: 
    0 14px 36px rgba(0, 0, 0, 0.45),
    0 0 30px rgba(255, 255, 255, 0.55);
}

.foundation-book-btn:active {
  transform: scale(0.96);
}

/* Glassmorphism Offerings Button */
.foundation-offerings-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 13px 26px;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(20px) saturate(190%);
  -webkit-backdrop-filter: blur(20px) saturate(190%);
  color: #ffffff;
  border: 1.5px solid rgba(255, 255, 255, 0.38);
  box-shadow: 
    0 8px 24px rgba(0, 0, 0, 0.25),
    inset 0 1px 1px rgba(255, 255, 255, 0.4);
  font-family: var(--font-sans);
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
  outline: none;
}

.foundation-offerings-btn:hover {
  background: rgba(255, 255, 255, 0.25);
  color: #ffffff;
  border-color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 
    0 12px 30px rgba(0, 0, 0, 0.35),
    0 0 20px rgba(255, 255, 255, 0.35);
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

/* Cards with Bright Luminous Lighting */
.foundation-card {
  flex: 0 0 clamp(190px, 20vw, 230px);
  height: clamp(280px, 30vw, 340px);
  border-radius: 20px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45);
  transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
  border: 2px solid rgba(255, 255, 255, 0.22);
  background: #0b0f19;
  outline: none;
}

.foundation-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 24px 50px rgba(0, 0, 0, 0.6), 0 0 20px rgba(255, 255, 255, 0.25);
  border-color: rgba(255, 255, 255, 0.6);
}

/* Pure White Luminous Active Card Border (Yellow Removed) */
.foundation-card.is-active {
  border: 2.5px solid #ffffff;
  box-shadow: 
    0 20px 48px rgba(0, 0, 0, 0.55),
    0 0 26px rgba(255, 255, 255, 0.4),
    inset 0 0 15px rgba(255, 255, 255, 0.12);
  transform: translateY(-4px);
}

.card-bg-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  filter: brightness(1.05) contrast(1.04);
  transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), filter 0.6s ease;
}

.foundation-card:hover .card-bg-img {
  transform: scale(1.06);
  filter: brightness(1.08) contrast(1.06);
}

/* Refined Scrim letting natural light pour in */
.card-gradient-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 48%, rgba(6, 8, 14, 0.85) 100%);
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

/* Pure White Category Line (Yellow Removed) */
.card-category-line {
  font-family: var(--font-sans);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.92);
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
}

/* White Dash (Yellow Removed) */
.card-category-line .dash {
  color: #ffffff;
  font-weight: 700;
  opacity: 0.9;
}

.card-main-heading {
  font-family: 'Bebas Neue', var(--font-condensed), sans-serif;
  font-size: 24px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  line-height: 1.05;
  color: #ffffff;
  margin: 0;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6);
}

/* Bottom Controls Bar */
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

/* Glassmorphism Circle Arrow Buttons */
.foundation-circle-btn {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(18px) saturate(180%);
  -webkit-backdrop-filter: blur(18px) saturate(180%);
  border: 1.5px solid rgba(255, 255, 255, 0.32);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s ease;
  box-shadow: 
    0 8px 20px rgba(0, 0, 0, 0.25),
    inset 0 1px 1px rgba(255, 255, 255, 0.4);
  outline: none;
}

.foundation-circle-btn:hover {
  border-color: #ffffff;
  background: rgba(255, 255, 255, 0.28);
  color: #ffffff;
  transform: scale(1.06);
  box-shadow: 
    0 12px 28px rgba(0, 0, 0, 0.35),
    0 0 16px rgba(255, 255, 255, 0.4);
}

/* Pure White Progress Bar (Yellow Removed) */
.foundation-progress-track {
  flex: 1;
  margin: 0 clamp(24px, 4vw, 56px);
  height: 2.5px;
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
  background: #ffffff;
  box-shadow: 0 0 14px rgba(255, 255, 255, 0.95);
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
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.6);
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
print("White Lighting CSS len:", len(css))
