from .user import User
from app.exceptions import NoUserError
from .access_level import ACCESS_LEVEL
from .student import Student


class Parent(User):
    def __init__(self, email:str, first_name:str, last_name:str, children:list=None, ID:str=None):
        from app import db
        super().__init__(email=email, first_name=first_name, last_name=last_name, ID=ID)
        
        self.children = []
        for child in children:
            try:
                user = db.get_user_by_name(usertype=Student,
                                           first_name=child['first_name'], 
                                           last_name=child['last_name'])
                self.children.append(user.ID)
            except BaseException:
                raise NoUserError
        
        self.access_level = ACCESS_LEVEL.PARENT
    

    def __repr__(self):
        return f'<Parent {self.ID}'

    
    def to_json(self):
        json_user = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'ID': self.ID,
            'password': self.password_hash,
            'children': self.children
        }
        return json_user

    @property
    def children(self):
        return self.children

    @children.setter
    def set_children(self, new_children_list:str):
        self.children = new_children_list

    
    @staticmethod
    def from_dict(dictionary:dict):
        from app import db
        user = Parent(email=dictionary['email'],
                      first_name=dictionary['first_name'],
                      last_name=dictionary['last_name'],
                      ID=dictionary['ID'] if 'ID' in dictionary else None)
        
        if 'children' in dictionary:
            children_id_list = []
            for child in dictionary['children']:
                try:
                    user = db.get_user_by_name(usertype=Student,
                                               first_name=child['first_name'],
                                               last_name=child['last_name'])
                    children_id_list.append(user.ID)
                except BaseException:
                    raise NoUserError
            
            user.set_children(children_id_list)

        if 'password' in dictionary:
            user.set_password(dictionary['password'])
        
        return user

    # Methods for accessing grades
