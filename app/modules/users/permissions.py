from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import abort
from app.modules.users.models import User
from .crud_services import UserService
from app.setup.utils import UserRole


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

        user_model_id = kwargs.get("user_id")
        user_model_id = UserService.get_user_by_id(user_model_id).id
        if user_model_id != user_id:
            return fn(*args, **kwargs)
        abort(403, description="Access denied: user not found")
    return wrapper
