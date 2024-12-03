from typing import Optional

from .models import Article, db
from .serializers import ArticleSerializer


class ArticleService:
    @staticmethod
    def create_article(dto: ArticleSerializer) -> Article:
        new_article = Article(
            id=dto.id,
            author_id=dto.author_id,
            title=dto.title,
            description=dto.description,
            body=dto.body,
        )
        db.session.add(new_article)
        db.session.commit()
        return new_article

    @staticmethod
    def get_all_articles():
        return Article.query.all()

    @staticmethod
    def get_article_by_id(article_id: int) -> Optional[Article]:
        return Article.query.get(article_id)

    @staticmethod
    def get_article_by_title(title) -> Optional[Article]:
        return Article.query.filter_by(title)

    @staticmethod
    def update_article(article_id: int, dto: ArticleSerializer) -> Article:
        article = Article.query.get(article_id)
        if not article:
            raise ValueError("Article not found")
        article.title = dto.title
        article.description = dto.description
        article.body = dto.body
        db.session.commit()
        return article

    @staticmethod
    def delete_article(article_id: int):
        article = Article.query.get(article_id)
        if not article:
            raise ValueError("Article not found")
        db.session.delete(article)
        db.session.commit()
