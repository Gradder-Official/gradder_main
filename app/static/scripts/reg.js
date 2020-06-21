// Registration script //

/* Loader */
$(window).on("load", function () {
   $('html, body').css('overflow', 'auto');
   $('html, body').css('background', 'white');
   maskHeight();
});

function maskHeight() {
   let slideHeight = $('.form-container:nth-child(5)').height();
   $('.rightMask').css({ height: slideHeight });
   $('.leftMask').css({ height: slideHeight });
   $('.slider').css({ height: slideHeight });
}

/* События при загрузке */
window.onload = function () {
   greetingsLang();

   document.getElementById('first name').focus();
   if (document.getElementById('second name').value != "") {
      document.getElementsByClassName('input')[1].getElementsByTagName('label').style.top = "-2px";
      document.getElementsByClassName('input')[1].getElementsByTagName('label').style.fontSize = "12px";
   }
   if (document.getElementById('email').value != "") {
      document.getElementsByClassName('input')[2].getElementsByTagName('label').style.top = "-2px";
      document.getElementsByClassName('input')[2].getElementsByTagName('label').style.fontSize = "12px";
   }

   window.addEventListener('submit', function (e) {
      validateSubmit(e, btnValid);
   });

   letterBugFix();

   localStorage.typeOfAcc = 'Student';
   convertRadioboxes();
}

