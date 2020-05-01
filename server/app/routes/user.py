"""Endpoints for User database model."""

from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    fresh_jwt_required, jwt_required
)
from http import HTTPStatus

from app.domain_logic import user_domain_logic
from app.schemas.user import user_schema, login_schema
from app.utilities import create_token, create_token_for_refresh

USER_BP = Blueprint('user_bp', __name__, url_prefix='/user')


@USER_BP.route('/signup', methods=["POST"])
def signup():
    user_data = user_schema.load(request.json)
    user = user_domain_logic.signup(user_data)
    access_token = create_token(user)
    refresh_token = create_token_for_refresh(user)
    return jsonify(token=access_token, refresh=refresh_token, user=user_schema.dump(user))


@USER_BP.route('/login', methods=["POST"])
def login():
    user_data = login_schema.load(request.json)
    user = user_domain_logic.login(user_data)
    access_token = create_token(user)
    refresh_token = create_token_for_refresh(user)
    return jsonify(token=access_token, refresh=refresh_token, user=user_schema.dump(user))


@jwt_required
@USER_BP.route('/', methods=['PATCH'])
def update_user_location():
    user = user_domain_logic.update_user_location(request.json)
    return user_schema.dump(user)


@jwt_required
@USER_BP.route('/nearby/', methods=['GET'])
def get_potential_neighbors():
    users = user_domain_logic.get_potential_neighbors()
    return jsonify([user_schema.dump(user) for user in users])


@USER_BP.route('/neighbors/', methods=['GET'])
def get_neighbors():
    users = user_domain_logic.get_neighbors()
    return jsonify([user_schema.dump(user) for user in users])


@USER_BP.route('/add_neighbor/', methods=['PUT'])
def add_neighbor():
    neighbor_id = request.json['neighbor_id']
    user_domain_logic.add_neighbor(neighbor_id)
    return "Updated successfully.", HTTPStatus.NO_CONTENT


@USER_BP.route('/remove_neighbor/', methods=['PUT'])
def remove_neighbor():
    neighbor_id = request.json['neighbor_id']
    user_domain_logic.black_list_neighbor(neighbor_id)
    return "Updated successfully.", HTTPStatus.NO_CONTENT
