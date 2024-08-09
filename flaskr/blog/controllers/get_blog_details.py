from flask import jsonify
from bson import ObjectId
from ..model import Blog
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
        return jsonify(blog), 200

    except PyMongoError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
