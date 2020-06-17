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

/* Animation selectors */
var svg = document.getElementById("slides");
var s = Snap(svg);

var blobBackgrounds = document.getElementById("blob-backgrounds")
var startZoom = Snap.select('#startZoom');
var startZoomBlob = document.getElementById("startZoom")

var slide1Blob = Snap.select('#slide-1-blob');
var slide2Blob = Snap.select('#slide-2-blob');
var slide3Blob = Snap.select('#slide-3-blob');

var slide1Points = slide1Blob.node.getAttribute('d');
var slide2Points = slide2Blob.node.getAttribute('d');
var slide3Points = slide3Blob.node.getAttribute('d');

var indicator1 = document.getElementById("indicator1");
var indicator2 = document.getElementById("indicator2");
var indicator3 = document.getElementById("indicator3");

var slide1Image = document.getElementById("slide1");
var slide2Image = document.getElementById("slide2");
var slide3Image = document.getElementById("slide3");
var timeOut

var video = document.getElementById("vid");

/* Animation template functions */
function changeIndicator(activeIndicator) {
    slide1Image.style.opacity = slide2Image.style.opacity = slide3Image.style.opacity = 0;
    slide1Image.className = slide2Image.className = slide3Image.className = "hero-image";
    indicator1.className = indicator2.className = indicator3.className = "";
    activeIndicator.className = "active";
}

function changeBlobShape(finalBlobPoints, finalBlobImage, activateIndicator) {
    video.pause();
    slide1Image.className = slide2Image.className = slide3Image.className = "hero-image";
    setTimeout(() => {
        slide1Image.style.opacity = slide2Image.style.opacity = slide3Image.style.opacity = 0;
        slide1Blob.animate({ d: finalBlobPoints }, 2000, mina.backout);
        activateIndicator;
    }, 1000);
    setTimeout(() => {
        finalBlobImage.className = "hero-image-active";
        finalBlobImage.style.opacity = 1;
    }, 3500);
}

/* Change blobs and images for slides */
function toOne () {
    changeBlobShape(slide1Points, slide1Image, changeIndicator(indicator1));
    timeOut = setTimeout(() => { toTwo() }, 10000);
}

function toTwo() {
    changeBlobShape(slide2Points, slide2Image, changeIndicator(indicator2));
    timeOut = setTimeout(() => { toThree() }, 10000);
}

function toThree() {
    changeBlobShape(slide3Points, slide3Image, changeIndicator(indicator3));
    setTimeout(() => { video.play(); }, 4500);
    timeOut = setTimeout(() => { toOne(); }, 23000);
}

/* Starting animation with book */
function dotToSlideOne() {
    slide1Image.className = slide2Image.className = slide3Image.className = "hero-image";
    setTimeout(() => {
        startZoom.animate({ d: slide1Points }, 2500, mina.backout);
    }, 1000);
    setTimeout(() => {
        startZoomBlob.style.opacity = 0;
        blobBackgrounds.style.opacity = 1;
    }, 5500);
    toOne();
}

/* Trigger animations */
setTimeout(() => { dotToSlideOne() }, 1500);

/* Clicking indicators to change slides instantly */
indicator1.onclick = function () {
    clearTimeout(timeOut);
    changeIndicator(indicator1);
    toOne();
}
indicator2.onclick = function () {
    clearTimeout(timeOut);
    changeIndicator(indicator2);
    toTwo();
}
indicator3.onclick = function () {
    clearTimeout(timeOut);
    changeIndicator(indicator3);
    toThree();
}

/* Показать текст
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

/* Открыть ссылки
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
} */
