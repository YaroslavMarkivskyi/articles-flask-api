from .setup.settings import app
from .modules.users import users_bp
from .modules.articles import articles_bp
from .commands.create_user import create_user
from .commands.init_database import init_db_command

from flasgger import Swagger

app.register_blueprint(users_bp)
app.register_blueprint(articles_bp)


app.cli.add_command(create_user)
app.cli.add_command(init_db_command)


swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,  # Include all endpoints
            "model_filter": lambda tag: True,  # Include all models
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/",
}
swagger = Swagger(app, config=swagger_config)


if __name__ == '__main__':
    app.run()
