from app.modules._classes import User


class Teacher(User):
    USERTYPE = 'Teacher'

    def __init__(self, email: str, first_name: str, last_name: str, class_list: list = None,
                 subjects: list = None, ID: str = None):
        super().__init__(email=email, first_name=first_name, last_name=last_name, ID=ID)
        if class_list:
            self.class_list = class_list
        if subjects:
            self.subjects = subjects

    def __repr__(self):
        return f'<Teacher {self.ID}'

    def to_json(self):
        json_user = super().to_json()

        try:
            json_user['class_list'] = self.class_list
        except BaseException:
            pass

        try:
            json_user['subjects'] = self.subjects
        except BaseException:
            pass

        return json_user

    @staticmethod
    def get_by_id(id: str):
        return Teacher.from_dict(super(Teacher, Teacher).get_by_id(id))

    @staticmethod
    def get_by_name(first_name: str, last_name: str):
        return Teacher.from_dict(super(Teacher, Teacher).get_by_name("teacher", first_name, last_name))

    @staticmethod
    def get_by_email(email: str):
        return Teacher.from_dict(super(Teacher, Teacher).get_by_email(email))

    @staticmethod
    def from_dict(dictionary: dict):
        user = Teacher(email=dictionary['email'],
                       first_name=dictionary['first_name'],
                       last_name=dictionary['last_name'],
                       ID=dictionary['ID'] if 'ID' in dictionary else None)

        if 'class_list' in dictionary:
            user.classes = dictionary['class_list']

        if 'subjects' in dictionary:
            user.subjects = dictionary['subjects']

        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        if 'secret_question' in dictionary and 'secret_answer' in dictionary:
            user.set_secret_question(
                dictionary['secret_question'], dictionary['secret_answer'])

        return user
