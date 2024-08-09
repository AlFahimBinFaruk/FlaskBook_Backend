from flask import request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..model import Vote
from flaskr.blog.model import Blog
from pymongo.errors import PyMongoError


@jwt_required()
def handle_upvote(blog_id):
    try:
        user_id = get_jwt_identity()

        # Check if a blog with the given ID exists
        blog = Blog.find_by_id(blog_id)
        if not blog:
            return jsonify({"error": "Blog not found"}), 404

        # Check if the user has already voted
        existing_vote = Vote.find_by_user_and_blog(user_id, blog_id)
        if existing_vote:
            if existing_vote['vote_type'] == 'upvote':
                # Remove the upvote
                Vote.delete_by_user_and_blog(user_id, blog_id)
                Blog.update_votes(blog_id, upvote_change=-1)
                return jsonify({"message": "Removed upvote"}), 200
            elif existing_vote['vote_type'] == 'downvote':
                # Remove the downvote and add an upvote
                Vote.delete_by_user_and_blog(user_id, blog_id)
                Blog.update_votes(blog_id, upvote_change=1, downvote_change=-1)
                return jsonify({"message": "Changed vote to upvote"}), 200

        # Create a new upvote
        vote = Vote(user_id, blog_id, 'upvote')
        vote.save()
        Blog.update_votes(blog_id, upvote_change=1)

        return jsonify({"message": "Upvoted successfully"}), 200

    except PyMongoError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
