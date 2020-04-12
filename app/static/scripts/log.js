/* Анимация полей для ввода при фокусе or блюре or загрузке */
$(".input input").focus(function() {

      $(this).parent(".input").each(function() {
         $("label", this).css({
            "font-size": "12px",
            "top": "0px"
         })
         $(".selection", this).css({
            "width": "100%",
            "margin-left": "0%"
         })
      });
   }).blur(function() {
      $(".selection").css({
         "width": "0%",
         "margin-left": "50%"
      })
      if ($(this).val() == "") {
         $(this).parent(".input").each(function() {
            $("label", this).css({
               "font-size": "16px",
               "top": "21px"
            })
         });
      }   
    });

/* События при загрузке */
window.onload = function(){ 
    log_firstName();

    document.getElementById('agree').checked = true;
    localStorage.log_checkbox = true;

    document.getElementById('email').focus();

    if (localStorage.getItem('log_failed') == "true") {
    	document.getElementById('email').value = localStorage.getItem('log_email');
    	emailValid = 1;
    	localStorage.removeItem('log_failed');
    	document.getElementById('error').style.display = "block";
    	setTimeout(function() {
     		appear('error', 'top');
  		}, 1);
    }

    window.addEventListener('submit', function(e){
    	validateSubmit(e, btnValid);
    })
}

/* Приветствие имени */
function log_firstName() {
   if (localStorage.getItem('reg_name') != null){
      document.getElementById('greetings').innerHTML = "З поверненням до<br>Gradder" + "<span id='spanName'>, " + localStorage.getItem('reg_name') + "</span>";
      document.getElementById('spanName').style.transition = "all 0.15s";

      setTimeout(function() {
         appear('spanName', 'opacity');
      }, 1);
   }
}

function appear(id, parameter) {
	if (parameter == 'opacity') {
   		document.getElementById(id).style.opacity = "1";
	}
	if (parameter == 'top') {
		document.getElementById(id).style.top = "0";
	}
}

/* Запоминание действий */
function agreeOnclick() {
   if (document.getElementById('agree').checked) {
      localStorage.log_checkbox = true;
   } else {
      localStorage.log_checkbox = false;
   }

   log_btnStatus();
}  

/* Возможность нажать на кнопку or отправить форму */
var pwdValid, emailValid, btnValid;

function log_btnStatus() { 
   let btn = document.getElementById('buttonA');

   if (emailValid == 1 && pwdValid == 1) {
      btn.style.background = "#2B9264";
      btn.style.color = "#fcfcfc";
      btn.classList.add('btn-active');
      btn.getElementsByTagName('p')[0].style.opacity = "1";
      btn.style.pointerEvents = 'auto';

      btnValid = true;
   } else {
      btn.style.background = "#EAF4EF";
      btn.style.color = "#5B5E61";
      btn.classList.remove('btn-active');
      btn.getElementsByTagName('p')[0].style.opacity = "0.55";
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

   log_btnStatus();
}   

function validateSubmit(e, id) {
   if (id != true) {
     e.preventDefault();
   } else {
      localStorage.log_email = document.getElementById('email').value;   
      dataValidation(); 
   }
} 

/* Проверка почты / пароля */
function dataValidation() {
	if (false) {

	} else {
		localStorage.log_failed = true;
	}
}

/* Проверка правильности пароля */
function pwdStatus(){
      let password = document.getElementById('password');

      if (password.value.length > 7) {   
        pwdValid = 1;
      } else {
      	pwdValid = 0;
      }

      log_btnStatus();
}

/* Показать пароль */
var blurred;

function eyeOnclick() {
   let password = document.getElementById('password');

   if (password.type == "password") {
         password.type = "text";
      /* document.getElementById("eye").classList.remove('fa-eye-slash');
         document.getElementById("eye").classList.add('fa-eye'); */
         document.getElementById('eye').setAttribute("name","eye");
   } else {
      password.type = "password";
     /* document.getElementById("eye").classList.remove('fa-eye');
      document.getElementById("eye").classList.add('fa-eye-slash'); */
      document.getElementById('eye').setAttribute("name","eye-off");
   } 
   if (blurred == password && password.value != "") {
      document.getElementById('passwordLine').style.background = "#28875D";
      password.focus();
   } else if (blurred == password && password.value == "") {
      document.getElementById('passwordLine').style.background = "#B6B6B6";

   }
}

function passwordOnfocus() {
   let els = document.querySelectorAll('input');

   document.getElementById('passwordLine').style.background = "#28875D";

   Array.prototype.forEach.call(els, function(el) {
      el.addEventListener('blur', function(){
         blurred = this;       
      });   
   });

   password.addEventListener('keyup', pwdStatus);
}

function outsideOnclick() {
   let eye = document.getElementById('eye');
   let password = document.getElementById('password');

   if (event.target != eye && event.target != password) {
      document.getElementById('passwordLine').style.background = "#B6B6B6";
      blurred = 0;
   }
}