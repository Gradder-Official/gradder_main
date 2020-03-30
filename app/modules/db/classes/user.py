from werkzeug.security import generate_password_hash, check_password_hash
from .. import db
from .access_level import ACCESS_LEVEL

class User:
    def __init__(self, email:str, first_name:str, last_name:str):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.ID = db.get_new_id()
        self.access_level = ACCESS_LEVEL.EMPTY

    def __repr__(self):
        return f'<User {self.ID}'

    
    def new_id(self):
        self.ID = db.get_new_id()


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
            'ID': self.ID,
            'password_hash': self.password_hash
        }
        return json_user

    
    def to_dict(self):
        return self.to_json()

    @staticmethod
    def from_dict(dictionary:dict):
        user = User(email=dictionary['email'],
                    first_name=dictionary['first_name'],
                    last_name=dictionary['last_name'])

        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        user.new_id()
        
        return user
