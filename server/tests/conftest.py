"""Provides common fixtures for integration and other test cases."""

from flask import url_for
from flask.testing import FlaskClient
import json
import pytest
from werkzeug.security import generate_password_hash

import app
from app.models.role import Role
from app.models.user import User


@pytest.fixture(scope='class')
def start_app():
    """Provide a configured Flask application."""
    application = app.create_app()
    yield application


@pytest.fixture
def client(start_app):
    """Provide a test client for integration calls."""
    with start_app.test_request_context():
        with start_app.test_client() as client:
            yield client


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

    latitude = -89.99999
    longitude = -179.00001
    user = User(
        email=email,
        name='Spicy Pete',
        hashed_password=generate_password_hash(USER_PASSWORD),
        email_verified=True,
        twilio_token=email,
        role=seeker,
        location={'type': 'Point', 'coordinates': [longitude, latitude]}
    )
    user.save()
    yield user
    user.delete()


@pytest.fixture
def seeker_user(user):
    yield user


@pytest.fixture
def user2(provider):
    email = 'email2@email.com'
    user = User.objects(email=email)
    if (user):
        user.delete()

    latitude = -89.99997 # basically the south pole also
    longitude = -100.00001
    user = User(
        email=email,
        name='Max the doggo',
        hashed_password='1234567890ABCDEF',
        email_verified=True,
        twilio_token=email,
        role=provider,
        location={'type': 'Point', 'coordinates': [longitude, latitude]}
    )
    user.save()
    yield user
    user.delete()


@pytest.fixture
def provider_user(user2):
    yield user2


@pytest.fixture
def user3(provider):
    email = 'email3@email.com'
    user = User.objects(email=email)
    if (user):
        user.delete()

    latitude = 0.00002
    longitude = 0.00001
    user = User(
        email=email,
        name='Claire',
        hashed_password='1234567890ABCDEF',
        email_verified=True,
        twilio_token=email,
        role=provider,
        location={'type': 'Point', 'coordinates': [longitude, latitude]}
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

    latitude = 0.00001
    longitude = 0.00001
    user = User(
        email=email,
        name='Steve',
        hashed_password='1234567890ABCDEF',
        email_verified=True,
        twilio_token=email,
        role=provider,
        location={'type': 'Point', 'coordinates': [longitude, latitude]}
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
