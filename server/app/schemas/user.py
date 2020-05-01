"""Serialized schemas for User model."""

from marshmallow import Schema, fields

from app.schemas import RoleSchema


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
    twilio_token = fields.String(dump_only=True)
    role = fields.Nested(RoleSchema, required=True)
    location_identified = fields.Boolean(dump_only=True)


user_schema = UserSchema()


class LoginSchema(Schema):
    """Serialized login schema."""

    email = fields.Email(load_only=True, required=True)
    password = fields.String(load_only=True, required=True)


login_schema = LoginSchema()
