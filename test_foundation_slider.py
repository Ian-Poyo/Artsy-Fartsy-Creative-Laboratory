import subprocess, tempfile

js = '''
// ============================================================
// FRIENDS OF ARTSY FARTSY FOUNDATION SLIDER CONTROLLER
// ============================================================
(function(){
  var slides = [
    {
      id: 'mission',
      eyebrow: '— Mission Statement',
      title: 'Friends of Artsy Fartsy Foundation',
      descHtml: '<p>Our mission is to ensure accessible, inspiring space for the Artsy Fartsy Creative Laboratory; expand equitable access to the arts through scholarships for high school students and adult learners; and strengthen arts education by delivering high-quality color science professional development for elementary, middle, and high school teachers.</p><p>We believe creativity is a powerful catalyst for learning, expression, and community, and we work to nurture it across ages, disciplines, and classrooms.</p>',
      bgImage: '/images/foundation-students.jpg',
      topicIndex: 0
    },
    {
      id: 'scholarships',
      eyebrow: '— Student Scholarships',
      title: 'Scholarships for High School & Adults',
      descHtml: '<p>Expanding equitable access to the arts by funding full and partial studio tuition, materials, and direct artist mentorship for high school students and adult emerging learners in our community.</p><p>Every aspiring creator deserves a seat at the wheel, an easel in the light, and the freedom to experiment without financial barriers.</p>',
      bgImage: '/images/card-classroom.webp',
      topicIndex: 1
    },
    {
      id: 'teachers',
      eyebrow: '— Educator Development',
      title: 'Color Science Teacher Development',
      descHtml: '<p>Delivering high-quality, research-backed color science and material experimentation professional development for elementary, middle, and high school educators.</p><p>We equip public school teachers with hands-on lesson frameworks, dynamic pigment chemistry, and process-based art pedagogy that transforms classrooms.</p>',
      bgImage: '/images/card-birthday.webp',
      topicIndex: 2
    },
    {
      id: 'space',
      eyebrow: '— Creative Laboratory Space',
      title: 'Accessible & Inspiring Community Atelier',
      descHtml: '<p>Securing, equipping, and sustaining an open-ended community sanctuary where unconventional ideas thrive, ceramic wheels spin, and materials are pushed beyond conventional boundaries.</p><p>A dedicated home for hands-on sensory art discovery and multidisciplinary artistic inquiry in Carmel.</p>',
      bgImage: '/images/card-starry.webp',
      topicIndex: 3
    },
    {
      id: 'community',
      eyebrow: '— Expression & Community',
      title: 'A Catalyst for Community Connection',
      descHtml: '<p>Nurturing creativity as an essential catalyst for learning, human empathy, and community expression across all ages, disciplines, and classrooms.</p><p>Through collaborative exhibitions, community open studios, and public school outreach, we weave art into the fabric of everyday life.</p>',
      bgImage: '/images/card-party.webp',
      topicIndex: 4
    }
  ];

  var currentIndex = 0;
  var bgEl = document.getElementById('foundationStageBg');
  var eyebrowEl = document.getElementById('foundationEyebrow');
  var titleEl = document.getElementById('foundationTitle');
  var descEl = document.getElementById('foundationDesc');
  var cards = document.querySelectorAll('.foundation-card');
  var track = document.getElementById('foundationCardsTrack');
  var prevBtn = document.getElementById('foundationPrevBtn');
  var nextBtn = document.getElementById('foundationNextBtn');
  var progressFill = document.getElementById('foundationProgressFill');
  var counterNum = document.getElementById('foundationCounterNum');

  function updateSlide() {
    var s = slides[currentIndex];

    // 1. Update Background with smooth transition
    if (bgEl) {
      bgEl.style.opacity = '0.3';
      setTimeout(function() {
        bgEl.style.backgroundImage = 'url(\"' + s.bgImage + '\")';
        bgEl.style.opacity = '1';
      }, 150);
    }

    // 2. Update Left Column Text
    if (eyebrowEl && titleEl && descEl) {
      eyebrowEl.style.opacity = '0';
      titleEl.style.opacity = '0';
      descEl.style.opacity = '0';
      setTimeout(function() {
        eyebrowEl.textContent = s.eyebrow;
        titleEl.textContent = s.title;
        descEl.innerHTML = s.descHtml;
        eyebrowEl.style.opacity = '1';
        titleEl.style.opacity = '1';
        descEl.style.opacity = '1';
      }, 150);
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
      var gap = 18;
      var offset = currentIndex * (cardW + gap);
      track.style.transform = 'translate3d(-' + offset + 'px, 0, 0)';
    }

    // 4. Update Progress Fill & Counter Number
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

  window.addEventListener('resize', updateSlide);

  // Initialize
  updateSlide();
})();
'''

with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as tf:
    tf.write(js)
    tf_name = tf.name

res = subprocess.run(['node', '--check', tf_name], capture_output=True, text=True)
if res.returncode == 0:
    print("Foundation Slider JS is 100% valid!")
else:
    print("Syntax error:", res.stderr)
