from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from ..model import User
from pymongo.errors import PyMongoError


# only admin have access to this.
@jwt_required()
def handle_get_user_list():
    try:
        admin_id = get_jwt_identity()

        admin = User.find_by_id(ObjectId(admin_id))

        if not admin or admin.role != "admin":
            return jsonify({"error": "Authentication failed"}), 400

        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        users = User.find_all(page=page, per_page=per_page)
        return jsonify(users), 200

    except PyMongoError as e:
        return jsonify({"error": f" {e}"}), 500
    except Exception as e:
        return jsonify({"error": f" {e}"}), 500
