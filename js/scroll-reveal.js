export function initScrollReveal() {
    function makeVisible(el) {
        if (el.classList.contains('visible')) return;
        const siblings = Array.from(
            el.parentElement.querySelectorAll('.reveal')
        );
        const index = Math.max(0, siblings.indexOf(el));
        setTimeout(() => el.classList.add('visible'), index * 80);
    }

    const revealObs = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            makeVisible(entry.target);
            revealObs.unobserve(entry.target);
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -48px 0px' });

    document.querySelectorAll('.reveal').forEach(el => revealObs.observe(el));

    // Safari/WebKit workaround: IntersectionObserver sometimes doesn't fire for
    // elements already in the viewport on load. Force a geometry check after load.
    window.addEventListener('load', () => {
        requestAnimationFrame(() => {
            document.querySelectorAll('.reveal:not(.visible)').forEach(el => {
                const rect = el.getBoundingClientRect();
                if (rect.top < window.innerHeight - 48 && rect.bottom > 0) {
                    makeVisible(el);
                }
            });
        });
    });
}
