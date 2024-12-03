from sqlalchemy.orm import relationship

from app.setup.settings import db


class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(
        db.Integer,
        db.Sequence("articles_id_seq"),
        primary_key=True,
        autoincrement=True,
    )
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"),
                          nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = relationship("User", backref="articles")
