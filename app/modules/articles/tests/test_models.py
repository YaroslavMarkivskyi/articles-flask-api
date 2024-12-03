import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.modules.users.models import User
from app.setup.settings import db

from ..models import Article


@pytest.fixture(scope="module")
def test_engine():
    engine = create_engine("sqlite:///:memory:")
    db.metadata.create_all(engine)
    yield engine
    db.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def session(test_engine):
    Session = sessionmaker(bind=test_engine)
    session = Session()
    yield session
    session.rollback()
    session.close()


def test_create_article(session):
    user = User(
        username="testuser",
        email="test@example.com",
        role="admin",
        password="hashed_password",
    )
    session.add(user)
    session.commit()

    article = Article(
        author_id=user.id,
        title="Test Article",
        description="This is a test description",
        body="This is the body of the test article",
    )
    session.add(article)
    session.commit()

    saved_article = (
        session.query(Article).filter_by(title="Test Article").first()
    )
    assert saved_article is not None
    assert saved_article.title == "Test Article"
    assert saved_article.author.username == "testuser"


def test_update_article(session):
    user = User(
        username="testuser2",
        email="test2@example.com",
        role="admin",
        password="hashed_password",
    )
    session.add(user)
    session.commit()

    article = Article(
        author_id=user.id,
        title="Test Article",
        description="This is a test description",
        body="This is the body of the test article",
    )
    session.add(article)
    session.commit()

    article.title = "Updated Test Article"
    session.commit()

    updated_article = (
        session.query(Article).filter_by(title="Updated Test Article").first()
    )
    assert updated_article is not None
    assert updated_article.title == "Updated Test Article"


def test_delete_article(session):
    # Створення користувача
    user = User(
        username="testuser3",
        email="test3@example.com",
        role="admin",
        password="hashed_password",
    )
    session.add(user)
    session.commit()

    # Створення статті
    article = Article(
        author_id=user.id,
        title="Delete Article",
        description="This is a test description",
        body="This is the body of the test article",
    )
    session.add(article)
    session.commit()

    session.delete(article)
    session.commit()

    deleted_article = (
        session.query(Article).filter_by(title="Delete Article").first()
    )
    assert deleted_article is None


def test_article_relationship(session):
    user = User(
        username="testuser4",
        email="test4@example.com",
        role="admin",
        password="hashed_password",
    )
    session.add(user)
    session.commit()

    article = Article(
        author_id=user.id,
        title="Test Article",
        description="This is a test description",
        body="This is the body of the test article",
    )
    session.add(article)
    session.commit()

    saved_article = (
        session.query(Article).filter_by(title="Test Article").first()
    )
    assert saved_article is not None
    assert saved_article.author.username == "testuser"
