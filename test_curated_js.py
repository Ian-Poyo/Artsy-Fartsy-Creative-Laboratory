js = '''
// ============================================================
// CURATED CAROUSELS (FUNKY TWIST 3D SHOWCASE CONTROLLER)
// ============================================================
(function(){
  var funkyChapters = [
    {
      id: 'funky-twist',
      title: 'Funky Twist',
      subtitle: 'Desktop',
      index: '01',
      category: 'A LAB FOR THE UNCONVENTIONAL',
      headline: 'For ideas that refuse to stay inside the lines.',
      desc: 'An experimental sanctuary where strange ideas take shape, materials are pushed to their breaking points, and creativity has no single direction.',
      sceneId: 'scene-starry',
      modalId: 'homeModal',
      topicIndex: 0
    },
    {
      id: 'floating-studio',
      title: 'Floating Studio',
      subtitle: 'Workshops',
      index: '02',
      category: 'CLASSES, WORKSHOPS & ATELIER',
      headline: 'Weekly classes, adult workshops, and open atelier in Carmel.',
      desc: 'Hands-on playful art exploration thoughtfully designed by educators to spark open-ended, process-based discovery across ceramics, printmaking, and glaze.',
      sceneId: 'scene-classroom',
      modalId: 'classesModal',
      topicIndex: 1
    },
    {
      id: 'color-magic',
      title: 'Color Magic',
      subtitle: 'Celebrations',
      index: '03',
      category: 'UNFORGETTABLE CELEBRATIONS',
      headline: 'Vibrant art parties dipped in joy, clay sculpting, and confetti.',
      desc: 'Celebrate your milestone with personalized painting, tactile clay sculpting, and guided mess-making where every guest creates a keepsake.',
      sceneId: 'scene-birthday',
      modalId: 'classesModal',
      topicIndex: 2
    },
    {
      id: 'cloud-vision',
      title: 'Cloud Vision',
      subtitle: 'Retreats',
      index: '04',
      category: 'COLLABORATIVE RETREATS',
      headline: 'Inspiring collaborative workshops and vision sessions in the clouds.',
      desc: 'Energize your organization with collaborative creative challenges designed to unlock breakthrough thinking, strategic clarity, and team synergy.',
      sceneId: 'scene-presentation',
      modalId: 'foundationModal',
      topicIndex: 3
    },
    {
      id: 'garden-twilight',
      title: 'Garden Twilight',
      subtitle: 'Evenings',
      index: '05',
      category: 'PRIVATE PARTIES & GATHERINGS',
      headline: 'Intimate celebratory gatherings under sunlit canopies and twilight.',
      desc: 'Tailored private evenings featuring guided art projects, lush floral settings, live music, and warm hospitality for your closest friends and family.',
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
  var categoryTag = document.getElementById('funkyCategoryTag');
  var metaIndex = document.getElementById('funkyMetaIndex');
  var headline = document.getElementById('funkyHeadline');
  var desc = document.getElementById('funkyDesc');
  var heroJumpBtn = document.getElementById('funkyHeroJumpBtn');
  var modalBtn = document.getElementById('funkyModalBtn');
  var detailsCard = document.getElementById('funkyDetailsCard');
  var viewport = document.getElementById('funkyViewport');

  function updateSlots() {
    cards.forEach(function(card) {
      var cardIdx = parseInt(card.getAttribute('data-index'), 10);
      var diff = (cardIdx - currentIndex + funkyChapters.length) % funkyChapters.length;
      if (diff === 0) {
        card.setAttribute('data-slot', '0');
        card.setAttribute('aria-hidden', 'false');
      } else if (diff === 1) {
        card.setAttribute('data-slot', '1');
        card.setAttribute('aria-hidden', 'true');
      } else if (diff === funkyChapters.length - 1) {
        card.setAttribute('data-slot', '-1');
        card.setAttribute('aria-hidden', 'true');
      } else {
        card.setAttribute('data-slot', 'deep');
        card.setAttribute('aria-hidden', 'true');
      }
    });

    var chapter = funkyChapters[currentIndex];

    // Smoothly update title
    if (activeTitle) {
      activeTitle.style.opacity = '0';
      activeTitle.style.transform = 'translateY(4px)';
      setTimeout(function() {
        activeTitle.textContent = chapter.title;
        activeTitle.style.opacity = '1';
        activeTitle.style.transform = 'translateY(0)';
      }, 200);
    }

    // Smoothly update details drawer
    if (detailsCard) {
      detailsCard.style.opacity = '0.4';
      detailsCard.style.transform = 'translateY(4px)';
      setTimeout(function() {
        if (categoryTag) categoryTag.textContent = chapter.category;
        if (metaIndex) metaIndex.textContent = chapter.index + ' / 05';
        if (headline) headline.textContent = chapter.headline;
        if (desc) desc.textContent = chapter.desc;
        if (modalBtn) modalBtn.setAttribute('data-modal', chapter.modalId);
        detailsCard.style.opacity = '1';
        detailsCard.style.transform = 'translateY(0)';
      }, 200);
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
    currentIndex = (newIdx + funkyChapters.length) % funkyChapters.length;
    updateSlots();
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

  // Click on cards to bring them into center
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

  // Keyboard navigation when Curated Section is visible
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
      var chapter = funkyChapters[currentIndex];
      if (window.jumpToHeroTopic) {
        window.jumpToHeroTopic(chapter.topicIndex);
      }
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Initial slot assignment
  updateSlots();
})();
'''
print("JS length:", len(js))
