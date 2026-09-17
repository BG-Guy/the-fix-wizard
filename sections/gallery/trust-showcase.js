// trust-showcase.js — big animated headline carousel above the gallery
// cards. Each promise holds, then "burns" apart into ember particles
// sampled from its own letterforms (a fire-ash take on the site's
// existing magic-poof motif — see why-us/magic-bubble.js), then the
// next phrase slides up from below. Loops forever, ~2s per phrase.

const PHRASES = [
    '100% Satisfaction Guaranteed',
    '3-Month Workmanship Warranty',
    'Licensed & Insured',
];

const HOLD_MS         = 900;
const DISINTEGRATE_MS = 700;
const ENTER_MS        = 400;

const FONT_FAMILY    = "'Cinzel', serif";
const MAX_FONT_SIZE  = 70;
const MIN_FONT_SIZE  = 18;
const EMBER_COLORS   = ['#FF6B35', '#FF8C42', '#FFD166', '#e55a22', '#ffffff'];

export function initTrustShowcase() {
    const canvas = document.getElementById('trustCanvas');
    const srText = document.getElementById('trustSrText');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    let dpr       = Math.max(1, window.devicePixelRatio || 1);
    let cssWidth  = 0;
    let cssHeight = 0;
    let fontSize  = MAX_FONT_SIZE;
    let index     = 0;
    let particles = [];
    let phase     = 'hold'; // 'hold' | 'disintegrate' | 'enter'
    let phaseStart = 0;
    let resizeTimer;

    // One shared size for every phrase (sized to the longest one) so the
    // carousel doesn't visibly grow/shrink as it cycles.
    function fitFontSizeForAll() {
        let size = MAX_FONT_SIZE;
        const maxWidth = cssWidth * 0.94;
        while (size >= MIN_FONT_SIZE) {
            ctx.font = `900 ${size}px ${FONT_FAMILY}`;
            const widest = Math.max(...PHRASES.map(p => ctx.measureText(p).width));
            if (widest <= maxWidth || size === MIN_FONT_SIZE) break;
            size -= 2;
        }
        fontSize = size;
    }

    function resize() {
        const rect = canvas.getBoundingClientRect();
        cssWidth  = rect.width;
        cssHeight = rect.height;
        dpr = Math.max(1, window.devicePixelRatio || 1);
        canvas.width  = Math.round(cssWidth * dpr);
        canvas.height = Math.round(cssHeight * dpr);
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        fitFontSizeForAll();
    }

    // Draws the phrase into an offscreen buffer, then samples its alpha
    // channel on a grid so every inked cell becomes one ember particle.
    function buildParticles(text) {
        const off  = document.createElement('canvas');
        off.width  = canvas.width;
        off.height = canvas.height;
        const octx = off.getContext('2d');
        octx.setTransform(dpr, 0, 0, dpr, 0, 0);
        octx.font = `900 ${fontSize}px ${FONT_FAMILY}`;
        octx.textAlign = 'center';
        octx.textBaseline = 'middle';
        octx.fillStyle = '#fff';
        octx.fillText(text, cssWidth / 2, cssHeight / 2);

        const step = Math.max(3, Math.round(fontSize / 14));
        const data = octx.getImageData(0, 0, off.width, off.height).data;
        const pts  = [];
        for (let y = 0; y < off.height; y += step * dpr) {
            for (let x = 0; x < off.width; x += step * dpr) {
                const alpha = data[(y * off.width + x) * 4 + 3];
                if (alpha > 120) pts.push({ x: x / dpr, y: y / dpr });
            }
        }
        return pts.map(p => ({
            x: p.x, y: p.y,
            vx: (Math.random() - 0.5) * 90,
            vy: -40 - Math.random() * 110,
            size: 1.6 + Math.random() * 2.2,
            color: EMBER_COLORS[(Math.random() * EMBER_COLORS.length) | 0],
            delay: Math.random() * 120,
        }));
    }

    function drawPhrase(text, opacity, offsetY) {
        ctx.clearRect(0, 0, cssWidth, cssHeight);
        ctx.save();
        ctx.globalAlpha = opacity;
        ctx.font = `900 ${fontSize}px ${FONT_FAMILY}`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        const grad = ctx.createLinearGradient(cssWidth / 2 - 220, 0, cssWidth / 2 + 220, 0);
        grad.addColorStop(0,   '#e55a22');
        grad.addColorStop(0.5, '#FF6B35');
        grad.addColorStop(1,   '#FF8C42');
        ctx.fillStyle   = grad;
        ctx.shadowColor = 'rgba(255,107,53,.35)';
        ctx.shadowBlur  = 24;
        ctx.fillText(text, cssWidth / 2, cssHeight / 2 + offsetY);
        ctx.restore();
    }

    function drawEmbers(elapsed) {
        ctx.clearRect(0, 0, cssWidth, cssHeight);
        const durSec = DISINTEGRATE_MS / 1000;
        particles.forEach(p => {
            const local = Math.max(0, elapsed - p.delay);
            const prog  = Math.min(1, local / (DISINTEGRATE_MS - p.delay));
            if (prog <= 0) return;
            const ease = 1 - Math.pow(1 - prog, 2);
            const x = p.x + p.vx * ease * durSec;
            const y = p.y + p.vy * ease * durSec + 26 * ease * ease;
            ctx.globalAlpha = 1 - prog;
            ctx.fillStyle = p.color;
            ctx.beginPath();
            ctx.arc(x, y, p.size * (1 - prog * 0.4), 0, Math.PI * 2);
            ctx.fill();
        });
        ctx.globalAlpha = 1;
    }

    function tick(now) {
        const elapsed = now - phaseStart;

        if (phase === 'hold') {
            drawPhrase(PHRASES[index], 1, 0);
            if (elapsed >= HOLD_MS) {
                particles  = buildParticles(PHRASES[index]);
                phase      = 'disintegrate';
                phaseStart = now;
            }
        } else if (phase === 'disintegrate') {
            drawEmbers(elapsed);
            if (elapsed >= DISINTEGRATE_MS) {
                index = (index + 1) % PHRASES.length;
                if (srText) srText.textContent = PHRASES[index];
                phase      = 'enter';
                phaseStart = now;
            }
        } else { // enter
            const prog = Math.min(1, elapsed / ENTER_MS);
            const ease = 1 - Math.pow(1 - prog, 3);
            drawPhrase(PHRASES[index], ease, (1 - ease) * 34);
            if (elapsed >= ENTER_MS) {
                phase      = 'hold';
                phaseStart = now;
            }
        }
        requestAnimationFrame(tick);
    }

    // Simple crossfade loop for users who've asked for less motion —
    // same infinite cycle, no ember particles.
    function tickReduced(now) {
        const elapsed  = now - phaseStart;
        const total    = HOLD_MS + DISINTEGRATE_MS + ENTER_MS;
        const fadeMs   = 300;
        if (elapsed < total - fadeMs) {
            drawPhrase(PHRASES[index], 1, 0);
        } else if (elapsed < total) {
            drawPhrase(PHRASES[index], 1 - (elapsed - (total - fadeMs)) / fadeMs, 0);
        } else {
            index = (index + 1) % PHRASES.length;
            if (srText) srText.textContent = PHRASES[index];
            phaseStart = now;
        }
        requestAnimationFrame(tickReduced);
    }

    resize();
    // Cinzel loads async (see head.html's preload/onload swap) — measuring
    // against the fallback serif before it's ready under-measures width,
    // so the fit calc has to re-run once the real font is actually in.
    if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(resize);
    }
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(resize, 150);
    });

    phaseStart = performance.now();
    requestAnimationFrame(reduceMotion ? tickReduced : tick);
}
