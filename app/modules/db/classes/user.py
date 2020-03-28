from werkzeug.security import generate_password_hash, check_password_hash
from .. import DB_API
from app.exceptions import NoUserError

class User:
    def __init__(self, _email:str, _first_name:str, _last_name:str):
        self.email = _email
        self.first_name = _first_name
        self.last_name = _last_name
        self.ID = 1 # get the latest from the database and assign next

    def __repr__(self):
        return f'<User {self.ID}'


    @property
    def password(self):
        raise AttributeError('password is not a readable property')
    

    @password.setter
    def set_password(self, password:str):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password_hash:str):
        return check_password_hash(self.password_hash, password_hash)


    def to_json(self):
        json_user = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'ID': self.ID
        }
        return json_user


class Teacher(User):
    def __init__(self, _email:str, _first_name:str, _last_name:str, _class_list:list=None, 
                 _subjects:list=None):
        super().__init__(_email, _first_name, _last_name)
        if _class_list:
            self.class_list = _class_list
        if _subjects:
            self.subjects = _subjects

    def __repr__(self):
        return f'<Teacher {self.ID}'

    
    # Methods for accessing/posting homework and grades


class Student(User):
    def __init__(self, _email:str, _first_name:str, _last_name:str, _class:str):
        super().__init__(_email, _first_name, _last_name)
        self.className = _class.lower()

    def __repr__(self):
        return f'<Student {self.ID}'

    
    # Methods for accessing/posting homework and grades


class Parent(User):
    def __init__(self, _email:str, _first_name:str, _last_name:str, _children:list):
        super().__init__(_email, _first_name, _last_name)
        
        self.children = []
        for child in _children:
            try:
                user = DB_API.get_user_by_name(first_name=child['first_name'], last_name=child['last_name'])
                self.children.append(user.ID)
            except BaseException:
                raise NoUserError
