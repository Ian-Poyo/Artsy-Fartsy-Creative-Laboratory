import subprocess, tempfile

js = '''
// ============================================================
// FRIENDS OF ARTSY FARTSY FOUNDATION SLIDER CONTROLLER
// 5 Experiences with 3-Second Automatic Loop & Pure White Styling
// ============================================================
(function(){
  var slides = [
    {
      id: 'mission',
      eyebrow: '— Mission Statement',
      title: 'Friends of Artsy Fartsy Foundation',
      descHtml: '<p>Our mission is to ensure accessible, inspiring space for the Artsy Fartsy Creative Laboratory; expand equitable access to the arts through scholarships for high school students and adult learners; and strengthen arts education by delivering high-quality color science professional development for elementary, middle, and high school teachers.</p><p>We believe creativity is a powerful catalyst for learning, expression, and community, and we work to nurture it across ages, disciplines, and classrooms.</p>',
      bgImage: '/images/foundation-music-children.jpg',
      actionsHtml: '<button class=\"foundation-donate-btn\" data-modal=\"donateModal\" aria-label=\"Donate to the Foundation\"><svg class=\"donate-heart\" viewBox=\"0 0 24 24\" width=\"18\" height=\"18\" fill=\"currentColor\"><path d=\"M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z\"/></svg><span>DONATE</span></button>'
    },
    {
      id: 'classes',
      eyebrow: '— Weekly Offerings',
      title: 'Studio Classes & Workshops',
      descHtml: '<p>Join us at our Carmel studio for fun-filled weekly classes, adult workshops, special events, and more! Hands-on playful art exploration thoughtfully designed by educators to spark open-ended, process based discovery.</p>',
      bgImage: '/images/foundation-students.jpg',
      actionsHtml: '<button class=\"foundation-book-btn\" data-modal=\"classesModal\" aria-label=\"Book a class\"><svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"3\" y=\"4\" width=\"18\" height=\"18\" rx=\"2\" ry=\"2\"></rect><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"6\"></line><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"6\"></line><line x1=\"3\" y1=\"10\" x2=\"21\" y2=\"10\"></line></svg><span>BOOK</span></button><button class=\"foundation-offerings-btn\" data-modal=\"classesModal\" aria-label=\"View Class Offerings\"><span>OFFERINGS &rarr;</span></button>'
    },
    {
      id: 'birthday',
      eyebrow: '— Milestone Celebrations',
      title: 'Birthday Parties & Celebrations',
      descHtml: '<p>Celebrate your milestone birthdays with pure color, wonder, and joy! Our signature birthday packages include dedicated artist hosts, vibrant color-splatter canvases, guided painting adventures, and custom party favors designed for all ages.</p>',
      bgImage: '/images/foundation-events-party.jpg',
      actionsHtml: '<button class=\"foundation-book-btn\" data-modal=\"eventsModal\" aria-label=\"Book a birthday party\"><svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"3\" y=\"4\" width=\"18\" height=\"18\" rx=\"2\" ry=\"2\"></rect><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"6\"></line><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"6\"></line><line x1=\"3\" y1=\"10\" x2=\"21\" y2=\"10\"></line></svg><span>BOOK</span></button><button class=\"foundation-offerings-btn\" data-modal=\"eventsModal\" aria-label=\"View Birthday Packages\"><span>OFFERINGS &rarr;</span></button>'
    },
    {
      id: 'private-events',
      eyebrow: '— Bespoke Gatherings',
      title: 'Private Events & Soirées',
      descHtml: '<p>Host an extraordinary private soirée, intimate celebration, bridal gathering, or celebratory luncheon in our sunlit ateliers. Enjoy tailored creative experiences, curated table scapes, atmospheric lighting, and bespoke artistic keepsakes.</p>',
      bgImage: '/images/foundation-private-events.jpg',
      actionsHtml: '<button class=\"foundation-book-btn\" data-modal=\"eventsModal\" aria-label=\"Book a private event\"><svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"3\" y=\"4\" width=\"18\" height=\"18\" rx=\"2\" ry=\"2\"></rect><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"6\"></line><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"6\"></line><line x1=\"3\" y1=\"10\" x2=\"21\" y2=\"10\"></line></svg><span>BOOK</span></button><button class=\"foundation-offerings-btn\" data-modal=\"eventsModal\" aria-label=\"View Private Event Offerings\"><span>OFFERINGS &rarr;</span></button>'
    },
    {
      id: 'corporate-events',
      eyebrow: '— Corporate Retreats',
      title: 'Corporate Events & Retreats',
      descHtml: '<p>Inspire innovation, camaraderie, and creative problem-solving with tailored corporate retreats and team-building events at Artsy Fartsy Studio. From collaborative group canvas projects and color theory workshops to elegant cocktail networking soirées, we curate elevated experiences that bring teams together.</p>',
      bgImage: '/images/foundation-corporate-events.jpg',
      actionsHtml: '<button class=\"foundation-book-btn\" data-modal=\"eventsModal\" aria-label=\"Book a corporate event\"><svg viewBox=\"0 0 24 24\" width=\"16\" height=\"16\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"3\" y=\"4\" width=\"18\" height=\"18\" rx=\"2\" ry=\"2\"></rect><line x1=\"16\" y1=\"2\" x2=\"16\" y2=\"6\"></line><line x1=\"8\" y1=\"2\" x2=\"8\" y2=\"6\"></line><line x1=\"3\" y1=\"10\" x2=\"21\" y2=\"10\"></line></svg><span>BOOK</span></button><button class=\"foundation-offerings-btn\" data-modal=\"eventsModal\" aria-label=\"View Corporate Offerings\"><span>OFFERINGS &rarr;</span></button>'
    }
  ];

  var currentIndex = 0;
  var bgEl = document.getElementById('foundationStageBg');
  var eyebrowEl = document.getElementById('foundationEyebrow');
  var titleEl = document.getElementById('foundationTitle');
  var descEl = document.getElementById('foundationDesc');
  var actionsEl = document.getElementById('foundationActionsRow');
  var cards = document.querySelectorAll('.foundation-card');
  var track = document.getElementById('foundationCardsTrack');
  var prevBtn = document.getElementById('foundationPrevBtn');
  var nextBtn = document.getElementById('foundationNextBtn');
  var progressFill = document.getElementById('foundationProgressFill');
  var counterNum = document.getElementById('foundationCounterNum');

  var autoTimer = null;
  var AUTO_INTERVAL = 3000; // 3 seconds loop per user request

  function updateSlide() {
    var s = slides[currentIndex];

    // 1. Update Background with smooth transition
    if (bgEl) {
      bgEl.style.opacity = '0.55';
      setTimeout(function() {
        bgEl.style.backgroundImage = 'url(\"' + s.bgImage + '\")';
        bgEl.style.opacity = '1';
      }, 140);
    }

    // 2. Update Left Column Text & Actions
    if (eyebrowEl && titleEl && descEl) {
      eyebrowEl.style.opacity = '0';
      titleEl.style.opacity = '0';
      descEl.style.opacity = '0';
      if (actionsEl) actionsEl.style.opacity = '0';

      setTimeout(function() {
        eyebrowEl.textContent = s.eyebrow;
        titleEl.textContent = s.title;
        descEl.innerHTML = s.descHtml;
        if (actionsEl) {
          actionsEl.innerHTML = s.actionsHtml;
          actionsEl.style.opacity = '1';
        }
        eyebrowEl.style.opacity = '1';
        titleEl.style.opacity = '1';
        descEl.style.opacity = '1';
      }, 140);
    }

    // 3. Update Cards Track Translation & Active Class
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
      var cardW = cards[0].offsetWidth || 210;
      var gap = 20;
      var offset = currentIndex * (cardW + gap);
      track.style.transform = 'translate3d(-' + offset + 'px, 0, 0)';
    }

    // 4. Update Progress Fill & Counter Number (Pure White styling)
    if (progressFill) {
      var pct = ((currentIndex + 1) / slides.length) * 100;
      progressFill.style.width = pct + '%';
    }
    if (counterNum) {
      counterNum.textContent = '0' + (currentIndex + 1);
    }
  }

  function goToIndex(newIdx) {
    currentIndex = (newIdx + slides.length) % slides.length;
    updateSlide();
  }

  function startAutoLoop() {
    stopAutoLoop();
    autoTimer = setInterval(function() {
      goToIndex(currentIndex + 1);
    }, AUTO_INTERVAL);
  }

  function stopAutoLoop() {
    if (autoTimer) {
      clearInterval(autoTimer);
      autoTimer = null;
    }
  }

  function resetAutoLoop() {
    stopAutoLoop();
    startAutoLoop();
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', function(e) {
      e.preventDefault();
      goToIndex(currentIndex + 1);
      resetAutoLoop();
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', function(e) {
      e.preventDefault();
      goToIndex(currentIndex - 1);
      resetAutoLoop();
    });
  }

  cards.forEach(function(card) {
    card.addEventListener('click', function() {
      var idx = parseInt(card.getAttribute('data-index'), 10);
      goToIndex(idx);
      resetAutoLoop();
    });
  });

  // Delegated event listener for dynamic data-modal buttons in actionsEl
  if (actionsEl) {
    actionsEl.addEventListener('click', function(e) {
      var btn = e.target.closest('[data-modal]');
      if (btn) {
        e.preventDefault();
        var id = btn.getAttribute('data-modal');
        if (typeof openModal === 'function') {
          openModal(id);
        } else {
          var m = document.getElementById(id);
          if (m) {
            document.querySelectorAll('.modal-overlay').forEach(function(item){ item.classList.remove('active'); });
            m.classList.add('active');
          }
        }
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

    if (e.key === 'ArrowRight') {
      goToIndex(currentIndex + 1);
      resetAutoLoop();
    } else if (e.key === 'ArrowLeft') {
      goToIndex(currentIndex - 1);
      resetAutoLoop();
    }
  });

  window.addEventListener('resize', updateSlide);

  // Initialize and start 3-second loop
  updateSlide();
  startAutoLoop();
})();
'''

with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as tf:
    tf.write(js)
    tf_name = tf.name

res = subprocess.run(['node', '--check', tf_name], capture_output=True, text=True)
if res.returncode == 0:
    print("3s Loop JS is 100% valid!")
else:
    print("Syntax error:", res.stderr)