function letterBugFix() {
   if (localStorage.getItem('lang') == "рус") {
      if (window.screen.width < 365) {
         document.getElementById('lettercase_li').innerHTML = '<img src="../static/icons/circle.svg?v={{ version }}">&nbsp;&nbsp;<span data-translate="_charge3">Имеются большие и малые латинские &nbsp;&nbsp;буквы</span>';
      }
   }   
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

/* Количество детей */
var groupsAmount = document.getElementById('groupsAmount');
var groupsAmountBorder = document.getElementById('amountBorder');
var val1, checkClassNamesStatus, checkChildrenNamesStatus;

var childrenAmount = document.getElementById("childrenAmount");
var childrenBorder = document.getElementById('childrenBorder');

function upChildren(max) {
   childrenAmount.value = parseInt(childrenAmount.value) + 1;
   if (childrenAmount.value >= parseInt(max)) {
      childrenAmount.value = max;
   }
   checkChildren();

   if (blurred == childrenAmount) {
      childrenBorder.style.transition = "none";
      childrenBorder.style.opacity = "1";
   }
   if (blurred != 0) {
      blurred.focus();
   }
}
function downChildren(min) {
   childrenAmount.value = parseInt(childrenAmount.value) - 1;
   if (childrenAmount.value <= parseInt(min)) {
      childrenAmount.value = min;
   }
   checkChildren();

   if (blurred == childrenAmount) {
      childrenBorder.style.transition = "none";
      childrenBorder.style.opacity = "1";
   }
   if (blurred != 0) {
      blurred.focus();
   }
}

function checkChildren() {
   var valStatus = 'down';

   childrenLang();
   checkChildrenNames()
   let valCurr = document.getElementById("childrenAmount").value;

   if (valCurr > val1) {
      valStatus = 'up';

      val1 = document.getElementById("childrenAmount").value;
   } else if (valCurr < val1) {
      valStatus = 'down';

      val1 = document.getElementById("childrenAmount").value;
   }

   let school3 =  document.getElementById('school3');
   let school4 =  document.getElementById('school4');
   if (val1 == 3) {
      school3.children[1].value = 'ТЛ НТУУ "КПІ"';
      school3.children[1].style.pointerEvents = "none";
      school3.children[0].style.top = "-2px";
      school3.children[0].style.fontSize = "12px";

      school4.children[1].value = 'ТЛ НТУУ "КПІ"';
      school4.children[1].style.pointerEvents = "none";
      school4.children[0].style.top = "-2px";
      school4.children[0].style.fontSize = "12px";
   } else if (val1 == 2){
      school3.children[1].value = 'ТЛ НТУУ "КПІ"';
      school3.children[1].style.pointerEvents = "none";
      school3.children[0].style.top = "-2px";
      school3.children[0].style.fontSize = "12px";
   }

   let container = document.getElementById('childrenContainer');

   if (valStatus == 'up') {
      for (i = 0; i < childrenAmount.value; i++) {
         container.getElementsByClassName('row-container')[i].style.display = "block";
         container.getElementsByClassName('row-container')[i].style.pointerEvents = "auto";
      }
   } else if (valStatus == 'down') {
      for (i = 2; i > (childrenAmount.value - 1); i--) {
         container.getElementsByClassName('row-container')[i].style.display = "none";
         container.getElementsByClassName('row-container')[i].style.pointerEvents = "none";
      }
   }   
}
function checkChildrenNames() {
   let container = document.getElementById('childrenContainer');

   for (i = 0; i < childrenAmount.value; i++) {
      let rowContainer = container.getElementsByClassName('row-container')[i];
      let inputs = rowContainer.getElementsByTagName('input');
      
      for (j = 0; j < inputs.length; j++) {
         if (inputs[j].value != "") {
           checkChildrenNamesStatus = true;
         } else {
            checkChildrenNamesStatus = false;
            break;
         }
      }
   }

   reg_btnStatus();
}
/* Количество классов */
function checkClassNames() {
   let firstRow = document.getElementById('firstRow');
   let secondRow = document.getElementById('secondRow');

   if (groupsAmount.value < 5) {
      for (i = 0; i < groupsAmount.value; i++) {
         if (firstRow.getElementsByTagName('input')[i].value != "") {
            checkClassNamesStatus = true;
         } else {
            checkClassNamesStatus = false;
            break;
         }
      }

      reg_btnStatus();
   } else if (groupsAmount.value > 4) {
      for (i = 0; i < (groupsAmount.value - 4); i++) {
         if (secondRow.getElementsByTagName('input')[i].value != "") {
            checkClassNamesStatus = true;
         } else {
            checkClassNamesStatus = false;
            break;
         }
      }

      reg_btnStatus();
   }
}

function upAmount(max) {
   groupsAmount.value = parseInt(groupsAmount.value) + 1;
   if (groupsAmount.value >= parseInt(max)) {
      groupsAmount.value = max;
   }
   checkAmount();

   if (blurred == groupsAmount) {
      groupsAmountBorder.style.transition = "none";
      groupsAmountBorder.style.opacity = "1";
   }
   if (blurred != 0) {
      blurred.focus();
   }
}
function downAmount(min) {
   groupsAmount.value = parseInt(groupsAmount.value) - 1;
   if (groupsAmount.value <= parseInt(min)) {
      groupsAmount.value = min;
   }
   checkAmount();

   if (blurred == groupsAmount) {
      groupsAmountBorder.style.transition = "none";
      groupsAmountBorder.style.opacity = "1";
   }
   if (blurred != 0) {
      blurred.focus();
   }
}
function amountFocus(id, id2, func) {
   val1 = document.getElementById(id).value;

   document.getElementById(id).addEventListener('change', func);

   document.getElementById(id2).style.transition = "none";
   setTimeout(function () {
      document.getElementById(id2).style.opacity = "1";
   }, 200);
}
function checkAmount() {
   var valStatus;

   checkClassNames();
   let valCurr = document.getElementById("groupsAmount").value;

   if (valCurr > val1) {
      valStatus = 'up';

      val1 = document.getElementById("groupsAmount").value;
   } else if (valCurr < val1) {
      valStatus = 'down';

      val1 = document.getElementById("groupsAmount").value;
   }

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

            firstRow.getElementsByClassName('input')[i].children[1].value = "";
            firstRow.getElementsByClassName('input')[i].children[1].blur();
            firstRow.getElementsByClassName('input')[i].children[0].style.fontSize = "16px";
            firstRow.getElementsByClassName('input')[i].children[0].style.top = "10px";
         }

         secondRow.getElementsByClassName('input')[0].children[1].value = "";
         secondRow.getElementsByClassName('input')[0].children[1].blur();
         secondRow.getElementsByClassName('input')[0].children[0].style.fontSize = "16px";
         secondRow.getElementsByClassName('input')[0].children[0].style.top = "10px";

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

            secondRow.getElementsByClassName('input')[i].children[1].value = "";
            secondRow.getElementsByClassName('input')[i].children[1].blur();
            secondRow.getElementsByClassName('input')[i].children[0].style.fontSize = "16px";
            secondRow.getElementsByClassName('input')[i].children[0].style.top = "10px";
         }
      }
   }
}

