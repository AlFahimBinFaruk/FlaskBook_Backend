from flask import Blueprint

from .controllers.upvote import handle_upvote
from .controllers.downvote import handle_downvote

vote_bp = Blueprint("vote_bp", __name__)

vote_bp.route("upvote/<string:blog_id>", methods=["POST"])(handle_upvote)
vote_bp.route("downvote/<string:blog_id>", methods=["POST"])(handle_downvote)
