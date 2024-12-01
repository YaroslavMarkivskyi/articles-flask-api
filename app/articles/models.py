from ..settings import db
from datetime import datetime

from sqlalchemy.orm import relationship


class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, db.Sequence('articles_id_seq'), primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    title = db.Column(db.String(255), nullable=False)
    # slug = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)

    # banner_image = db.Column(db.String(255), default="profile_default.png")

    # created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    author = relationship("User", backref="articles")
