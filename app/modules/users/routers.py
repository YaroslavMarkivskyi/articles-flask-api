from flask import request, jsonify, abort
from werkzeug.security import check_password_hash
from http import HTTPStatus, HTTPMethod
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from flask import Blueprint

from .models import User
from .crud_services import UserService
from .serializers import UserSerializer

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route("/", methods=[HTTPMethod.GET])
@jwt_required()
def get_users():
    entity_users = UserService.get_all_users()
    json_users = [UserSerializer.to_dict(user) for user in entity_users]
    return jsonify({"users": json_users}), HTTPStatus.OK

@users_bp.route("/", methods=[HTTPMethod.POST])
@jwt_required()
def register_user():
    data = request.json
    # ArticleValidator.is_exist_fields(data)
    dto_user = UserSerializer.from_dict(data)
    entity_user = UserService.create_article(dto_user)
    json_user = UserSerializer.to_dict(entity_user)
    return jsonify(json_user), HTTPStatus.CREATED


@users_bp.route("/<int:user_id>", methods=[HTTPMethod.GET])
@jwt_required()
def get_user(user_id):
    entity_user = UserService.get_article_by_id(user_id)
    # ArticleValidator.is_exist_article(entity_user)
    json_user = UserSerializer.to_dict(entity_user)
    return jsonify(json_user), HTTPStatus.OK


@users_bp.route("/<int:user_id>", methods=[HTTPMethod.PUT])
@jwt_required()
def update_user(user_id):
    data = request.json
    # ArticleValidator.is_exist_fields(data)

    dto_user = UserSerializer.from_dict(data)
    # ArticleValidator.is_exist_article(dto_article)

    entity_user = UserService.update_article(user_id, dto_user)
    json_user = UserSerializer.to_dict(entity_user)
    return jsonify(json_user), HTTPStatus.OK


# TODO: SRP failed. Can't do validate and delete user.
@users_bp.route("/<int:user_id>",  methods=[HTTPMethod.DELETE])
@jwt_required()
def delete_user(user_id):
    UserService.delete_article(user_id)
    return jsonify({"message": "Book deleted successfully"}), HTTPStatus.OK


@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user is None or not check_password_hash(user.password, password):
        abort(HTTPStatus.UNAUTHORIZED, description="Invalid username or password")

    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), HTTPStatus.OK


# @users_bp.route("/user_profile", methods=["GET"])
# @jwt_required()
# def user_profile():
#     print(get_jwt())
#     user_id = get_jwt_identity()  # Retrieve user ID from the JWT
#     user = User.query.get(user_id)

#     if user is None:
#         abort(HTTPStatus.NOT_FOUND, description="User not found")

#     return jsonify(user.to_dict()), HTTPStatus.OK
