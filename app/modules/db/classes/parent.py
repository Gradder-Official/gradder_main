from .user import User
from app.exceptions import NoUserError
from .access_level import ACCESS_LEVEL
from .student import Student


class Parent(User):
    def __init__(self, email: str, first_name: str, last_name: str, children: list = None, ID: str = None):
        from app import db
        super().__init__(email=email, first_name=first_name, last_name=last_name,
                         usertype='parent', ID=ID)

        self.children = []
        if children is not None:
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
        return f'<Parent {self.ID}>'

    def to_json(self):
        json_user = super().to_json()

        try:
            json_user['children'] = self.children
        except BaseException:
            pass

        return json_user

    @staticmethod
    def from_dict(dictionary: dict):
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

            user.children = children_id_list

        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        if 'secret_question' in dictionary and 'secret_answer' in dictionary:
            user.set_secret_question(dictionary['secret_question'], dictionary['secret_answer'])

        return user

    # Methods for accessing grades
