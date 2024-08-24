from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..model import Vote
from flaskr.blog.model import Blog
from pymongo.errors import PyMongoError


@jwt_required()
def handle_downvote(blog_id):
    try:
        user_id = get_jwt_identity()

        # Check if the blog exists
        blog = Blog.find_by_id(blog_id)
        if not blog:
            return jsonify({"error": "Blog not found"}), 404

        # Check if the user has already voted
        existing_vote = Vote.find_by_user_and_blog(user_id, blog_id)
        if existing_vote:
            vote_type = existing_vote.get('vote_type')
            if vote_type == "downvote":
                # Remove the downvote
                Vote.delete_by_user_and_blog(user_id, blog_id)
                Blog.update_votes(blog_id, downvote_change=-1)
                return jsonify({"message": "Downvote removed"}), 200
            elif vote_type == "upvote":
                # Change the upvote to a downvote
                Vote.update_vote(user_id, blog_id, "downvote")
                Blog.update_votes(blog_id, upvote_change=-1, downvote_change=1)
                return jsonify({"message": "Vote changed to downvote"}), 200
        else:
            # Create a new downvote
            Vote(user_id=user_id, blog_id=blog_id, vote_type='downvote').save()
            Blog.update_votes(blog_id, downvote_change=1)
            return jsonify({"message": "Downvoted successfully"}), 200

    except PyMongoError as e:
        return jsonify({"error": "Database error", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": "Unexpected error", "details": str(e)}), 500
