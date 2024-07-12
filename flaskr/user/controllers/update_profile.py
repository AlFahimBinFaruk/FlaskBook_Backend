from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from ..model import User
from pymongo.errors import PyMongoError


@jwt_required()
def handle_update_profile():
    try:
        user_id = get_jwt_identity()

        data = request.json

        user = User.find_by_id(ObjectId(user_id))

        if data.get("password") or data.get("role"):
            return jsonify({"error": "can't update requested fields"}), 400

        if not user:
            return jsonify({"error": "No such user exists"}), 400

        updated_user = User.update(user_id, data)

        if updated_user:
            return jsonify({
                "message": "Profile updated successfully",
                "user": {
                    "first_name": updated_user.get("first_name"),
                    "last_name": updated_user.get("last_name"),
                    "email": updated_user.get("email")
                }
            }), 200
        else:
            return jsonify({"error": "User update failed"}), 400
    except PyMongoError as e:
        return jsonify({"error": f" {e}"}), 500
    except Exception as e:
        return jsonify({"error": f" {e}"}), 500
