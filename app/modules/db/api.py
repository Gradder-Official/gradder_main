from .classes import Subscriber, User, Teacher, Parent, Student, Admin
from google.cloud import firestore
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import login_manager


class DB:
    def __init__(self):
        self.db = firestore.Client()
        self.collection_parents = self.db.collection('parents')
        self.collection_students = self.db.collection('students')
        self.collection_teachers = self.db.collection('teachers')
        self.collection_admins = self.db.collection('admins')
        self.collection_subscribers = self.db.collection('subscribers')
        self.collection_tokens = self.db.collection('tokens')
        self.ADMIN_TOKEN_HASH = 'pbkdf2:sha256:150000$p1711QE3$5fd0be7223ce989f55697f3afb3665e1b2a011214455c7e5f96d38586130969f'

    def __repr__(self):
        return '<Firestore database>'

    @staticmethod
    def get_new_id():
        new_id = generate_password_hash("id"+str(datetime.utcnow()))
        new_id = new_id[new_id.index('$')+1:]
        return new_id[new_id.index('$')+1:]

    def new_auth_token(self, password):
        if check_password_hash(self.ADMIN_TOKEN_HASH, password):
            new_token = generate_password_hash(str("token"+datetime.utcnow()))
            new_token = new_token[new_token.index('$')+1:]
            new_token = new_token[new_token.index('$')+1:][:20]
            self.collection_tokens.document().set(new_token)
            return new_token
        else:
            return False

    @staticmethod
    def delete_auth_token(token):
        from app import db
        db.collection_tokens.document(token).delete()

    @staticmethod
    @login_manager.user_loader
    def get_user_by_id(id):
        from app import db
        if id:
            id = str(id)
            try:
                user = db.collection_admins.document(id)

                return Admin.from_dict(user.get().to_dict())
            except BaseException:
                pass

            try:
                user = db.collection_teachers.document(id)

                return Teacher.from_dict(user.get().to_dict())
            except BaseException:
                pass

            try:
                user = db.collection_students.document(id)

                return Student.from_dict(user.get().to_dict())
            except BaseException:
                pass

            try:
                user = db.collection_parents.document(id)

                return Parent.from_dict(user.get().to_dict())
            except:
                return None

    def get_user_by_name(self, usertype: User, first_name: str, last_name: str):
        if first_name and last_name:
            received_user = eval(
                f'self.collection_{type(usertype).__name__.lower()+"s"}.where(u"last_name", u"==", {last_name}).where(u"first_name", u"==", {first_name})')
            if received_user:
                received_user = list(received_user.stream())[0].to_dict()
                return eval(f'{type(usertype).__name__}.from_dict(received_user)')
            else:
                return None

    def get_user_by_email(self, email: str):
        if email:
            try:
                user = self.collection_admins.where(u'email', u'==', email)
                user = list(user.stream())[0].to_dict()

                print(user)
                print(Admin.from_dict(user))

                return Admin.from_dict(user)
            except BaseException:
                pass

            try:
                user = self.collection_teachers.where(u'email', u'==', email)
                user = list(user.stream())[0].to_dict()

                return Teacher.from_dict(user)
            except BaseException:
                pass

            try:
                user = self.collection_students.where(u'email', u'==', email)
                user = list(user.stream())[0].to_dict()

                return Student.from_dict(user)
            except BaseException:
                pass

            try:
                user = self.collection_parents.where(u'email', u'==', email)
                user = list(user.stream())[0].to_dict()

                return Parent.from_dict(user)
            except:
                return None

    def add_user(self, user: User):
        try:
            eval(
                f'self.collection_{type(user).__name__.lower()+"s"}.document(str(user.ID)).set(user.to_dict())')
            return True
        except BaseException as e:
            print(e)
            return False

    def delete_user(self, user: User):
        eval(
            f'self.collection_{type(user).__name__.lower()+"s"}.document(str(user.ID)).delete()')

    def get_subscriber(self, subscriber: Subscriber):
        subscr = self.collection_subscribers.document(str(subscriber.ID))
        if subscr:
            return Subscriber.from_dict(subscr.get())
        else:
            return None

    def add_subscriber(self, subscriber: Subscriber):
        try:
            self.collection_subscribers.document(
                str(subscriber.ID)).set(subscriber.to_dict())
            return True
        except BaseException:
            return False

    def delete_subscriber(self, subsciber: Subscriber):
        try:
            self.collection_subscribers.document(str(subsciber.ID)).delete()
            return True
        except BaseException:
            return False
