from .user import User
from .access_level import ACCESS_LEVEL


class Student(User):
    def __init__(self, email: str, first_name: str, last_name: str, class_name: str = None, ID: str = None):
        super().__init__(email=email, first_name=first_name, last_name=last_name,
                         usertype='student', ID=ID)
        if class_name is not None:
            self.class_name = class_name.lower()
        else:
            self.class_name = ""
        self.access_level = ACCESS_LEVEL.STUDENT

    def __repr__(self):
        return f'<Student {self.ID}'

    def to_json(self):
        json_user = super().to_json()

        try:
            json_user['class_name'] = self.class_name
        except BaseException:
            pass

        return json_user

    @staticmethod
    def from_dict(dictionary: dict):
        user = Student(email=dictionary['email'],
                       first_name=dictionary['first_name'],
                       last_name=dictionary['last_name'],
                       ID=dictionary['ID'] if 'ID' in dictionary else None)

        if 'class_name' in dictionary:
            user.class_name = (dictionary['class_name'])

        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        if 'secret_question' in dictionary and 'secret_answer' in dictionary:
            user.set_secret_question(dictionary['secret_question'], dictionary['secret_answer'])

        return user

    # Methods for accessing/posting homework and grades
