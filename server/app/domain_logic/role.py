"""Data access layer for Role model."""

from app.models import Role


def get_role(role_id: str) -> Role:
    """Get role from database."""
    return Role.objects.get(id=role_id)
