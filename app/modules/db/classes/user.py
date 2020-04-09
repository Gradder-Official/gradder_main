from werkzeug.security import generate_password_hash, check_password_hash
from re import match
from flask_login import UserMixin

from .access_level import ACCESS_LEVEL


class User(UserMixin):
    def __init__(self, email: str, first_name: str, last_name: str, usertype: str, ID: str = None):
        from app import db
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.usertype = usertype
        if ID is not None:
            self.ID = ID
        else:
            self.ID = db.get_new_id()
        self.secret_question = None
        self.secret_answer = None
        self.access_level = ACCESS_LEVEL.EMPTY

    def __repr__(self):
        return f'<User {self.ID}'

    def set_password(self, password: str):
        if match(r"(pbkdf2:sha256:)([^\$.]+)(\$)([^\$.]+)(\$)([^\$.]+)", password) is not None:
            self.password_hash = password
        else:
            self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str):
        return check_password_hash(self.password_hash, password)

    
    def set_secret_question(self, question:str, answer:str):
        self.secret_question = question
        if match(r"(pbkdf2:sha256:)([^\$.]+)(\$)([^\$.]+)(\$)([^\$.]+)", answer) is not None:
            self.secret_answer = answer
        else:
            self.secret_answer = generate_password_hash(answer)

    
    def verify_secret_question(self, answer:str):
        return check_password_hash(self.secret_answer, answer)


    def get_id(self):
        return self.ID

    def to_json(self):
        json_user = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'ID': self.ID,
            'password': self.password_hash,
            'usertype': self.usertype,
            'secret_question': self.secret_question,
            'secret_answer': self.secret_answer
        }
        return json_user

    def to_dict(self):
        return self.to_json()

    @staticmethod
    def from_dict(dictionary: dict):
        user = User(email=dictionary['email'],
                    first_name=dictionary['first_name'],
                    last_name=dictionary['last_name'],
                    ID=dictionary['ID'] if 'ID' in dictionary else None,
                    usertype=dictionary['usertype'])

        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        if 'secret_question' in dictionary and 'secret_answer' in dictionary:
            user.set_secret_question(dictionary['secret_question'], dictionary['secret_answer'])

        return user
