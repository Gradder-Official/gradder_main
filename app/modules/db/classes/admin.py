from re import match

from .user import User
from .access_level import ACCESS_LEVEL


class Admin(User):
    def __init__(self, email: str, first_name: str, last_name: str, ID: str = None):
        super().__init__(email=email, first_name=first_name, last_name=last_name,
                         usertype='admin', ID=ID)

        self.access_level = ACCESS_LEVEL.ADMIN

    def __repr__(self):
        return f'<Admin {self.ID}> '

    def to_json(self):
        json_user = super().to_json()
        return json_user

    @staticmethod
    def from_dict(dictionary: dict):
        user = Admin(email=dictionary['email'],
                     first_name=dictionary['first_name'],
                     last_name=dictionary['last_name'],
                     ID=dictionary['ID'] if 'ID' in dictionary else None)

        if 'password' in dictionary:
            user.set_password(dictionary['password'])
        
        if 'secret_question' in dictionary and 'secret_answer' in dictionary:
            user.set_secret_question(dictionary['secret_question'], dictionary['secret_answer'])

        return user

    # Methods for accessing/posting homework and grades
