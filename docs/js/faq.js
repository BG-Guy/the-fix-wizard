export function initFAQ() {
    const faqButtons = document.querySelectorAll('.faq-question');
    if (!faqButtons.length) return;

    faqButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const item = btn.closest('.faq-item');
            const open = item.classList.contains('open');

            // Collapse any other open item (accordion behaviour)
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
}
