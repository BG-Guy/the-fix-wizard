export function initScrollReveal() {
    const revealObs = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;

            // Stagger sibling items within the same grid/list parent
            const siblings = Array.from(
                entry.target.parentElement.querySelectorAll('.reveal')
            );
            const index = siblings.indexOf(entry.target);

            setTimeout(() => entry.target.classList.add('visible'), index * 80);
            revealObs.unobserve(entry.target);
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -48px 0px' });

    document.querySelectorAll('.reveal').forEach(el => revealObs.observe(el));
}
