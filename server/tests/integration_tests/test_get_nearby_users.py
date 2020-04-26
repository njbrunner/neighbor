"""This module provides edge case testing of calcululate_nearby_positions['"""

from flask import url_for
from flask.testing import FlaskClient
from mongoengine import GeoJsonBaseField
import pytest
from werkzeug.security import generate_password_hash

import app.domain_logic.user as user_domain_logic
from app.models.role import Role
from app.models.user import User

USER_PASSWORD = 'password'

@pytest.fixture
def provider():
    role = Role.objects.get(value='provider')
    yield role

@pytest.fixture
def seeker():
    role = Role.objects.get(value='seeker')
    yield role

@pytest.fixture
def user(seeker):
    email = 'email@email.com'
    user = User.objects(email=email)
    if (user):
        user.delete()

    latitude = -89.999
    longitude = -179.001
    user = User(
        email = email, 
        hashed_password = generate_password_hash(USER_PASSWORD),
        email_verified = True,
        auth_token = email,
        role = seeker,
        location = {'type': 'Point', 'coordinates': [longitude, latitude]}
        )
    user.save()
    yield user
    user.delete()

@pytest.fixture
def user2(provider):
    email = 'email2@email.com'
    user = User.objects(email=email)
    if (user):
        user.delete()

    latitude = -89.997 # basically the south pole also
    longitude = -100.01
    user = User(
        email = email, 
        hashed_password = '1234567890ABCDEF',
        email_verified = True,
        auth_token = email,
        role = provider,
        location = {'type': 'Point', 'coordinates': [longitude, latitude]}
        )
    user.save()
    yield user
    user.delete()

@pytest.fixture
def user3(provider):
    email = 'email3@email.com'
    user = User.objects(email=email)
    if (user):
        user.delete()

    latitude = 0.02
    longitude = 0.01
    user = User(
        email = email, 
        hashed_password = '1234567890ABCDEF',
        email_verified = True,
        auth_token = email,
        role = provider,
        location = {'type': 'Point', 'coordinates': [longitude, latitude]}
        )
    user.save()
    yield user
    user.delete()

@pytest.fixture
def user4(provider):
    email = 'email4@email.com'
    user = User.objects(email=email)
    if (user):
        user.delete()

    latitude = 0.0001
    longitude = 0.0001
    user = User(
        email = email, 
        hashed_password = '1234567890ABCDEF',
        email_verified = True,
        auth_token = email,
        role = provider,
        location = {'type': 'Point', 'coordinates': [longitude, latitude]}
        )
    user.save()
    yield user
    user.delete()

@pytest.fixture
def login(start_app, client: FlaskClient, user: User):
    response = client.post(
        url_for('user_bp.login'),
        json={
            'email': user.email,
            'password': USER_PASSWORD
        }
    )
    print(response)
    #client.environ_base['HTTP_AUTHORIZATION'] = f"Bearer {response.json['token']}"
    yield client
    #del client.environ_base['HTTP_AUTHORIZATION']


def test_get_nearby_users(user, user2, user3, login, client):
    """Should return user 2."""
    response = client.get(
        f'user/nearby/{user.id}'
    )
    print(response.data)


def test_get_nearby_users_no_results(user, user2, user3, user4, login, client):
    """Should not return results (user 4 us also a provider and should not be returned)."""
    response = client.get(
        f'user/nearby/{user3.id}'
    )
    print(response.data)
