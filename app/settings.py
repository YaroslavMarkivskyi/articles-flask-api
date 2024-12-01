from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

db_user = os.getenv("DB_USER", "")
db_pass = os.getenv("DB_PASS", "")
db_host = os.getenv("DB_HOST", "")
db_port = os.getenv("DB_PORT", "")
db_name = os.getenv("DB_NAME", "")


DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config['SECRET_KEY'] = os.getenv("APP_SECRET_KEY", "")

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()
