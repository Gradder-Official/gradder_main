$(window).on("load",function(){
    $('html, body').css('overflow', 'auto'); 
    AOS.init();
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
    blobBackgrounds.style.opacity = 1;
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

/* Navigation */
var scrollspyNav = document.getElementById("scrollspy-nav");
$(document).scroll(function () {
    var y = $(this).scrollTop();
    if (y > 600) {
        scrollspyNav.style.opacity = 1;
    } else {
        scrollspyNav.style.opacity = 0;
    }
});