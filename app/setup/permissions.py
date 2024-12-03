from functools import wraps

from flask import abort
from flask_jwt_extended import get_jwt_identity

from app.modules.users.models import User
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


def role_or_owner_required(owner_check_function):
    def editor_required(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            if not user:
                abort(403, description="Access denied: user not found")

            if user.role in (UserRole.ADMIN.value, UserRole.EDITOR.value):
                return fn(*args, **kwargs)

            if owner_check_function(user_id, **kwargs):
                return fn(*args, **kwargs)
            abort(403, description="Access denied: insufficient permissions")

        return wrapper
