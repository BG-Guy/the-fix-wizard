/* =====================================================
   The Fix Wizard – main.js
   ===================================================== */

/* ---- Loader ---- */
window.addEventListener('load', () => {
    const loader = document.getElementById('loader');
    setTimeout(() => {
        loader.classList.add('out');
        setTimeout(() => {
            loader.style.display = 'none';
            document.body.classList.remove('no-scroll');
        }, 650);
    }, 3200);
    document.body.classList.add('no-scroll');
});

/* ---- Navbar scroll effect ---- */
const navbar = document.getElementById('navbar');

// Cache root and compute expanded nav height (50% larger)
const _root = document.documentElement;
const _baseNavHVal = getComputedStyle(_root).getPropertyValue('--nav-h') || '72px';
const _baseNavH = parseFloat(_baseNavHVal.trim()) || 72;
const _expandedNavH = (_baseNavH * 1.5) + 'px';

function handleNavScroll() {
    if (window.scrollY > 60) {
        navbar.classList.add('scrolled');
        _root.style.setProperty('--nav-h', _expandedNavH);
    } else {
        navbar.classList.remove('scrolled');
        _root.style.setProperty('--nav-h', _baseNavH + 'px');
    }
}

window.addEventListener('scroll', handleNavScroll, { passive: true });
handleNavScroll();

/* ---- Active nav link on scroll ---- */
const sections   = document.querySelectorAll('section[id]');
const navLinks   = document.querySelectorAll('.nav-link');

const sectionObs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            navLinks.forEach(link => {
                link.classList.toggle('active',
                    link.getAttribute('href') === `#${entry.target.id}`);
            });
        }
    });
}, { threshold: 0.45 });

sections.forEach(s => sectionObs.observe(s));

/* ---- Mobile menu ---- */
const hamburger     = document.getElementById('hamburger');
const mobileMenu    = document.getElementById('mobileMenu');
const mobileOverlay = document.getElementById('mobileOverlay');
const mobileClose   = document.getElementById('mobileClose');

function openMenu() {
    mobileMenu.classList.add('open');
    mobileOverlay.classList.add('show');
    hamburger.classList.add('open');
    document.body.classList.add('no-scroll');
}

function closeMenu() {
    mobileMenu.classList.remove('open');
    mobileOverlay.classList.remove('show');
    hamburger.classList.remove('open');
    document.body.classList.remove('no-scroll');
}

hamburger.addEventListener('click', () =>
    mobileMenu.classList.contains('open') ? closeMenu() : openMenu());
mobileClose.addEventListener('click', closeMenu);
mobileOverlay.addEventListener('click', closeMenu);

// Close menu when any mobile link is clicked
document.querySelectorAll('.mobile-link').forEach(link =>
    link.addEventListener('click', closeMenu));

/* ---- Smooth scroll ---- */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
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

/* ---- Scroll reveal ---- */
const revealObs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (!entry.isIntersecting) return;

        // Stagger cards/items in the same grid parent
        const siblings = Array.from(
            entry.target.parentElement.querySelectorAll('.reveal')
        );
        const index = siblings.indexOf(entry.target);

        setTimeout(() => {
            entry.target.classList.add('visible');
        }, index * 80);

        revealObs.unobserve(entry.target);
    });
}, { threshold: 0.1, rootMargin: '0px 0px -48px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObs.observe(el));

/* ---- Counter animation ---- */
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

const counterObs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        animateCounter(entry.target);
        counterObs.unobserve(entry.target);
    });
}, { threshold: 0.6 });

document.querySelectorAll('.counter').forEach(el => counterObs.observe(el));

/* ---- Contact form ---- */
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const btn      = this.querySelector('[type="submit"]');
        const original = btn.innerHTML;

        btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending…';
        btn.disabled  = true;

        // Simulate async submission
        setTimeout(() => {
            btn.innerHTML = '<i class="fas fa-check"></i> Request Sent!';
            btn.style.cssText = 'background:#27ae60;border-color:#27ae60;';

            setTimeout(() => {
                btn.innerHTML  = original;
                btn.style.cssText = '';
                btn.disabled   = false;
                contactForm.reset();
            }, 3200);
        }, 1400);
    });
}

/* ---- Footer year ---- */
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

/* ---- FAQ / Accordion ---- */
document.addEventListener('DOMContentLoaded', () => {
    const faqButtons = document.querySelectorAll('.faq-question');
    if (!faqButtons.length) return;

    faqButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const item = btn.closest('.faq-item');
            const open = item.classList.contains('open');

            // Close other items (accordion behavior)
            document.querySelectorAll('.faq-item.open').forEach(i => {
                if (i === item) return;
                i.classList.remove('open');
                i.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
                const a = i.querySelector('.faq-answer');
                a.setAttribute('aria-hidden', 'true');
                a.style.maxHeight = null;
            });

            const answer = item.querySelector('.faq-answer');
            if (!open) {
                item.classList.add('open');
                btn.setAttribute('aria-expanded', 'true');
                answer.setAttribute('aria-hidden', 'false');
                answer.style.maxHeight = answer.scrollHeight + 'px';
            } else {
                item.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
                answer.setAttribute('aria-hidden', 'true');
                answer.style.maxHeight = null;
            }
        });
    });
});
