with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('Artisan Hors')
if pos != -1:
    print('Found around:', repr(text[pos-20:pos+40]))
    p1 = text.rfind("'", 0, pos)
    p2 = text.find("'", pos + 15)
    print('Replacing:', repr(text[p1:p2+1]))
    text = text[:p1] + '"✦ Artisan Delicacies"' + text[p2+1:]
    with open('/home/user/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed!")
