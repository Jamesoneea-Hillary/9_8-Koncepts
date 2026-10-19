document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.counter').forEach((counter) => {
        const value = counter.dataset.counterValue || counter.dataset.target || '0';
        const match = value.match(/^([\d,.]+)(.*)$/);

        if (!match) return;

        const target = Number(match[1].replace(/,/g, ''));
        const suffix = counter.dataset.suffix || match[2];

        if (!Number.isFinite(target)) return;

        const startTime = performance.now();
        const duration = 1800;

        const update = (time) => {
            const progress = Math.min((time - startTime) / duration, 1);
            counter.textContent = `${Math.floor(progress * target)}${suffix}`;

            if (progress < 1) {
                requestAnimationFrame(update);
            }
        };

        requestAnimationFrame(update);
    });
});