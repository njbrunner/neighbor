"""Provides token management functionality."""

from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    create_access_token, get_jwt_identity, fresh_jwt_required, jwt_refresh_token_required, jwt_required
)
from http import HTTPStatus

from app.models import User
from app.domain_logic import user_domain_logic

MAIN_BP = Blueprint('main_bp', __name__, url_prefix='/')


@jwt_refresh_token_required
@MAIN_BP.route('/refresh-token', methods=['GET'])
def refresh_token(self):
    """Generates a new JWT token to replace an expiring token."""
    user_id = get_jwt_identity()
    # return a non-fresh token for the user
    new_token = create_access_token(identity=user_id, fresh=False)
    return {'access_token': new_token}, HTTPStatus.OK


@MAIN_BP.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), HTTPStatus.OK
