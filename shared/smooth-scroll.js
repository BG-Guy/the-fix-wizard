// smooth-scroll.js — smooth-scrolls links that point at a section on the
// current page ("#services", or "/#services" while on the homepage — the
// shared navbar uses the latter so it works from every page), offset by the
// navbar's height so the target section isn't hidden underneath it.

// True when the link targets a #section of the page we're already on.
export function isSamePageHash(a) {
    if (!a.hash) return false;
    const page = p => p.replace(/index\.html$/, '');
    return a.origin === location.origin && page(a.pathname) === page(location.pathname);
}

export function initSmoothScroll() {
    document.querySelectorAll('a[href*="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            if (!isSamePageHash(this)) return;
            const target = document.querySelector(this.hash);
            if (!target) return;
            e.preventDefault();
            const offset = parseInt(
                getComputedStyle(document.documentElement).getPropertyValue('--nav-h')
            ) || 72;
            window.scrollTo({
                top: target.getBoundingClientRect().top + window.scrollY - offset,
                behavior: 'smooth',
            });
        });
    });
}
