from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import abort
from app.modules.auth.models import User
from .crud_services import ArticleService
from app.utils import UserRole


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
        article_id = kwargs.get("article_id")
        user_roles = (UserRole.ADMIN.value, UserRole.EDITOR.value)
        author_id = ArticleService.get_article_by_id(article_id).author_id
        if not user or user.role not in user_roles or author_id != user_id:
            abort(403, description="Editor access required")
        return fn(*args, **kwargs)
    return wrapper
