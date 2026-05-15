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

document.getElementById('year').textContent = new Date().getFullYear();
