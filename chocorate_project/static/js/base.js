$(document).ready(function () {
    // get current URL path and assign 'active' class
    var pathname = window.location.pathname;
    $('.nav > li > a[href="' + pathname + '"]').parent().addClass('active');
    $(".body-block").css("margin-top", function () {
        if ($(".navbar-toggle").attr('aria-expanded')=="true") {
            return "400px";
        }
        else {
            return "50px";
        }

    })
})

