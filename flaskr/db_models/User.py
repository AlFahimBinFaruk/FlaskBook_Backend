from flask_pymongo import PyMongo
from datetime import datetime

from .. import mongo


class User:

    # id will be added by default.

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save(self):
        mongo.db.users.insert_one({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.last_name,
            "password": self.password,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        })
