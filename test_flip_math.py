# Simulate window and elements
window_width = 1440
window_height = 900

# Center title (State 1)
# Title block is centered in viewport with top: 50%, left: 50%, transform: translate(-50%, -50%)
start_width = 650.0
start_height = 160.0
start_left = (window_width - start_width) / 2 # 395.0
start_top = (window_height - start_height) / 2 # 370.0

# Target ghost in .tier-upper-left (State 2)
# Position in bottom left above divider line
target_width = 440.0
target_height = 95.0
target_left = 72.0
target_top = 710.0

# Scale factor
scale = target_height / start_height # 95 / 160 = ~0.59375
# Or target_width / start_width = 440 / 650 = ~0.6769

print(f"Start rect: left={start_left}, top={start_top}, w={start_width}, h={start_height}")
print(f"Target rect: left={target_left}, top={target_top}, w={target_width}, h={target_height}")

# If we transform from start position:
# In start position, element has:
# left: 50%; top: 50%; transform: translate(-50%, -50%)
# So center is at (window_width/2, window_height/2)
center_x = window_width / 2 # 720
center_y = window_height / 2 # 450

# Target center:
target_center_x = target_left + (start_width * scale) / 2
target_center_y = target_top + (start_height * scale) / 2

dx = target_center_x - center_x
dy = target_center_y - center_y

print(f"Target center: ({target_center_x}, {target_center_y})")
print(f"dx: {dx}, dy: {dy}, scale: {scale}")

# Resulting left and top after translate(calc(-50% + dx), calc(-50% + dy)) scale(scale):
res_center_x = center_x + dx
res_center_y = center_y + dy
res_left = res_center_x - (start_width * scale) / 2
res_top = res_center_y - (start_height * scale) / 2

print(f"Resulting left: {res_left} (matches target_left: {target_left})")
print(f"Resulting top: {res_top} (matches target_top: {target_top})")
