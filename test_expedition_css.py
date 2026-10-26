css = '''
/* ============================================================
   SECTION 2: ARTSY FARTSY EXPEDITIONS SHOWCASE (PIN DESIGN)
   Clean White Background with Horizontal Card Slider
   ============================================================ */
.expedition-section {
  position: relative;
  width: 100%;
  min-height: 100vh;
  padding: clamp(80px, 11vh, 130px) clamp(24px, 5vw, 64px) clamp(80px, 12vh, 130px);
  box-sizing: border-box;
  background-color: #ffffff;
  color: #0f172a;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  z-index: 20;
}

.expedition-container {
  width: 100%;
  max-width: 1360px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: clamp(36px, 5.5vh, 56px);
  position: relative;
  z-index: 10;
}

/* Top Row: Left Info & Right Horizontal Cards */
.expedition-main-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: clamp(32px, 4vw, 56px);
  width: 100%;
}

/* Left Column: Active Experience Details */
.expedition-info-col {
  flex: 0 0 clamp(300px, 34%, 430px);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
}

.expedition-eyebrow-wrap {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 8px;
}

.eyebrow-dash {
  color: #d97706;
  font-weight: 700;
  font-size: 16px;
}

.expedition-eyebrow {
  font-family: var(--font-sans);
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #d97706;
  transition: opacity 0.25s ease;
}

.expedition-title {
  margin: 8px 0 16px;
  font-family: 'Bebas Neue', var(--font-condensed), sans-serif;
  font-size: clamp(3.6rem, 6.2vw, 5.8rem);
  line-height: 0.92;
  letter-spacing: 0.02em;
  color: #0f172a;
  text-transform: uppercase;
  transition: opacity 0.25s ease;
}

.expedition-desc {
  margin: 0 0 28px;
  font-family: var(--font-sans);
  font-size: 14.5px;
  line-height: 1.65;
  color: #475569;
  max-width: 420px;
  transition: opacity 0.25s ease;
}

/* Action Buttons Matching Pin Layout */
.expedition-actions-row {
  display: flex;
  align-items: center;
  gap: 14px;
}

.expedition-bookmark-btn {
  width: 46px;
  height: 46px;
  border-radius: 9999px;
  background: #f59e0b;
  color: #ffffff;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 6px 18px rgba(245, 158, 11, 0.35);
  transition: transform 0.2s ease, background 0.2s ease;
  outline: none;
}

.expedition-bookmark-btn:hover {
  transform: scale(1.08);
  background: #d97706;
}

.expedition-discover-btn {
  padding: 12px 28px;
  border-radius: 9999px;
  border: 1.5px solid #0f172a;
  background: transparent;
  color: #0f172a;
  font-family: var(--font-sans);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.25s ease;
  outline: none;
}

.expedition-discover-btn:hover {
  background: #0f172a;
  color: #ffffff;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(15, 23, 42, 0.25);
}

.expedition-modal-btn {
  background: none;
  border: none;
  font-family: var(--font-sans);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #64748b;
  cursor: pointer;
  transition: color 0.2s ease, transform 0.2s ease;
  padding: 12px 4px;
}

.expedition-modal-btn:hover {
  color: #0f172a;
  transform: translateX(3px);
}

/* Right Column: Horizontal Cards Slider Track */
.expedition-cards-viewport {
  flex: 1;
  overflow: hidden;
  padding: 12px 0 24px;
  position: relative;
  mask-image: linear-gradient(90deg, #000 75%, transparent 100%);
  -webkit-mask-image: linear-gradient(90deg, #000 75%, transparent 100%);
}

.expedition-cards-track {
  display: flex;
  gap: 20px;
  transition: transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1);
  will-change: transform;
}

/* Cards Matching Pin Design */
.expedition-card {
  flex: 0 0 clamp(200px, 22vw, 240px);
  height: clamp(300px, 34vw, 360px);
  border-radius: 20px;
  overflow: hidden;
  position: relative;
  cursor: pointer;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.12);
  transition: transform 0.35s ease, box-shadow 0.35s ease, border-color 0.35s ease;
  border: 2.5px solid transparent;
  background: #e2e8f0;
  outline: none;
}

.expedition-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 22px 46px rgba(0, 0, 0, 0.18);
}

.expedition-card.is-active {
  border-color: #f59e0b;
  box-shadow: 0 20px 48px rgba(245, 158, 11, 0.3);
  transform: translateY(-4px);
}

.card-bg-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s ease;
}

.expedition-card:hover .card-bg-img {
  transform: scale(1.06);
}

.card-gradient-scrim {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 35%, rgba(0, 0, 0, 0.82) 100%);
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
  font-size: 25px;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  line-height: 1.05;
  color: #ffffff;
  margin: 0;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
}

/* Bottom Controls Bar Matching Pin Layout */
.expedition-controls-bar {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.expedition-arrow-buttons {
  display: flex;
  align-items: center;
  gap: 12px;
}

.expedition-circle-btn {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 1.5px solid rgba(15, 23, 42, 0.25);
  background: transparent;
  color: #0f172a;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s ease;
  outline: none;
}

.expedition-circle-btn:hover {
  border-color: #0f172a;
  background: #0f172a;
  color: #ffffff;
  transform: scale(1.05);
}

.expedition-progress-track {
  flex: 1;
  margin: 0 clamp(24px, 4vw, 56px);
  height: 2px;
  background: rgba(15, 23, 42, 0.12);
  position: relative;
  border-radius: 2px;
  overflow: hidden;
}

.expedition-progress-fill {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 20%;
  background: #0f172a;
  transition: width 0.4s cubic-bezier(0.2, 0.8, 0.2, 1);
}

.expedition-counter-display {
  min-width: 60px;
  text-align: right;
}

.expedition-counter-num {
  font-family: 'Bebas Neue', var(--font-condensed), sans-serif;
  font-size: 52px;
  font-weight: 700;
  color: #0f172a;
  letter-spacing: 0.04em;
  line-height: 1;
}

/* Responsive Breakpoints */
@media (max-width: 960px) {
  .expedition-main-row {
    flex-direction: column;
    align-items: flex-start;
  }
  .expedition-info-col {
    flex: none;
    width: 100%;
    max-width: 600px;
  }
  .expedition-cards-viewport {
    width: 100%;
    mask-image: none;
    -webkit-mask-image: none;
  }
}

@media (max-width: 640px) {
  .expedition-section {
    padding: 70px 18px 80px;
  }
  .expedition-card {
    flex: 0 0 190px;
    height: 280px;
  }
  .expedition-title {
    font-size: 3.4rem;
  }
  .expedition-circle-btn {
    width: 44px;
    height: 44px;
  }
  .expedition-counter-num {
    font-size: 42px;
  }
}
'''
print("CSS valid, len:", len(css))
