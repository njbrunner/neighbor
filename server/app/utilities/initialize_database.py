"""Initialize database with pre-defined data."""

from typing import Dict
from app.models import Role
from mongoengine import DoesNotExist

default_roles = [
    {"value": "provider", "label": "I can provide help"},
    {"value": "seeker", "label": "I am seeking help"}
]


def create_default_roles():
    """Add pre-defined roles to database."""
    for role in default_roles:
        if not role_exists(role):
            new_role = Role(
                value=role['value'],
                label=role['label']
            )
            new_role.save()


def role_exists(role: Dict[str, str]) -> bool:
    """Check if role exists in database."""
    try:
        if Role.objects.get(value=role['value']):
            return True
    except DoesNotExist:
        return False
