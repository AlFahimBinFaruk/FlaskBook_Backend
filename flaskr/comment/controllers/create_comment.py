from flask import request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from pymongo.errors import PyMongoError
from ..model import Comment
from flaskr.blog.model import Blog


@jwt_required()
def handle_create_comment():
    try:
        user_id = get_jwt_identity()
        data = request.json

        blog_id = data.get("blog_id")
        body = data.get("body")

        if not all([blog_id, body]):
            return jsonify({"error": "Missing required fields."}), 400

        # Check if the blog exists
        if not Blog.find_by_id(blog_id):
            return jsonify({"error": "Blog not found."}), 404

        comment = Comment(user_id=user_id, blog_id=blog_id, body=body)
        comment_id = comment.save()

        return jsonify({"message": "Comment created successfully.", "comment_id": str(comment_id)}), 201

    except PyMongoError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
