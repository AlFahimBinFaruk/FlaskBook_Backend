from flask import request, jsonify
from ..model import Blog
from pymongo.errors import PyMongoError
from flask_jwt_extended import jwt_required, get_jwt_identity


@jwt_required()
def handle_get_my_blog_list():
    try:
        user_id = get_jwt_identity()
        # Get page and per_page parameters from query params, default to page 1 and 10 items per page
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        # Fetch the blogs with pagination
        blogs, total_blogs = Blog.find_by_user(user_id, page, per_page)

        # Convert ObjectId to string for JSON serialization
        blog_list = []
        for blog in blogs:
            blog['_id'] = str(blog['_id'])
            blog['user_id'] = str(blog['user_id'])
            blog_list.append(blog)

        return jsonify({
            "page": page,
            "per_page": per_page,
            "total": total_blogs,
            "blogs": blog_list
        }), 200

    except PyMongoError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
