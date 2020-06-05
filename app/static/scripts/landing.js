/* Loader */
$(window).on("load",function(){
     $(".loader-wrapper").fadeOut("slow");

     $('html, body').css('overflow', 'auto'); 
});

window.onload = function(){ 
   	if (localStorage.getItem('lang') == null) {
      localStorage.lang = "укр";
   	}
} 	

/* Landing page carousel */
$(document).ready(function () {
    $(".carousel").carousel({ interval: 10000 });
});

/* Показать текст */
document.getElementsByClassName('custom-options')[0].addEventListener('click', function() {
	document.getElementById('problem').style.opacity = "1";
	document.getElementById('problem').style.pointerEvents = "auto";
	document.getElementById('problemLink').style.color = "#212121";

	document.getElementById('solution').style.opacity = "0";
	document.getElementById('solution').style.pointerEvents = "none";
	document.getElementById('solutionLink').style.color = "#A3A3A3";
});

function showText(text){
	if (text == 'solution') {
		document.getElementById(text).style.opacity = "1";
		document.getElementById(text).style.pointerEvents = "auto";
		document.getElementById('solutionLink').style.color = "#212121";

		document.getElementById('problem').style.opacity = "0";
		document.getElementById('problem').style.pointerEvents = "none";
		document.getElementById('problemLink').style.color = "#A3A3A3";
	} else if (text == 'problem') {
		document.getElementById(text).style.opacity = "1";
		document.getElementById(text).style.pointerEvents = "auto";
		document.getElementById('problemLink').style.color = "#212121";

		document.getElementById('solution').style.opacity = "0";
		document.getElementById('solution').style.pointerEvents = "none";
		document.getElementById('solutionLink').style.color = "#A3A3A3";
	}
}

/* Открыть ссылки */
function linkOpen(url, type) {
	if (type == 'blank') {
  		window.open(url); // в новой вкладке
	} else if (type == 'curr') {
  		window.location.assign(url); // в текущем окне
	}	
}

function outsideOnclick() {
   let langScreen = document.getElementsByClassName('custom-options')[0];
   let langBtn = document.getElementsByClassName('custom-select-trigger')[0];

   if (event.target != langScreen && event.target != langBtn) {
      document.getElementsByClassName('custom-options')[0].style.opacity = "0";
      langAppear('none', 70);
   }
}
