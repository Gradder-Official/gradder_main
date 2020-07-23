$(".custom-select").each(function() {
  var classes = $(this).attr("class"),
    id = $(this).attr("id"),
    name = $(this).attr("name");
  var template = '<div class="' + classes + '">';
  template +=
    '<span class="custom-select-trigger">' +
    $(this).attr("placeholder") +
    "</span>";
  template += '<div class="custom-options">';
  $(this).find("option").each(function() {
    template +=
      '<span class="custom-option ' +
      $(this).attr("class") +
      '" data-value="' +
      $(this).attr("value") +
      '">' +
      $(this).html() +
      "</span>";
  });
  template += "</div></div>";

  $(this).wrap('<div class="custom-select-wrapper"></div>');
  //$(this).hide();
  $(this).after(template);
});
$(".custom-select-trigger").on("click", function() {
  /*"html").one("click", function() {
    $(".custom-select").removeClass("opened");
  });*/
  $(this).parents(".custom-select").addClass("opened");
  $(".custom-options").css('opacity', '1');
  $(".custom-option:nth-child(1)").css('opacity', '1');
  langAppear('block', 190);
  //event.stopPropagation();
  $(document).keyup(function(e) {
     if (e.key === "Escape") {
        $(".custom-options").css('opacity', '0');
  		langAppear('none', 70);
     }
  });
});

function langAppear(display, time){
  	setTimeout(function(){
  		$(".custom-option:nth-child(1)").css('display', display);
  		$(".custom-option:nth-child(2)").css('display', display);
  		$(".custom-option:nth-child(3)").css('display', display);

  		if (display == 'none') {
  			$(".custom-select").removeClass("opened");
  		}
  	}, time);
}

$(".custom-option").on("click", function() {
  $(this)
    .parents(".custom-select-wrapper")
    .val($(this).data("value"));
  $(".custom-options").css('opacity', '0');
  langAppear('none', 70);
  $(this)
    .parents(".custom-select")
    .find(".custom-select-trigger")
    .text($(this).text());

  setLang($(this).text());
});

function setLang(lang) {
	$('#lang').val(lang);
	localStorage.lang = lang.toLowerCase();
	$('#lang').trigger("change");
}

