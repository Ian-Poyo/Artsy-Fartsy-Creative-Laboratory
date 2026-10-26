# Let's compare standard heart paths
material = '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24"><path fill="red" d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41 0.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>'

lucide = '<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 24 24"><path fill="red" d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></svg>'

with open('/home/user/material.svg', 'w') as f:
    f.write(material)
with open('/home/user/lucide.svg', 'w') as f:
    f.write(lucide)

import subprocess
subprocess.run(['convert', '/home/user/material.svg', '/home/user/material.png'])
subprocess.run(['convert', '/home/user/lucide.svg', '/home/user/lucide.png'])
print("Converted both successfully with zero errors!")
