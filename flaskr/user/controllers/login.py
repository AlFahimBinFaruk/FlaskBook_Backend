from flask import request, jsonify, current_app
from flask_jwt_extended import create_access_token
from ..model import User
from pymongo.errors import PyMongoError


def handle_login():
    try:
        data = request.json

        email = data.get("email")
        password = data.get("password")

        if not all([email, password]):
            return jsonify({"error": "provide all info."}), 400

        user = User.find_by_email(email)

        if not user:
            return jsonify({"error": "Invalid email or password"}), 400

        if not current_app.bcrypt.check_password_hash(user["password"], password):
            return jsonify({"error": "Invalid email or password"}), 400

        access_token = create_access_token(identity=str(user['_id']))

        return jsonify({"message": "Login successful", "access_token": access_token}), 200
    except PyMongoError as e:
        return jsonify({"error": f" {e}"}), 500
    except Exception as e:
        return jsonify({"error": f" {e}"}), 500
