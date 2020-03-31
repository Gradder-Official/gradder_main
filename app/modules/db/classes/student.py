from .user import User
from .access_level import ACCESS_LEVEL

class Student(User):
    def __init__(self, email:str, first_name:str, last_name:str, class_name:str=None, ID:str=None):
        super().__init__(email=email, first_name=first_name, last_name=last_name, ID=ID)
        self.class_name = class_name.lower()
        self.access_level = ACCESS_LEVEL.STUDENT

    def __repr__(self):
        return f'<Student {self.ID}'

    def to_json(self):
        json_user = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'ID': self.ID,
            'password': self.password_hash,
            'class_name': self.class_name
        }
        return json_user
    

    @property
    def class_name(self):
        return self.class_name

    @class_name.setter
    def set_class_name(self, new_class_name:str):
        self.class_name = new_class_name

    
    @staticmethod
    def from_dict(dictionary:dict):
        user = Student(email=dictionary['email'],
                       first_name=dictionary['first_name'],
                       last_name=dictionary['last_name'],
                       ID=dictionary['ID'] if 'ID' in dictionary else None)
        
        if 'class_name' in dictionary:
            user.set_class_name(dictionary['class_name'])

        if 'password' in dictionary:
            user.set_password(dictionary['password'])
        
        return user

    # Methods for accessing/posting homework and grades

