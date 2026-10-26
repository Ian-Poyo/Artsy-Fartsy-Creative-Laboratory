# Check card data and files
import os

images = [
    '/home/user/images/card-starry.webp',
    '/home/user/images/card-classroom.webp',
    '/home/user/images/card-birthday.webp',
    '/home/user/images/card-presentation.jpg',
    '/home/user/images/card-party.webp'
]

for img in images:
    exists = os.path.exists(img)
    size = os.path.getsize(img) if exists else 0
    print(f"{img}: exists={exists}, size={size} bytes")
