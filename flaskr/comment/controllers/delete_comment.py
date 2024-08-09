from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from pymongo.errors import PyMongoError
from ..model import Comment
from flaskr.user.model import User
from bson import ObjectId


@jwt_required()
def handle_delete_comment(comment_id):
    try:
        user_id = get_jwt_identity()
        comment = Comment.find_by_id(comment_id)

        if not comment:
            return jsonify({"error": "Comment not found."}), 404

        # Check if the user is an admin or the owner of the comment
        current_user = User.find_by_id(user_id)
        if current_user.get("role") != "admin" and comment["user_id"] != ObjectId(user_id):
            return jsonify({"error": "Permission denied."}), 403

        if Comment.delete(comment_id):
            return jsonify({"message": "Comment deleted successfully."}), 200
        else:
            return jsonify({"error": "Failed to delete comment."}), 400

    except PyMongoError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
