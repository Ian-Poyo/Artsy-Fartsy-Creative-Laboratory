import subprocess, tempfile

js = '''
// ============================================================
// ARTSY FARTSY EXPEDITIONS SHOWCASE CONTROLLER (PIN DESIGN)
// ============================================================
(function(){
  var chapters = [
    {
      id: 'starry',
      eyebrow: 'A LAB FOR THE UNCONVENTIONAL',
      titleHtml: 'CREATIVE<br>LABORATORY',
      desc: 'An experimental sanctuary where strange ideas take shape, materials are pushed to their breaking points, and creativity has no single direction.',
      modalId: 'homeModal',
      topicIndex: 0
    },
    {
      id: 'classroom',
      eyebrow: 'CLASSES & SPECIAL WORKSHOPS',
      titleHtml: 'FLOATING<br>WORKSHOPS',
      desc: 'Weekly classes, adult workshops, and open atelier in Carmel. Hands-on playful art exploration thoughtfully designed by educators to spark open-ended, process-based discovery.',
      modalId: 'classesModal',
      topicIndex: 1
    },
    {
      id: 'birthday',
      eyebrow: 'UNFORGETTABLE CELEBRATIONS',
      titleHtml: 'COLOR &<br>CONFETTI',
      desc: 'Celebrate your milestone with personalized painting, tactile clay sculpting, and guided mess-making where every guest creates a cherished keepsake.',
      modalId: 'classesModal',
      topicIndex: 2
    },
    {
      id: 'presentation',
      eyebrow: 'COLLABORATIVE INNOVATION',
      titleHtml: 'VISION IN<br>CLOUDS',
      desc: 'Energize your organization with collaborative creative challenges designed to unlock breakthrough thinking, strategic clarity, and team synergy.',
      modalId: 'foundationModal',
      topicIndex: 3
    },
    {
      id: 'party',
      eyebrow: 'PRIVATE EVENINGS & PARTIES',
      titleHtml: 'TWILIGHT<br>SOIRÉES',
      desc: 'Tailored private evenings featuring guided art projects, lush floral settings, live acoustic music, and warm hospitality for your closest friends.',
      modalId: 'donateModal',
      topicIndex: 4
    }
  ];

  var currentIndex = 0;
  var track = document.getElementById('expeditionCardsTrack');
  var cards = document.querySelectorAll('.expedition-card');
  var prevBtn = document.getElementById('expeditionPrevBtn');
  var nextBtn = document.getElementById('expeditionNextBtn');
  var eyebrowEl = document.getElementById('expeditionEyebrow');
  var titleEl = document.getElementById('expeditionTitle');
  var descEl = document.getElementById('expeditionDesc');
  var modalBtn = document.getElementById('expeditionModalBtn');
  var discoverBtn = document.getElementById('expeditionDiscoverBtn');
  var bookmarkBtn = document.getElementById('expeditionBookmarkBtn');
  var progressFill = document.getElementById('expeditionProgressFill');
  var counterNum = document.getElementById('expeditionCounterNum');

  function updateSlider() {
    var chapter = chapters[currentIndex];

    // 1. Update Left Info Column with smooth fade
    if (eyebrowEl && titleEl && descEl) {
      eyebrowEl.style.opacity = '0';
      titleEl.style.opacity = '0';
      descEl.style.opacity = '0';
      setTimeout(function() {
        eyebrowEl.textContent = chapter.eyebrow;
        titleEl.innerHTML = chapter.titleHtml;
        descEl.textContent = chapter.desc;
        if (modalBtn) modalBtn.setAttribute('data-modal', chapter.modalId);
        eyebrowEl.style.opacity = '1';
        titleEl.style.opacity = '1';
        descEl.style.opacity = '1';
      }, 160);
    }

    // 2. Update Cards Track Translation & Active Class
    cards.forEach(function(card, idx) {
      if (idx === currentIndex) {
        card.classList.add('is-active');
        card.setAttribute('aria-selected', 'true');
      } else {
        card.classList.remove('is-active');
        card.setAttribute('aria-selected', 'false');
      }
    });

    if (track && cards.length > 0) {
      var cardW = cards[0].offsetWidth || 220;
      var gap = 20;
      var offset = currentIndex * (cardW + gap);
      track.style.transform = 'translate3d(-' + offset + 'px, 0, 0)';
    }

    // 3. Update Progress Fill & Number Counter
    if (progressFill) {
      var pct = ((currentIndex + 1) / chapters.length) * 100;
      progressFill.style.width = pct + '%';
    }
    if (counterNum) {
      counterNum.textContent = '0' + (currentIndex + 1);
    }
  }

  function goToIndex(newIdx) {
    currentIndex = (newIdx + chapters.length) % chapters.length;
    updateSlider();
  }

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

  cards.forEach(function(card) {
    card.addEventListener('click', function() {
      var idx = parseInt(card.getAttribute('data-index'), 10);
      goToIndex(idx);
    });
  });

  if (discoverBtn) {
    discoverBtn.addEventListener('click', function(e) {
      e.preventDefault();
      var chapter = chapters[currentIndex];
      if (window.jumpToHeroTopic) {
        window.jumpToHeroTopic(chapter.topicIndex);
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  if (bookmarkBtn) {
    bookmarkBtn.addEventListener('click', function(e) {
      e.preventDefault();
      bookmarkBtn.classList.toggle('bookmarked');
      if (bookmarkBtn.classList.contains('bookmarked')) {
        bookmarkBtn.style.background = '#10b981';
      } else {
        bookmarkBtn.style.background = '#f59e0b';
      }
    });
  }

  // Keyboard navigation when section is in view
  window.addEventListener('keydown', function(e) {
    var sec = document.getElementById('curatedSection');
    if (!sec) return;
    var r = sec.getBoundingClientRect();
    var isVisible = (r.top < window.innerHeight && r.bottom > 0);
    if (!isVisible) return;

    if (e.key === 'ArrowRight') goToIndex(currentIndex + 1);
    else if (e.key === 'ArrowLeft') goToIndex(currentIndex - 1);
  });

  // Touch Swipe on viewport
  var touchStartX = 0;
  var viewport = document.getElementById('expeditionCardsViewport');
  if (viewport) {
    viewport.addEventListener('touchstart', function(e) {
      if (e.changedTouches && e.changedTouches[0]) {
        touchStartX = e.changedTouches[0].screenX;
      }
    }, { passive: true });

    viewport.addEventListener('touchend', function(e) {
      if (e.changedTouches && e.changedTouches[0]) {
        var dx = e.changedTouches[0].screenX - touchStartX;
        if (Math.abs(dx) > 40) {
          if (dx < 0) goToIndex(currentIndex + 1);
          else goToIndex(currentIndex - 1);
        }
      }
    }, { passive: true });
  }

  window.addEventListener('resize', updateSlider);

  // Initialize
  updateSlider();
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
