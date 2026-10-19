document.addEventListener("DOMContentLoaded", () => {

    /*
     * =====================================================
     * ABOUT PAGE — SCROLL REVEALS
     * =====================================================
     */

    const revealItems = document.querySelectorAll(
        ".about-section__header, " +
        ".about-who__statement, " +
        ".about-who__content, " +
        ".philosophy-card, " +
        ".engineering-stage, " +
        ".technology-category, " +
        ".product-line, " +
        ".standard-item, " +
        ".about-team-card, " +
        ".about-cta__content"
    );


    if ("IntersectionObserver" in window) {

        const observer = new IntersectionObserver(
            (entries, observerInstance) => {

                entries.forEach((entry) => {

                    if (!entry.isIntersecting) {
                        return;
                    }

                    entry.target.classList.add(
                        "is-visible"
                    );

                    observerInstance.unobserve(
                        entry.target
                    );

                });

            },
            {
                threshold: 0.12,
                rootMargin: "0px 0px -40px 0px"
            }
        );


        revealItems.forEach((item, index) => {

            item.style.setProperty(
                "--reveal-delay",
                `${Math.min(index * 35, 300)}ms`
            );

            observer.observe(item);

        });

    } else {

        revealItems.forEach((item) => {
            item.classList.add("is-visible");
        });

    }


    /*
     * =====================================================
     * ENGINEERING STAGE INTERACTION
     * =====================================================
     */

    const engineeringStages =
        document.querySelectorAll(
            ".engineering-stage"
        );


    const progress =
        document.querySelector(
            ".engineering-progress span"
        );


    engineeringStages.forEach((stage, index) => {

        stage.addEventListener("mouseenter", () => {

            engineeringStages.forEach((item) => {
                item.classList.remove("is-active");
            });

            stage.classList.add("is-active");


            if (progress) {

                const percentage =
                    ((index + 1) /
                    engineeringStages.length) * 100;

                progress.style.height =
                    `${percentage}%`;
            }

        });

    });


    /*
     * =====================================================
     * TECHNOLOGY NODE INTERACTION
     * =====================================================
     */

    const technologyNodes =
        document.querySelectorAll(
            ".technology-node"
        );


    technologyNodes.forEach((node) => {

        node.addEventListener("mouseenter", () => {

            technologyNodes.forEach((item) => {
                item.classList.remove(
                    "technology-node--active"
                );
            });

            node.classList.add(
                "technology-node--active"
            );

        });

    });

});