from flask import request, jsonify
from ..model import Blog
from pymongo.errors import PyMongoError


def handle_get_all_blog_list():
    try:
        # Get page and per_page parameters from query params, default to page 1 and 10 items per page
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))



        # Fetch the blogs with pagination
        blogs, total_blogs = Blog.find_all(page, per_page)

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
