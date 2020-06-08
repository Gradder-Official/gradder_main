from typing import List

from app import db


class Message:
    def __init__(self, email: str, subject: str, first_name: str, last_name: str, message: str, ID: str):
        self.email = email
        self.subject = subject
        self.first_name = first_name
        self.last_name = last_name
        self.message = message
        self.ID = ID

    def to_dict(self):
        json_dict = {
            'email': self.email,
            'subject': self.subject,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'message': self.message,
            'id': self.ID
        }

        return json_dict

    def to_json(self):
        return self.to_dict()

    def add(self):
        try:
            db.collection_messages.document(self.ID).set(self.to_dict())
            return True
        except BaseException as e:
            print(e)
            return False
