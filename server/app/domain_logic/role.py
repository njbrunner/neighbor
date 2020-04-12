"""Data access layer for Role model."""

from typing import List

from app.models import Role


def get_role(role_id: str) -> Role:
    """Get role from database."""
    return Role.objects.get(id=role_id)


def get_roles() -> List[Role]:
    """Get roles from the database."""
    return Role.objects
