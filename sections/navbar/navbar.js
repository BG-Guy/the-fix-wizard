// navbar.js — adds the "scrolled" background once the page scrolls past
// the hero, and highlights the nav link for whichever section is in view.

export function initNavbar() {
    const navbar   = document.getElementById('navbar');
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');

    function handleNavScroll() {
        navbar.classList.toggle('scrolled', window.scrollY > 60);
    }
    window.addEventListener('scroll', handleNavScroll, { passive: true });
    handleNavScroll();

    const sectionObs = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            navLinks.forEach(link => {
                link.classList.toggle('active',
                    link.getAttribute('href') === `#${entry.target.id}`);
            });
        });
    }, { threshold: 0.45 });

    sections.forEach(s => sectionObs.observe(s));
}
