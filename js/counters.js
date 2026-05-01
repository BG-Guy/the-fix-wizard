function animateCounter(el) {
    const target   = parseInt(el.dataset.target, 10);
    const duration = 1800; // ms
    const fps      = 60;
    const steps    = duration / (1000 / fps);
    const step     = target / steps;
    let current    = 0;

    const tick = setInterval(() => {
        current += step;
        if (current >= target) {
            el.textContent = target;
            clearInterval(tick);
        } else {
            el.textContent = Math.round(current);
        }
    }, 1000 / fps);
}

export function initCounters() {
    const counterObs = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            animateCounter(entry.target);
            counterObs.unobserve(entry.target);
        });
    }, { threshold: 0.6 });

    document.querySelectorAll('.counter').forEach(el => counterObs.observe(el));
}
