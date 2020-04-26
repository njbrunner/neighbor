"""Provides common fixtures for integration and other test cases."""

import pytest

import app

@pytest.fixture(scope='class')
def start_app():
    """Provide a configured Flask application."""
    application = app.create_app()
    yield application

@pytest.fixture
def client(start_app):
    """Provides a test client for integration calls."""
    with start_app.test_request_context():
        with start_app.test_client() as client:
            yield client
