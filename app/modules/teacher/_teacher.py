from app.modules._classes import User, Classes
from app.logs import user_logger
from app import db
from app.modules.student._student import Student 
from bson import ObjectId

class Teacher(User):
    USERTYPE = 'Teacher'

    def __init__(self, email: str, first_name: str, last_name: str, class_list: list = [], ID: str = None):
        super().__init__(email=email, first_name=first_name, last_name=last_name, ID=ID)
        if class_list:
            self.class_list = class_list

    def __repr__(self):
        return f'<Teacher {self.ID}>'

    def to_json(self):
        json_user = super().to_json()
        try:
            json_user['class_list'] = self.class_list
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
    def add_student(class_id: str, email: str):
        student = Student.get_by_email(email)
        db.classes.update_one({"_id": ObjectId(class_id)}, {"$push": {"students": ObjectId(student.ID)}})

    @staticmethod
    def from_dict(dictionary: dict):
        user = Teacher(email=dictionary['email'],
                       first_name=dictionary['first_name'],
                       last_name=dictionary['last_name'],
                       ID=str(dictionary['_id']) if '_id' in dictionary else None)

        if 'class_list' in dictionary:
            user.class_list = dictionary['class_list']

        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        if 'secret_question' in dictionary and 'secret_answer' in dictionary:
            user.set_secret_question(
                dictionary['secret_question'], dictionary['secret_answer'])

        return user

    def get_class_names(self):
        classes = []
        if self.class_list:
            for class_ in self.class_list:
                classes.append((class_, Classes.get_by_id(class_)["name"]))
        
        return classes
