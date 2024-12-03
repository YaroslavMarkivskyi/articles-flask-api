import os

from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from .swagger_config import swagger_info

app = Flask(__name__)

db_user = os.getenv("DB_USER", "")
db_pass = os.getenv("DB_PASS", "")
db_host = os.getenv("DB_HOST", "")
db_port = os.getenv("DB_PORT", "")
db_name = os.getenv("DB_NAME", "")


DB_URL = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY", "")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "default_secret")

jwt = JWTManager(app)
db = SQLAlchemy(app)
CORS(app)

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

swagger = Swagger(app, config=swagger_config, template=swagger_info)
