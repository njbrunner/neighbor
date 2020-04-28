"""Tests functionality around neighbor relationship interactions."""

from datetime import datetime
import json
import pytest


def test_create_neighbor(seeker, provider, login, client):
    """Should return user 2."""
    response = client.post(
        f'neighbor/',
        {
            'seeker': seeker.unique_identity,
            'provider': provider.unique_identity,
            'contaact_channel_name': seeker.unique_identity + provider.unique_identity,
            'last_contact': datetime.utcnow(),
            'distance': 12.2
        }
    )

    response_json = json.loads(response.data)
    assert(len(response_json) == 1)
