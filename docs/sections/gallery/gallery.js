// gallery.js — "Our Work" before/after cards. Each card's toggle button
// wipes the "after" photo into view (or back out) via a CSS clip-path
// transition, restarting the light-sweep animation on every click.

export function initGallery() {
    document.querySelectorAll('.reveal-card').forEach(card => {
        const toggle = card.querySelector('.reveal-toggle');
        const label  = toggle && toggle.querySelector('.reveal-toggle-text');
        if (!toggle) return;

        toggle.addEventListener('click', () => {
            const revealed = card.classList.toggle('is-revealed');
            if (label) label.textContent = revealed ? 'Show Before' : 'Reveal The Fix';
            toggle.setAttribute('aria-pressed', String(revealed));

            card.classList.remove('is-revealing');
            void card.offsetWidth; // restart the shimmer animation
            card.classList.add('is-revealing');
            setTimeout(() => card.classList.remove('is-revealing'), 1100);
        });
    });
}
