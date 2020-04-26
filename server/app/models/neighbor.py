from datetime import datetime

from mongoengine import Document, fields

from app.models import Role

"""Define the model for a neighbor."""


class Neighbor(Document):
    """Neighbor database model which represents relationships with nearby peers."""

    seeker = fields.StringField(required=True)
    provider = fields.StringField(required=True)
    contact_channel_name = fields.StringField()
    last_contact = fields.DateField(default=datetime.now())
    distance = fields.FloatField(required=True)
    relationship_disabled = fields.BooleanField(default=False)
