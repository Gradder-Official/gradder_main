from .user import User
from app.exceptions import NoUserError
from .. import db


class Parent(User):
    def __init__(self, email:str, first_name:str, last_name:str, children:list=None):
        super().__init__(email=email, first_name=first_name, last_name=last_name)
        
        self.children = []
        for child in children:
            try:
                user = db.get_user_by_name(first_name=child['first_name'], 
                                           last_name=child['last_name'])
                self.children.append(user.ID)
            except BaseException:
                raise NoUserError
    

    def __repr__(self):
        return f'<Parent {self.ID}'

    
    def to_json(self):
        json_user = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'ID': self.ID,
            'password_hash': self.password_hash,
            'children': self.children
        }
        return json_user

    @staticmethod
    def from_dict(dictionary:dict):
        user = Parent(email=dictionary['email'],
                      first_name=dictionary['first_name'],
                      last_name=dictionary['last_name'],
                      )

        if 'password' in dictionary:
            user.set_password(dictionary['password'])
    

        return user

    # Methods for accessing grades
