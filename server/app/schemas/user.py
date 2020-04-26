"""Serialized schemas for User model."""
import uuid

from marshmallow import Schema, fields, post_load
from werkzeug.security import generate_password_hash

from app.models import User
from app.schemas import RoleSchema
from app.utilities import generate_access_token


class UserSchema(Schema):
    """Serialized user schema."""

    name = fields.String(required=True)
    email = fields.Email(required=True)
    role = fields.Nested(RoleSchema, required=True)

    # load only
    password = fields.String(load_only=True, required=True)

    # dump only
    id = fields.String(dump_only=True)
    date_registered = fields.Date(dump_only=True)
    auth_token = fields.String(dump_only=True)
    unique_identity = fields.String(dump_only=True)

    @post_load
    def create_user(self, data, **kwargs):
        """Create user after load."""
        unique_identity = str(uuid.uuid4())
        token = generate_access_token(identity=unique_identity)
        user_data = {
            'unique_identity': unique_identity,
            'name': data['name'],
            'email': data['email'],
            'role': data['role'],
            'hashed_password': generate_password_hash(data['password']),
            'auth_token': token
        }
        return User(**user_data)


user_schema = UserSchema()


class LoginSchema(Schema):
    """Serialized login schema."""

    email = fields.Email(load_only=True, required=True)
    password = fields.String(load_only=True, required=True)


login_schema = LoginSchema()
