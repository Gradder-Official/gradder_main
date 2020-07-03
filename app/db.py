from google.cloud import firestore
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class DB:
    def __init__(self):
        self.db = firestore.Client()
        self.collection_parents = self.db.collection('parents')
        self.collection_students = self.db.collection('students')
        self.collection_teachers = self.db.collection('teachers')
        self.collection_admins = self.db.collection('admins')

        self.collection_subscribers = self.db.collection('subscribers')
        self.collection_tokens = self.db.collection('tokens')
        self.collection_messages = self.db.collection('messages')

        self.collection_applications = self.db.collection('applications')
        self.collection_classes = self.db.collection('classes')
        self.ADMIN_TOKEN_HASH = 'pbkdf2:sha256:150000$p1711QE3$5fd0be7223ce989f55697f3afb3665e1b2a011214455c7e5f96d38586130969f'

    def __repr__(self):
        return '<Firestore database>'

    @staticmethod
    def get_new_id():
        # TODO: rewrite for a different method
        new_id = generate_password_hash("id"+str(datetime.utcnow()))
        new_id = new_id[new_id.index('$')+1:]
        return new_id[new_id.index('$')+1:]

    # TODO: this method should be in Admin class
    def new_auth_token(self, password):
        # TODO: don't do auth tokens with md5 hashs -- too complicated
        if check_password_hash(self.ADMIN_TOKEN_HASH, password):
            new_token = generate_password_hash(str("token"+datetime.utcnow()))
            new_token = new_token[new_token.index('$')+1:]
            new_token = new_token[new_token.index('$')+1:][:20]
            self.collection_tokens.document().set(new_token)
            return new_token
        else:
            return False

    # TODO: this method should be in Admin class
    def delete_auth_token(self, token):
        self.collection_tokens.document(token).delete()
