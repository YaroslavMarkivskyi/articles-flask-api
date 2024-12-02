import click
from flask.cli import with_appcontext
from ..settings import db
from ..auth.models import User  # Імпортуйте всі моделі
from ..articles.models import Article  # Інші моделі

def initialize_database():
    """Функція для створення таблиць у базі даних."""
    try:
        db.create_all()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")



@click.command("init-db")
@with_appcontext
def init_db_command():
    """Ініціалізує базу даних."""
    initialize_database()
