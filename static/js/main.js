document.addEventListener('DOMContentLoaded', () => {
    const scrollTopButton = document.querySelector('#scrollTop');

    if (!scrollTopButton) {
        return;
    }

    const toggleVisibility = () => {
        scrollTopButton.classList.toggle('is-visible', window.scrollY > 400);
    };

    window.addEventListener('scroll', toggleVisibility, { passive: true });
    toggleVisibility();

    scrollTopButton.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
});
