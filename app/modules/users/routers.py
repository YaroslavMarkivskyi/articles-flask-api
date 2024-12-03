from flask import request, jsonify, abort
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
from .permissions import admin_required, editor_required
from .validators import UserValidator
from flasgger import swag_from

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route("/", methods=[HTTPMethod.GET])
@jwt_required()
@swag_from("./swagger.yml")
def get_users():
    entity_users = UserService.get_all_users()
    json_users = [UserSerializer.to_dict(user) for user in entity_users]
    return jsonify({"users": json_users}), HTTPStatus.OK

@users_bp.route("/", methods=[HTTPMethod.POST])
@jwt_required()
@admin_required
@swag_from("./swagger.yml")
def register_user():
    data = request.json
    UserValidator.is_exist_fields(data)
    dto_user = UserSerializer.from_dict(data)
    entity_user = UserService.create_user(dto_user)
    json_user = UserSerializer.to_dict(entity_user)
    return jsonify(json_user), HTTPStatus.CREATED


@users_bp.route("/<int:user_id>", methods=[HTTPMethod.GET])
@jwt_required()
@swag_from("./swagger.yml")
def get_user(user_id):
    entity_user = UserService.get_user_by_id(user_id)
    UserValidator.is_exist_user(entity_user)
    json_user = UserSerializer.to_dict(entity_user)
    return jsonify(json_user), HTTPStatus.OK


@users_bp.route("/<int:user_id>", methods=[HTTPMethod.PUT])
@jwt_required()
@editor_required
@swag_from("./swagger.yml")
def update_user(user_id):
    data = request.json
    UserValidator.is_exist_fields(data)

    dto_user = UserSerializer.from_dict(data)
    UserValidator.is_exist_user(dto_user)

    entity_user = UserService.update_user(user_id, dto_user)
    json_user = UserSerializer.to_dict(entity_user)
    return jsonify(json_user), HTTPStatus.OK


@users_bp.route("/<int:user_id>",  methods=[HTTPMethod.DELETE])
@jwt_required()
@admin_required
@swag_from("./swagger.yml")
def delete_user(user_id):
    entity_user = UserService.get_article_by_id(user_id)
    UserValidator.is_exist_user(entity_user)
    UserService.delete_user(user_id)
    return jsonify({"message": "User deleted successfully"}), HTTPStatus.OK


@users_bp.route('/login', methods=['POST'])
@swag_from("./swagger.yml")
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    UserValidator.is_exist_username(user)
    UserValidator.is_valid_password(user.password, password)

    access_token = create_access_token(identity=str(user.id))
    return jsonify({"access_token": access_token}), HTTPStatus.OK


@users_bp.route("/user_profile", methods=[HTTPMethod.GET])
@jwt_required()
@swag_from("./swagger.yml")
def user_profile():
    user_id = get_jwt_identity()
    entity_user = UserService.get_user_by_id(user_id)
    UserValidator.is_exist_user(entity_user)
    json_user = UserSerializer.to_dict(entity_user)

    return jsonify(json_user), HTTPStatus.OK


@users_bp.route("/search", methods=[HTTPMethod.GET])
@jwt_required()
@swag_from("./swagger.yml")
def search_user_by_username():
    username = request.args.get("username")  # Отримання параметра з URL
    UserValidator.is_exist_username(username)
    entity_user = UserService.get_user_by_username(username)
    UserValidator.is_exist_user(entity_user)
    json_user = UserSerializer.to_dict(entity_user)
    return jsonify(json_user), HTTPStatus.OK
