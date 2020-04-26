"""Serialized schema for Neighbor model."""
from datetime import datetime
from marshmallow import Schema, fields, post_load

from app.domain_logic import neighbor_domain_logic
from app.models import Neighbor


class NeighborSchema(Schema):
    """Serialized neighbor schema."""

    seeker = fields.String(required=True)
    provider = fields.String(required=True)
    contact_channel_name = fields.String(dump_only=True)
    last_contact = fields.DateTime()
    distance = fields.Float(dump_only=True)
    relationship_disabled = fields.Boolean(dump_only=True)


    @post_load
    def create_user(self, data, **kwargs):
        """Create user after load."""
        contact_channel_name = 'asdf'
        distance = neighbor_domain_logic.get_neighbor_distance(data['seeker'], data['provider'])
        neighbor_data = {
            'seeker': data['seeker'],
            'provider': data['provider'],
            'contact_channel_name': contact_channel_name,
            'last_contact': datetime.utcnow(),
            'distance': 0,
            'relationship_disabled': False
        }
        return Neighbor(**neighbor_data)

neighbor_schema = NeighborSchema()