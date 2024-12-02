from .settings import app, db
from .auth import auth_bp
from .articles import articles_bp
from .auth.models import User
from .articles.models import Article


app.register_blueprint(auth_bp)
app.register_blueprint(articles_bp)

with app.app_context():
    db.create_all()

import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

from .utils import UserRole
@click.command('create-user')
@click.option('--username', prompt='Username', help='The username for the new user.')
@click.option('--email', prompt='Email', help='The email for the new user.')
@click.option('--role', prompt='Role', type=click.Choice([role.value for role in UserRole]), help='The role for the new user.')
@click.option('--password', prompt='Password', hide_input=True, confirmation_prompt=True, help='The password for the new user.')
@with_appcontext
def create_user(username, email, role, password):
    """Creates a new user with a specified role."""
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        click.echo('User with this username or email already exists.')
        return

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, role=role, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        click.echo(f'User {username} with role {role} created successfully.')
    except Exception as e:
        click.echo(f'Error creating user: {e}')


app.cli.add_command(create_user)





if __name__ == '__main__':
    app.run()