/* Дані про дитину */
document.getElementsByClassName('custom-options')[0].addEventListener('click', childrenLang);

function childrenLang() {
   if (childrenAmount.value > 1) {
      if (localStorage.getItem('lang') == "укр") {
         document.getElementById('firstChild').innerHTML = "Дані про першу дитину";
      } else if (localStorage.getItem('lang') == "рус") {
         document.getElementById('firstChild').innerHTML = "Данные о первом ребенке";
      } else if (localStorage.getItem('lang') == "eng") {
         document.getElementById('firstChild').innerHTML = "Information about the first child";
      }
   } else {
      if (localStorage.getItem('lang') == "укр") {
         document.getElementById('firstChild').innerHTML = "Дані про дитину";
      } else if (localStorage.getItem('lang') == "рус") {
         document.getElementById('firstChild').innerHTML = "Данные о ребенке";
      } else if (localStorage.getItem('lang') == "eng") {
         document.getElementById('firstChild').innerHTML = "Information about the child";
      }
   }

   letterBugFix();
}

/* Приветствие имени */
var firstName, reg_name = 0;

function firstnameOnblur() {
   firstName = document.getElementById('first name').value;

   firstName = firstName.charAt(0).toUpperCase() + firstName.slice(1);

   if (firstName != "") {
      if (reg_name == 0) {
         if (window.screen.width > 489) {
            document.getElementById('greetings').innerHTML = "Ласкаво просимо до<br>Gradder" + "<span id='spanName'>, " + firstName + "</span>";
         } else if (window.screen.width <= 489) {
            document.getElementById('greetings').innerHTML = "Ласкаво просимо до Gradder" + "<span id='spanName'>, <br>" + firstName + "</span>";
         }   
         document.getElementById('spanName').style.transition = "all 0.15s";

         setTimeout(function () {
            appear('spanName');
         }, 1);

         reg_name = 1;
         localStorage.reg_name = firstName;
      } else if (reg_name == 1) {
         if (window.screen.width > 489) {
            document.getElementById('greetings').innerHTML = "Ласкаво просимо до<br>Gradder" + "<span id='spanName'>, " + firstName + "</span>";
         } else if (window.screen.width <= 489) {
            document.getElementById('greetings').innerHTML = "Ласкаво просимо до Gradder" + "<span id='spanName'>, <br>" + firstName + "</span>";
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

   next_btnStatus();
   greetingsLang();
}

document.getElementsByClassName('custom-options')[0].addEventListener('click', greetingsLang);

function greetingsLang() {
   if (window.screen.width > 489) {
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
   } else if (window.screen.width <= 489) {
      if (reg_name == 1) {
         if (localStorage.getItem('lang') == "укр") {
            document.getElementById('greetings').innerHTML = "Ласкаво просимо до Gradder" + "<span id='spanName'>, <br>" + firstName + "</span>";
            document.getElementById('spanName').style.opacity = "1";
         } else if (localStorage.getItem('lang') == "рус") {
            document.getElementById('greetings').innerHTML = "Добро пожаловать в Gradder" + "<span id='spanName'>, <br>" + firstName + "</span>";
            document.getElementById('spanName').style.opacity = "1";
         } else if (localStorage.getItem('lang') == "eng") {
            document.getElementById('greetings').innerHTML = "You're welcome to Gradder" + "<span id='spanName'>, <br>" + firstName + "</span>";
            document.getElementById('spanName').style.opacity = "1";
         }
      } else if (reg_name == 0) {
         if (localStorage.getItem('lang') == "укр") {
            document.getElementById('greetings').innerHTML = "Ласкаво просимо до Gradder<br>";
         } else if (localStorage.getItem('lang') == "рус") {
            document.getElementById('greetings').innerHTML = "Добро пожаловать в Gradder<br>";
         } else if (localStorage.getItem('lang') == "eng") {
            document.getElementById('greetings').innerHTML = "You're welcome to Gradder<br>";
         }
      }
   }  

   let btnA = document.getElementsByClassName('buttonA');
   if (localStorage.getItem('lang') == "рус") {
      if (window.screen.width > 489) {
         for (i = 0; i < btnA.length; i++)
            btnA[i].style.width = "56%";
      } else if (window.screen.width <= 489) {
         for (i = 0; i < btnA.length; i++)
            btnA[i].style.width = "66%";
      }
   } else {
      if (window.screen.width > 489) {
         for (i = 0; i < btnA.length; i++)
            btnA[i].style.width = "48%";
      } else if (window.screen.width <= 489) {
         for (i = 0; i < btnA.length; i++)
            btnA[i].style.width = "60.5%";
      }    
   }   
}
function textDelete() {
   document.getElementById('greetings').innerHTML = "Ласкаво просимо до<br>Gradder";
}
function appear(id) {
   document.getElementById(id).style.opacity = "1";
}

/* Нажатие по 'согласен' */
var reg_checkbox;

function agreeOnclick(input, i) {
   let checkmark = document.getElementsByClassName('checkmark');

   if (document.getElementById(input).checked) {
      reg_checkbox = true;
      checkmark[i].style.background = "#59BD7D";
      checkmark[i].style.border = "2px solid #59BD7D";
      checkmark[i].style.animation = "dotJump 0.4s ease";
   } else {
      reg_checkbox = false;
      checkmark[i].style.background = "none";
      checkmark[i].style.border = "2px solid #B6B6B6";
      checkmark[i].style.animation = "none";
   }

   reg_btnStatus();
}

/* Слайд формы */
var progress = document.getElementsByClassName('progress')[0];
var classToFocus = document.getElementById('classToFocus');

function slide(slide) {
   let school =  document.getElementById('school');
   let school2 =  document.getElementById('school2');
   let form = document.getElementsByClassName('form-container');
   // 0 = mail, 1 = type, 2 = advisor, 3 = student, 4 = parent

   if (slide == 3) {
      progress.children[0].style.backgroundPosition = "0% 50%";
      progress.children[1].style.backgroundPosition = "-100% 50%";
      progress.children[2].style.backgroundPosition = "0% 50%";
      if (localStorage.getItem('typeOfAcc') == 'Advisor') {
         form[0].style.left = "-100%";
         form[1].style.left = "-100%";
         form[2].style.left = "0";
         form[0].style.opacity = "0.2";
         form[1].style.opacity = "0.2";
         form[2].style.opacity = "1";
         form[2].style.pointerEvents = "auto";
         form[0].style.pointerEvents = "none";
         form[1].style.pointerEvents = "none";
         form[3].style.pointerEvents = "none";
         form[4].style.pointerEvents = "none";
         reg_checkbox = false;
         setTimeout(function() {
            groupsAmount.focus();
         }, 195);
      } else if (localStorage.getItem('typeOfAcc') == 'Parent') {
         form[0].style.left = "-100%";
         form[1].style.left = "-100%";
         form[4].style.left = "0";
         form[0].style.opacity = "0.2";
         form[1].style.opacity = "0.2";
         form[4].style.opacity = "1";
         form[4].style.pointerEvents = "auto";
         form[0].style.pointerEvents = "none";
         form[1].style.pointerEvents = "none";
         form[2].style.pointerEvents = "none";
         form[3].style.pointerEvents = "none";
         reg_checkbox = false;
         val1 = 1;
         checkChildren();
         document.getElementById('childrenAmount').addEventListener('change', checkChildren);

         school2.children[1].value = 'ТЛ НТУУ "КПІ"';
         school2.children[1].style.pointerEvents = "none";
         school2.children[0].style.top = "-2px";
         school2.children[0].style.fontSize = "12px";

         setTimeout(function() {
            document.getElementById('first name2').focus();
         }, 195);
      } else if (localStorage.getItem('typeOfAcc') == 'Student') {
         form[0].style.left = "-100%";
         form[1].style.left = "-100%";
         form[3].style.left = "0";
         form[0].style.opacity = "0.2";
         form[1].style.opacity = "0.2";
         form[3].style.opacity = "1";
         form[3].style.pointerEvents = "auto";
         form[0].style.pointerEvents = "none";
         form[1].style.pointerEvents = "none";
         form[2].style.pointerEvents = "none";
         form[4].style.pointerEvents = "none";

         school.children[1].value = 'ТЛ НТУУ "КПІ"';
         school.children[1].style.pointerEvents = "none";
         school.children[0].style.top = "-2px";
         school.children[0].style.fontSize = "12px";
         reg_checkbox = false;
         setTimeout(function() {
            classToFocus.focus();
         }, 195);
      }
   } else if (slide == 1) {
      form[0].style.left = "0";
      form[2].style.left = "calc(100% + 5px)";
      form[2].style.opacity = "0.2";
      form[3].style.left = "calc(100% + 5px)";
      form[3].style.opacity = "0.2";
      form[4].style.left = "calc(100% + 5px)";
      form[4].style.opacity = "0.2";
      form[1].style.left = "calc(100% + 5px)";
      form[1].style.opacity = "0.2";
      form[0].style.opacity = "1";
      form[0].style.pointerEvents = "auto";
      form[2].style.pointerEvents = "none";
      form[3].style.pointerEvents = "none";
      form[1].style.pointerEvents = "none";
      form[4].style.pointerEvents = "none";
      progress.children[0].style.backgroundPosition = "100% 50%";
      progress.children[1].style.backgroundPosition = "100% 50%";
      progress.children[2].style.backgroundPosition = "100% 50%";
   } else if (slide == 2) {
      form[0].style.left = "-100%";
      form[1].style.left = "0";
      form[2].style.left = "calc(100% + 5px)";
      form[3].style.left = "calc(100% + 5px)";
      form[0].style.opacity = "0.5";
      form[1].style.opacity = "1";
      form[2].style.opacity = "0.2";
      form[2].style.pointerEvents = "none";
      form[3].style.opacity = "0.2";
      form[3].style.pointerEvents = "none";
      form[0].style.pointerEvents = "none";
      form[1].style.pointerEvents = "auto";
      form[4].style.pointerEvents = "none";
      form[4].style.left = "calc(100% + 5px)";
      form[4].style.opacity = "0.2";
      progress.children[0].style.backgroundPosition = "0% 50%";
      progress.children[1].style.backgroundPosition = "0% 50%";
      progress.children[2].style.backgroundPosition = "100% 50%";
   }
}
/* Возможность нажать на кнопку or отправить форму */
var pwdValid, emailValid, btnValid;

function reg_btnStatus() {
   let token = document.getElementById('token').value;
   let btn = document.getElementsByClassName('btn_reg');

   if (localStorage.getItem('typeOfAcc') == 'Advisor') {
      if (token != "" && reg_checkbox == true && checkClassNamesStatus == true) {
         btn[0].style.background = "#4DB071";
         btn[0].style.color = "#fcfcfc";
         btn[0].classList.add('btn-active');
         btn[0].style.pointerEvents = 'auto';

         btnValid = true;
      } else {
         btn[0].style.background = "#EAF4EF";
         btn[0].style.color = "#9EA1A3";
         btn[0].classList.remove('btn-active');
         btn[0].style.pointerEvents = 'none';

         btnValid = false;
      }
   } else if (localStorage.getItem('typeOfAcc') == 'Student') {
      if (classToFocus.value != "" && reg_checkbox == true && school.children[1].value != "") {
         btn[1].style.background = "#4DB071";
         btn[1].style.color = "#fcfcfc";
         btn[1].classList.add('btn-active');
         btn[1].style.pointerEvents = 'auto';

         btnValid = true;
      } else {
         btn[1].style.background = "#EAF4EF";
         btn[1].style.color = "#9EA1A3";
         btn[1].classList.remove('btn-active');
         btn[1].style.pointerEvents = 'none';

         btnValid = false;
      }
   } else if (localStorage.getItem('typeOfAcc') == 'Parent') {
      if (reg_checkbox == true && checkChildrenNamesStatus == true) {
         btn[2].style.background = "#4DB071";
         btn[2].style.color = "#fcfcfc";
         btn[2].classList.add('btn-active');
         btn[2].style.pointerEvents = 'auto';

         btnValid = true;
      } else {
         btn[2].style.background = "#EAF4EF";
         btn[2].style.color = "#9EA1A3";
         btn[2].classList.remove('btn-active');
         btn[2].style.pointerEvents = 'none';

         btnValid = false;
      }
   }   
}

function next_btnStatus() {
   let surname = document.getElementById('second name').value;
   let name = document.getElementById('first name').value;
   let btn = document.getElementById('btn_next');

   name = name.charAt(0).toUpperCase() + name.slice(1);

   //if (pwdValid == 1 && reg_name == 1 && name == firstName && surname != "" && emailValid == 1) {
   if (true) {
      btn.style.background = "#4DB071";
      btn.style.color = "#fcfcfc";
      btn.classList.add('btn-active');
      btn.style.pointerEvents = 'auto';
      btn.getElementsByTagName('img')[0].style.filter = "invert(100%) sepia(99%) saturate(3%) hue-rotate(78deg) brightness(105%) contrast(98%)";
      progress.children[1].style.pointerEvents = "auto";

      next2_btnStatus();
   } else {
      btn.style.background = "#EAF4EF";
      btn.style.color = "#9EA1A3";
      btn.classList.remove('btn-active');
      btn.style.pointerEvents = 'none';
      btn.getElementsByTagName('img')[0].style.filter = "invert(71%) sepia(0%) saturate(317%) hue-rotate(247deg) brightness(91%) contrast(90%)";
      progress.children[1].style.pointerEvents = "none";
   }
}
function next2_btnStatus(value) {
   let btn = document.getElementById('btn_next2');

   if (true) {
      btn.style.background = "#4DB071";
      btn.style.color = "#fcfcfc";
      btn.classList.add('btn-active');
      btn.style.pointerEvents = 'auto';
      btn.getElementsByTagName('img')[0].style.filter = "invert(100%) sepia(99%) saturate(3%) hue-rotate(78deg) brightness(105%) contrast(98%)";
      progress.children[2].style.pointerEvents = "auto";
   } else {
      btn.style.background = "#EAF4EF";
      btn.style.color = "#9EA1A3"; 
      btn.classList.remove('btn-active');
      btn.style.pointerEvents = 'none';
      btn.getElementsByTagName('img')[0].style.filter = "invert(71%) sepia(0%) saturate(317%) hue-rotate(247deg) brightness(91%) contrast(90%)";
      progress.children[2].style.pointerEvents = "none";
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

   next_btnStatus();
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
      li.style.color = "#4DB071";
      li.getElementsByTagName('img')[0].src = "../static/icons/checkmark.svg";
      li.getElementsByTagName('img')[0].style.width = "16px";
      li.getElementsByTagName('img')[0].style.marginBottom = "-1px";
      li.getElementsByTagName('img')[0].style.marginLeft = "1px";
      li.getElementsByTagName('img')[0].style.filter = "invert(52%) sepia(80%) saturate(258%) hue-rotate(89deg) brightness(97%) contrast(99%)";
   } else {
      eight = 0;
      let li = document.getElementById('length_li');
      li.style.color = "#5F6368";
      li.getElementsByTagName('img')[0].src = "../static/icons/circle.svg";
      li.getElementsByTagName('img')[0].style.width = "17px";
      li.getElementsByTagName('img')[0].style.marginBottom = "-4px";
      li.getElementsByTagName('img')[0].style.marginLeft = "0px";
      li.getElementsByTagName('img')[0].style.filter = "none";
   }
   if (password.value.search(/[0-9]/) != -1 && password.value.search(/[a-zA-Z]/) != -1) {
      numnum = 1;
      let li = document.getElementById('symbols_li');
      //li.style.color = "#1C8256";
      li.style.color = "#4DB071";
      li.getElementsByTagName('img')[0].src = "../static/icons/checkmark.svg";
      li.getElementsByTagName('img')[0].style.width = "16px";
      li.getElementsByTagName('img')[0].style.marginBottom = "-1px";
      li.getElementsByTagName('img')[0].style.marginLeft = "1px";
      //li.getElementsByTagName('img')[0].style.filter = "invert(44%) sepia(19%) saturate(1306%) hue-rotate(101deg) brightness(94%) contrast(92%)";
      li.getElementsByTagName('img')[0].style.filter = "invert(52%) sepia(80%) saturate(258%) hue-rotate(89deg) brightness(97%) contrast(99%)";
   } else {
      numnum = 0;
      let li = document.getElementById('symbols_li');
      li.style.color = "#5F6368";
      li.getElementsByTagName('img')[0].src = "../static/icons/circle.svg";
      li.getElementsByTagName('img')[0].style.width = "17px";
      li.getElementsByTagName('img')[0].style.marginBottom = "-4px";
      li.getElementsByTagName('img')[0].style.marginLeft = "0px";
      li.getElementsByTagName('img')[0].style.filter = "none";
   }
   if (password.value.search(/[a-z]/) != -1 && password.value.search(/[A-Z]/) != -1) {
      lettercase = 1;
      let li = document.getElementById('lettercase_li');
      li.style.color = "#4DB071";
      li.getElementsByTagName('img')[0].src = "../static/icons/checkmark.svg";
      li.getElementsByTagName('img')[0].style.width = "16px";
      li.getElementsByTagName('img')[0].style.marginBottom = "-1px";
      li.getElementsByTagName('img')[0].style.marginLeft = "1px";
      li.getElementsByTagName('img')[0].style.filter = "invert(52%) sepia(80%) saturate(258%) hue-rotate(89deg) brightness(97%) contrast(99%)";
   } else {
      lettercase = 0;
      let li = document.getElementById('lettercase_li');
      li.style.color = "#5F6368";
      li.getElementsByTagName('img')[0].src = "../static/icons/circle.svg";
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

   next_btnStatus();
}

/* Показать пароль */
var blurred;
var passwordBorder = document.getElementById('passwordBorder');

function eyeOnclick() { // оставлять фокус на поле пароля
   let password = document.getElementById('password');
   let eye = document.getElementById('eye');

   if (password.type == "password") {
      password.type = "text";
      eye.src = "../static/icons/visibility-24px.svg";
   } else {
      password.type = "password";
      eye.src = "../static/icons/visibility_off-24px.svg";

   }
   if (blurred == password && password.value != "") {
      passwordBorder.style.transition = "none";
      passwordBorder.style.opacity = "1";
      password.focus();
   } else if (blurred == password && password.value == "") {
      passwordBorder.style.transition = "opacity 0.2s";
      setTimeout(function () {
         passwordBorder.style.opacity = "0";
      }, 1);
   }
}

function passwordOnfocus(e) {
   let els = document.querySelectorAll('input');

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

/* Используется многими элементами */
function outsideOnclick() {
   let eye = document.getElementById('eye');
   let password = document.getElementById('password');
   let langScreen = document.getElementsByClassName('custom-options')[0];
   let langBtn = document.getElementsByClassName('custom-select-trigger')[0];
   let reg_amount = document.getElementsByClassName('reg-amount'); 

   if (event.target != eye && event.target != password) { // клик не по глазу
      passwordBorder.style.transition = "opacity 0.2s";
      passwordBorder.style.opacity = "0";
      blurred = 0;
   }

   if (event.target != reg_amount[0] && event.target != reg_amount[1] && event.target != reg_amount[2] && event.target != reg_amount[3]) { // клик не по amount
      groupsAmountBorder.style.transition = "opacity 0.2s";
      groupsAmountBorder.style.opacity = "0";
      blurred = 0;
   }

   if (event.target != reg_amount[4] && event.target != reg_amount[5] && event.target != reg_amount[6] && event.target != reg_amount[7]) { // клик не по amount
      childrenBorder.style.transition = "opacity 0.2s";
      childrenBorder.style.opacity = "0";
      blurred = 0;
   }

   if (event.target != langScreen && event.target != langBtn) { // закрыть выбор языков
      document.getElementsByClassName('custom-options')[0].style.opacity = "0";
      langAppear('none', 70);
   }
}

/* Radio buttons */
function convertRadioboxes() {
  let buttons = document.querySelectorAll("input[blink]");

  let svg = (`
    <svg width="156" height="144" viewBox="0 0 156 144" fill="green" xmlns="http://www.w3.org/2000/svg">
      <circle cx="42" cy="28" r="3"/>
      <circle cx="42" cy="88" r="3"/>
      <circle cx="102" cy="119" r="3"/>
      <circle cx="122" cy="58" r="3"/>
      <circle cx="102" cy="20" r="3"/>
      <circle cx="70.5" cy="30.5" r="1.5"/>
      <circle cx="20.5" cy="62.5" r="1.5"/>
      <circle cx="50.5" cy="114.5" r="1.5"/>
      <circle cx="130.5" cy="86.5" r="1.5"/>
      <circle cx="100.5" cy="48.5" r="1.5"/>
      <circle cx="87.5" cy="93.5" r="1.5"/>
    </svg>
  `);

  /*buttons.forEach(function() {
    let radio = document.getElementsByClassName('blink');
    for (i = 0; i < radio.length; i++) {
      let radioWrapper = radio[i];
      radioWrapper.querySelector('div').innerHTML = (`<span></span>${buttons[i].value + svg + svg}`);
    }
  });*/
}
