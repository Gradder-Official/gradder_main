from werkzeug.security import generate_password_hash, check_password_hash
from re import match
from flask_login import UserMixin
from app.logs.user_logger import user_logger
from app import db


class User(UserMixin):
    USERTYPE = None  # is unique per each class, acts as access levels

    def __init__(self, email: str, first_name: str, last_name: str, ID: str = None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

        if ID is not None:
            self.ID = ID
        else:
            self.ID = db.get_new_id()

        self.secret_question = None
        self.secret_answer = None

    def __repr__(self):
        return f'<User {self.ID}>'

    def set_password(self, password: str):
        if match(r"(pbkdf2:sha256:)([^\$.]+)(\$)([^\$.]+)(\$)([^\$.]+)", password) is not None:
            self.password_hash = password
        else:
            self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str):
        return check_password_hash(self.password_hash, password)

    def set_secret_question(self, question: str, answer: str):
        self.secret_question = question
        if match(r"(pbkdf2:sha256:)([^\$.]+)(\$)([^\$.]+)(\$)([^\$.]+)", answer) is not None:
            self.secret_answer = answer
        else:
            self.secret_answer = generate_password_hash(answer)

    def verify_secret_question(self, answer: str):
        return check_password_hash(self.secret_answer, answer)

    @staticmethod
    def get_by_id(id: str):
        if id:
            try:
                user = db.collection_admins.document(id)

                user = user.get().to_dict()

                if user is not None:
                    return user
                else: 
                    raise(BaseException)
            except BaseException as e:
                pass

            try:
                user = db.collection_teachers.document(id)

                user = user.get().to_dict()

                if user is not None:
                    return user
                else: 
                    raise(BaseException)
            except BaseException:
                pass

            try:
                user = db.collection_students.document(id)

                user = user.get().to_dict()

                if user is not None:
                    return user
                else: 
                    raise(BaseException)
            except BaseException as e:
                pass

            try:
                user = db.collection_parents.document(id)

                user = user.get().to_dict()

                if user is not None:
                    return user
                else: 
                    raise(BaseException)
            except BaseException:
                return None

    @staticmethod
    def get_by_name(usertype: str, first_name: str, last_name: str):
        # TODO: what if there are many people with same names?
        if first_name and last_name:
            received_user = eval(
                f'db.collection_{usertype+"s"}.where(u"last_name", u"==", {last_name}).where(u"first_name", u"==", {first_name})'
            )
            if received_user:
                received_user = list(received_user.stream())[0].to_dict()
                return received_user
            else:
                return None

    @staticmethod
    def get_by_email(email: str):
        if email:
            try:
                user = db.collection_admins.where(u"email", u"==", email)

                return list(user.stream())[0].to_dict()
            except BaseException as e:
                pass

            try:
                user = db.collection_teachers.where(u"email", u"==", email)

                return list(user.stream())[0].to_dict()
            except BaseException as e:
                pass

            try:
                user = db.collection_parents.where(u"email", u"==", email)

                return list(user.stream())[0].to_dict()
            except BaseException as e:
                pass

            try:
                user = db.collection_students.where(u"email", u"==", email)

                return list(user.stream())[0].to_dict()
            except BaseException as e:
                return None

    def add(self):
        r"""Adds the user to the DB.
        """

        try:
            eval(
                f'db.collection_{self.USERTYPE.lower() + "s"}.document(self.ID).set(self.to_dict())')
            return True
        except BaseException as e:
            user_logger.exception("Failed adding")
            return False

    def remove(self):
        try:
            eval(
                f'db.collection_{self.USERTYPE.lower()+"s"}.document(str(self.ID)).delete()'
            )

            return True
        except BaseException as e:
            user_logger.exception("Failed removing")
            return False

    def get_id(self):
        return self.ID

    def to_json(self):
        json_user = {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'ID': self.ID,
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
                    ID=dictionary['ID'] if 'ID' in dictionary else None)

        if 'password' in dictionary:
            user.set_password(dictionary['password'])

        if 'secret_question' in dictionary and 'secret_answer' in dictionary:
            user.set_secret_question(
                dictionary['secret_question'], dictionary['secret_answer'])

        return user
