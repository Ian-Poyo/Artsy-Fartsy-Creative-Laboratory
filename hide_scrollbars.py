with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_block = '''html {
  scroll-behavior: smooth;
}

html {
  scroll-behavior: smooth;
  width: 100%;
  min-height: 100%;
}

body {
  width: 100%;
  min-height: 100%;
  margin: 0;
  padding: 0;
  background-color: var(--bg-deep);
  color: var(--text-main);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  overflow-y: auto;
}'''

new_block = '''html {
  scroll-behavior: smooth;
  width: 100%;
  min-height: 100%;
  overflow-x: hidden;
  overflow-y: auto;
  scrollbar-width: none !important;
  -ms-overflow-style: none !important;
}

body {
  width: 100%;
  min-height: 100%;
  margin: 0;
  padding: 0;
  background-color: var(--bg-deep);
  color: var(--text-main);
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  overflow-x: hidden;
  overflow-y: visible;
  scrollbar-width: none !important;
  -ms-overflow-style: none !important;
}

/* Eliminate all browser native scrollbars ("ugly sliders") completely */
html::-webkit-scrollbar,
body::-webkit-scrollbar,
*::-webkit-scrollbar {
  display: none !important;
  width: 0 !important;
  height: 0 !important;
  background: transparent !important;
}

* {
  scrollbar-width: none !important;
  -ms-overflow-style: none !important;
}'''

if old_block in text:
    text = text.replace(old_block, new_block, 1)
    print("Replaced html and body block successfully!")
else:
    print("WARNING: old_block not found, searching with regex...")
    import re
    m = re.search(r'html\s*\{[^}]*\}\s*html\s*\{[^}]*\}\s*body\s*\{[^}]*\}', text)
    if m:
        text = text[:m.start()] + new_block + text[m.end():]
        print("Replaced via regex!")
    else:
        print("Regex failed to match!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved index.html!")
