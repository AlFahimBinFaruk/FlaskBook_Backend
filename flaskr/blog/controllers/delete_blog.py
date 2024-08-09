from flask import jsonify
from bson import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..model import Blog
from flaskr.user.model import User
from pymongo.errors import PyMongoError


@jwt_required()
def handle_delete_blog(blog_id):
    try:
        user_id = get_jwt_identity()  # Get the ID of the currently logged-in user
        user = User.find_by_id(ObjectId(user_id))

        if not user:
            return jsonify({"error": "User not found"}), 404

        # Find the blog by its ID
        blog = Blog.find_by_id(ObjectId(blog_id))

        if not blog:
            return jsonify({"error": "Blog not found"}), 404

        # Check if the user is the owner of the blog or an admin
        if blog['user_id'] != user_id and user.get("role") != "admin":
            return jsonify({"error": "Permission denied"}), 403

        # Delete the blog
        deleted = Blog.delete(blog_id)

        if deleted:
            return jsonify({"message": "Blog deleted successfully"}), 200
        else:
            return jsonify({"error": "Failed to delete blog"}), 400

    except PyMongoError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
