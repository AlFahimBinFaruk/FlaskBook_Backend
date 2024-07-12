from flask import request, jsonify
from flask_jwt_extended import create_access_token
from ..model import User
from pymongo.errors import PyMongoError


def handle_register_user():
    try:
        data = request.json

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        password = data.get("password")

        role = "user"

        if not all([first_name, email, password]):
            return jsonify({"error": "Provide all info"}), 400

        if len(password) < 6:
            return jsonify({"error": "password must be at least 6 characters"}), 400

        if User.find_by_email(email):
            return jsonify({"error": "User already exists"}), 400

        new_user = User(first_name, last_name, email, password, role)
        new_user_id = new_user.save()
        access_token = create_access_token(identity=str(new_user_id))

        return jsonify({"message": "User registered successfully", "access_token": access_token}), 201

    except PyMongoError as e:
        return jsonify({"error": f" {e}"}), 500
    except Exception as e:
        return jsonify({"error": f" {e}"}), 500
