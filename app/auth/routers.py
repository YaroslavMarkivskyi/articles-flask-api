from flask import request, jsonify, abort
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from flask import Blueprint

from .models import User


auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user is None or not check_password_hash(user.password, password):
        abort(HTTPStatus.UNAUTHORIZED, description="Invalid username or password")

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), HTTPStatus.OK


@auth_bp.route("/user_profile", methods=["GET"])
@jwt_required()
def user_profile():
    user_id = get_jwt_identity()  # Retrieve user ID from the JWT
    user = User.query.get(user_id)

    if user is None:
        abort(HTTPStatus.NOT_FOUND, description="User not found")

    return jsonify(user.to_dict()), HTTPStatus.OK