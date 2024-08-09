from datetime import datetime
from .. import mongo
from bson import ObjectId

class Blog:
    def __init__(self, user_id: str, title: str, description: str, thumbnail_url: str = None):
        self.user_id = ObjectId(user_id)  # Foreign key
        self.title = title
        self.description = description
        self.thumbnail_url = thumbnail_url
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.upvotes = 0
        self.downvotes = 0

    def save(self):
        blogs_collection = mongo.db.blogs
        result = blogs_collection.insert_one({
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'thumbnail_url': self.thumbnail_url,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'upvotes': self.upvotes,
            'downvotes': self.downvotes
        })
        return result.inserted_id

    @staticmethod
    def find_by_id(blog_id):
        blogs_collection = mongo.db.blogs
        return blogs_collection.find_one({'_id': ObjectId(blog_id)})

    @staticmethod
    def find_all(page=0, per_page=10):
        blogs_collection = mongo.db.blogs
        blogs = list(blogs_collection.find().skip((page - 1) * per_page).limit(per_page))
        total_blogs = blogs_collection.count_documents({})
        return blogs, total_blogs

    @staticmethod
    def update(blog_id, update_data):
        blogs_collection = mongo.db.blogs
        update_data['updated_at'] = datetime.utcnow()
        return blogs_collection.update_one({'_id': ObjectId(blog_id)}, {'$set': update_data})

    @staticmethod
    def delete(blog_id):
        blogs_collection = mongo.db.blogs
        return blogs_collection.delete_one({'_id': ObjectId(blog_id)})

    @staticmethod
    def find_by_user(user_id,page=1, per_page=10):
        blogs_collection = mongo.db.blogs
        blogs = list(blogs_collection.find({'user_id': ObjectId(user_id)}).skip((page - 1) * per_page).limit(per_page))
        total_blogs = blogs_collection.count_documents({'user_id': ObjectId(user_id)})
        return blogs, total_blogs

    @staticmethod
    def update_votes(blog_id, upvote_change=0, downvote_change=0):
        blogs_collection = mongo.db.blogs
        return blogs_collection.update_one(
            {'_id': ObjectId(blog_id)},
            {'$inc': {'upvotes': upvote_change, 'downvotes': downvote_change}}
        )

