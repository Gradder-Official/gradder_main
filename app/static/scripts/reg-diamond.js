// Registration script //

/* Loader */
$(window).on("load", function () {
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
         "border": "2px solid #2B9264"
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

/* События при загрузке */
window.onload = function () {
   greetingsLang();

   if (localStorage.getItem('lang') == null) {
      localStorage.lang = "укр";
   }

   document.getElementById('first name').focus();

   window.addEventListener('submit', function (e) {
      validateSubmit(e, btnValid);
   })
}

/* Открыть ссылку в текущем окне */
function openLink(link) {
   window.open(link);
}

/* Запоминание класса */
function classOnblur(classNum) {
   className = document.getElementById(classNum).value;

   if (className != "") {
      if (classNum == 'class1') {

      } else if (classNum == 'class2') {

      } else if (classNum == 'class3') {

      } else if (classNum == 'class4') {

      } else if (classNum == 'class5') {

      } else if (classNum == 'class6') {

      } else if (classNum == 'class7') {

      } else if (classNum == 'class8') {

      }
   }
}

/* Количество классов */
var groupsAmount = document.getElementById("groupsAmount");
var val1, valStatus;

function upAmount(max) {
   groupsAmount.value = parseInt(groupsAmount.value) + 1;
   if (groupsAmount.value >= parseInt(max)) {
      groupsAmount.value = max;
   }

   checkAmount();
}
function downAmount(min) {
   groupsAmount.value = parseInt(groupsAmount.value) - 1;
   if (groupsAmount.value <= parseInt(min)) {
      groupsAmount.value = min;
   }

   checkAmount();
}

function amountFocus() {
   val1 = document.getElementById("groupsAmount").value;

   groupsAmount.addEventListener('change', checkAmount);
}
function checkAmount() {
   let valCurr = document.getElementById("groupsAmount").value;

   if (valCurr > val1) {
      valStatus = 'up';

      val1 = document.getElementById("groupsAmount").value;
   } else if (valCurr < val1) {
      valStatus = 'down';

      val1 = document.getElementById("groupsAmount").value;
   }

   //let nthValue = 'div.input:nth-child(-n+' + groupsAmount.value + ')';
   //let nthValue2 = 'div.input:nth-child(-n+' + (groupsAmount.value - 4) + ')';
   let firstRow = document.getElementById('firstRow');
   let secondRow = document.getElementById('secondRow');

   if (groupsAmount.value < 5) {
      if (valStatus == 'up') {
         for (i = 0; i < groupsAmount.value; i++) {
            firstRow.getElementsByClassName('input')[i].style.opacity = "1";
            firstRow.getElementsByClassName('input')[i].style.pointerEvents = "auto";
         }
      } else if (valStatus == 'down') {
         for (i = 3; i > (groupsAmount.value - 1); i--) {
            firstRow.getElementsByClassName('input')[i].style.opacity = "0";
            firstRow.getElementsByClassName('input')[i].style.pointerEvents = "none";
         }

         secondRow.getElementsByClassName('input')[0].style.opacity = "0";
         secondRow.getElementsByClassName('input')[0].style.position = "absolute";
         secondRow.getElementsByClassName('input')[0].style.pointerEvents = "none";
         secondRow.style.marginBottom = "0";
      }
   } else if (groupsAmount.value > 4) {
      if (valStatus == 'up') {
         for (i = 0; i < 4; i++) {
            firstRow.getElementsByClassName('input')[i].style.opacity = "1";
            firstRow.getElementsByClassName('input')[i].style.pointerEvents = "auto";
         }
         for (i = 0; i < (groupsAmount.value - 4); i++) {
            secondRow.getElementsByClassName('input')[i].style.opacity = "1";
            secondRow.getElementsByClassName('input')[i].style.position = "relative";
            secondRow.getElementsByClassName('input')[i].style.pointerEvents = "auto";
         }

         secondRow.style.marginBottom = "14px";
      } else if (valStatus == 'down') {
         for (i = 3; i > (groupsAmount.value - 5); i--) {
            secondRow.getElementsByClassName('input')[i].style.opacity = "0";
            secondRow.getElementsByClassName('input')[i].style.position = "absolute";
            secondRow.getElementsByClassName('input')[i].style.pointerEvents = "none";
         }
      }
   }
}

/* Приветствие имени */
var firstName, reg_name = 0;

function firstnameOnblur() {
   firstName = document.getElementById('first name').value;

   firstName = firstName.charAt(0).toUpperCase() + firstName.slice(1);

   if (firstName != "") {
      if (reg_name == 0) {
         if (localStorage.getItem('lang') == "укр") {
            document.getElementById('greetings').innerHTML = "Ласкаво просимо до<br>Gradder" + "<span id='spanName'>, " + firstName + "</span>";
         } else if (localStorage.getItem('lang') == "рус") {
            document.getElementById('greetings').innerHTML = "Добро пожаловать в<br>Gradder" + "<span id='spanName'>, " + firstName + "</span>";
         } else if (localStorage.getItem('lang') == "eng") {
            document.getElementById('greetings').innerHTML = "Welcome to<br>Gradder" + "<span id='spanName'>, " + firstName + "</span>";
         }
         document.getElementById('spanName').style.transition = "all 0.15s";

         setTimeout(function () {
            appear('spanName');
         }, 1);

         reg_name = 1;
         localStorage.reg_name = firstName;
      } else if (reg_name == 1) {
         if (localStorage.getItem('lang') == "укр") {
            document.getElementById('greetings').innerHTML = "Ласкаво просимо до<br>Gradder" + "<span id='spanName'>, " + firstName + "</span>";
         } else if (localStorage.getItem('lang') == "рус") {
            document.getElementById('greetings').innerHTML = "Добро пожаловать в<br>Gradder" + "<span id='spanName'>, " + firstName + "</span>";
         } else if (localStorage.getItem('lang') == "eng") {
            document.getElementById('greetings').innerHTML = "Welcome to<br>Gradder" + "<span id='spanName'>, " + firstName + "</span>";
         }
         document.getElementById('spanName').style.transition = "all 0s";

         appear('spanName');

         localStorage.reg_name = firstName;
      }
   } else if (reg_name == 1) {
      document.getElementById('spanName').style.opacity = "0";
      document.getElementById('spanName').style.transition = "all 0.15s";

      setTimeout(textDelete, 150);

      reg_name = 0;
   }

   reg_btnStatus();
}

document.getElementsByClassName('custom-options')[0].addEventListener('click', greetingsLang);

function greetingsLang() {
   if (reg_name == 1) {
      if (localStorage.getItem('lang') == "укр") {
         document.getElementById('greetings').innerHTML = "Ласкаво просимо до<br>Gradder" + "<span id='spanName'>, " + firstName + "</span>";
         document.getElementById('spanName').style.opacity = "1";
      } else if (localStorage.getItem('lang') == "рус") {
         document.getElementById('greetings').innerHTML = "Добро пожаловать в<br>Gradder" + "<span id='spanName'>, " + firstName + "</span>";
         document.getElementById('spanName').style.opacity = "1";
      } else if (localStorage.getItem('lang') == "eng") {
         document.getElementById('greetings').innerHTML = "You're welcome to<br>Gradder" + "<span id='spanName'>, " + firstName + "</span>";
         document.getElementById('spanName').style.opacity = "1";
      }
   } else if (reg_name == 0) {
      if (localStorage.getItem('lang') == "укр") {
         document.getElementById('greetings').innerHTML = "Ласкаво просимо до<br>Gradder";
      } else if (localStorage.getItem('lang') == "рус") {
         document.getElementById('greetings').innerHTML = "Добро пожаловать в<br>Gradder";
      } else if (localStorage.getItem('lang') == "eng") {
         document.getElementById('greetings').innerHTML = "You're welcome to<br>Gradder";
      }
   }
}

function textDelete() {
   if (localStorage.getItem('lang') == "укр") {
      document.getElementById('greetings').innerHTML = "Ласкаво просимо до<br>Gradder";
   } else if (localStorage.getItem('lang') == "рус") {
      document.getElementById('greetings').innerHTML = "Добро пожаловать в<br>Gradder";
   } else if (localStorage.getItem('lang') == "eng") {
      document.getElementById('greetings').innerHTML = "Welcome to<br>Gradder";
   }
}
function appear(id) {
   document.getElementById(id).style.opacity = "1";
}

/* Запоминание действий */
function agreeOnclick() {
   if (document.getElementById('agree').checked) {
      localStorage.reg_checkbox = true;
   } else {
      localStorage.reg_checkbox = false;
   }

   reg_btnStatus();
}

/* Возможность нажать на кнопку or отправить форму */
var pwdValid, emailValid, btnValid;

function reg_btnStatus() {
   let name = document.getElementById('first name').value;
   let btn = document.getElementById('buttonA');

   name = name.charAt(0).toUpperCase() + name.slice(1);

   if (reg_name == 1 && name == firstName && emailValid == 1) {
      btn.style.background = "#2B9264";
      btn.style.color = "#fcfcfc";
      btn.classList.add('btn-active');
      btn.style.pointerEvents = 'auto';

      btnValid = true;
   } else {
      btn.style.background = "#EAF4EF";
      btn.style.color = "#9EA1A3";
      btn.classList.remove('btn-active');
      btn.style.pointerEvents = 'none';

      btnValid = false;
   }
}

function validateEmail(input) {
   let format = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
   let text = document.getElementById(input).value;

   if (format.test(text)) {
      emailValid = 1;
   } else {
      emailValid = 0;
   }

   reg_btnStatus();
}

function validateSubmit(e, id) {
   if (id != true) {
      e.preventDefault();
   } else {
      localStorage.reg_completed = true;
   }
}

/* Проверка правильности пароля */
function pwdStatus() {
   let password = document.getElementById('password');
   let eight, numnum, lettercase;

   if (password.value.length > 7) {
      eight = 1;
      let li = document.getElementById('length_li');
      li.style.color = "#1C8256";
      li.getElementsByTagName('img')[0].src = "../icons/checkmark.svg";
      li.getElementsByTagName('img')[0].style.width = "16px";
      li.getElementsByTagName('img')[0].style.marginBottom = "-1px";
      li.getElementsByTagName('img')[0].style.marginLeft = "1px";
      li.getElementsByTagName('img')[0].style.filter = "invert(44%) sepia(19%) saturate(1306%) hue-rotate(101deg) brightness(94%) contrast(92%)";
   } else {
      eight = 0;
      let li = document.getElementById('length_li');
      li.style.color = "#5F6368";
      li.getElementsByTagName('img')[0].src = "../icons/circle.svg";
      li.getElementsByTagName('img')[0].style.width = "17px";
      li.getElementsByTagName('img')[0].style.marginBottom = "-4px";
      li.getElementsByTagName('img')[0].style.marginLeft = "0px";
      li.getElementsByTagName('img')[0].style.filter = "none";
   }
   if (password.value.search(/[0-9]/) != -1 && password.value.search(/[a-zA-Z]/) != -1) {
      numnum = 1;
      let li = document.getElementById('symbols_li');
      li.style.color = "#1C8256";
      li.getElementsByTagName('img')[0].src = "../icons/checkmark.svg";
      li.getElementsByTagName('img')[0].style.width = "16px";
      li.getElementsByTagName('img')[0].style.marginBottom = "-1px";
      li.getElementsByTagName('img')[0].style.marginLeft = "1px";
      li.getElementsByTagName('img')[0].style.filter = "invert(44%) sepia(19%) saturate(1306%) hue-rotate(101deg) brightness(94%) contrast(92%)";
   } else {
      numnum = 0;
      let li = document.getElementById('symbols_li');
      li.style.color = "#5F6368";
      li.getElementsByTagName('img')[0].src = "../icons/circle.svg";
      li.getElementsByTagName('img')[0].style.width = "17px";
      li.getElementsByTagName('img')[0].style.marginBottom = "-4px";
      li.getElementsByTagName('img')[0].style.marginLeft = "0px";
      li.getElementsByTagName('img')[0].style.filter = "none";
   }
   if (password.value.search(/[a-z]/) != -1 && password.value.search(/[A-Z]/) != -1) {
      lettercase = 1;
      let li = document.getElementById('lettercase_li');
      li.style.color = "#1C8256";
      li.getElementsByTagName('img')[0].src = "../icons/checkmark.svg";
      li.getElementsByTagName('img')[0].style.width = "16px";
      li.getElementsByTagName('img')[0].style.marginBottom = "-1px";
      li.getElementsByTagName('img')[0].style.marginLeft = "1px";
      li.getElementsByTagName('img')[0].style.filter = "invert(44%) sepia(19%) saturate(1306%) hue-rotate(101deg) brightness(94%) contrast(92%)";
   } else {
      lettercase = 0;
      let li = document.getElementById('lettercase_li');
      li.style.color = "#5F6368";
      li.getElementsByTagName('img')[0].src = "../icons/circle.svg";
      li.getElementsByTagName('img')[0].style.width = "17px";
      li.getElementsByTagName('img')[0].style.marginBottom = "-4px";
      li.getElementsByTagName('img')[0].style.marginLeft = "0px";
      li.getElementsByTagName('img')[0].style.filter = "none";
   }

   if (eight == 1 && numnum == 1 && lettercase == 1) {
      pwdValid = 1;
   } else {
      pwdValid = 0;
   }

   reg_btnStatus();
}

/* Показать пароль */
var blurred;
var passwordBorder = document.getElementById('passwordBorder');

function eyeOnclick() {
   let password = document.getElementById('password');
   let eye = document.getElementById('eye');

   if (password.type == "password") {
      password.type = "text";
      // document.getElementById('eye').setAttribute("name","eye");
      eye.src = "../icons/visibility-24px.svg";
   } else {
      password.type = "password";
      // document.getElementById('eye').setAttribute("name","eye-off");
      eye.src = "../icons/visibility_off-24px.svg";

   }
   if (blurred == password && password.value != "") {
      // document.getElementById('passwordLine').style.background = "#28875D";
      passwordBorder.style.transition = "none";
      passwordBorder.style.opacity = "1";
      password.focus();
   } else if (blurred == password && password.value == "") {
      passwordBorder.style.transition = "opacity 0.2s";
      setTimeout(function () {
         passwordBorder.style.opacity = "0";
      }, 1);
      // document.getElementById('passwordLine').style.background = "#B6B6B6";
   }
}

function passwordOnfocus(e) {
   let els = document.querySelectorAll('input');

   // document.getElementById('passwordLine').style.background = "#28875D";
   passwordBorder.style.transition = "none";
   setTimeout(function () {
      passwordBorder.style.opacity = "1";
   }, 200);


   Array.prototype.forEach.call(els, function (el) {
      el.addEventListener('blur', function () {
         blurred = this;
      });
   });

   password.addEventListener('keyup', pwdStatus);
}

function outsideOnclick() {
   let langScreen = document.getElementsByClassName('custom-options')[0];
   let langBtn = document.getElementsByClassName('custom-select-trigger')[0];

   if (event.target != langScreen && event.target != langBtn) {
      document.getElementsByClassName('custom-options')[0].style.opacity = "0";
      langAppear('none', 70);
   }
}
