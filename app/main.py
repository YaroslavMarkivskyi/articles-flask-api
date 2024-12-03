from .commands.create_user import create_user
from .commands.init_database import init_db_command
from .commands.seed_articles import seed_articles
from .commands.seed_users import seed_users
from .modules.articles import articles_bp
from .modules.users import users_bp
from .setup.settings import app


app.register_blueprint(users_bp)
app.register_blueprint(articles_bp)


app.cli.add_command(create_user)
app.cli.add_command(init_db_command)
app.cli.add_command(seed_users)
app.cli.add_command(seed_articles)


if __name__ == "__main__":
    app.run()
