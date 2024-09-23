
// toggle navbar
// toggle navbar
// toggle navbar
// toggle navbar


var toggle = document.getElementById("items");
var body_toggle = document.getElementById("bag_img");
var display = 1;



function myFunction() {
    let w = window.outerWidth;
    if (w > 1030) {
        toggle.style.top = "-310px"
        body_toggle.style.top = "0px"

    }
}


function slide() {

    if (display == 1) {

        toggle.style.top = "0px"
        body_toggle.style.top = "210px"
        display = 0;
    }

    else {

        toggle.style.top = "-310px"
        body_toggle.style.top = "0px"
        display = 1;
    }

}









