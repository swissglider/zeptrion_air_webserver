(function($) {
  "use strict"; // Start of use strict

  //$SCRIPT_ROOT = {{ request.script_root|tojson|safe }};

  // Smooth scrolling using jQuery easing
  $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: (target.offset().top - 70)
        }, 1000, "easeInOutExpo");
        return false;
      }
    }
  });

  // Scroll to top button appear
  $(document).scroll(function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $('.scroll-to-top').fadeIn();
    } else {
      $('.scroll-to-top').fadeOut();
    }
  });

  // Closes responsive menu when a scroll trigger link is clicked
  $('.js-scroll-trigger').click(function() {
    $('.navbar-collapse').collapse('hide');
  });

  // Activate scrollspy to add active class to navbar items on scroll
  $('body').scrollspy({
    target: '#mainNav',
    offset: 80
  });

  // Collapse Navbar
  var navbarCollapse = function() {
    if ($("#mainNav").offset().top > 100) {
      $("#mainNav").addClass("navbar-shrink");
    } else {
      $("#mainNav").removeClass("navbar-shrink");
    }
  };
  // Collapse now if page is not at top
  navbarCollapse();
  // Collapse the navbar when page is scrolled
  $(window).scroll(navbarCollapse);

  // Modal popup$(function () {
  $('.portfolio-item').magnificPopup({
    type: 'inline',
    preloader: false,
    focus: '#username',
    modal: true
  });
  $(document).on('click', '.portfolio-modal-send', function(e) {
    alert('Hallo')
    e.preventDefault();
    $.magnificPopup.close();
  });
  $( "#send_btn" ).click(function() {
    $('#progressbar_smart_button').removeClass('in_end')
    $('#progressbar_smart_button').addClass('in')
    $('#change_smart_button_config_status_div').removeClass('alert alert-success')
    $('#change_smart_button_config_status_div').addClass('alert alert-warning')
    $('#change_smart_button_config_status').text('waiting to press a smart button ...')
    $.getJSON('/_change_smart_button', {
      ip_input: $("#ip_input").val(),
      port_input: $("#port_input").val(),
      path_input: $("#path_input").val(),
      content_type_input: $("#content_type_input").val(),
      request_type_input: $("#request_type_input option:selected").text(),
      body_input: $("#body_input").val()
    }, function(data) {
      $('#progressbar_smart_button').removeClass('in')
      $('#progressbar_smart_button').addClass('in_end')
      $('#change_smart_button_config_status_div').removeClass('alert alert-warning')
      $('#change_smart_button_config_status_div').addClass('alert alert-success')
      $('#change_smart_button_config_status').text(data.result)
    });
  });
  $(document).on('click', '.portfolio-modal-dismiss', function(e) {
    e.preventDefault();
    $.magnificPopup.close();
  });

  // Floating label headings for the contact form
  $(function() {
    $("body").on("input propertychange", ".floating-label-form-group", function(e) {
      $(this).toggleClass("floating-label-form-group-with-value", !!$(e.target).val())
    }).on("focus", ".floating-label-form-group", function() {
      $(this).addClass("floating-label-form-group-with-focus")
    }).on("blur", ".floating-label-form-group", function() {
      $(this).removeClass("floating-label-form-group-with-focus")
    })
  })

})(jQuery); // End of use strict
