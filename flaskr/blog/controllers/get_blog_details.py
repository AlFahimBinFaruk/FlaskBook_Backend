from flask import jsonify
from bson import ObjectId
from ..model import Blog
from flaskr.user.model import User

from pymongo.errors import PyMongoError


def handle_get_blog_details(blog_id):
    try:
        # Fetch the blog by its ID
        blog = Blog.find_by_id(blog_id)

        if not blog:
            return jsonify({"error": "Blog not found"}), 404

        # Convert MongoDB ObjectId to string for JSON serialization
        blog['_id'] = str(blog['_id'])
        blog['user_id'] = str(blog['user_id'])

        # Fetch user details
        user = User.find_by_id(blog['user_id'])
        if user:
            blog['user_first_name'] = user.get('first_name', 'N/A')
            blog['user_last_name'] = user.get('last_name', 'N/A')

        return jsonify(blog), 200

    except PyMongoError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
