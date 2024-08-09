from datetime import datetime
from bson import ObjectId
from .. import mongo  # Adjust the import path as needed


class Comment:
    def __init__(self, user_id: str, blog_id: str, body: str):
        self.user_id = ObjectId(user_id)
        self.blog_id = ObjectId(blog_id)
        self.body = body
        self.created_at: datetime = datetime.utcnow()
        self.updated_at: datetime = datetime.utcnow()

    def save(self):
        comments_collection = mongo.db.comments
        result = comments_collection.insert_one({
            'user_id': self.user_id,
            'blog_id': self.blog_id,
            'body': self.body,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        })

        return result.inserted_id

    @staticmethod
    def find_by_id(comment_id: str):
        comments_collection = mongo.db.comments
        return comments_collection.find_one({'_id': ObjectId(comment_id)})

    @staticmethod
    def find_by_blog(blog_id: str, page=1, per_page=10):
        comments_collection = mongo.db.comments
        skip = (page - 1) * per_page
        return list(comments_collection.find({'blog_id': ObjectId(blog_id)}).skip(skip).limit(per_page))

    @staticmethod
    def update(comment_id: str, update_fields: dict):
        comments_collection = mongo.db.comments
        update_fields['updated_at'] = datetime.utcnow()
        result = comments_collection.update_one({'_id': ObjectId(comment_id)}, {'$set': update_fields})
        return result.matched_count > 0

    @staticmethod
    def delete(comment_id: str):
        comments_collection = mongo.db.comments
        result = comments_collection.delete_one({'_id': ObjectId(comment_id)})
        return result.deleted_count > 0
