export function initLoader() {
    const loader = document.getElementById('loader');
    if (!loader) return;

    document.body.classList.add('no-scroll');

    // Cap total loader time at 800ms from navigation start.
    // performance.now() tells us how much time has already passed by the time
    // this script runs — so we only wait the remaining gap, not a fixed delay.
    // On slow connections (Lighthouse) the loader fades almost immediately;
    // on fast connections users see a ~700ms branded animation.
    const MAX_MS = 800;
    const delay  = Math.max(0, MAX_MS - Math.round(performance.now()));

    setTimeout(() => {
        loader.classList.add('out');
        setTimeout(() => {
            loader.style.display = 'none';
            document.body.classList.remove('no-scroll');
        }, 450);
    }, delay);
}
