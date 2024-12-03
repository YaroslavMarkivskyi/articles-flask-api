from functools import wraps

from flask import abort
from flask_jwt_extended import get_jwt_identity

from app.modules.users.models import User
from app.setup.utils import UserRole

from .crud_services import ArticleService


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user or user.role != UserRole.ADMIN.value:
            abort(403, description="Admin access required")
        return fn(*args, **kwargs)

    return wrapper


def editor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if not user:
            abort(403, description="Access denied: user not found")

        if user.role in (UserRole.ADMIN.value, UserRole.EDITOR.value):
            return fn(*args, **kwargs)

        article_id = kwargs.get("article_id")
        author_id = ArticleService.get_article_by_id(article_id).author_id
        if author_id != user_id:
            return fn(*args, **kwargs)
        abort(403, description="Access denied: user not found")

    return wrapper
