from flask import Blueprint

from .controllers.get_comment_list import handle_get_comment_list
from .controllers.create_comment import handle_create_comment
from .controllers.update_comment import handle_update_comment
from .controllers.delete_comment import handle_delete_comment

comment_bp = Blueprint("comment_bp", __name__)

comment_bp.route("all/<string:blog_id>", methods=["GET"])(handle_get_comment_list)
comment_bp.route("add-new", methods=["POST"])(handle_create_comment)
comment_bp.route("update/<string:comment_id>", methods=["PUT"])(handle_update_comment)
comment_bp.route("delete/<string:comment_id>", methods=["DELETE"])(handle_delete_comment)
