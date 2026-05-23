(function () {
  /* ── Inject styles ─────────────────────────────────────────────────────── */
  var style = document.createElement('style');
  style.textContent = [
    '@keyframes cs-pop{0%{transform:scale(.5) translateY(14px);opacity:0}',
    '65%{transform:scale(1.07) translateY(-6px);opacity:1}',
    '82%{transform:scale(.96) translateY(0)}100%{transform:scale(1) translateY(0);opacity:1}}',

    '@keyframes cs-shimmer{0%{left:-80%}55%,100%{left:130%}}',

    /* Lightning flicker on the COMING SOON text — 1.6s loop */
    '@keyframes cs-flicker{',
    '0%,74%,100%{color:#FF6B35;text-shadow:0 0 8px rgba(255,107,53,.95),0 0 22px rgba(255,107,53,.65),0 0 48px rgba(255,107,53,.35);opacity:1}',
    '75%{opacity:.7;color:#FF6B35;text-shadow:0 0 3px rgba(255,107,53,.4)}',
    '76%{color:#ffe066;text-shadow:0 0 14px rgba(255,220,100,1),0 0 36px rgba(255,107,53,.9),0 0 70px rgba(255,107,53,.5);opacity:1}',
    '77%{opacity:.75;color:#FF6B35;text-shadow:0 0 4px rgba(255,107,53,.4)}',
    '78%{color:#ffbc55;text-shadow:0 0 10px rgba(255,200,80,.95),0 0 28px rgba(255,107,53,.7),0 0 55px rgba(255,107,53,.4);opacity:1}',
    '}',

    '.cs-tip{',
    'position:fixed;z-index:999999;pointer-events:none;display:none;',
    'flex-direction:column;align-items:center;gap:5px;',
    'background:linear-gradient(135deg,#060d2e 0%,#091236 50%,#152468 100%);',
    'border:2px solid #FF6B35;border-radius:20px;',
    'padding:20px 36px 18px;min-width:240px;text-align:center;overflow:hidden;',
    'animation:cs-pop .42s cubic-bezier(.18,.9,.32,1.28) both}',

    '.cs-tip::before{content:"";position:absolute;top:0;left:-80%;width:40%;height:100%;',
    'background:linear-gradient(90deg,transparent,rgba(255,255,255,.14),transparent);',
    'transform:skewX(-14deg);animation:cs-shimmer 2.6s ease-in-out .42s infinite}',

    '.cs-tip-arrow{position:absolute;bottom:-12px;left:50%;transform:translateX(-50%);',
    'border:10px solid transparent;border-top-color:#FF6B35}',
    '.cs-tip-arrow::after{content:"";position:absolute;top:-11px;left:-9px;',
    'border:9px solid transparent;border-top-color:#091236}',

    '.cs-tip-icon{font-size:24px;color:#FF6B35;line-height:1}',

    '.cs-tip-text{font-family:"Cinzel",serif;font-size:20px;font-weight:900;',
    'color:#FF6B35;letter-spacing:5px;text-transform:uppercase;line-height:1.2;',
    'animation:cs-flicker 1.6s ease-in-out .42s infinite}',

    '.cs-tip-sub{font-size:11px;color:rgba(255,255,255,.4);',
    'letter-spacing:2.5px;text-transform:uppercase;font-weight:600;margin-top:2px}',

    /* Dim every intercepted element on hover so the tip stands out */
    '.cs-active-el{opacity:.72!important;cursor:not-allowed!important;',
    'filter:saturate(.8)!important}',
  ].join('');
  document.head.appendChild(style);

  /* ── Create tooltip DOM ────────────────────────────────────────────────── */
  var tip = document.createElement('div');
  tip.className = 'cs-tip';
  tip.innerHTML =
    '<i class="fas fa-hat-wizard cs-tip-icon"></i>' +
    '<span class="cs-tip-text">Coming Soon</span>' +
    '<span class="cs-tip-sub">Launching shortly — stay tuned</span>' +
    '<div class="cs-tip-arrow"></div>';
  document.body.appendChild(tip);

  /* ── Selectors ─────────────────────────────────────────────────────────── */
  var SEL = [
    'button.btn',
    'a[href^="tel:"]', 'a[href^="mailto:"]',
    'a[href="#contact"]', 'a[href*="#contact"]',
    '.nav-cta', '.sticky-cta', '.mobile-cta',
    'button[type="submit"]', 'input[type="submit"]',
  ].join(',');

  var currentEl = null;

  /* ── Position & show ───────────────────────────────────────────────────── */
  function place(el) {
    var rect = el.getBoundingClientRect();
    var W = 264;
    var x = rect.left + rect.width / 2 - W / 2;
    var aboveY = rect.top - 128; /* above the element */
    var belowY = rect.bottom + 14;
    var useBelow = aboveY < 10;

    x = Math.max(8, Math.min(x, window.innerWidth - W - 8));

    tip.style.left  = x + 'px';
    tip.style.top   = (useBelow ? belowY : aboveY) + 'px';
    tip.style.width = W + 'px';

    /* flip arrow when showing below */
    var arrow = tip.querySelector('.cs-tip-arrow');
    if (useBelow) {
      arrow.style.cssText = 'position:absolute;top:-12px;bottom:auto;left:50%;' +
        'transform:translateX(-50%);border:10px solid transparent;' +
        'border-bottom-color:#FF6B35;border-top:none';
      arrow.style.setProperty('--after-border', 'border-bottom-color:#091236;border-top:none');
    } else {
      arrow.style.cssText = '';
    }
  }

  function show(el) {
    if (currentEl) currentEl.classList.remove('cs-active-el');
    currentEl = el;
    el.classList.add('cs-active-el');

    place(el);
    tip.style.display = 'flex';
    tip.style.animation = 'none';
    void tip.offsetWidth; /* reflow to restart */
    tip.style.animation = 'cs-pop .42s cubic-bezier(.18,.9,.32,1.28) both';
  }

  function hide() {
    if (currentEl) { currentEl.classList.remove('cs-active-el'); currentEl = null; }
    tip.style.display = 'none';
  }

  /* ── Events ────────────────────────────────────────────────────────────── */
  document.addEventListener('mouseover', function (e) {
    var el = e.target.closest(SEL);
    if (el) show(el);
  });

  document.addEventListener('mouseout', function (e) {
    if (e.relatedTarget && e.relatedTarget.closest && e.relatedTarget.closest(SEL)) return;
    hide();
  });

  /* Block clicks */
  document.addEventListener('click', function (e) {
    var el = e.target.closest(SEL);
    if (el) { e.preventDefault(); e.stopImmediatePropagation(); show(el); }
  }, true);

  /* Block touch on mobile */
  document.addEventListener('touchstart', function (e) {
    var el = e.target.closest(SEL);
    if (el) { e.preventDefault(); show(el); }
  }, { passive: false, capture: true });

  document.addEventListener('touchend', function (e) {
    setTimeout(hide, 1800);
  }, { passive: true });

  /* Reposition on scroll/resize */
  window.addEventListener('scroll', function () { if (currentEl) place(currentEl); }, { passive: true });
  window.addEventListener('resize', function () { if (currentEl) place(currentEl); }, { passive: true });
})();
