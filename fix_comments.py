with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix Floating classroom comment
bad_1 = '''</script>

// ============================================================
// FLOATING CLASSROOM SCENE ENGINES (CANVAS 2D & WEBGL SHADER) - OPTIMIZED SLEEP MODE
// ============================================================
<script>'''

good_1 = '''</script>
<script>
// ============================================================
// FLOATING CLASSROOM SCENE ENGINES (CANVAS 2D & WEBGL SHADER) - OPTIMIZED SLEEP MODE
// ============================================================'''

if bad_1 in text:
    text = text.replace(bad_1, good_1, 1)
    print("Fixed comment block 1!")
else:
    print("WARNING: bad_1 not found!")

# 2. Fix Happy birthday comment
bad_2 = '''</script>
// ============================================================
// HAPPY BIRTHDAY SCENE ENGINES (CANVAS 2D & WEBGL SHADER) - OPTIMIZED SLEEP MODE
// ============================================================
<script>'''

good_2 = '''</script>
<script>
// ============================================================
// HAPPY BIRTHDAY SCENE ENGINES (CANVAS 2D & WEBGL SHADER) - OPTIMIZED SLEEP MODE
// ============================================================'''

if bad_2 in text:
    text = text.replace(bad_2, good_2, 1)
    print("Fixed comment block 2!")
else:
    print("WARNING: bad_2 not found!")

with open('/home/user/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved cleaned file!")
