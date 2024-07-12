from flask import request, jsonify, current_app
from flask_jwt_extended import create_access_token
from ..model import User
from pymongo.errors import PyMongoError
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId


@jwt_required()
def handle_change_password():
    try:
        user_id = get_jwt_identity()
        data = request.json

        old_password = data.get("old_password")
        new_password = data.get("new_password")

        if not all([old_password, new_password]):
            return jsonify({"error": "provide all info."}), 400

        if len(new_password) < 6:
            return jsonify({"error": "password must be at least 6 characters"}), 400

        user = User.find_by_id(ObjectId(user_id))

        if not user:
            return jsonify({"error": "No such user exists"}), 400

        if not current_app.bcrypt.check_password_hash(user["password"], old_password):
            return jsonify({"error": "Invalid password"}), 400

        hashed_password = current_app.bcrypt.generate_password_hash(new_password).decode('utf-8')
        updated_user = User.update(user_id, {"password": hashed_password})

        if updated_user:
            return jsonify({
                "message": "Password changed successfully"
            }), 200
        else:
            return jsonify({"error": "Failed to change password"}), 400
    except PyMongoError as e:
        return jsonify({"error": f" {e}"}), 500
    except Exception as e:
        return jsonify({"error": f" {e}"}), 500
