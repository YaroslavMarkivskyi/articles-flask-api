from flask import Blueprint, request

auth_bp = Blueprint('auth_blueprint', __name__)

@auth_bp.route('/login', methods=["POST"])
def login():
    data = request.get_json()

@example_blueprint.route('/profile')
def profile():
    return "This is an example app"


@example_blueprint.route('/logout')
def logout():
    return "This is an example app"