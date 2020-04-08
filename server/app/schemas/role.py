"""Serialized schema for Role model."""

from marshmallow import Schema, fields, post_load

from app.domain_logic import role_domain_logic


class RoleSchema(Schema):
    """Serialized role schema."""

    id = fields.String(required=True)
    value = fields.String(dump_only=True)
    label = fields.String(dump_only=True)

    @post_load
    def fetch_role(self, data, **kwargs):
        """Fetch role after load."""
        return role_domain_logic.get_role(data['id'])
