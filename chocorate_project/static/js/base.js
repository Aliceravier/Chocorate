$(document).ready(function () {
    // get current URL path and assign 'active' class
    var pathname = window.location.pathname;
    $('.nav > li > a[href="' + pathname + '"]').parent().addClass('active');

    /*
    var icon = document.getElementsByClassName("icon-bars");
    var pushDown = document.getElementById("body-block");
    $(icon[0]).click(function () {
        if ($(pushDown).hasClass("push")) {
            pushDown.className = "pushUp";
        }
        else {
            pushDown.className = "push";
        }
    }*/
  
})

