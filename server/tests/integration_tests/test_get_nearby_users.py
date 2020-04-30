"""This module provides edge case testing of calcululate_nearby_positions['"""

import json

import app.domain_logic.user as user_domain_logic
from app.models.role import Role
from app.models.user import User


def test_get_potential_neighbors(user, user2, user3, login, client):
    """Should return user 2."""
    response = client.get(
        f'user/nearby/{user.id}'
    )

    response_json = json.loads(response.data)
    assert(len(response_json) == 1)


def test_get_potential_neighbors_no_results(user, user2, user3, user4, login, client):
    """Should not return results (user 4 is also a provider and should not be returned)."""
    response = client.get(
        f'user/nearby/{user3.id}'
    )

    response_json = json.loads(response.data)
    assert(len(response_json) == 0)
