from flask import abort
from .models import Article
from http import HTTPStatus


class ArticleValidator:
    @staticmethod
    def is_exist_article(article):
        if article is None:
            abort(HTTPStatus.NOT_FOUND, description="Article not found")

    @staticmethod
    def is_exist_fields(data: dict):
        if not data:
            abort(HTTPStatus.BAD_REQUEST, description="Body is empty!")
        if (
            'author_id' not in data or
            'title' not in data or
            'description' not in data or
            'body' not in data
        ):
            abort(HTTPStatus.BAD_REQUEST, description="Missing data for required fields")
