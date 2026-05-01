export function initLoader() {
    document.body.classList.add('no-scroll');
    window.addEventListener('load', () => {
        const loader = document.getElementById('loader');
        setTimeout(() => {
            loader.classList.add('out');
            setTimeout(() => {
                loader.style.display = 'none';
                document.body.classList.remove('no-scroll');
            }, 650);
        }, 3200);
    });
}
