/* Loader */
$(window).on("load",function(){
     $('html, body').css('overflow', 'auto'); 
});

/* Анимация полей для ввода при фокусе or блюре or загрузке */
$(".input input").focus(function () {
   $(this).parent(".input").each(function () {
      $("label", this).css({
         "font-size": "12px",
         "top": "-2px"
      })
      $(this).css({
         "border": "2px solid #4DB071"
      })
   });
}).blur(function () {
   $(".input").css({
      "border": "2px solid #D5D7DA"
   })
   if ($(this).val() == "") {
      $(this).parent(".input").each(function () {
         $("label", this).css({
            "font-size": "16px",
            "top": "10px"
         })
      });
   }
});

/* Открыть ссылки */
function linkOpen(url, type) {
  if (type == 'blank') {
      window.open(url); // в новой вкладке
  } else if (type == 'curr') {
      window.location.assign(url); // в текущем окне
  } 
}

/* Ripples animation */
$(window, document, undefined).ready(function() {

  var $ripples = $('.ripples');

  $ripples.on('click.Ripples', function(e) {
    var $this = $(this);
    var $offset = $this.parent().offset();
    var $circle = $this.find('.ripplesCircle');

    var x = e.pageX - $offset.left;
    var y = e.pageY - $offset.top;

    $circle.css({
      top: y + 'px',
      left: x + 'px'
    });

    $this.addClass('is-active');
  });

  $ripples.on('animationend webkitAnimationEnd mozAnimationEnd oanimationend MSAnimationEnd', function(e) {
    $(this).removeClass('is-active');
  });
});
