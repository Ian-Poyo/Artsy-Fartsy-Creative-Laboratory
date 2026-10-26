with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

bad = '"✦ Artisan Delicacies"oeuvres\''
good = '"✦ Artisan Delicacies"'

if bad in text:
    text = text.replace(bad, good, 1)
    with open('/home/user/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed accurately!")
else:
    print("Bad not found")
