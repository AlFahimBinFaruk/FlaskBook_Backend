from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from ..model import User
from pymongo.errors import PyMongoError


# only admin have access to this.
@jwt_required()
def handle_delete_profile_by_id(user_id):
    try:
        admin_id = get_jwt_identity()

        admin = User.find_by_id(ObjectId(admin_id))

        if not admin or admin.get("role") != "admin":
            return jsonify({"error": "Authentication failed"}), 400

        user = User.find_by_id(ObjectId(user_id))

        if not user:
            return jsonify({"error": "No such user exists"}), 400

        # Delete user using User model
        result = User.delete(user_id)  # Use the id parameter

        if result:
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"error": "User deletion failed"}), 400
    except PyMongoError as e:
        return jsonify({"error": f" {e}"}), 500
    except Exception as e:
        return jsonify({"error": f" {e}"}), 500
