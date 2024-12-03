# import pytest
# from flask import Flask
# from http import HTTPStatus
# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import JWTManager

# from app.modules.articles import articles_bp  # Імпортуйте ваш Blueprint
# from app.setup.settings import db  # База даних для тестів
# from ..models import Article  # Модель статті
# from ..serializers import ArticleSerializer

# @pytest.fixture
# def app():
#     """Налаштування тестового додатку."""
#     app = Flask(__name__)
#     app.config["TESTING"] = True
#     app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # SQLite для тестів
#     app.config["JWT_SECRET_KEY"] = "test_jwt_secret"
#     db.init_app(app)
#     app.register_blueprint(articles_bp)
#     jwt = JWTManager(app)
#     with app.app_context():
#         db.create_all()
#         yield app
#         db.drop_all()


# @pytest.fixture
# def client(app):
#     """Тестовий клієнт Flask."""
#     return app.test_client()


# @pytest.fixture
# def token(app):
#     """JWT-токен для аутентифікації."""
#     with app.app_context():
#         access_token = create_access_token(identity=str(1))
#         return {"Authorization": f"Bearer {access_token}"}


# def test_get_articles(client, token):
#     # Попереднє створення статей у базі
#     article = Article(
#         author_id=1,
#         title="Test Article",
#         description="Test Description",
#         body="Test body"
#         )
#     db.session.add(article)
#     db.session.commit()

#     response = client.get("/articles/", headers=token)
#     assert response.status_code == HTTPStatus.OK
#     assert "articles" in response.json
#     assert len(response.json["articles"]) == 1


# def test_get_article(client, token):
#     """Тест отримання однієї статті за ID."""
#     article = Article(
#         author_id=1,
#         title="Single Article",
#         description="Test Description",
#         body="Test body"
#         )
#     db.session.add(article)
#     db.session.commit()

#     response = client.get(f"/articles/{article.id}", headers=token)
#     json_article = ArticleSerializer.to_dict(article)
#     assert response.status_code == HTTPStatus.OK
#     assert response.json["title"] == json_article['title']


# def test_add_article(client, token):
#     """Тест створення нової статті."""
#     new_article = Article(
#         author_id=1,
#         title="New Article",
#         description="Test Description",
#         body="Test body"
#         )
#     json_article = ArticleSerializer.to_dict(new_article)
#     response = client.post("/articles/", json=json_article, headers=token)
#     assert response.status_code == HTTPStatus.CREATED
#     assert response.json["title"] == json_article["title"]


# def test_update_article(client, token):
#     """Тест оновлення статті."""
#     article = Article(
#         author_id=1,
#         title="Old Article",
#         description="Test Description",
#         body="Test body"
#         )
#     db.session.add(article)
#     db.session.commit()
#     updated_data = {"title": "Updated Title", "content": "Updated Content"}
#     json_article = ArticleSerializer.to_dict(article)
#     response = client.put(f"/articles/{article.id}", json=json_article, headers=token)
#     assert response.status_code == HTTPStatus.OK
#     assert response.json["title"] == updated_data["title"]


# # def test_delete_article(client, token):
# #     """Тест видалення статті."""
# #     article = Article(title="To Be Deleted", content="Delete Me")
# #     db.session.add(article)
# #     db.session.commit()

# #     response = client.delete(f"/articles/{article.id}", headers=token)
# #     assert response.status_code == HTTPStatus.OK
# #     assert response.json["message"] == "Article deleted successfully"
