from .user import User
from .access_level import ACCESS_LEVEL


class Teacher(User):
    def __init__(self, email: str, first_name: str, last_name: str, class_list: list = None,
                 subjects: list = None, ID: str = None):
        super().__init__(email=email, first_name=first_name, last_name=last_name,
                         usertype='teacher', ID=ID)
        if class_list:
            self.class_list = class_list
        if subjects:
            self.subjects = subjects

        self.access_level = ACCESS_LEVEL.TEACHER

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

    @property
    def classes(self):
        return self.class_list

    @classes.setter
    def set_classes(self, new_classes: list):
        self.class_list = new_classes

    @property
    def subjects(self):
        return self.subjects

    @subjects.setter
    def set_subjects(self, new_subjects: list):
        self.subjects = new_subjects

    @staticmethod
    def from_dict(dictionary: dict):
        user = Teacher(email=dictionary['email'],
                       first_name=dictionary['first_name'],
                       last_name=dictionary['last_name'],
                       ID=dictionary['ID'] if 'ID' in dictionary else None)

        if 'class_list' in dictionary:
            user.set_classes(dictionary['class_list'])

        if 'subjects' in dictionary:
            user.set_subjects(dictionary['subjects'])

        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        return user

    # Methods for accessing/posting homework and grades
