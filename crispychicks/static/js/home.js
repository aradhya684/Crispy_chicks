
// toggle navbar
// toggle navbar
// toggle navbar
// toggle navbar


var toggle = document.getElementById("items");
var body_toggle = document.getElementById("bag_img");
var about_toggle = document.getElementById("about");
var manu_toggle = document.getElementById("menu_before");
var display = 1;



function myFunction() {
    let w = window.outerWidth;
    if (w > 1030) {
        toggle.style.top = "-400px"
        body_toggle.style.top = "0px"
        about_toggle.style.top = "80px"
        manu_toggle.style.top = "300px"
    }
    
}


function slide() {

    if (display == 0) {

        toggle.style.top = "5px"
        body_toggle.style.top = "192px"
        about_toggle.style.top = "250px"
        manu_toggle.style.top = "350px"
        display = 1;
    }

    else {

        toggle.style.top = "-400px"
        body_toggle.style.top = "0px"
        about_toggle.style.top = "80px"
        manu_toggle.style.top = "300px"
        display = 0;
    }

}









