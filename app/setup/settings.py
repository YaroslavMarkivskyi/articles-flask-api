from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_jwt_extended import JWTManager
from flask_cors import CORS


app = Flask(__name__)

db_user = os.getenv("DB_USER", "")
db_pass = os.getenv("DB_PASS", "")
db_host = os.getenv("DB_HOST", "")
db_port = os.getenv("DB_PORT", "")
db_name = os.getenv("DB_NAME", "")


DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY", "")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "default_secret")

jwt = JWTManager(app)
db = SQLAlchemy(app)
CORS(app)
