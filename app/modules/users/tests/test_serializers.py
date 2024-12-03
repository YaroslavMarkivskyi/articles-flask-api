from app.modules.users.serializers import UserSerializer

# Тест для методу from_dict
def test_from_dict():
    # Тестовий словник
    data = {
        "id": 1,
        "username": "testuser",
        "email": "testuser@example.com",
        "role": "ADMIN",
        "password": "hashed_password"
    }

    user_serializer = UserSerializer.from_dict(data)

    assert user_serializer.id == 1
    assert user_serializer.username == "testuser"
    assert user_serializer.email == "testuser@example.com"
    assert user_serializer.role == "ADMIN"
    assert user_serializer.password == "hashed_password"


def test_to_dict():
    user_serializer = UserSerializer(
        id=1,
        username="testuser",
        email="testuser@example.com",
        role="ADMIN",
        password="hashed_password"
    )

    result = user_serializer.to_dict()

    assert result == {
        "id": 1,
        "username": "testuser",
        "email": "testuser@example.com",
        "role": "ADMIN"
    }

    assert "password" not in result


def test_optional_id():
    data = {
        "username": "testuser2",
        "email": "testuser2@example.com",
        "role": "EDITOR",
        "password": "hashed_password"
    }

    user_serializer = UserSerializer.from_dict(data)

    assert user_serializer.id is None
    assert user_serializer.username == "testuser2"
    assert user_serializer.email == "testuser2@example.com"
    assert user_serializer.role == "EDITOR"
    assert user_serializer.password == "hashed_password"
