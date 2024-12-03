from flask import Flask

import pytest
from app.modules.articles.models import Article, db
from app.modules.articles.serializers import ArticleSerializer
from app.modules.articles.crud_services import ArticleService
from app.modules.users.models import User


@pytest.fixture(scope='module')
def app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
def valid_article_dto():
    return ArticleSerializer(id=1, author_id=1, title="Test Article", description="Test Description", body="Test Body")


@pytest.fixture
def existing_user():
    user = User(username="existinguser", email="existing@example.com", role="user", password="hashed_password")
    db.session.add(user)
    db.session.commit()
    return user


@pytest.fixture
def existing_article(existing_user):
    article = Article(author_id=existing_user.id, title="Existing Article", description="Existing Description", body="Existing Body")
    db.session.add(article)
    db.session.commit()
    return article


def test_create_article(client, valid_article_dto):
    article = ArticleService.create_article(valid_article_dto)
    assert article.title == valid_article_dto.title
    assert article.description == valid_article_dto.description
    assert article.body == valid_article_dto.body


def test_get_all_articles(client, valid_article_dto):
    articles = ArticleService.get_all_articles()
    assert len(articles) == 1
    assert articles[0].title == valid_article_dto.title


def test_get_article_by_id(client, valid_article_dto):
    article = ArticleService.get_article_by_id(valid_article_dto.id)
    assert article.id == valid_article_dto.id
    assert article.title == valid_article_dto.title


def test_get_article_by_title(client, valid_article_dto):
    article = ArticleService.get_article_by_title(valid_article_dto.title).first()
    assert article.title == valid_article_dto.title


def test_update_article(client, valid_article_dto):
    updated_dto = ArticleSerializer(id=valid_article_dto.id,
                                    author_id=valid_article_dto.author_id,
                                    title="Updated Title",
                                    description="Updated Description",
                                    body="Updated Body")
    updated_article = ArticleService.update_article(valid_article_dto.id, updated_dto)
    assert updated_article.title == "Updated Title"
    assert updated_article.description == "Updated Description"
    assert updated_article.body == "Updated Body"


def test_update_article_not_found(client):
    invalid_dto = ArticleSerializer(id=999, author_id=1, title="Nonexistent Article", description="None", body="None")
    with pytest.raises(ValueError):
        ArticleService.update_article(999, invalid_dto)


def test_delete_article(client, valid_article_dto):
    ArticleService.delete_article(valid_article_dto.id)
    article = ArticleService.get_article_by_id(valid_article_dto.id)
    assert article is None


def test_delete_article_not_found(client):
    with pytest.raises(ValueError):
        ArticleService.delete_article(999)
