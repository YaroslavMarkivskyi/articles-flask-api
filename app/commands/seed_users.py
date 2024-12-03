from app.setup.settings import db
from faker import Faker
import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

from app.modules.users.models import User
from app.setup.utils import UserRole

fake = Faker()


@click.command('seed-users')
@click.option('--admin_count', default=2, type=int, help='Number of users to create')
@click.option('--editor_count', default=5, type=int, help='Number of users to create')
@click.option('--viewer_count', default=10, type=int, help='Number of users to create')
@click.option('--password', prompt='Password', hide_input=True, confirmation_prompt=True, help='The password for the new user.')
@with_appcontext
def seed_users(admin_count, editor_count, viewer_count, password):
    create_users(UserRole.ADMIN.value, admin_count, password)
    create_users(UserRole.EDITOR.value, editor_count, password)
    create_users(UserRole.VIEWER.value, viewer_count, password)


def create_users(role, count, password):
    hashed_password = generate_password_hash(password)

    for _ in range(count):
        username, email = generate_unique_user()
        new_user = User(username=username, email=email, role=role, password=hashed_password)
        try:
            db.session.add(new_user)
            db.session.commit()
            click.echo(f'User {username} with role {role} created successfully.')
        except Exception as e:
            click.echo(f'Error creating user: {e}')


def generate_unique_user():
    username = fake.user_name()
    email = fake.email()
    while User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        username = fake.user_name()
        email = fake.email()
    return username, email
