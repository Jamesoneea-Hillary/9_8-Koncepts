document.addEventListener("DOMContentLoaded", () => {

    /* =====================================================
       SCROLL REVEAL
    ===================================================== */

    const revealElements = document.querySelectorAll(
        ".reveal"
    );

    const revealObserver = new IntersectionObserver(
        (entries) => {

            entries.forEach((entry) => {

                if (entry.isIntersecting) {

                    entry.target.classList.add("active");

                    revealObserver.unobserve(
                        entry.target
                    );

                }

            });

        },
        {
            threshold: 0.15
        }
    );


    revealElements.forEach((element) => {

        revealObserver.observe(element);

    });



    /* =====================================================
       MAGNETIC PROJECT CARDS
    ===================================================== */

    const projectCards = document.querySelectorAll(
        ".magnetic-card"
    );

    projectCards.forEach((card) => {

        card.addEventListener(
            "mousemove",
            (event) => {

                const rect =
                    card.getBoundingClientRect();

                const x =
                    event.clientX -
                    rect.left;

                const y =
                    event.clientY -
                    rect.top;

                const centerX =
                    rect.width / 2;

                const centerY =
                    rect.height / 2;

                const moveX =
                    (x - centerX) * 0.05;

                const moveY =
                    (y - centerY) * 0.05;

                card.style.transform =
                    `translate(${moveX}px, ${moveY}px)`;

            }
        );


        card.addEventListener(
            "mouseleave",
            () => {

                card.style.transform =
                    "translate(0px, 0px)";

            }
        );

    });



    /* =====================================================
       PORTFOLIO FILTERING
    ===================================================== */

    const filterButtons =
        document.querySelectorAll(
            ".filter-btn"
        );

    const projects =
        document.querySelectorAll(
            ".portfolio-project"
        );


    filterButtons.forEach((button) => {

        button.addEventListener(
            "click",
            () => {

                const filter =
                    button.dataset.filter;


                /* ACTIVE BUTTON */

                filterButtons.forEach(
                    (btn) => {

                        btn.classList.remove(
                            "active"
                        );

                    }
                );


                button.classList.add(
                    "active"
                );


                /* FILTER PROJECTS */

                projects.forEach(
                    (project) => {

                        const category =
                            project.dataset.category;


                        project.classList.remove(
                            "show"
                        );


                        setTimeout(
                            () => {

                                if (
                                    filter === "all" ||
                                    category === filter
                                ) {

                                    project.style.display =
                                        "block";


                                    setTimeout(
                                        () => {

                                            project.classList.add(
                                                "show"
                                            );

                                        },
                                        30
                                    );

                                } else {

                                    project.style.display =
                                        "none";

                                }

                            },
                            250
                        );

                    }
                );

            }
        );

    });



    /* =====================================================
       IMAGE LIGHTBOX
    ===================================================== */

    const galleryImages =
        document.querySelectorAll(
            ".lightbox-image"
        );


    if (
        galleryImages.length > 0
    ) {

        const lightbox =
            document.createElement(
                "div"
            );


        lightbox.className =
            "image-lightbox";


        lightbox.innerHTML = `

            <div
                class="lightbox-backdrop"
            ></div>

            <div
                class="lightbox-container"
            >

                <button
                    class="lightbox-close"
                    aria-label="Close image"
                >
                    ×
                </button>


                <img
                    src=""
                    alt=""
                    class="lightbox-preview"
                >


            </div>

        `;


        document.body.appendChild(
            lightbox
        );


        const preview =
            lightbox.querySelector(
                ".lightbox-preview"
            );


        const closeButton =
            lightbox.querySelector(
                ".lightbox-close"
            );


        const backdrop =
            lightbox.querySelector(
                ".lightbox-backdrop"
            );


        galleryImages.forEach(
            (image) => {

                image.addEventListener(
                    "click",
                    () => {

                        preview.src =
                            image.src;

                        preview.alt =
                            image.alt;


                        lightbox.classList.add(
                            "open"
                        );


                        document.body.style.overflow =
                            "hidden";

                    }
                );

            }
        );


        const closeLightbox =
            () => {

                lightbox.classList.remove(
                    "open"
                );


                document.body.style.overflow =
                    "";

            };


        closeButton.addEventListener(
            "click",
            closeLightbox
        );


        backdrop.addEventListener(
            "click",
            closeLightbox
        );


        document.addEventListener(
            "keydown",
            (event) => {

                if (
                    event.key === "Escape"
                ) {

                    closeLightbox();

                }

            }
        );

    }

});