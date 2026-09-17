// service-page.js — entry point for every auto-generated service/location
// detail page (loaded as /generated-pages/service-page.js). Only wires up
// the behaviors those pages actually use — no loader, no magic bubble,
// no sticky CTA, no contact form (those are homepage-only).
import { initNavbar }       from '../sections/navbar/navbar.js';
import { initMobileMenu }   from '../sections/navbar/mobile-menu.js';
import { initSmoothScroll } from '../shared/smooth-scroll.js';
import { initScrollReveal } from '../shared/scroll-reveal.js';
import { initFAQ }          from '../sections/faq/faq.js';
import { initCounters }     from '../shared/counters.js';

initNavbar();
initMobileMenu();
initSmoothScroll();
initScrollReveal();
initFAQ();
initCounters();

// Make an entire location card clickable — navigates to its first service
// link, unless the click landed on a button inside the card already.
document.querySelectorAll('.loc-card').forEach(card => {
    card.addEventListener('click', e => {
        if (e.target.closest('.loc-svc-btn')) return;
        const first = card.querySelector('.loc-svc-btn');
        if (first) window.location.href = first.href;
    });
});

// Footer copyright year
document.getElementById('year').textContent = new Date().getFullYear();
