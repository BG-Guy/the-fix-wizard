import { initNavbar }       from './navbar.js';
import { initMobileMenu }   from './mobile-menu.js';
import { initSmoothScroll } from './smooth-scroll.js';
import { initScrollReveal } from './scroll-reveal.js';
import { initFAQ }          from './faq.js';
import { initCounters }     from './counters.js';

initNavbar();
initMobileMenu();
initSmoothScroll();
initScrollReveal();
initFAQ();
initCounters();

// Make entire loc-card clickable — navigates to first service link unless a button was clicked
document.querySelectorAll('.loc-card').forEach(card => {
    card.addEventListener('click', e => {
        if (e.target.closest('.loc-svc-btn')) return;
        const first = card.querySelector('.loc-svc-btn');
        if (first) window.location.href = first.href;
    });
});

document.getElementById('year').textContent = new Date().getFullYear();
