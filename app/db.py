import os
import ssl
from datetime import datetime
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

class DB:
    client = MongoClient(os.environ.get("MONGO_CONNECTION_STRING"), ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
    
    def __init__(self, school: str):
        self.db = self.client.get_database(school)
        self.classes = self.db.classes
        self.admins = self.db.admins
        self.teachers = self.db.teachers
        self.students = self.db.students
        self.parents = self.db.parents
        self.general_info = self.db.general_info
        self.tokens = self.db.tokens
        self.subscribers = self.db.subscribers
        self.inquiries = self.db.inquiries
        self.ADMIN_TOKEN_HASH = 'pbkdf2:sha256:150000$p1711QE3$5fd0be7223ce989f55697f3afb3665e1b2a011214455c7e5f96d38586130969f'
    
    def __repr__(self):
        return '<MongoDB database>' 
    
    @staticmethod
    def get_new_id():
        # TODO: rewrite for a different method
        new_id = generate_password_hash("id"+str(datetime.utcnow()))
        new_id = new_id[new_id.index('$')+1:]
        return new_id[new_id.index('$')+1:]

    # TODO: this method should be in Admin class
    def new_auth_token(self, password):
        # TODO: don't do auth tokens with md5 hashs -- too complicated
        #if check_password_hash(self.ADMIN_TOKEN_HASH, password):
        new_token = generate_password_hash(str("token"+str(datetime.utcnow())))
        new_token = new_token[new_token.index('$')+1:]
        new_token = new_token[new_token.index('$')+1:][:20]
        self.tokens.insert_one({"_id": new_token})
        return new_token
        # else:
        #     return False

    # TODO: this method should be in Admin class
    def delete_auth_token(self, token):
        self.tokens.delete_one({"_id": token})
    


