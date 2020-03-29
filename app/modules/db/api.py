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
        self.collection_admins = self.db.collectoin('admins')
        self.collection_subscribers = self.db.collection('subscribers')
    

    def __repr__(self):
        return '<Firestore database>'


    @staticmethod
    def get_new_id():
        return generate_password_hash(str(datetime.utcnow()))

    def get_user(self, user:User):
        if type(user) == Teacher:
            received_user = self.collection_teachers.document(user.ID)
            if received_user:
                return Teacher.from_dict(received_user.get())
            else:
                return None
        elif type(user) == Student:
            received_user = self.collection_students.document(user.ID)
            if received_user:
                return Student.from_dict(received_user.get())
            else:
                return None
        elif type(user) == Parent:
            received_user = self.collection_parents.document(user.ID)
            if received_user:
                return Parent.from_dict(received_user.get())
            else:
                return None
        elif type(user) == Student:
            received_user = self.collection_students.document(user.ID)
            if received_user:
                return Student.from_dict(received_user.get())
            else:
                return None

    def get_user_by_name(self, first_name:str, last_name:str):
        user = None
        return user

    def add_user(self, user:User):
        status = False # add the user to the database and get the status
        return status

    def delete_user(self, user:User):
        status = False # delete the user from the databse and return the status
        return status

    def get_subscriber(self, subscriber:Subscriber):
        subscriber = None # get the subsciber from the database
        return subscriber

    def add_subscriber(self, subsciber:Subscriber):
        status = False # add the subscriber to the database and get the status
        return status

    def delete_subscriber(self, subsciber:Subscriber):
        status = False # delere the subscriber from the database and get the status
        return status
