const header = document.getElementById("header");

window.addEventListener("scroll", () => {

    if (window.scrollY > 60) {

        header.classList.add("scrolled");

    } else {

        header.classList.remove("scrolled");

    }

});

//    MOBILE MENU
const menu = document.getElementById("mobileMenu");

const overlay = document.getElementById("mobileOverlay");

const openBtn = document.getElementById("menuToggle");

const closeBtn = document.getElementById("closeMenu");

function openMenu(){

    menu.classList.add("active");

    overlay.classList.add("active");

    document.body.classList.add("menu-open");

    openBtn.setAttribute("aria-expanded", "true");

}

function closeMenu(){

    menu.classList.remove("active");

    overlay.classList.remove("active");

    document.body.classList.remove("menu-open");

    openBtn.setAttribute("aria-expanded", "false");

}

openBtn.addEventListener("click", openMenu);

closeBtn.addEventListener("click", closeMenu);

overlay.addEventListener("click", closeMenu);

document.addEventListener("keydown", function(e){

    if(e.key==="Escape"){

        closeMenu();

    }

});
