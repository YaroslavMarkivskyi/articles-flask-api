import click
from flask.cli import with_appcontext

from app.modules.articles.models import Article  # noqa: F401
from app.modules.users.models import User  # noqa: F401

from ..setup.settings import db


def initialize_database():
    try:
        db.create_all()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")


@click.command("init-db")
@with_appcontext
def init_db_command():
    initialize_database()
