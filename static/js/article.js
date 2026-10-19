document.addEventListener("DOMContentLoaded", () => {

    /*
    ---------------------------------------
    READING PROGRESS
    ---------------------------------------
    */

    const progressBar =
        document.getElementById("readingProgress");

    const article =
        document.getElementById("articleContent");


    function updateReadingProgress() {

        if (!progressBar || !article) {
            return;
        }


        const articleTop =
            article.offsetTop;

        const articleHeight =
            article.offsetHeight;

        const scrollPosition =
            window.scrollY;


        const readableHeight =
            articleHeight -
            window.innerHeight;


        if (scrollPosition <= articleTop) {

            progressBar.style.width = "0%";

            return;

        }


        const progress =
            (
                (scrollPosition - articleTop)
                /
                readableHeight
            ) * 100;


        const clampedProgress =
            Math.min(
                Math.max(progress, 0),
                100
            );


        progressBar.style.width =
            `${clampedProgress}%`;

    }


    window.addEventListener(
        "scroll",
        updateReadingProgress,
        { passive: true }
    );


    updateReadingProgress();


    /*
    ---------------------------------------
    ARTICLE OUTLINE
    ---------------------------------------
    */

    const outline =
        document.getElementById("articleOutline");


    if (outline && article) {

        const headings =
            article.querySelectorAll(
                "h2, h3"
            );


        if (!headings.length) {

            outline.innerHTML =
                "<span>No sections</span>";

        } else {

            outline.innerHTML = "";


            headings.forEach(
                (heading, index) => {

                    const id =
                        `section-${index}`;

                    heading.id = id;


                    const link =
                        document.createElement("a");


                    link.href =
                        `#${id}`;


                    link.textContent =
                        heading.textContent;


                    outline.appendChild(
                        link
                    );

                }
            );

        }

    }

});