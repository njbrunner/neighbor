"""Serialized schemas for User model."""

from flask_jwt_extended import create_access_token
from marshmallow import Schema, fields, post_load
from werkzeug.security import generate_password_hash

from app.models import User


class UserSchema(Schema):
    """Serialized user schema."""

    id = fields.UUID(dump_only=True)
    email = fields.Email(required=True)
    password = fields.Str(load_only=True, required=True)
    date_registered = fields.Date(dump_only=True)
    auth_token = fields.Str(dump_only=True)

    @post_load
    def create_user(self, data, **kwargs):
        """Create user after load."""
        user_data = {
            'email': data['email'],
            'hashed_password': generate_password_hash(data['password']),
            'auth_token': create_access_token(identity=data['email'])
        }
        return User(**user_data)


class LoginSchema(Schema):
    """Serialized login schema."""

    email = fields.Email(load_only=True, required=True)
    password = fields.Str(load_only=True, required=True)
