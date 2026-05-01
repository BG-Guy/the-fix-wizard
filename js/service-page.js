import { initNavbar }       from './navbar.js';
import { initMobileMenu }   from './mobile-menu.js';
import { initSmoothScroll } from './smooth-scroll.js';
import { initScrollReveal } from './scroll-reveal.js';
import { initFAQ }          from './faq.js';

initNavbar();
initMobileMenu();
initSmoothScroll();
initScrollReveal();
initFAQ();

document.getElementById('year').textContent = new Date().getFullYear();
