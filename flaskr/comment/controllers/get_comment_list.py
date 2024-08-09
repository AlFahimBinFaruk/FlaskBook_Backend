from flask import request, jsonify
from pymongo.errors import PyMongoError
from ..model import Comment
from flaskr.blog.model import Blog


def handle_get_comment_list(blog_id):
    try:
        # Check if the blog exists
        if not Blog.find_by_id(blog_id):
            return jsonify({"error": "Blog not found."}), 404

        # Get page and per_page parameters from query params, default to page 1 and 10 items per page
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        comments = Comment.find_by_blog(blog_id, page=page, per_page=per_page)
        comment_arr = []
        for comment in comments:
            comment['_id'] = str(comment['_id'])
            comment['user_id'] = str(comment['user_id'])
            comment['blog_id'] = str(comment['blog_id'])

            comment_arr.append(comment)

        return jsonify({
            "page": page,
            "per_page": per_page,
            "comments": comment_arr
        }), 200

    except PyMongoError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
