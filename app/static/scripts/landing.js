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

/* Blob animations */
var svg = document.getElementById("slides");
var s = Snap(svg);

var slide1Blob = Snap.select('#slide-1-blob');
var slide2Blob = Snap.select('#slide-2-blob');
var slide3Blob = Snap.select('#slide-3-blob');

var slide1Points = slide1Blob.node.getAttribute('d');
var slide2Points = slide2Blob.node.getAttribute('d');
var slide3Points = slide3Blob.node.getAttribute('d');

/* Book zoom animation */
var blobBackgrounds = document.getElementById("blob-backgrounds")
var startZoom = Snap.select('#startZoom');
var startZoomBlob = document.getElementById("startZoom")

function changeAnimationOpacity() {
    startZoomBlob.style.opacity = 0;
    blobBackgrounds.style.opacity = 1; 
}

setTimeout(() => {
    startZoom.animate({ d: slide1Points }, 1500, mina.backout);
}, 2500);
setTimeout(() => { changeAnimationOpacity() }, 3000);

/* Indicators */
var indicator1 = document.getElementById("indicator1")
var indicator2 = document.getElementById("indicator2")
var indicator3 = document.getElementById("indicator3")

function activateOne() {
    indicator1.className = "active";
    indicator2.className = "";
    indicator3.className = "";
}

function activateTwo() {
    indicator1.className = "";
    indicator2.className = "active";
    indicator3.className = "";
}

function activateThree() {
    indicator1.className = "";
    indicator2.className = "";
    indicator3.className = "active";
}

/* Landing page images */
var slide1Image = document.getElementById("slide1")
var slide2Image = document.getElementById("slide2")
var slide3Image = document.getElementById("slide3")
var timeOut

var toOne = function () {
    slide2Image.className = "hero-image";
    slide3Image.className = "hero-image";
    setTimeout(() => {
        slide1Blob.animate({ d: slide1Points }, 1500, mina.backout);
        activateOne();
    }, 1000);
    setTimeout(() => {
        slide1Image.className = "hero-image-active";
    }, 2000);
    timeOut = setTimeout(() => { toTwo() }, 5000);
}

var toTwo = function () {
    slide1Image.className = "hero-image";
    slide3Image.className = "hero-image";
    setTimeout(() => {
        slide1Blob.animate({ d: slide2Points }, 1500, mina.backout);
        activateTwo();
    }, 1000);
    setTimeout(() => { 
        slide2Image.className = "hero-image-active";
    }, 2000);
    timeOut = setTimeout(() => { toThree() }, 5000);
}

var toThree = function () {
    slide1Image.className = "hero-image";
    slide2Image.className = "hero-image";
    setTimeout(() => {
        slide1Blob.animate({ d: slide3Points }, 1500, mina.backout);
        activateThree();
    }, 1000);
    setTimeout(() => {
        slide3Image.className = "hero-image-active";
    }, 2000);
    timeOut = setTimeout(() => { toOne() }, 5000);
}

setTimeout(() => { toOne() }, 1500);

/* Changing slides manually */

indicator1.onclick = function () {
    clearTimeout(timeOut)
    activateOne();
    toOne();
}
indicator2.onclick = function () {
    clearTimeout(timeOut)
    activateTwo();
    toTwo();
}
indicator3.onclick = function () {
    clearTimeout(timeOut)
    activateThree();
    toThree();
}

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
