from flask import Blueprint

from .controllers.register import handle_register_user
from .controllers.login import handle_login
from .controllers.update_profile import handle_update_profile
from .controllers.update_profile_by_id import handle_update_profile_by_id
from .controllers.delete_profile import handle_delete_profile
from .controllers.delete_profile_by_id import handle_delete_profile_by_id
from .controllers.change_password import handle_change_password
from .controllers.get_user_list import handle_get_user_list
from .controllers.get_user_details import handle_get_user_details
from .controllers.get_user_details_by_id import handle_get_user_details_by_id

user_bp = Blueprint("user_bp", __name__)

user_bp.route("register", methods=["POST"])(handle_register_user)
user_bp.route("login", methods=["POST"])(handle_login)
user_bp.route("/profile/update", methods=["PUT"])(handle_update_profile)
user_bp.route("/profile/update/<string:id>", methods=["PUT"])(handle_update_profile_by_id)
user_bp.route("/profile/delete", methods=["DELETE"])(handle_delete_profile)
user_bp.route("/profile/delete/<string:id>", methods=["DELETE"])(handle_delete_profile_by_id)
user_bp.route("/profile/update/change-password", methods=["PUT"])(handle_change_password)
user_bp.route("/user/list", methods=["GET"])(handle_get_user_list)
user_bp.route("/user/details", methods=["GET"])(handle_get_user_details)
user_bp.route("/user/details/<string:id>", methods=["GET"])(handle_get_user_details_by_id)
