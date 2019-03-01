function navbarLocater() {
    nav = document.getElementById("homeNavbar");
    image = document.getElementById("reddishKnob");
    if (window.scrollY > "300") {
        nav.style.top = window.screenTop;
        //need to fix the nav bar to top of the page
    } else if (window.scrollY < "300") {
        nav.style.top = "300px";
    }
    
}