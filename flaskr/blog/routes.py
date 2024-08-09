from flask import Blueprint

from .controllers.get_all_blog_list import handle_get_all_blog_list
from .controllers.get_my_blog_list import handle_get_my_blog_list
from .controllers.get_blog_details import handle_get_blog_details
from .controllers.create_new_blog import handle_create_new_blog
from .controllers.update_blog import handle_update_blog
from .controllers.delete_blog import handle_delete_blog

blog_bp = Blueprint("blog_bp", __name__)

blog_bp.route("all", methods=["GET"])(handle_get_all_blog_list)
blog_bp.route("my/all", methods=["GET"])(handle_get_my_blog_list)
blog_bp.route("details/<string:blog_id>", methods=["GET"])(handle_get_blog_details)
blog_bp.route("add-new", methods=["POST"])(handle_create_new_blog)
blog_bp.route("update/<string:blog_id>", methods=["PUT"])(handle_update_blog)
blog_bp.route("delete/<string:blog_id>", methods=["DELETE"])(handle_delete_blog)
