"""Provides token management functionality."""
from flask_jwt_extended import (
    create_access_token, create_refresh_token, JWTManager
)

from app.models import User
from app.domain_logic import user_domain_logic


def create_token(user: User):
    """Generates a fresh JWT token."""
    return create_access_token(identity=str(user.id))


def create_token_for_refresh(user: User):
    """Generates a fresh JWT refresh token."""
    return create_refresh_token(identity=str(user.id))
