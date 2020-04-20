"""This module provides edge case testing of calcululate_nearby_positions['"""

import pytest

import app.domain_logic.user as user_domain_logic
from app.models.role import Role
from app.models.user import User

@pytest.fixture
def user():
    user = User(
        email = 'email@email.com', 
        hashed_password = '1234567890ABCDEF',
        email_verified = True,
        role = Role(value='helper', label='Giver of help'),
        latitude = 0,
        longitude = 0
        )
    yield user

def test___calculate_nearby_positions_normal(user):
    positions = user_domain_logic.__calculate_nearby_positions(user)
    assert positions['use_latitude'] == True
    assert positions['latitude_minimum'] == -5
    assert positions['longitude_minimum'] == -5
    assert positions['latitude_maximum'] == 5
    assert positions['longitude_maximum'] == 5


def test___calculate_nearby_positions_latitude_overflow(user):
    user.latitude = 179
    positions = user_domain_logic.__calculate_nearby_positions(user)
    assert positions['use_latitude'] == True
    assert positions['latitude_minimum'] == 174
    assert positions['longitude_minimum'] == -5
    assert positions['latitude_maximum'] == -176
    assert positions['longitude_maximum'] == 5

    user.latitude = -179
    positions = user_domain_logic.__calculate_nearby_positions(user)
    assert positions['use_latitude'] == True
    assert positions['latitude_minimum'] == 176
    assert positions['longitude_minimum'] == -5
    assert positions['latitude_maximum'] == -174
    assert positions['longitude_maximum'] == 5
    

def test___calculate_nearby_positions_longitude_overflow(user):
    user.longitude = 89
    positions = user_domain_logic.__calculate_nearby_positions(user)
    assert positions['use_latitude'] == False
    assert positions['latitude_minimum'] == -5
    assert positions['longitude_minimum'] == 84
    assert positions['latitude_maximum'] == 5
    assert positions['longitude_maximum'] == 90

    user.longitude = -89
    positions = user_domain_logic.__calculate_nearby_positions(user)
    assert positions['use_latitude'] == False
    assert positions['latitude_minimum'] == -5
    assert positions['longitude_minimum'] == -90
    assert positions['latitude_maximum'] == 5
    assert positions['longitude_maximum'] == -84