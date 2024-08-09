from datetime import datetime
from .. import mongo
from bson import ObjectId


class Vote:
    def __init__(self, user_id: str, blog_id: str, vote_type: str):
        self.user_id = ObjectId(user_id)  # Foreign key
        self.blog_id = ObjectId(blog_id)  # Foreign key
        self.vote_type = vote_type  # 'upvote' or 'downvote'
        self.created_at = datetime.utcnow()

    def save(self):
        votes_collection = mongo.db.votes
        return votes_collection.insert_one({
            'user_id': self.user_id,
            'blog_id': self.blog_id,
            'vote_type': self.vote_type,
            'created_at': self.created_at
        })

    @staticmethod
    def find_by_user_and_blog(user_id, blog_id):
        votes_collection = mongo.db.votes
        return votes_collection.find_one({
            'user_id': ObjectId(user_id),
            'blog_id': ObjectId(blog_id)
        })

    @staticmethod
    def delete_by_user_and_blog(user_id, blog_id):
        votes_collection = mongo.db.votes
        return votes_collection.delete_one({
            'user_id': ObjectId(user_id),
            'blog_id': ObjectId(blog_id)
        })
