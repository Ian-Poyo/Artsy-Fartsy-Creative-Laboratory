import subprocess, tempfile

js = '''
// ============================================================
// CURATED CAROUSELS (FUNKY TWIST 3D SHOWCASE CONTROLLER)
// Elevated for Artsy Fartsy Creative Laboratory Theme
// ============================================================
(function(){
  var chapters = [
    {
      id: 'funky-twist',
      index: '01',
      title: 'Funky Twist',
      subtitle: 'Creative Laboratory',
      category: 'A LAB FOR THE UNCONVENTIONAL',
      headline: 'For ideas that refuse to stay inside the lines.',
      desc: 'An experimental sanctuary where strange ideas take shape, materials are pushed to their breaking points, and creativity has no single direction.',
      tags: ['✦ Process-Based Discovery', '✦ Raw Pigments & Clay', '✦ Carmel Studio', '✦ All Skill Levels'],
      sceneId: 'scene-starry',
      modalId: 'homeModal',
      topicIndex: 0
    },
    {
      id: 'floating-studio',
      index: '02',
      title: 'Floating Studio',
      subtitle: 'Workshops & Atelier',
      category: 'CLASSES & SPECIAL WORKSHOPS',
      headline: 'Weekly classes, adult workshops, and open atelier in Carmel.',
      desc: 'Hands-on playful art exploration thoughtfully designed by educators to spark open-ended, process-based discovery across ceramics, printmaking, and glaze.',
      tags: ['✦ Wheel & Handbuilding', '✦ Specialty Glazes', '✦ Small Cohorts', '✦ Master Instructors'],
      sceneId: 'scene-classroom',
      modalId: 'classesModal',
      topicIndex: 1
    },
    {
      id: 'color-magic',
      index: '03',
      title: 'Color Magic',
      subtitle: 'Celebrations & Joy',
      category: 'UNFORGETTABLE CELEBRATIONS',
      headline: 'Vibrant art parties dipped in joy, clay sculpting, and confetti.',
      desc: 'Celebrate your milestone with personalized painting, tactile clay sculpting, and guided mess-making where every guest creates a keepsake.',
      tags: ['✦ Private Milestone Suites', '✦ Custom Color Palettes', '✦ Keepsake Artworks', '✦ Full Hospitality'],
      sceneId: 'scene-birthday',
      modalId: 'classesModal',
      topicIndex: 2
    },
    {
      id: 'cloud-vision',
      index: '04',
      title: 'Cloud Vision',
      subtitle: 'Retreats & Innovation',
      category: 'COLLABORATIVE RETREATS',
      headline: 'Inspiring collaborative workshops and vision sessions in the clouds.',
      desc: 'Energize your organization with collaborative creative challenges designed to unlock breakthrough thinking, strategic clarity, and team synergy.',
      tags: ['✦ Executive Offsites', '✦ Creative Facilitation', '✦ Synergy Canvases', '✦ Catered Receptions'],
      sceneId: 'scene-presentation',
      modalId: 'foundationModal',
      topicIndex: 3
    },
    {
      id: 'garden-twilight',
      index: '05',
      title: 'Garden Twilight',
      subtitle: 'Private Gatherings',
      category: 'PRIVATE PARTIES & EVENINGS',
      headline: 'Intimate celebratory gatherings under sunlit canopies and twilight.',
      desc: 'Tailored private evenings featuring guided art projects, lush floral settings, live music, and warm hospitality for your closest friends and family.',
      tags: ['✦ Secret Garden Setting', '✦ Candlelit Easels', '✦ Artisan Hors d\\'oeuvres', '✦ Twilight Ambience'],
      sceneId: 'scene-party',
      modalId: 'donateModal',
      topicIndex: 4
    }
  ];

  var currentIndex = 0;
  var isInteracted = false;

  var cards = document.querySelectorAll('.funky-card');
  var prevBtn = document.getElementById('funkyPrevBtn');
  var nextBtn = document.getElementById('funkyNextBtn');
  var handCursor = document.getElementById('funkyHandCursor');
  var activeTitle = document.getElementById('funkyActiveTitle');
  var activeSub = document.getElementById('funkyActiveSub');
  var progressDots = document.querySelectorAll('.p-dot');
  var progressCounter = document.getElementById('funkyProgressCounter');
  var chapterTabs = document.querySelectorAll('.chapter-tab');
  
  var categoryTag = document.getElementById('storyCategoryTag');
  var indexTag = document.getElementById('storyIndexTag');
  var headline = document.getElementById('storyHeadline');
  var desc = document.getElementById('storyDesc');
  var tagsList = document.getElementById('storyTagsList');
  var heroJumpBtn = document.getElementById('storyHeroJumpBtn');
  var modalBtn = document.getElementById('storyModalBtn');
  var drawer = document.getElementById('curatedStoryDrawer');
  var viewport = document.getElementById('funkyViewport');

  function updateSlots() {
    cards.forEach(function(card) {
      card.style.transform = '';
      var cardIdx = parseInt(card.getAttribute('data-index'), 10);
      var diff = (cardIdx - currentIndex + chapters.length) % chapters.length;
      if (diff === 0) {
        card.setAttribute('data-slot', '0');
        card.setAttribute('aria-hidden', 'false');
      } else if (diff === 1) {
        card.setAttribute('data-slot', '1');
        card.setAttribute('aria-hidden', 'true');
      } else if (diff === chapters.length - 1) {
        card.setAttribute('data-slot', '-1');
        card.setAttribute('aria-hidden', 'true');
      } else {
        card.setAttribute('data-slot', 'deep');
        card.setAttribute('aria-hidden', 'true');
      }
    });

    var chapter = chapters[currentIndex];

    // Update Chapter Tabs
    chapterTabs.forEach(function(tab) {
      var tabIdx = parseInt(tab.getAttribute('data-index'), 10);
      if (tabIdx === currentIndex) {
        tab.classList.add('is-active');
        tab.setAttribute('aria-selected', 'true');
      } else {
        tab.classList.remove('is-active');
        tab.setAttribute('aria-selected', 'false');
      }
    });

    // Update Progress Dots
    progressDots.forEach(function(dot) {
      var dotIdx = parseInt(dot.getAttribute('data-index'), 10);
      if (dotIdx === currentIndex) {
        dot.classList.add('is-active');
      } else {
        dot.classList.remove('is-active');
      }
    });

    // Update Counter
    if (progressCounter) {
      progressCounter.textContent = chapter.index + ' / 05';
    }

    // Update Title & Subtitle with smooth fade
    if (activeTitle && activeSub) {
      activeTitle.style.opacity = '0';
      activeTitle.style.transform = 'translateY(4px)';
      activeSub.style.opacity = '0';
      setTimeout(function() {
        activeTitle.textContent = chapter.title;
        activeSub.textContent = chapter.subtitle;
        activeTitle.style.opacity = '1';
        activeTitle.style.transform = 'translateY(0)';
        activeSub.style.opacity = '1';
      }, 180);
    }

    // Update Story & Action Drawer
    if (drawer) {
      drawer.style.opacity = '0.5';
      drawer.style.transform = 'translateY(4px)';
      setTimeout(function() {
        if (categoryTag) categoryTag.textContent = chapter.category;
        if (indexTag) indexTag.textContent = 'CHAPTER ' + chapter.index + ' OF 05';
        if (headline) headline.textContent = chapter.headline;
        if (desc) desc.textContent = chapter.desc;
        if (modalBtn) modalBtn.setAttribute('data-modal', chapter.modalId);
        
        // Update tags
        if (tagsList && chapter.tags) {
          tagsList.innerHTML = chapter.tags.map(function(t) {
            return '<span class="story-tag">' + t + '</span>';
          }).join('');
        }

        drawer.style.opacity = '1';
        drawer.style.transform = 'translateY(0)';
      }, 180);
    }
  }

  function dismissHandPrompt() {
    if (!isInteracted && handCursor) {
      isInteracted = true;
      handCursor.classList.add('is-dismissed');
    }
  }

  function goToIndex(newIdx) {
    dismissHandPrompt();
    currentIndex = (newIdx + chapters.length) % chapters.length;
    updateSlots();
  }

  // Next / Prev button listeners
  if (nextBtn) {
    nextBtn.addEventListener('click', function(e) {
      e.preventDefault();
      goToIndex(currentIndex + 1);
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', function(e) {
      e.preventDefault();
      goToIndex(currentIndex - 1);
    });
  }

  // Chapter tab click listeners
  chapterTabs.forEach(function(tab) {
    tab.addEventListener('click', function(e) {
      e.preventDefault();
      var idx = parseInt(tab.getAttribute('data-index'), 10);
      goToIndex(idx);
    });
  });

  // Progress dot click listeners
  progressDots.forEach(function(dot) {
    dot.addEventListener('click', function(e) {
      e.preventDefault();
      var idx = parseInt(dot.getAttribute('data-index'), 10);
      goToIndex(idx);
    });
  });

  // Direct card click listeners (bringing background cards forward)
  cards.forEach(function(card) {
    card.addEventListener('click', function() {
      var slot = card.getAttribute('data-slot');
      if (slot === '1') {
        goToIndex(currentIndex + 1);
      } else if (slot === '-1') {
        goToIndex(currentIndex - 1);
      }
    });
  });

  // Interactive 3D micro-tilt on mousemove
  if (viewport) {
    viewport.addEventListener('mousemove', function(e) {
      var rect = viewport.getBoundingClientRect();
      var x = (e.clientX - rect.left) / rect.width - 0.5;
      var y = (e.clientY - rect.top) / rect.height - 0.5;
      var activeCard = document.querySelector('.funky-card[data-slot="0"]');
      if (activeCard) {
        var rx = -y * 7;
        var ry = x * 7;
        activeCard.style.transform = 'translate3d(' + (x * 12) + 'px, ' + (y * 8) + 'px, 50px) rotate(' + (-10 + rx) + 'deg) rotateY(' + ry + 'deg)';
      }
    });

    viewport.addEventListener('mouseleave', function() {
      var activeCard = document.querySelector('.funky-card[data-slot="0"]');
      if (activeCard) {
        activeCard.style.transform = '';
      }
    });
  }

  // Touch Swipe support
  var touchStartX = 0;
  var touchStartY = 0;
  if (viewport) {
    viewport.addEventListener('touchstart', function(e) {
      if (e.changedTouches && e.changedTouches[0]) {
        touchStartX = e.changedTouches[0].screenX;
        touchStartY = e.changedTouches[0].screenY;
      }
    }, { passive: true });

    viewport.addEventListener('touchend', function(e) {
      if (e.changedTouches && e.changedTouches[0]) {
        var dx = e.changedTouches[0].screenX - touchStartX;
        var dy = e.changedTouches[0].screenY - touchStartY;
        if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 35) {
          if (dx < 0) goToIndex(currentIndex + 1);
          else goToIndex(currentIndex - 1);
        }
      }
    }, { passive: true });
  }

  // Keyboard navigation
  window.addEventListener('keydown', function(e) {
    var curSection = document.getElementById('curatedSection');
    if (!curSection) return;
    var rect = curSection.getBoundingClientRect();
    var isVisible = (rect.top < window.innerHeight && rect.bottom > 0);
    if (!isVisible) return;

    if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
      goToIndex(currentIndex + 1);
    } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
      goToIndex(currentIndex - 1);
    }
  });

  // Jump to Hero Scene from active chapter
  if (heroJumpBtn) {
    heroJumpBtn.addEventListener('click', function() {
      var chapter = chapters[currentIndex];
      if (window.jumpToHeroTopic) {
        window.jumpToHeroTopic(chapter.topicIndex);
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Initialize slots
  updateSlots();
})();
'''

with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as tf:
    tf.write(js)
    tf_name = tf.name

res = subprocess.run(['node', '--check', tf_name], capture_output=True, text=True)
if res.returncode == 0:
    print("JS syntax is 100% valid!")
else:
    print("Syntax error:", res.stderr)
