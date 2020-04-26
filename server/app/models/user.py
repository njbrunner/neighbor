from datetime import datetime

from mongoengine import Document, fields

from app.models import Role

"""Define the model for a user."""


class User(Document):
    """User database model."""

    # required
    email = fields.EmailField(unique=True, required=True)
    name = fields.StringField(required=True)
    unique_identity = fields.StringField(unique=True, required=True)
    hashed_password = fields.StringField(required=True)
    auth_token = fields.StringField(unique=True, required=False)
    role = fields.ReferenceField(Role, required=True)

    date_registered = fields.DateField(default=datetime.now())
    email_verified = fields.BooleanField(default=False)
    latitude = fields.FloatField()
    longitude = fields.FloatField()
