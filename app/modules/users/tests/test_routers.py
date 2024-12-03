# import pytest
# from http import HTTPStatus
# from flask import Flask

# from app.modules.users.routers import users_bp
# from app.modules.users.models import User
# from app.modules.users.crud_services import UserService

# @pytest.fixture
# def app():
#     app = Flask(__name__)
#     app.register_blueprint(users_bp)
#     app.config['TESTING'] = True
#     return app

# @pytest.fixture
# def client(app):
#     return app.test_client()

# @pytest.fixture
# def mock_get_all_users(mocker):
#     users = [
#         User(id=1, username='testuser1', email="test1@email.com", role='admin'),
#         User(id=2, username='testuser2', email="test2@email.com", role='editor'),
#         User(id=3, username='testuser3', email="test3@email.com", role='viewer'),
#     ]
#     mocker.patch('app.modules.users.crud_services.UserService.get_all_users', return_value=users)


# # Тест для POST /users/login (успішний)
# def test_login_success(client, mocker):
#     mock_user = User(id=1, username='testuser', email="test@email.com", role='viewer', password="12345")
#     mocker.patch('app.modules.users.models.User.query').return_value.filter_by.return_value.first.return_value = mock_user
#     data = {"username": "testuser", "password": "12345"}
#     response = client.post('/users/login', json=data)
#     assert response.status_code == HTTPStatus.OK
#     assert "access_token" in response.json


# def test_get_users_success(client, mock_get_all_users):
#     response = client.get('/users/')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json == {
#         "users": [
#             {"id": 1, "username": "testuser1", "role": "user"},
#             {"id": 2, "username": "testuser2", "role": "admin"},
#         ]
#     }

# # Тест для POST /users (успішний)
# def test_register_user_success(client, mocker):
#     mock_create_user = mocker.patch('your_module.UserService.create_user', return_value=User(id=3, username='newuser', role='user'))
#     data = {"username": "newuser", "password": "password", "role": "user"}
#     response = client.post('/users', json=data)
#     assert response.status_code == HTTPStatus.CREATED
#     assert response.json == {"id": 3, "username": "newuser", "role": "user"}
#     mock_create_user.assert_called_once()

# # Тест для GET /users/<user_id> (успішний)
# def test_get_user_success(client, mocker):
#     mock_get_user_by_id = mocker.patch('your_module.UserService.get_user_by_id', return_value=User(id=1, username='testuser1', role='user'))
#     response = client.get('/users/1')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json == {"id": 1, "username": "testuser1", "role": "user"}
#     mock_get_user_by_id.assert_called_once_with(1)

# # Тест для PUT /users/<user_id> (успішний)
# def test_update_user_success(client, mocker):
#     mock_update_user = mocker.patch('your_module.UserService.update_user', return_value=User(id=1, username='updateduser', role='admin'))
#     data = {"username": "updateduser", "role": "admin"}
#     response = client.put('/users/1', json=data)
#     assert response.status_code == HTTPStatus.OK
#     assert response.json == {"id": 1, "username": "updateduser", "role": "admin"}
#     mock_update_user.assert_called_once()

# # Тест для DELETE /users/<user_id> (успішний)
# def test_delete_user_success(client, mocker):
#     mock_get_article_by_id = mocker.patch('your_module.UserService.get_article_by_id', return_value=User(id=1, username='testuser1', role='user'))
#     mock_delete_user = mocker.patch('your_module.UserService.delete_user', return_value=None)
#     response = client.delete('/users/1')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json == {"message": "User deleted successfully"}
#     mock_get_article_by_id.assert_called_once_with(1)
#     mock_delete_user.assert_called_once_with(1)


# # Тест для GET /users/user_profile (успішний)
# def test_user_profile_success(client, mocker):
#     mock_get_user_by_id = mocker.patch('your_module.UserService.get_user_by_id', return_value=User(id=1, username='testuser1', role='user'))
#     mocker.patch('your_module.get_jwt_identity', return_value=1)
#     response = client.get('/users/user_profile')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json == {"id": 1, "username": "testuser1", "role": "user"}
#     mock_get_user_by_id.assert_called_once_with(1)

# # Тест для GET /users/search (успішний)
# def test_search_user_by_username_success(client, mocker):
#     mock_get_user_by_username = mocker.patch('your_module.UserService.get_user_by_username', return_value=User(id=1, username='testuser1', role='user'))
#     response = client.get('/users/search?username=testuser1')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json == {"id": 1, "username": "testuser1", "role": "user"}
#     mock_get_user_by_username.assert_called_once_with('testuser1')
