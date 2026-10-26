with open('/home/user/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '''          <!-- Permanently anchored title block (Zero-jump FLIP transition) -->
          <div class="hero-title-block" id="heroTitleBlock" title="Click to replay title transition">
            <h1 class="hero-title-main" id="heroTitleMain">
              <span class="title-line-mask">
                <span class="title-line-inner" id="titleLineInner1">
                  <span class="title-primary" id="titlePrimary">Artsy Fartsy</span>
                </span>
              </span>
              <span class="title-line-mask">
                <span class="title-line-inner" id="titleLineInner2">
                  <span class="title-secondary" id="titleSecondary">Creative Laboratory.</span>
                </span>
              </span>
            </h1>
          </div>'''

replacement = '''          <!-- Permanently anchored title block (Zero-jump FLIP transition) -->
          <div class="hero-title-block" id="heroTitleBlock" title="Click to replay title transition">
            <h1 class="hero-title-main" id="heroTitleMain">
              <span class="title-line-mask">
                <span class="title-line-inner" id="titleLineInner1">
                  <span class="title-primary" id="titlePrimary">Artsy Fartsy</span>
                </span>
              </span>
              <span class="title-line-mask">
                <span class="title-line-inner" id="titleLineInner2">
                  <span class="title-secondary" id="titleSecondary">Creative Laboratory.</span>
                </span>
              </span>
            </h1>
          </div>
          <script>
            (function(){
              try {
                var tb = document.getElementById('heroTitleBlock');
                var p1 = document.getElementById('titlePrimary');
                var p2 = document.getElementById('titleSecondary');
                if(!tb || !p1 || !p2) return;
                var r = tb.getBoundingClientRect();
                var r1 = p1.getBoundingClientRect();
                var r2 = p2.getBoundingClientRect();
                var scale = window.innerWidth < 640 ? 1.35 : (window.innerWidth < 1024 ? 1.5 : 1.62);
                var restCenterX = r.left + r.width / 2;
                var restCenterY = r.top + r.height / 2;
                var tx = (window.innerWidth / 2) - restCenterX;
                var ty = (window.innerHeight / 2) - restCenterY;
                var lineOffset = (r2.width - r1.width) / 2;
                tb.style.transform = 'translate3d(' + tx + 'px, ' + ty + 'px, 0) scale(' + scale + ')';
                p1.style.transform = 'translate3d(' + lineOffset + 'px, 0, 0)';
              } catch(e) {}
            })();
          </script>'''

if target in content:
    content = content.replace(target, replacement, 1)
    with open('/home/user/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added frame-0 immediate synchronous center transform script")
else:
    print("Target block not matched")
