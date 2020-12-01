from flask import current_app
from pymongo import MongoClient


class DB:
    def __init__(self, connection_string: str, database: str):
        self.db = MongoClient(connection_string).get_database(database)

        # All the collection initializations go here
        self.courses = self.db.courses
        self.admins = self.db.admins
        self.teachers = self.db.teachers
        self.students = self.db.students
        self.parents = self.db.parents
        self.general_info = self.db.general_info

    def __repr__(self):
        return "<MongoDB database>"
