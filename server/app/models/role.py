"""Define the model for a role."""

from mongoengine import Document, fields


class Role(Document):
    """User database model."""

    value = fields.StringField(required=True, unique=True)
    label = fields.StringField(required=True)
