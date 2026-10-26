svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24">
  <defs>
    <linearGradient id="rainbowHeart" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff0055"/>
      <stop offset="20%" stop-color="#ff5500"/>
      <stop offset="40%" stop-color="#ffcc00"/>
      <stop offset="60%" stop-color="#00e676"/>
      <stop offset="80%" stop-color="#00b0ff"/>
      <stop offset="100%" stop-color="#9d00ff"/>
    </linearGradient>
  </defs>
  <path fill="url(#rainbowHeart)" d="M 12 21.35 l -1.45 -1.32 C 5.4 15.36 2 12.28 2 8.5 C 2 5.42 4.42 3 7.5 3 c 1.74 0 3.41 0.81 4.5 2.09 C 13.09 3.81 14.76 3 16.5 3 c 3.08 0 5.5 2.42 5.5 5.5 c 0 3.78 -3.4 6.86 -8.55 11.54 L 12 21.35 z"/>
</svg>'''

with open('/home/user/full_heart.svg', 'w') as f:
    f.write(svg)

import subprocess
res = subprocess.run(['convert', '/home/user/full_heart.svg', '/home/user/full_heart.png'], capture_output=True, text=True)
print("Return code:", res.returncode)
print("Stderr:", res.stderr)
