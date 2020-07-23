// Drag and drop script //

var dropArea = document.getElementById("drop-area");
var input = document.getElementById('fileElem');
var border = document.getElementById('border');
var btn = document.getElementById('upload-btn');
let error = document.getElementById('error');

let filesStatus;
function resetStatus(variable){
	if (variable == 'filesStatus') {
		filesStatus = 0;
	}
}

dropArea.addEventListener('click', function(e) {
	if (filesStatus != 1) {
		input.click();
		errorDisappear();
	}	
});

dropArea.addEventListener('drop', function(e){	
	if (filesStatus != 1) {
		let dt = e.dataTransfer;
  		let files = dt.files;

  		checkFiles(files);
  	}	
});

/* Prevent default drag behaviors */
function preventDefaults(e) {
  	e.preventDefault();
  	e.stopPropagation();
}

;['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
  	dropArea.addEventListener(eventName, preventDefaults);  
  	document.body.addEventListener(eventName, preventDefaults);
});

/* Подсветка формы при наведении файла */
;['dragenter', 'dragover'].forEach(eventName => {
  	dropArea.addEventListener(eventName, highlight);
});
;['dragleave', 'drop'].forEach(eventName => {
  	dropArea.addEventListener(eventName, unhighlight);
});
function highlight(e) {
  	border.style.opacity = "1";
  	dropArea.style.background = "#f5f7f9";
}
function unhighlight(e) {
  	border.style.opacity = "0";
  	dropArea.style.background = "white";
}

/* Проверить формат файла */
function getFileExtension(file) { // https://www.jstips.co/en/javascript/get-file-extension/
	filename = file[0].name;

  	return filename.slice((filename.lastIndexOf(".") - 1 >>> 0) + 2);
}

function checkFiles(file) {
	if (filesStatus == 1) {
		preventDefaults(event);
  		error.innerHTML = "<p>Щось пішло не так. Спробуйте ще раз.</p>"
  		error.style.display = "block";
    	setTimeout(function() {
     		appear('error', 'top');
  		}, 1);
	} else if (file.length > 1) {
  		preventDefaults(event);
  		error.innerHTML = "<p>Можна завантажити лише 1 файл.</p>"
  		error.style.display = "block";
    	setTimeout(function() {
     		appear('error', 'top');
  		}, 1);
  	} else if (getFileExtension(file) != 'xls' && getFileExtension(file) != 'xlsx') {
  		preventDefaults(event);
  		error.innerHTML = "<p>Файл повинен бути формату .xls або .xlsx</p>"
  		error.style.display = "block";
    	setTimeout(function() {
     		appear('error', 'top');
  		}, 1);
  	} else {
  		handleFiles(file);
  	}
}

/* Отправить файл на загрузку */
function handleFiles(files) {
  document.getElementById('file-name').innerHTML = files[0].name;
  files = [...files];
  initializeProgress(files.length);
  // files.forEach(previewFile);
  files.forEach(uploadFile);
}

var uploadProgress;
var progressBar = document.getElementById('progress-bar');
var progressShadow = document.getElementById('progress-shadow');
var progressContainer = document.getElementById('progress-container');
var previewContainer = document.getElementById('preview');

/* Показать полосу загрузки */
function initializeProgress(numFiles) {
  progressShadow.style.width = "5%";
  uploadProgress = [];
  progressBar.value = 5;
  progressContainer.style.visibility = "visible";
  progressContainer.style.opacity = "1";

  for (let i = numFiles; i > 0; i--) {
    uploadProgress.push(0);
  }
}

/* Загрузить файл на сервер + полоска загрузки */
function updateProgress(fileNumber, percent) {
  filesStatus = 1;
  uploadProgress[fileNumber] = percent;
  let total = uploadProgress.reduce((tot, curr) => tot + curr, 0) / uploadProgress.length;

  if (total >= 5) {
  	progressBar.value = total;
  	progressShadow.style.width = total + "%";
  } else {
  	progressBar.value = 5;
  	progressShadow.style.width = "5%";
  }	
  if (progressBar.value == 100) {
  	setTimeout(function(){
  		previewContainer.style.pointerEvents = "auto";
  		previewContainer.style.visibility = "visible";
  		previewContainer.style.opacity = "1";
  		previewContainer.children[0].style.transform = "scale(1)";
  		previewContainer.children[0].style.opacity = "1";

  		btn.style.background = "#2B9264";
      	btn.style.color = "#fcfcfc";
      	btn.classList.add('btn-active');
      	btn.getElementsByTagName('p')[0].style.opacity = "1";
      	btn.style.pointerEvents = 'auto';
  	}, 330);
  	setTimeout(function() {
  		progressContainer.style.opacity = "0";
  	}, 450);
  	setTimeout(function() {
  		progressContainer.style.visibility = "hidden";
  		progressBar.value = 5;
  		progressShadow.style.width = "5%";
  	}, 555);
  }
}
/*function previewFile(file) {
  let reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onloadend = function() {
 
  }
}*/
function uploadFile(file, i) {
  let url = 'https://api.cloudinary.com/v1_1/joezimim007/image/upload';
  let xhr = new XMLHttpRequest();
  let formData = new FormData();
  xhr.open('POST', url, true);
  xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');

  xhr.upload.addEventListener("progress", function(e) {
    updateProgress(i, (e.loaded * 100.0 / e.total) || 100);
  })

  xhr.addEventListener('readystatechange', function(e) {
    if (xhr.readyState == 4 && xhr.status == 200) {
      updateProgress(i, 100);
      errorDisappear();
    } else if (xhr.readyState == 4 && xhr.status != 200) {
    	error.innerHTML = "<p>Сервер не відповідає. Перезагрузіть сторінку<br>(Gradder team, не надо ничего перезагружать. Просто сервера ещё нет :D )</p>"
  		error.style.display = "block";
    	setTimeout(function() {
     		appear('error', 'top');
  		}, 1);
    }
  })

  // try catch не работает с httprequests, потому-что они выполняют код асинхронно
  //formData.append('upload_preset', 'ujpu6gyk');
  formData.append('file', file);
  xhr.send(formData);
}

/* Удалить файл при нажатии на крестик */
document.getElementById('close-file').addEventListener('click', closeFile);

function closeFile() {
	btn.style.background = "#EAF4EF";
    btn.style.color = "#5B5E61";
    btn.classList.remove('btn-active');
    btn.getElementsByTagName('p')[0].style.opacity = "0.55";
    btn.style.pointerEvents = 'none';

	previewContainer.children[0].style.transform = "scale(0.85)";
  	previewContainer.children[0].style.opacity = "0"; 
	previewContainer.style.pointerEvents = "none";
	previewContainer.style.transition = "opacity 0.52s";
	previewContainer.style.opacity = "0";
    setTimeout(function() {
  		previewContainer.style.visibility = "hidden";
  		previewContainer.style.transition = "unset";
  		document.getElementById('upload-form').reset();
  		resetStatus('filesStatus');
  	}, 555);
}  	

/* Появление элемента */
function appear(id, parameter) {
	if (parameter == 'opacity') {
   		document.getElementById(id).style.opacity = "1";
	}
	if (parameter == 'top') {
		document.getElementById(id).style.top = "0";
	}
}

/* Исчезновение ошибки */
function errorDisappear() {
	error.style.top = "-45px";
	error.style.transition = "top 0.17s ease-in";
	setTimeout(function(){
		error.style.transition = "top 0.25s ease-out";
		error.style.display = "none";
	}, 220)
}