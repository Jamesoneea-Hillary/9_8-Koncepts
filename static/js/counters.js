document.addEventListener('DOMContentLoaded', () => {
    const counters = document.querySelectorAll('.counter');

    const animateCounter = (counter) => {
        const value = counter.dataset.counterValue || counter.dataset.target || '0';
        const match = value.match(/^([\d,.]+)(.*)$/);

        if (!match) {
            return;
        }

        const target = Number(match[1].replace(/,/g, ''));
        const suffix = counter.dataset.suffix || match[2];

        if (!Number.isFinite(target)) {
            return;
        }

        const duration = 1800;
        const startTime = performance.now();

        const updateCounter = (time) => {
            const progress = Math.min((time - startTime) / duration, 1);
            const displayedValue = Math.floor(progress * target);

            counter.textContent = `${displayedValue}${suffix}`;

            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = `${target}${suffix}`;
            }
        };

        requestAnimationFrame(updateCounter);
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) {
                return;
            }

            animateCounter(entry.target);
            observer.unobserve(entry.target);
        });
    }, { threshold: 0.4 });

    counters.forEach((counter) => observer.observe(counter));
});
