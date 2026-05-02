import { initLoader }       from './loader.js';
import { initNavbar }       from './navbar.js';
import { initMobileMenu }   from './mobile-menu.js';
import { initSmoothScroll } from './smooth-scroll.js';
import { initScrollReveal } from './scroll-reveal.js';
import { initCounters }     from './counters.js';
import { initContactForm }  from './contact-form.js';
import { initMagicBubble }  from './magic-bubble.js';
import { initFAQ }          from './faq.js';
import { initStickyCTA }    from './sticky-cta.js';

initLoader();
initNavbar();
initMobileMenu();
initSmoothScroll();
initScrollReveal();
initCounters();
initContactForm();
initMagicBubble();
initFAQ();
initStickyCTA();

document.getElementById('year').textContent = new Date().getFullYear();