$(function () {
    "use strict";
    var dictionary, set_lang;
    dictionary = {
    	"рус": {
      "_greetings": "Добро пожаловать в",
      "_tagline": "Мы создаем новую связь между школой и родителями",
			"_firstName": "Имя",
			"_secondName": "Фамилия",
			"_email": "Почтовый адрес",
			"_password": "Пароль",
			"_charge1": "Пароль содержит 8 символов",
			"_charge2": "Имеются цифры",
			"_charge3": "Имеются большие и малые латинские буквы",
			"_login": "Вход",
			"_next": "Дальше",
			"_photoBy": "Фото от",
			"_class": "Класс",
			"_back": "Назад",
			"_register": "Зарегистрироваться",
			"_token": "Ваш токен",
			"_agree": "Я согласен с",
			"_terms": "условиями обслуживания Gradder",
			"_mailList": "Подпишитесь на нашу рассылку, чтобы получать уведомления об обновлениях Gradder",
			"_mailBtn": "Подписаться",
			"_tagline2": "Платформа для украинских школ, использующая искусственный интеллект",
			"_problem": "Проблема",
			"_solution": "Решение",
			"_problemText": "Единственными надежными способами для родителей узнать информацию об оценках являются телефонный звонок или визиты в школу. Текущая система отслеживания успеваемости требует от классных руководителей немало монотонной работы, ведь эта система слишком устарела.",
			"_solutionText": "Родители и ученики будут получать еженедельную рассылку о состоянии успеваемости на протяжении недели через Viber, WhatsApp и другие. Классные руководители смогут передавать информацию об оценках в 100 раз быстрее благодаря AI системе обработки информации.",
			"_join": "Подпишитесь на нашу рассылку, чтобы получать уведомления об обновлениях Gradder",
			"_joinMailing": "Узнавать про обновления",
			"_wip": "Работа в процессе",
      "_typeOfAccount": "Выберите тип учетной записи, которая подходит вам",
      "_regAdvisor": "Куратор",
      "_regParent": "Родитель",
      "_regStudent": "Ученик",
      "_regSchool": "Школа",
      "_childAmount": "Сколько у вас детей?",
      "_secondChild": "Данные о втором ребенке",
      "_thirdChild": "Данные о третьем ребенке",
      "_regYourSchool": "Из какой вы школы?",
      "_regYourGroup": "Из какого вы класса?",
      "_groupsAmount": "Сколько у вас классов?",
      "_groupsNames": "Как называются классы?",
      "_regToken": "Введите ваш пригласительный токен",
      },
    	"укр": {
    	"_greetings": "Ласкаво просимо до",
      "_tagline": "Ми створюємо новий зв’язок між школою та батьками",
			"_firstName": "Ім’я",
			"_secondName": "Прізвище",
			"_email": "Поштова адреса",
			"_password": "Пароль",
			"_charge1": "Пароль містить 8 символів",
			"_charge2": "Наявні цифри",
			"_charge3": "Наявні великі та малі латинські літери",
			"_login": "Вхід",
			"_next": "Далі",
			"_photoBy": "Фото від",
			"_class": "Клас",
			"_back": "Назад",
			"_register": "Зареєструватися",
			"_token": "Ваш токен",
			"_agree": "Я згоден з",
			"_terms": "умовами обслуговування Gradder",
			"_mailList": "Підпишіться на нашу розсилку, щоб отримувати повідомлення про оновлення Gradder",
			"_mailBtn": "Підписатися",
			"_tagline2": "Унікальна платформа для українських шкіл на базі штучного інтелекту",
			"_problem": "Проблема",
			"_solution": "Рішення",
			"_problemText": "Єдиним надійним способом для батьків і учнів дізнатися інформацію про оцінки є телефонний дзвінок або особисті візити до школи. Наявна система відслідковування успішності вимагає від класних керівників чимало монотонної роботи, адже ця система є застарілою та до сих пір базованою лише на папері.",
			"_solutionText": "Батьки та учні отримуватимуть щотижневу розсилку про стан успішності протягом поточного тижня через Viber, WhatsApp та інші. Класні керівники зможуть передавати інформацію про оцінки в 100 разів швидше завдяки системі обробки інформації, що використовує штучний інтелект.",
			"_join": "Підпишіться на нашу розсилку, щоб отримувати повідомлення про оновлення Gradder",
			"_joinMailing": "Бути в курсі оновлень",
			"_wip": "Робота в процесі",
      "_typeOfAccount": "Виберіть тип облікового запису, який вам підходить",
      "_regAdvisor": "Куратор",
      "_regParent": "Батківський",
      "_regStudent": "Учень",
      "_regSchool": "Школа",
      "_childAmount": "Скільки у вас дітей?",
      "_secondChild": "Дані про другу дитину",
      "_thirdChild": "Дані про третю дитину",
      "_regYourSchool": "З якої ви школи?",
      "_regYourGroup": "З якого ви класу?",
      "_groupsAmount": "Скільки у вас класів?",
      "_groupsNames": "Як називаються класи?",
      "_regToken": "Введіть ваш запрошувальний токен",
    	},
    	"eng": {
      "_greetings": "You're welcome to",
      "_tagline": "We build bridges between schools and parents",
			"_firstName": "First Name",
			"_secondName": "Last Name",
			"_email": "Your email",
			"_password": "Password",
			"_charge1": "Minimum 8 characters",
			"_charge2": "Numbers",
			"_charge3": "Capital and lowercase latin letters",
			"_login": "Log In",
			"_next": "Next",
			"_photoBy": "Photo by",
			"_class": "Group",
			"_back": "Back",
			"_register": "Sign Up",
			"_token": "Your token",
			"_agree": "I agree to the",
			"_terms": "Gradder Terms",
			"_mailList": "Join our mailing list today to be notified about Gradder updates",
			"_mailBtn": "Join the List",
			"_tagline2": "AI-driven platform for Ukrainian public schools",
			"_problem": "Problem",
			"_solution": "Solution",
			"_problemText": "Right now, the only reliable way to find out grades for parents and students in Ukrainian public schools is by conducting phone calls or in-person visits. In addition, the existing grade tracking system requires a lot of unnecessary manual work from academic advisors because it's obsolete and paper-based.",
			"_solutionText": "Parents and students get weekly grade reports through Viber, WhatsApp, Telegram, or Facebook Messenger. Academic advisors can create monthly reports 100 times faster thanks to an Artificial Intelligence-driven scanner app created by Gradder.",
			"_join": "Join our mailing list today to be notified about Gradder updates",
			"_joinMailing": "Join Mailing List",
			"_wip": "Work in progress",
      "_typeOfAccount": "Choose the type of account that suits you",
      "_regAdvisor": "Advisor",
      "_regParent": "Parent",
      "_regStudent": "Student",
      "_regSchool": "School",
      "_childAmount": "How many kids do you have?",
      "_secondChild": "Information about the second child",
      "_thirdChild": "Information about the third child",
      "_regYourSchool": "Which school are you in?",
      "_regYourGroup": "Which group are you in?",
      "_groupsAmount": "How many groups do you have?",
      "_groupsNames": "How are your groups called?",
      "_regToken": "Enter your invitation token",
      },
    };
    set_lang = function (dictionary) {
        $("[data-translate]").text(function () {
            var key = $(this).data("translate");
            if (dictionary.hasOwnProperty(key)) {
                return dictionary[key];
            }
        });
    };
    $("#lang").on("change", function () {
        var language = localStorage.getItem('lang');
        if (dictionary.hasOwnProperty(language)) {
        	set_lang(dictionary[language]);
        }
    });
});

$(document).ready(function() {
    $('#lang').trigger("change");

    if (localStorage.getItem('lang') != null) {
    	$(".custom-select-trigger").text(localStorage.getItem('lang').toUpperCase());
    } else {
    	$(".custom-select-trigger").text('УКР');
    }
});
