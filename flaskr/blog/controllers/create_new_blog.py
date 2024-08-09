from flask import request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..model import Blog
from pymongo.errors import PyMongoError


@jwt_required()
def handle_create_new_blog():
    try:
        user_id = get_jwt_identity()  # Get the user ID from the JWT token
        data = request.json

        # Extract blog details from the request
        title = data.get('title')
        description = data.get('description')
        thumbnail_url = data.get('thumbnail_url', None)

        if not all([title, description]):
            return jsonify({"error": "Title and description are required."}), 400

        # Create a new Blog object
        blog = Blog(user_id=user_id, title=title, description=description, thumbnail_url=thumbnail_url)

        # Save the blog post
        blog_id = blog.save()

        return jsonify({
            "message": "Blog post created successfully.",
            "blog_id": str(blog_id)
        }), 201

    except PyMongoError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
