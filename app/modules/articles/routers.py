from http import HTTPMethod, HTTPStatus

from flasgger import swag_from
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from .crud_services import ArticleService
from .permissions import admin_required, editor_required
from .serializers import ArticleSerializer
from .validators import ArticleValidator

articles_bp = Blueprint("articles", __name__, url_prefix="/articles")


@articles_bp.route("/", methods=[HTTPMethod.GET])
@jwt_required()
@swag_from("./swagger.yml")
def get_articles():
    entity_articles = ArticleService.get_all_articles()
    json_articles = [
        ArticleSerializer.to_dict(article) for article in entity_articles
    ]
    return jsonify({"articles": json_articles}), HTTPStatus.OK


@articles_bp.route("/<int:article_id>", methods=[HTTPMethod.GET])
@jwt_required()
@swag_from("./swagger.yml")
def get_article(article_id):
    entity_article = ArticleService.get_article_by_id(article_id)
    ArticleValidator.is_exist_article(entity_article)
    json_article = ArticleSerializer.to_dict(entity_article)
    return jsonify(json_article), HTTPStatus.OK


@articles_bp.route("/search", methods=[HTTPMethod.GET])
@jwt_required()
@swag_from("./swagger.yml")
def get_article_by_title():
    title = request.args.get("title")
    entity_article = ArticleService.get_article_by_title(title)
    ArticleValidator.is_exist_article(entity_article)
    json_article = ArticleSerializer.to_dict(entity_article)
    return jsonify(json_article), HTTPStatus.OK


@articles_bp.route("/", methods=[HTTPMethod.POST])
@jwt_required()
@swag_from("./swagger.yml")
def add_article():
    data = request.json
    ArticleValidator.is_exist_fields(data)
    dto_article = ArticleSerializer.from_dict(data)
    entity_article = ArticleService.create_article(dto_article)
    json_article = ArticleSerializer.to_dict(entity_article)
    return jsonify(json_article), HTTPStatus.CREATED


@articles_bp.route("/<int:article_id>", methods=[HTTPMethod.PUT])
@jwt_required()
@editor_required
@swag_from("./swagger.yml")
def update_article(article_id):
    data = request.json
    ArticleValidator.is_exist_fields(data)

    dto_article = ArticleSerializer.from_dict(data)
    ArticleValidator.is_exist_article(dto_article)

    entity_article = ArticleService.update_article(article_id, dto_article)
    json_article = ArticleSerializer.to_dict(entity_article)
    return jsonify(json_article), HTTPStatus.OK


@articles_bp.route("/<int:article_id>", methods=[HTTPMethod.DELETE])
@jwt_required()
@admin_required
@swag_from("./swagger.yml")
def delete_article(article_id):
    entity_article = ArticleService.get_article_by_id(article_id)
    ArticleValidator.is_exist_article(entity_article)
    ArticleService.delete_article(article_id)
    return jsonify({"message": "Article deleted successfully"}), HTTPStatus.OK
