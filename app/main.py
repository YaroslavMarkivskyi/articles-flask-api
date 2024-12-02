from .setup.settings import app
from .modules.auth import auth_bp
from .modules.articles import articles_bp
from .commands.create_user import create_user
from .commands.init_database import init_db_command


app.register_blueprint(auth_bp)
app.register_blueprint(articles_bp)


app.cli.add_command(create_user)
app.cli.add_command(init_db_command)


if __name__ == '__main__':
    app.run()
