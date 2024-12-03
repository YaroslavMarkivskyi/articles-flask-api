from http import HTTPStatus

from flask import abort

from .models import Article


class ArticleValidator:
    @staticmethod
    def is_exist_article(article):
        if article is None:
            abort(HTTPStatus.NOT_FOUND, description="User not found")

    @staticmethod
    def is_exist_fields(data: dict):
        if not data:
            abort(HTTPStatus.BAD_REQUEST, description="Body is empty!")
        if (
            "author_id" not in data
            or "title" not in data
            or "description" not in data
            or "body" not in data
        ):
            abort(
                HTTPStatus.BAD_REQUEST,
                description="Missing data for required fields",
            )

    @staticmethod
    def is_article_owner(user_id, **kwargs):
        article = Article.query.get(kwargs.get("article_id"))
        if article is None:
            abort(HTTPStatus.NOT_FOUND, description="User not found")
        return article.author_id == user_id
