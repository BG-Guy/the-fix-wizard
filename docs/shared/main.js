// main.js — homepage entry point.
// Loaded via <script type="module" src="shared/main.js"> at the end of the
// page (in sections/sticky-cta/sticky-cta.html). Wires up every section's
// interactive behavior, in the order they appear on the page.
import { initLoader }       from '../sections/loader/loader.js';
import { initNavbar }       from '../sections/navbar/navbar.js';
import { initMobileMenu }   from '../sections/navbar/mobile-menu.js';
import { initSmoothScroll } from './smooth-scroll.js';
import { initScrollReveal } from './scroll-reveal.js';
import { initCounters }     from './counters.js';
import { initContactForm }  from '../sections/contact/contact-form.js';
import { initMagicBubble }  from '../sections/why-us/magic-bubble.js';
import { initGallery }        from '../sections/gallery/gallery.js';
import { initTrustShowcase }  from '../sections/gallery/trust-showcase.js';
import { initFAQ }          from '../sections/faq/faq.js';
import { initStickyCTA }    from '../sections/sticky-cta/sticky-cta.js';

initLoader();
initNavbar();
initMobileMenu();
initSmoothScroll();
initScrollReveal();
initCounters();
initContactForm();
initMagicBubble();
initGallery();
initTrustShowcase();
initFAQ();
initStickyCTA();

// Footer copyright year
document.getElementById('year').textContent = new Date().getFullYear();
