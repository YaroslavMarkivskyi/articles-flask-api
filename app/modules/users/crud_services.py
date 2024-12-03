from typing import Optional
from flask import abort
from .models import User, db
from .serializers import UserSerializer
from http import HTTPStatus


class UserService:
    @staticmethod
    def create_user(dto: UserSerializer) -> User:
        """Створення нового користувача."""
        new_user = User(
            id=dto.id,
            username=dto.username,
            email=dto.email,
            role=dto.role,
            password=dto.password,  # Передбачається, що пароль хешується перед передачею
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_all_users():
        """Отримання списку всіх користувачів."""
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """Отримання користувача за ідентифікатором."""
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id: int, dto: UserSerializer) -> User:
        """Оновлення інформації про користувача."""
        user = User.query.get(user_id)
        if not user:
            abort(HTTPStatus.NOT_FOUND, description="Article not found")
        user.username = dto.username
        user.email = dto.email
        user.role = dto.role
        user.password = dto.password  # Передбачається, що пароль хешується перед передачею
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id: int):
        """Видалення користувача за ідентифікатором."""
        user = User.query.get(user_id)
        if not user:
            abort(HTTPStatus.NOT_FOUND, description="Article not found")
        db.session.delete(user)
        db.session.commit()
