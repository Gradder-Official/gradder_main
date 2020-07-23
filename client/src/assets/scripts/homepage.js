// Homepage script //

/* События при загрузке */
window.onload = function(){
	calendar(); 
    log_firstName();

    localStorage.group1 = "6-Г";
    localStorage.group2 = "9-А";
    localStorage.group3 = "11-В";
}

/* Приветствие имени */
function log_firstName() {
   if (localStorage.getItem('reg_name') != null){
      document.getElementById('greetings').innerHTML = "Доброго ранку" + "<span id='spanName'>, " + localStorage.getItem('reg_name') + "</span>";
      document.getElementById('spanName').style.transition = "all 0.55s";

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

/* Календарь */
function calendar(){
	let now = new Date();
    let date = now.getDate();
    let day = now.getDay();
    let month = now.getMonth();

    let day_str, month_str;

    if (day == 1) {
    	day_str = 'Понеділок';
    } else if (day == 2) {
    	day_str = 'Вівторок';
    } else if (day == 3) {
    	day_str = 'Середа';
    } else if (day == 4) {
    	day_str = 'Четвер';
    } else if (day == 5) {
    	day_str = "П'ятниця";
    } else if (day == 6) {
    	day_str = 'Субота';
    } else if (day == 0) {
    	day_str = 'Неділя';
    }

   if (month == 0) {
   		month_str = "Січ"
   } else if (month == 1) {
   		month_str = "Лют";
   } else if (month == 2) {
   		month_str = "Бер";
   } else if (month == 3) {
   		month_str = "Квіт";
   } else if (month == 4) {
   		month_str = "Трав";
   } else if (month == 5) {
   		month_str = "Черв";
   } else if (month == 6) {
   		month_str = "Лип";
   } else if (month == 7) {
   		month_str = "Сер";
   } else if (month == 8) {
   		month_str = "Вер";
   } else if (month == 9) {
   		month_str = "Жовт";
   } else if (month == 10) {
   		month_str = "Лист";
   } else if (month == 11) {
   		month_str = "Груд";
   }

   document.getElementById('calendar').innerHTML = day_str + ", " + date + " " + month_str;
}

/* Открыть закрыть окно для загрузки таблиц */
var group;

function modalOpen(id) {
	let modal = document.getElementById('overlay');
	let previewContainer = document.getElementById('preview');

	if (id == 'group1') {
		group = 'group1';

		document.getElementById('class-name').innerHTML = "Завантаження оцінок для " + localStorage.getItem('group1') + " класу";
	} else if (id == 'group2') {
		group = 'group2';

		document.getElementById('class-name').innerHTML = "Завантаження оцінок для " + localStorage.getItem('group2') + " класу";
	} // Ну и добавить 3й класс

	modal.style.visibility = "visible";
	modal.style.opacity = "1";
	modal.children[0].style.transform = "scale(1)";

  	// Закрыть при нажатии на ESC
  	document.addEventListener('keydown', function(event) {
    	const key = event.key; // const {key} = event; 
    	if (key == "Escape") {
    		errorDisappear();

    		modal.children[0].style.opacity = "0";
    		modal.children[0].style.transform = "scale(0.85)";
    		modal.style.background = "rgba(0, 0, 0, 0)";
    		setTimeout(function(){
    			modal.style.visibility = "hidden";
    			modal.style.opacity = "0";
    		}, 220);
    		setTimeout(function(){
    			modal.children[0].style.opacity = "1";
    			modal.style.background = "rgba(0, 0, 0, 0.55)";
    		}, 310);

    		setTimeout(closeFile, 260);
    	}
  	});

  	// Закрыть при нажатии на крестик
  	let close = document.getElementById('close-modal');
	
	close.addEventListener('click', function() {
		errorDisappear();

    	modal.children[0].style.opacity = "0";
    	modal.children[0].style.transform = "scale(0.85)";
    	modal.style.background = "rgba(0, 0, 0, 0)";
    	setTimeout(function(){
    		modal.style.visibility = "hidden";
    		modal.style.opacity = "0";
    	}, 220);
    	setTimeout(function(){
    		modal.children[0].style.opacity = "1";
    		modal.style.background = "rgba(0, 0, 0, 0.55)";
    	}, 310);

  		setTimeout(closeFile, 260);
  	});
}

/* Загрузить таблицу */
function sheetsDownload() {
	let downloadBtn = document.getElementById('download');

	if (group == 'group1') {
		downloadBtn.href = '../static/resources/6-Г, Оцінки.xlsx';

		downloadBtn.click();
	} else if (group == 'group2') {
		downloadBtn.href = '../static/resources/9-А, Оцінки.xlsx';

		downloadBtn.click();
	} else if (group == 'group3') {
		downloadBtn.href = '../static/resources/11-В, Оцінки.xlsx';

		downloadBtn.click();
	}
}