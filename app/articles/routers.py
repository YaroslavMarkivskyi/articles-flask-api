from flask import request, jsonify, abort
from http import HTTPStatus
from flask import Blueprint
from flask_jwt_extended import jwt_required

from .crud_services import ArticleService
from .serializers import ArticleSerializer

articles_bp = Blueprint('articles', __name__, url_prefix='/articles')

@articles_bp.route('/', methods=['POST'])
@jwt_required()
def get_articles():
    entity_articles = ArticleService.get_all_articles()
    json_articles = [ArticleSerializer.from_entity(article) for article in entity_articles]
    return jsonify({"articles": json_articles}), HTTPStatus.OK


@articles_bp.route("/<int:article_id>", methods=["GET"])
@jwt_required()
def get_article(article_id):
    entity_article = ArticleService.get_article_by_id(article_id)
    if entity_article is None:
        abort(HTTPStatus.NOT_FOUND, description="Article not found")
    json_article = ArticleSerializer.from_entity(entity_article)
    return jsonify(json_article), HTTPStatus.OK


@articles_bp.route("/", methods=["POST"])
@jwt_required()
def add_article():
    data = request.json
    dto_article = ArticleSerializer.from_dict(data)
    entity_article = ArticleService.create_article(dto_article)
    json_article = ArticleSerializer.from_entity(entity_article)
    return jsonify(json_article), HTTPStatus.CREATED


@articles_bp.route("/<int:article_id>", methods=["PUT"])
@jwt_required()
def update_article(article_id):
    data = request.json
    dto_article = ArticleSerializer.from_dict(data)
    entity_article = ArticleService.update_article(article_id, dto_article)
    json_article = ArticleSerializer.from_entity(entity_article)
    return jsonify(json_article), HTTPStatus.OK


@articles_bp.route("/<int:article_id>", methods=["DELETE"])
@jwt_required()
def delete_article(article_id):
    ArticleService.delete_article(article_id)
    return jsonify({"message": "Book deleted successfully"}), HTTPStatus.OK