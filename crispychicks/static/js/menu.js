
// toggle navbar
// toggle navbar
// toggle navbar
// toggle navbar


const toggle = document.getElementById("items");
const togglemenu = document.getElementById("toggle");
var display = 1;
var w;


function sizefunction() {
    w = window.outerWidth;
    if (w > 1030) {
        toggle.style.top = "-305px"
        togglemenu.style.top = "0px"
    }
};

function slide() {

    if (display == 1) {

        toggle.style.top = "0px"
        togglemenu.style.top = "205px"
        display = 0;
    }

    else {

        toggle.style.top = "-305px"
        togglemenu.style.top = "0px"
        display = 1;
    }

}



function scrollfunction(){

    //for more then 1100
    //for more then 1100
    //for more then 1100
    //for more then 1100
    //for more then 1100

    w = window.outerWidth;
    var scroll = scrollY;

    const card_1 = document.querySelector(".side-element-1")
    const card_2 = document.querySelector(".side-element-2")
    const card_3 = document.querySelector(".side-element-3")
    const card_4 = document.querySelector(".side-element-4")
    const card_5 = document.querySelector(".side-element-5")
    const card_6 = document.querySelector(".side-element-6")
    const card_7 = document.querySelector(".side-element-7")
    const card_8 = document.querySelector(".side-element-8")
    const card_9 = document.querySelector(".side-element-9")

    if(w>1100){
     
     // console.log(scroll)
 
     if (scroll>255 && scroll<1994 ) {
         
         card_1.classList.add("show-red");
     } 
     else{
         
         card_1.classList.remove("show-red");
     }
 
     if (scroll>1995 && scroll<3209 ) {
     
         card_2.classList.add("show-red");
     } 
     else{
         
         card_2.classList.remove("show-red");
     }
 
 
     if (scroll>3210 && scroll<4417 ) {
      
         card_3.classList.add("show-red");
     } 
     else{
         
         card_3.classList.remove("show-red");
     }
 
     if (scroll>4418 && scroll<5104 ) {
        
         card_4.classList.add("show-red");
     } 
     else{
        
         card_4.classList.remove("show-red");
     }
 
     if (scroll>5105 && scroll<6839 ) {
         
         card_5.classList.add("show-red");
     } 
     else{
         
         card_5.classList.remove("show-red");
     }
     
 
     if (scroll>6840 && scroll<7524 ) {
         
         card_6.classList.add("show-red");
     } 
     else{
         
         card_6.classList.remove("show-red");
     }
 
     if (scroll>7525 && scroll<9785 ) {
         
         card_7.classList.add("show-red");
     } 
     else{
         
         card_7.classList.remove("show-red");
     }
 
     if (scroll>9786 && scroll<12574 ) {
         
         card_8.classList.add("show-red");
     } 
     else{
        
         card_8.classList.remove("show-red");
     }
 
     if (scroll>12575 ) {
         
         card_9.classList.add("show-red");
     } 
     else{
      
         card_9.classList.remove("show-red");
     }
 
    }


    // for screen between 1100 and 835
    // for screen between 1100 and 835
    // for screen between 1100 and 835
    // for screen between 1100 and 835
    // for screen between 1100 and 835
    // for screen between 1100 and 835

    if (835<w && w<=1100) {


    if (scroll>260 && scroll<1950) {
        
        card_1.classList.add("show-red");
    } 
    else{
        
        card_1.classList.remove("show-red");
    }

    if (scroll>1951 && scroll<3175) {
    
        card_2.classList.add("show-red");
    } 
    else{
        
        card_2.classList.remove("show-red");
    }


    if (scroll>3176 && scroll<4395) {
     
        card_3.classList.add("show-red");
    } 
    else{
        
        card_3.classList.remove("show-red");
    }

    if (scroll>4396 && scroll<5095 ) {
       
        card_4.classList.add("show-red");
    } 
    else{
       
        card_4.classList.remove("show-red");
    }

    if (scroll>5096 && scroll<6836 ) {
        
        card_5.classList.add("show-red");
    } 
    else{
        
        card_5.classList.remove("show-red");
    }
    

    if (scroll>6837 && scroll<7595 ) {
        
        card_6.classList.add("show-red");
    } 
    else{
        
        card_6.classList.remove("show-red");
    }

    if (scroll>7596 && scroll<9802 ) {
        
        card_7.classList.add("show-red");
    } 
    else{
        
        card_7.classList.remove("show-red");
    }

    if (scroll>9803 && scroll<12588 ) {
        
        card_8.classList.add("show-red");
    } 
    else{
       
        card_8.classList.remove("show-red");
    }

    if (scroll>12589 ) {
        
        card_9.classList.add("show-red");
    } 
    else{
     
        card_9.classList.remove("show-red");
    }

    }

    };



