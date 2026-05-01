export function initMobileMenu() {
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

    document.querySelectorAll('.mobile-link').forEach(link =>
        link.addEventListener('click', closeMenu));
}
