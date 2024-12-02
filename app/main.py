from .settings import app
from .auth import auth_bp
from .articles import articles_bp
from .commands.create_user import create_user
from .commands.init_database import init_db_command


app.register_blueprint(auth_bp)
app.register_blueprint(articles_bp)

# with app.app_context():
#     db.create_all()




app.cli.add_command(create_user)
app.cli.add_command(init_db_command)


if __name__ == '__main__':
    app.run()
