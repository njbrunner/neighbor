"""Endpoints for User database model."""

from flask import Blueprint, jsonify, request

from app.domain_logic import user_domain_logic
from app.schemas.user import user_schema

USER_BP = Blueprint('user_bp', __name__, url_prefix='/user')


@USER_BP.route('/signup', methods=["POST"])
def signup():
    user = user_domain_logic.signup(request.json)
    return user_schema.dump(user)


@USER_BP.route('/login', methods=["POST"])
def login():
    user = user_domain_logic.login(request.json)
    return user_schema.dump(user)


@USER_BP.route('/<user_id>', methods=['PATCH'])
def update_user_location(user_id: str):
    user = user_domain_logic.update_user_location(user_id, request.json)
    return user_schema.dump(user)


@USER_BP.route('/nearby/<user_id>', methods=['GET'])
def get_nearby_users(user_id: str):
    users = user_domain_logic.get_nearby_users(user_id)
    return jsonify([user_schema.dump(user) for user in users])
