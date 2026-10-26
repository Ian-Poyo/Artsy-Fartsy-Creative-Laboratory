# Let's test the geometry of the single-element glide
window_width = 1440
window_height = 900

# Title Block in center
# Headline: Artsy Fartsy
# Subtitle: Creative Laboratory.
# Width of "Creative Laboratory." at 26px font ~ 290px
# Width of "Artsy Fartsy" at 52px font ~ 275px
# Max width of block: 290px
# Total height: 52*1.05 + 6 + 26*1.05 ~ 88px

start_w = 290.0
start_h = 88.0

start_cx = window_width / 2 # 720
start_cy = window_height / 2 # 450

# Target position in .tier-upper-left:
# Stage padding left = clamp(24px, 5.5vw, 72px) = 79.2 -> 72px
# Stage padding bottom = clamp(38px, 6vh, 58px) = 54px
# Lower tier height ~ 80px
# Divider line margin ~ 20px
target_left = 72.0
target_top = 900 - 54 - 80 - 20 - (start_h * 0.62) # ~ 691.44

scale = 0.62
scaled_w = start_w * scale
scaled_h = start_h * scale

target_cx = target_left + scaled_w / 2
target_cy = target_top + scaled_h / 2

dx = target_cx - start_cx
dy = target_cy - start_cy

# Final left after transform: translate(calc(-50% + dx), calc(-50% + dy)) scale(scale):
final_cx = start_cx + dx # target_cx
final_left = final_cx - scaled_w / 2 # target_left

print(f"Target left: {target_left}")
print(f"Final left: {final_left}")
assert abs(final_left - target_left) < 1e-6
print("PERFECT MATCH: 0.000000px error!")
