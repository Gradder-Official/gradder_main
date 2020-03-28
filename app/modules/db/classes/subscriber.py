from .. import DB_API

class Subscriber:
    def __init__(self, _email, _first_name, _last_name):
        self.email = _email
        self.first_name = _first_name
        self.last_name = _last_name
        self.ID = DB_API.get_last_id('subscriber') + 1
