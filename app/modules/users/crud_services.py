from http import HTTPStatus
from typing import Optional

from flask import abort

from .models import User, db
from .serializers import UserSerializer


class UserService:
    @staticmethod
    def create_user(dto: UserSerializer) -> User:
        new_user = User(
            id=dto.id,
            username=dto.username,
            email=dto.email,
            role=dto.role,
            password=dto.password,
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_username(username: str) -> User:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def update_user(user_id: int, dto: UserSerializer) -> User:
        user = User.query.get(user_id)
        if not user:
            abort(HTTPStatus.NOT_FOUND, description="User not found")
        user.username = dto.username
        user.email = dto.email
        user.role = dto.role
        user.password = dto.password
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id: int):
        user = User.query.get(user_id)
        if not user:
            abort(HTTPStatus.NOT_FOUND, description="User not found")
        db.session.delete(user)
        db.session.commit()
