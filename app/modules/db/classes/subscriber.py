from .user import User


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
