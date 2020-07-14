from app import db


class Application:
    def __init__(self, email: str, job: str, ID: str, first_name: str, last_name: str, resume_url: str, comments: str):
        self.email = email
        self.job = job
        self.first_name = first_name
        self.last_name = last_name
        self.resume_url = resume_url
        self.comments = comments
        self.ID = ID

    def to_dict(self):
        json_dict = {
            'email': self.email,
            'job': self.job,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'resume_url': self.resume_url,
            'comments': self.comments,
            'id': self.ID
        }

        return json_dict

    def to_json(self):
        return self.to_dict()

    def add(self):
        try:
            db.collection_applications.document(self.ID).set(self.to_dict())
            return True
        except BaseException as e:
            return False
