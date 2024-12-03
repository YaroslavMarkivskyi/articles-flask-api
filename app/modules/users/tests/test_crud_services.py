from http import HTTPStatus

import pytest
from flask import Flask
from sqlalchemy.exc import IntegrityError

from app.modules.users.crud_services import UserService
from app.modules.users.models import User, db
from app.modules.users.serializers import UserSerializer


@pytest.fixture(scope="module")
def app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def valid_user_dto():
    return UserSerializer(
        id=1,
        username="testuser",
        email="test@example.com",
        role="admin",
        password="hashed_password",
    )


@pytest.fixture
def existing_user():
    user = User(
        username="existinguser",
        email="existing@example.com",
        role="user",
        password="hashed_password",
    )
    db.session.add(user)
    db.session.commit()
    return user


def test_create_user(client, valid_user_dto):
    user = UserService.create_user(valid_user_dto)
    assert user.username == valid_user_dto.username
    assert user.email == valid_user_dto.email
    assert user.role == valid_user_dto.role


def test_create_user_with_existing_email(client, valid_user_dto, existing_user):
    duplicate_dto = UserSerializer(
        id=None,
        username="anotheruser",
        email=existing_user.email,
        role="admin",
        password="hashed_password",
    )

    with pytest.raises(IntegrityError):
        UserService.create_user(duplicate_dto)
    db.session.rollback()  # Оскільки транзакція не була завершена


def test_get_all_users(client):
    users = UserService.get_all_users()
    assert len(users) == 2


def test_get_user_by_id(client, valid_user_dto):
    user = UserService.get_user_by_id(valid_user_dto.id)
    assert user.id == valid_user_dto.id
    assert user.username == valid_user_dto.username


def test_get_user_by_username(client, valid_user_dto):
    user = UserService.get_user_by_username(valid_user_dto.username)
    assert user.username == valid_user_dto.username
    assert user.email == valid_user_dto.email


def test_update_user(client, valid_user_dto):
    updated_dto = UserSerializer(
        id=valid_user_dto.id,
        username="updateduser",
        email="updated@example.com",
        role="admin",
        password="newhashedpassword",
    )
    updated_user = UserService.update_user(valid_user_dto.id, updated_dto)
    assert updated_user.username == "updateduser"
    assert updated_user.email == "updated@example.com"


def test_update_user_not_found(client):
    invalid_dto = UserSerializer(
        id=999,
        username="nonexistent",
        email="nonexistent@example.com",
        role="admin",
        password="password",
    )
    with pytest.raises(Exception):
        UserService.update_user(999, invalid_dto)


def test_delete_user(client, valid_user_dto):
    UserService.delete_user(valid_user_dto.id)
    user = UserService.get_user_by_id(valid_user_dto.id)
    assert user is None


def test_delete_user_not_found(client):
    with pytest.raises(Exception):
        UserService.delete_user(999)
