from http import HTTPStatus

from flask import abort
from werkzeug.security import check_password_hash


class UserValidator:
    @staticmethod
    def is_exist_user(article):
        if article is None:
            abort(HTTPStatus.NOT_FOUND, description="User not found")

    @staticmethod
    def is_exist_fields(data: dict):
        if not data:
            abort(HTTPStatus.BAD_REQUEST, description="Body is empty!")
        if (
            "username" not in data
            or "email" not in data
            or "password" not in data
            or "role" not in data
        ):
            abort(
                HTTPStatus.BAD_REQUEST,
                description="Missing data for required fields",
            )

    @staticmethod
    def is_exist_username(username):
        if not username:
            abort(HTTPStatus.BAD_REQUEST, description="Username is required")

    @staticmethod
    def is_valid_password(user_password, password):
        if not check_password_hash(user_password, password):
            abort(
                HTTPStatus.UNAUTHORIZED,
                description="Invalid username or password",
            )
