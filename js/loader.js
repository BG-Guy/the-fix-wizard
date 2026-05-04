export function initLoader() {
    const loader = document.getElementById('loader');
    if (!loader) return; // page has no loader — don't lock scroll

    document.body.classList.add('no-scroll');
    window.addEventListener('load', () => {
        setTimeout(() => {
            loader.classList.add('out');
            setTimeout(() => {
                loader.style.display = 'none';
                document.body.classList.remove('no-scroll');
            }, 650);
        }, 3200);
    });
}
