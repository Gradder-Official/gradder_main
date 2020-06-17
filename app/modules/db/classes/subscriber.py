from .user import User
from app.logs.user_logger import user_logger
from app import db


class Subscriber(User):
    def __init__(self, email: str, first_name: str, last_name: str, ID: str = None):
        super().__init__(email=email, first_name=first_name, last_name=last_name,
                         usertype='subscriber', ID=ID)

    def __repr__(self):
        return f'<Subscriber {self.ID}>'

    def to_json(self):
        return {
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    @staticmethod
    def from_dict(dictionary: dict):
        return Subscriber(email=dictionary['email'],
                          first_name=dictionary['first_name'],
                          last_name=dictionary['last_name'],
                          ID=dictionary['ID'] if 'ID' in dictionary else None)

    @staticmethod
    def get_by_id(ID: str):
        subscr = db.collection_subscribers.document(ID)

        if subscr:
            return Subscriber.from_dict(subscr.get())
        else:
            return None

    def add(self):
        try:
            db.collection_subscribers.document(self.ID).set(self.to_dict())
            return True
        except BaseException as e:
            user_logger.exception("Failed adding")
            return False

    def remove(self):
        try:
            db.collection_subscribers.document(self.ID).delete()
            return True
        except BaseException:
            return False
