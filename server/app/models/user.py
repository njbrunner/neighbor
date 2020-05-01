from datetime import datetime

from mongoengine import Document, fields

from app.models import Role

"""Define the model for a user."""


class User(Document):
    """User database model."""

    id = fields.ObjectId()
    email = fields.EmailField(unique=True, required=True)
    name = fields.StringField(required=True)
    hashed_password = fields.StringField(required=True)
    twilio_token = fields.StringField(unique=True, required=False)
    role = fields.ReferenceField(Role, required=True)
    location = fields.PointField()
    location_identified = fields.BooleanField(default=False, required=True)
    date_registered = fields.DateField(default=datetime.now())
    email_verified = fields.BooleanField(default=False)
    neighbors = fields.ListField(fields.ReferenceField('self'))
    blacklisted_neighbors = fields.ListField(fields.ReferenceField('self'))
