# Clean, standard, well-formed heart path with explicit spaces and commands
clean_svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24">
  <path fill="red" d="M 12 21.35 L 10.55 20.03 C 5.4 15.36 2 12.28 2 8.5 C 2 5.42 4.42 3 7.5 3 C 9.24 3 10.91 3.81 12 5.09 C 13.09 3.81 14.76 3 16.5 3 C 19.58 3 22 8.5 22 8.5 C 22 12.28 18.6 15.36 13.45 20.04 L 12 21.35 Z"/>
</svg>'''

with open('/home/user/clean_heart.svg', 'w') as f:
    f.write(clean_svg)

print("Wrote clean_heart.svg")
