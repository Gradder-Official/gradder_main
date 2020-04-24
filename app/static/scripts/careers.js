var emailValid, btnValid;

window.onload = function () {
  window.addEventListener('submit', function (e) {
    validateSubmit(e, btnValid);
  });
}

/* Возможность нажать на кнопку or отправить форму */
var emailValid;

function next_btnStatus() {
  let first_name = document.getElementById('first_name').value;
  let last_name = document.getElementById('last_name').value;

  let btn = document.getElementById('btn_next');
  let select = document.getElementsByTagName('select')[0].value;

  first_name = first_name.charAt(0).toUpperCase() + first_name.slice(1);
  last_name = last_name.charAt(0).toUpperCase() + last_name.slice(1);

  //if (pwdValid == 1 && reg_name == 1 && name == firstName && surname != "" && emailValid == 1) {
  if (first_name != "" && last_name != "" && emailValid == 1 && select != "") {
    btn.style.background = "#4DB071";
    btn.style.color = "#fcfcfc";
    btn.classList.add('btn-active');
    btn.style.pointerEvents = 'auto';

    btnValid = true;
  } else {
    btn.style.background = "#EAF4EF";
    btn.style.color = "#9EA1A3";
    btn.classList.remove('btn-active');
    btn.style.pointerEvents = 'none';

    btnValid = 0;
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

function fileValidate() {
  let file = document.getElementById('resume');
  if (file.value != "") {
    if (file.value.lastIndexOf('\\') != -1) {
      file = file.value.slice(file.value.lastIndexOf('\\') + 1, file.value.length);
    }
    if (file.lastIndexOf('/') != -1) {
      file = file.slice(file.lastIndexOf('/') + 1, file.length);
    }

    document.getElementById("upload_text").style = "color: rgb(77, 176, 113);";
    document.getElementById("upload_text").innerHTML = file.slice(0, 6) + '...' + file.slice(file.length - 8, file.length);
  }
}

function validateSubmit(e, id) {
  if (id != true) {
    e.preventDefault();
  } else {
    localStorage.reg_completed = true;
  }
}

/* SOME DROPDOWN SHIT */
var x, i, j, selElmnt, a, b, c;
/*look for any elements with the class "custom-select":*/
x = document.getElementsByClassName("custom-select");
for (i = 0; i < x.length; i++) {
  selElmnt = x[i].getElementsByTagName("select")[0];
  /*for each element, create a new DIV that will act as the selected item:*/
  a = document.createElement("DIV");
  a.setAttribute("class", "select-selected");
  a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
  x[i].appendChild(a);
  /*for each element, create a new DIV that will contain the option list:*/
  b = document.createElement("DIV");
  b.setAttribute("class", "select-items select-hide");
  for (j = 1; j < selElmnt.length; j++) {
    /*for each option in the original select element,
    create a new DIV that will act as an option item:*/
    c = document.createElement("DIV");
    c.innerHTML = selElmnt.options[j].innerHTML;
    c.addEventListener("click", function (e) {
      /*when an item is clicked, update the original select box,
      and the selected item:*/
      var y, i, k, s, h;
      s = this.parentNode.parentNode.getElementsByTagName("select")[0];
      h = this.parentNode.previousSibling;
      for (i = 0; i < s.length; i++) {
        if (s.options[i].innerHTML == this.innerHTML) {
          s.selectedIndex = i;
          h.innerHTML = this.innerHTML;
          y = this.parentNode.getElementsByClassName("same-as-selected");
          for (k = 0; k < y.length; k++) {
            y[k].removeAttribute("class");
          }
          this.setAttribute("class", "same-as-selected");
          break;
        }
      }
      h.click();
    });
    b.appendChild(c);
  }
  x[i].appendChild(b);
  a.addEventListener("click", function (e) {
    /*when the select box is clicked, close any other select boxes,
    and open/close the current select box:*/
    e.stopPropagation();
    closeAllSelect(this);
    this.nextSibling.classList.toggle("select-hide");
    this.classList.toggle("select-arrow-active");
  });
}
function closeAllSelect(elmnt) {
  /*a function that will close all select boxes in the document,
  except the current select box:*/
  var x, y, i, arrNo = [];
  x = document.getElementsByClassName("select-items");
  y = document.getElementsByClassName("select-selected");
  for (i = 0; i < y.length; i++) {
    if (elmnt == y[i]) {
      arrNo.push(i)
    } else {
      y[i].classList.remove("select-arrow-active");
    }
  }
  for (i = 0; i < x.length; i++) {
    if (arrNo.indexOf(i)) {
      x[i].classList.add("select-hide");
    }
  }
}
/*if the user clicks anywhere outside the select box,
then close all select boxes:*/
document.addEventListener("click", closeAllSelect);