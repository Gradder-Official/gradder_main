from app.modules._classes import User, Classes
from app.logs import user_logger
from app import db
from app.modules.student._student import Student 
from bson import ObjectId

class Teacher(User):
    USERTYPE = 'Teacher'

    def __init__(self, email: str, first_name: str, last_name: str, classes: list = None, ID: str = None):
        super().__init__(email=email, first_name=first_name, last_name=last_name, ID=ID)
        self.classes = classes if classes is not None else list()

    def __repr__(self):
        return f'<Teacher {self.ID}>'

    def to_json(self):
        json_user = super().to_json()

        json_user['classes'] = self.classes

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
                       ID=str(dictionary['_id']) if '_id' in dictionary else None,
                       classes=dictionary['classes'] if 'classes' in dictionary else None)

        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        if 'secret_question' in dictionary and 'secret_answer' in dictionary:
            user.set_secret_question(
                dictionary['secret_question'], dictionary['secret_answer'])

        return user

    def get_class_names(self):
        classes = list()
        print(self.classes)
        for class_ in self.classes:
            classes.append((class_, Classes.get_by_id(class_).name))
        
        return classes


    