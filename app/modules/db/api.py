from .classes import Subscriber, User, Teacher, Parent, Student
from firebase_admin import firestore
from werkzeug.security import generate_password_hash
from datetime import datetime

class DB:
    def __init__(self):
        self.db = firestore.client()
        self.collection_parents = self.db.collection('parents')
        self.collection_students = self.db.collection('students')
        self.collection_teachers = self.db.collection('teachers')
        self.collection_admins = self.db.collection('admins')
        self.collection_subscribers = self.db.collection('subscribers')
    

    def __repr__(self):
        return '<Firestore database>'


    @staticmethod
    def get_new_id():
        return generate_password_hash(str(datetime.utcnow()))

    def get_user(self, user:User):
        received_user = exec(f'self.collection_{type(user).__name__.lower()+"s"}.document(user.ID)')
        if received_user:
            received_user = exec(f'{type(user).__name__}.from_dict(received_user.get())')
            return exec(f'{type(user).__name__}.from_dict(received_user)')
        else:
            return None

    def get_user_by_name(self, usertype:User, first_name:str, last_name:str):
        if first_name and last_name:
            received_user = exec(f'self.collection_{type(usertype).__name__.lower()+"s"}\
                .where(u"last_name", u"==", {last_name.decode("utf-8")})\
                .where(u"first_name", u"==", {first_name.decode("utf-8")})')
            if received_user:
                received_user = exec(f'{type(usertype).__name__}.from_dict(received_user.get())')
                return exec(f'{type(usertype).__name__}.from_dict(received_user)')
            else:
                return None

    def add_user(self, user:User):
        try:
            exec(f'self.collection_{type(user).__name__.lower()+"s"}.document(str(user.ID)\
                .decode("utf-8")).set(user.to_dict())')
            return True
        except BaseException:
            return False

    def delete_user(self, user:User):
        exec(f'self.collection_{type(user).__name__.lower()+"s"}.document(str(user.ID)\
            .decode("utf-8")).delete()')

    def get_subscriber(self, subscriber:Subscriber):
        subscr = self.collection_subscribers.document(str(subscriber.ID).decode("utf-8"))
        if subscr:
            return subsciber.to_dict(subscr)
        else:
            return None

    def add_subscriber(self, subscriber:Subscriber):
        try:
            self.collection_subscribers.document(str(subscriber.ID).decode("utf-8"))\
                .set(subscriber.to_dict())
            return True
        except BaseException:
            return False

    def delete_subscriber(self, subsciber:Subscriber):
        try:
            self.collection_subscribers.document(str(subsciber.ID).decode("utf-8")).delete()
            return True
        except BaseException:
            return False
