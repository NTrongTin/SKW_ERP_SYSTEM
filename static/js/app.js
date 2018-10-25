$( document ).ready(function() {
     $('.sidebarToggle').on('click', function(e) {
     $('.side-nav').toggleClass("open");
     e.preventDefault();
    });
});