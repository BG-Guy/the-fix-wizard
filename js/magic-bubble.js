const REASONS = [
    'Satisfaction Guaranteed',
    'Same-Day Fix',
    'Honest Flat Pricing',
    'Licensed & Insured',
    'Done Right, First Time',
    '500+ Happy Homes',
    'On-Time, Every Time',
    '10+ Years Experience',
];

const PARTICLE_CHARS  = ['✦', '★', '✸', '✶', '◆', '⋆', '·', '✺'];
const PARTICLE_COLORS = [
    '#b97fe8', '#9B59B6', '#d4a8f0', '#7D3C98',
    '#e0c3f7', '#C39BD3', '#f5eaff', '#FFD166', '#ffffff',
];

function spawnParticles(bubble) {
    const count = 22;

    const flash = document.createElement('span');
    flash.className = 'poof-flash';
    bubble.appendChild(flash);
    setTimeout(() => flash.remove(), 500);

    [
        { w: 260, h: 260, dur: '.65s', color: 'rgba(155,89,182,.35)' },
        { w: 180, h: 180, dur: '.9s',  color: 'rgba(180,120,220,.25)' },
    ].forEach(({ w, h, dur, color }) => {
        const s = document.createElement('span');
        s.className    = 'poof-smoke';
        s.style.width  = w + 'px';
        s.style.height = h + 'px';
        s.style.border = `2px solid ${color}`;
        s.style.setProperty('--dur', dur);
        bubble.appendChild(s);
        setTimeout(() => s.remove(), 950);
    });

    for (let i = 0; i < count; i++) {
        const p       = document.createElement('span');
        p.className   = 'poof-particle';
        p.textContent = PARTICLE_CHARS[i % PARTICLE_CHARS.length];
        p.style.color = PARTICLE_COLORS[i % PARTICLE_COLORS.length];

        const angle = (i / count) * 360 + (Math.random() - .5) * 25;
        const dist  = 90  + Math.random() * 110;
        const sz    = 10  + Math.random() * 14;
        const dur   = (.7 + Math.random() * .5) + 's';

        p.style.setProperty('--a',   angle + 'deg');
        p.style.setProperty('--d',   dist  + 'px');
        p.style.setProperty('--sz',  sz    + 'px');
        p.style.setProperty('--dur', dur);
        p.style.animationDelay = (Math.random() * 80) + 'ms';
        bubble.appendChild(p);
        setTimeout(() => p.remove(), 1350);
    }
}

export function initMagicBubble() {
    const bubble = document.getElementById('magicBubble');
    const textEl = document.getElementById('magicText');
    if (!bubble || !textEl) return;

    let current = 0;
    let busy    = false;

    function poof() {
        if (busy) return;
        busy = true;

        spawnParticles(bubble);
        bubble.classList.remove('poof-in');
        bubble.classList.add('poof-out');

        setTimeout(() => {
            current = (current + 1) % REASONS.length;
            textEl.textContent = REASONS[current];

            bubble.classList.remove('poof-out');
            bubble.classList.add('poof-in');

            setTimeout(() => {
                bubble.classList.remove('poof-in');
                busy = false;
            }, 580);
        }, 380);
    }

    bubble.addEventListener('click', poof);
    bubble.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); poof(); }
    });
}
