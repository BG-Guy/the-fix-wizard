const PARTICLE_CHARS  = ['✦', '★', '✸', '·', '◆', '⋆', '✺'];
const PARTICLE_COLORS = ['#FFD166', '#FF8C42', '#ffffff', '#FF6B35', '#ffd9c0', '#ffb347', '#fffbe0'];

function spawnParticles(btn) {
    // Estimate button center from its fixed CSS position
    // (getBoundingClientRect on a scale(0) element returns zero dimensions)
    const cs     = getComputedStyle(btn);
    const bottom = parseFloat(cs.bottom) || 28;
    const right  = parseFloat(cs.right)  || 28;
    const vw     = window.innerWidth;
    const vh     = window.innerHeight;
    const btnW   = vw < 768 ? 110 : 148;
    const btnH   = vw < 768 ?  42 :  46;
    const cx     = vw - right  - btnW / 2;
    const cy     = vh - bottom - btnH / 2;

    const count = 16;
    for (let i = 0; i < count; i++) {
        const p       = document.createElement('span');
        p.className   = 'sticky-cta-particle';
        p.textContent = PARTICLE_CHARS[i % PARTICLE_CHARS.length];
        p.style.color = PARTICLE_COLORS[i % PARTICLE_COLORS.length];

        const angle = (i / count) * 360 + (Math.random() - .5) * 28;
        const dist  = 45 + Math.random() * 75;
        const sz    = 8  + Math.random() * 10;
        const dur   = (.45 + Math.random() * .45) + 's';
        const rad   = angle * (Math.PI / 180);

        p.style.left = cx + 'px';
        p.style.top  = cy + 'px';
        p.style.setProperty('--sz',  sz  + 'px');
        p.style.setProperty('--tx',  (Math.cos(rad) * dist) + 'px');
        p.style.setProperty('--ty',  (Math.sin(rad) * dist) + 'px');
        p.style.setProperty('--dur', dur);
        p.style.animationDelay = (Math.random() * 60) + 'ms';

        document.body.appendChild(p);
        setTimeout(() => p.remove(), 950);
    }
}

export function initStickyCTA() {
    const cta     = document.getElementById('stickyCTA');
    const hero    = document.getElementById('home');
    const contact = document.getElementById('contact');
    if (!cta || !hero || !contact) return;

    let pastHero    = false;
    let inContact   = false;
    let isVisible   = false;
    let isAnimating = false;

    function updateState() {
        const shouldShow = pastHero && !inContact;
        if (shouldShow && !isVisible)  showCTA();
        if (!shouldShow && isVisible)  hideCTA();
    }

    function showCTA() {
        if (isVisible || isAnimating) return;
        isVisible   = true;
        isAnimating = true;
        cta.classList.remove('shown', 'leaving');
        spawnParticles(cta);
        cta.classList.add('entering');
        setTimeout(() => {
            // Add .shown BEFORE removing .entering so the transition
            // never sees a scale(0) intermediate frame
            cta.classList.add('shown');
            cta.classList.remove('entering');
            isAnimating = false;
        }, 650);
    }

    function hideCTA() {
        if (!isVisible || isAnimating) return;
        isVisible   = false;
        isAnimating = true;
        cta.classList.remove('shown', 'entering');
        cta.classList.add('leaving');
        setTimeout(() => {
            cta.classList.remove('leaving');
            isAnimating = false;
        }, 400);
    }

    // Show when hero scrolls out of view
    new IntersectionObserver(entries => {
        pastHero = !entries[0].isIntersecting;
        updateState();
    }, { threshold: 0 }).observe(hero);

    // Hide when contact section enters view
    new IntersectionObserver(entries => {
        inContact = entries[0].isIntersecting;
        updateState();
    }, { threshold: 0.15 }).observe(contact);
}
