from werkzeug.security import generate_password_hash, check_password_hash
from re import match
from flask_login import UserMixin
from app.logs.user_logger import user_logger
from app import db
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from bson.objectid import ObjectId


class User(UserMixin):
    USERTYPE = None  # is unique per each class, acts as access levels

    def __init__(self, email: str, first_name: str, last_name: str, ID: str=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.secret_question = None
        self.secret_answer = None

    def __repr__(self):
        return f'<User {self.ID}>'

    def set_password(self, password: str):
        if match(r"(pbkdf2:sha256:)([^\$.]+)(\$)([^\$.]+)(\$)([^\$.]+)", password) is not None:
            self.password_hash = password
        else:
            self.password_hash = generate_password_hash(password)

    def update_password(self, password: str):
        self.password_hash=generate_password_hash(password)
        self.add()

    def verify_password(self, password: str):
        return check_password_hash(self.password_hash, password)

    def set_secret_question(self, question: str, answer: str):
        self.secret_question = question
        self.secret_answer = generate_password_hash(answer)

    def verify_secret_question(self, answer: str):
        return check_password_hash(self.secret_answer, answer)

    @staticmethod
    def get_by_id(id: str):
        if id:
            try:
                user = db.students.find_one({"_id": ObjectId(id)})
                user["_id"]
                return user
            except BaseException as e:
                pass

            try:
                user = db.teachers.find_one({"_id": ObjectId(id)})
                user["_id"]
                return user
            except BaseException as e:
                pass

            try:
                user = db.parents.find_one({"_id": ObjectId(id)})
                user["_id"]
                return user
            except BaseException as e:
                pass

            try:
                user = db.admins.find_one({"_id": ObjectId(id)})
                user["_id"]
                return user
            except BaseException as e:
                return None

    @staticmethod
    def get_by_email(email: str):
        if email:
            try:
                user = db.students.find_one({"email": email})
                user["_id"]
                return user
            except BaseException as e:
                pass

            try:
                user = db.teachers.find_one({"email": email})
                user["_id"]
                return user
            except BaseException as e:
                pass

            try:
                user = db.parents.find_one({"email": email})
                user["_id"]
                return user
            except BaseException as e:
                pass

            try:
                user = db.admins.find_one({"email": email})
                user["_id"]
                return user
            except BaseException as e:
                return None

    def add(self):
        r"""Adds the user to the DB.
        """
        try:
            dictionary = self.to_dict()
            if self.USERTYPE == "Teacher":
                print(dictionary)
                dictionary["class_list"] = []
            
            eval(f'db.{self.USERTYPE.lower() + "s"}.insert_one(dictionary)')
            return True
        except BaseException as e:
            user_logger.exception("Failed adding")
            return False
        return True


    def remove(self):
        try:
            eval(f'db.{self.USERTYPE.lower() + "s"}.delete({{"email": self.email}})')
            return True
        except BaseException as e:
            user_logger.exception("Failed removing")
            return False

    def to_json(self):
        json_user = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password_hash,
            'usertype': self.USERTYPE,
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
                    ID=dictionary['_id'] if '_id' in dictionary else None)

        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        if 'secret_question' in dictionary and 'secret_answer' in dictionary:
            user.set_secret_question(
                dictionary['secret_question'], dictionary['secret_answer'])

        return user

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.ID}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.get_by_id(user_id)
    
    def get_id(self):
        return self.ID