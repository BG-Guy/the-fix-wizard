export function initContactForm() {
    const contactForm = document.getElementById('contactForm');
    if (!contactForm) return;

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
                btn.innerHTML     = original;
                btn.style.cssText = '';
                btn.disabled      = false;
                contactForm.reset();
            }, 3200);
        }, 1400);
    });
}
