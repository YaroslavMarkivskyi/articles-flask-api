from app.setup.settings import db

# from app.utils import UserRole


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(
        db.Integer,
        db.Sequence("user_id_seq"),
        primary_key=True,
        autoincrement=True,
    )
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    role = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(255), nullable=False)
