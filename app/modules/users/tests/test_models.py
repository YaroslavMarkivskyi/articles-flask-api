import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.setup.settings import db

from ..models import User


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


def test_create_user(session):
    user = User(
        username="testuser",
        email="test@example.com",
        role="admin",
        password="hashed_password",
    )
    session.add(user)
    session.commit()

    saved_user = session.query(User).filter_by(username="testuser").first()
    assert saved_user is not None
    assert saved_user.email == "test@example.com"
    assert saved_user.role == "admin"


def test_unique_constraints(session):
    user1 = User(
        username="user1",
        email="duplicate@example.com",
        role="admin",
        password="hashed_password",
    )
    user2 = User(
        username="user2",
        email="duplicate@example.com",
        role="viewer",
        password="hashed_password",
    )

    session.add(user1)
    session.commit()

    session.add(user2)
    with pytest.raises(Exception):  # SQLAlchemy має викликати помилку
        session.commit()


def test_update_user(session):
    user = User(
        username="testuser1",
        email="test1@example.com",
        role="admin",
        password="hashed_password",
    )
    session.add(user)
    session.commit()

    user.role = "user"
    session.commit()

    updated_user = session.query(User).filter_by(username="testuser1").first()
    assert updated_user.role == "user"


def test_delete_user(session):
    user = User(
        username="testuse2",
        email="test2@example.com",
        role="admin",
        password="hashed_password",
    )
    session.add(user)
    session.commit()

    session.delete(user)
    session.commit()

    deleted_user = session.query(User).filter_by(username="testuser2").first()
    assert deleted_user is None
