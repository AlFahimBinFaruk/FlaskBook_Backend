from datetime import datetime
from flask_bcrypt import Bcrypt
from .. import mongo
from bson import ObjectId
from flask import current_app


class User:
    def __init__(self, first_name: str, last_name: str, email: str, password: str, role:str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        # Hash the password before storing it
        self.password = current_app.bcrypt.generate_password_hash(password).decode('utf-8')
        self.role = role
        self.created_at: datetime = datetime.utcnow()
        self.updated_at: datetime = datetime.utcnow()

    def save(self):
        users_collection = mongo.db.users
        result = users_collection.insert_one({
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'role': self.role,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        })

        return result.inserted_id

    @staticmethod
    def find_by_email(email):
        users_collection = mongo.db.users
        return users_collection.find_one({'email': email})

    @staticmethod
    def find_by_id(user_id):
        users_collection = mongo.db.users
        return users_collection.find_one({"_id": ObjectId(user_id)})

    @staticmethod
    def find_all(page=1, per_page=10):
        users_collection = mongo.db.users
        skip_count = (page - 1) * per_page
        users = users_collection.find().skip(skip_count).limit(per_page)
        return list(users)

    @staticmethod
    def update(user_id, update_data):
        users_collection = mongo.db.users
        update_data["updated_at"] = datetime.utcnow()  # Update the updated_at field
        result = users_collection.find_one_and_update(
            {'_id': ObjectId(user_id)},
            {'$set': update_data},
            return_document=True  # Return the updated document
        )
        return result

    @staticmethod
    def delete(user_id):
        users_collection = mongo.db.users
        result = users_collection.delete_one({'_id': ObjectId(user_id)})
        return result.deleted_count > 0  # Return True if a document was deleted, otherwise False
