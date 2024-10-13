
// toggle navbar
// toggle navbar
// toggle navbar
// toggle navbar


var toggle = document.getElementById("items");

var togglemanu = document.getElementById("toggle");
var display = 1;



function myFunction() {
    let w = window.outerWidth;
    if (w > 1030) {
        toggle.style.top = "-310px"
        togglemanu.style.top = "0px"

    }

}


function slide() {

    if (display == 1) {

        toggle.style.top = "10px"
        togglemanu.style.top = "240px"

        display = 0;
    }

    else {

        toggle.style.top = "-310px"
        togglemanu.style.top = "0px"
        display = 1;
    }

}









