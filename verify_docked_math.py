import math

# Test various viewport sizes
for w, h in [(1920, 1080), (1440, 900), (1280, 800), (768, 1024), (390, 844)]:
    # Simulated start rect (centered title block)
    # Primary font: clamp(3.6rem, 8vw, 6.2rem)
    # Secondary font: clamp(1.8rem, 3.6vw, 2.8rem)
    # Docked font: clamp(2.4rem, 4.4vw, 3.6rem) and clamp(1.4rem, 2.5vw, 2.1rem)
    
    start_w = min(w * 0.85, 680)
    start_h = 160
    
    start_cx = w / 2
    start_cy = h / 2
    start_left = start_cx - start_w / 2
    start_top = start_cy - start_h / 2
    
    # Docked target rect
    target_left = max(24, w * 0.055)
    target_bottom = h - max(38, h * 0.06) - 20 # padding + divider
    target_h = 100
    target_top = target_bottom - target_h
    target_w = min(w * 0.5, 480)
    
    scale = target_h / start_h
    scaled_w = start_w * scale
    scaled_h = start_h * scale
    
    target_cx = target_left + scaled_w / 2
    target_cy = target_top + scaled_h / 2
    
    dx = target_cx - start_cx
    dy = target_cy - start_cy
    
    final_cx = start_cx + dx
    final_cy = start_cy + dy
    final_left = final_cx - scaled_w / 2
    final_top = final_cy - scaled_h / 2
    
    assert abs(final_left - target_left) < 1e-6
    assert abs(final_top - target_top) < 1e-6
    print(f"Viewport {w}x{h}: EXACT MATCH! Left error = {abs(final_left - target_left)}, Top error = {abs(final_top - target_top)}")

print("ALL VIEWPORT MATH 100% PERFECT!")
