$(function() {
  $('a[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});

var trigStickyNav = $('#navigation').offset();
$( window ).scroll(function() {
  if ( $( window ).scrollTop() >= trigStickyNav.top ) {
    $('.Navigation').addClass('fixedTop');
  }
  if ( $( window ).scrollTop() < trigStickyNav.top ) {
    $('.Navigation').removeClass('isOpen fixedTop');
  }
});

$('.js-open-navmenu').click(function() {
  if ( $('.Navigation').hasClass('fixedTop') ) {
    $('.Navigation').toggleClass('isOpen');
  }
});

$('.Navigation-link').click(function() {
  $('.Navigation').removeClass('isOpen');
});