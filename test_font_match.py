# Let's test font sizes and heights across screen widths:
# 1920 (large desktop), 1440 (standard desktop), 1280 (laptop), 768 (tablet), 390 (mobile)
screen_widths = [1920, 1440, 1280, 768, 390]

for vw in screen_widths:
    # Centered Start Typography:
    # Primary: clamp(3.2rem, 6.8vw, 5.2rem)
    p_start = max(3.2 * 16, min(vw * 0.068, 5.2 * 16))
    # Secondary: clamp(1.35rem, 2.1vw, 1.8rem)
    s_start = max(1.35 * 16, min(vw * 0.021, 1.8 * 16))
    
    # Docked Typography:
    # Primary: clamp(2.2rem, 3.8vw, 3.2rem)
    p_dock = max(2.2 * 16, min(vw * 0.038, 3.2 * 16))
    # Secondary: clamp(0.92rem, 1.15vw, 1.12rem)
    s_dock = max(0.92 * 16, min(vw * 0.0115, 1.12 * 16))
    
    # Scale is p_dock / p_start
    scale = p_dock / p_start
    
    # Scaled secondary size during flight:
    s_flight = s_start * scale
    
    diff = abs(s_flight - s_dock)
    print(f"vw={vw}px: Start Secondary={s_start:.1f}px, Docked Secondary={s_dock:.1f}px, Flight Secondary={s_flight:.1f}px, Diff={diff:.2f}px")
