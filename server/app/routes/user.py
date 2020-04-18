"""Endpoints for User database model."""

from flask import Blueprint, request

from app.domain_logic import user_domain_logic
from app.schemas.user import UserSchema

USER_BP = Blueprint('user_bp', __name__, url_prefix='/user')


@USER_BP.route('/signup', methods=["POST"])
def signup():
    user = user_domain_logic.signup(request.json)
    return UserSchema().dump(user)


@USER_BP.route('/login', methods=["POST"])
def login():
    user = user_domain_logic.login(request.json)
    return UserSchema().dump(user)


@USER_BP.route('/<user_id>', methods=['PATCH'])
def update_user_location(user_id: str):
    user = user_domain_logic.update_user_location(user_id, request.json)
    return UserSchema().dump(user)
