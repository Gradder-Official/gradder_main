from .user import User

class Student(User):
    def __init__(self, email:str, first_name:str, last_name:str, class_name:str=None):
        super().__init__(email=email, first_name=first_name, last_name=last_name)
        self.class_name = class_name.lower()

    def __repr__(self):
        return f'<Student {self.ID}'

    def to_json(self):
        json_user = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'ID': self.ID,
            'password_hash': self.password_hash,
            'class_name': self.class_name
        }
        return json_user

    # Methods for accessing/posting homework and grades

