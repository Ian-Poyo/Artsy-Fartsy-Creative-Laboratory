# Check dimensions and styling of emblem
w = 1560
h = 1020
aspect = w / h # 1.5294

# If emblem width is 160px - 220px:
for ew in [140, 180, 200, 220]:
    eh = ew / aspect
    print(f"Emblem width: {ew}px, height: {eh:.1f}px")

