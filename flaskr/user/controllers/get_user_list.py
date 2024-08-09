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

        # Retrieve the admin user from the database
        admin = User.find_by_id(ObjectId(admin_id))

        # Check if the user is an admin
        if not admin or admin.get('role') != "admin":
            return jsonify({"error": "Authentication failed"}), 400

        # Retrieve and paginate the user list
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        users, total_users = User.find_all(page=page, per_page=per_page)

        return jsonify({
            "page": page,
            "per_page": per_page,
            "total": total_users,
            "users": users
        }), 200

    except PyMongoError as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500
