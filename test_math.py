# Simulate window and elements
window_width = 1440
window_height = 900

# Suppose .hero-editorial-stage padding is 72px left, 58px bottom
# .tier-upper is above line
# Title block resting position:
final_left = 72
final_bottom = 900 - 58 - 22 - 18 # Stage bottom padding + divider margin + tier gap
final_height = 100
final_top = final_bottom - final_height
final_width = 460

final_cx = final_left + final_width / 2 # 72 + 230 = 302
final_cy = final_top + final_height / 2 # ~752

viewport_cx = window_width / 2 # 720
viewport_cy = window_height / 2 # 450

tx = viewport_cx - final_cx # 720 - 302 = 418
ty = viewport_cy - final_cy # 450 - 752 = -302

print(f"Rest center: ({final_cx}, {final_cy})")
print(f"Viewport center: ({viewport_cx}, {viewport_cy})")
print(f"tx: {tx}, ty: {ty}")

# When transformed by translate(tx, ty) with scale 1.55 around center (transform-origin: center center):
# Scaled center = Rest center + (tx, ty) = (final_cx + tx, final_cy + ty) = (viewport_cx, viewport_cy)
print(f"Resulting center: ({final_cx + tx}, {final_cy + ty}) == ({viewport_cx}, {viewport_cy}) -> TRUE DEAD CENTER!")
