from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId
from ..model import User
from pymongo.errors import PyMongoError


@jwt_required()
def handle_get_user_details():
    try:
        user_id = get_jwt_identity()

        user = User.find_by_id(ObjectId(user_id))

        if not user:
            return jsonify({"error": "No such user exists"}), 400
        else:
            return jsonify({
                "first_name": user.get("first_name"),
                "last_name": user.get("last_name"),
                "email": user.get("email")

            }), 200

    except PyMongoError as e:
        return jsonify({"error": f" {e}"}), 500
    except Exception as e:
        return jsonify({"error": f" {e}"}), 500
