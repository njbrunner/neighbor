import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo

from app.utilities import create_default_roles
from app.domain_logic import user_domain_logic
from app.models import User

jwt_manager = JWTManager()

def create_app(config):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    initialize_extensions(app)

    register_blueprints(app)

    create_default_roles()

    # a simple page that says hello
    @app.route('/version')
    def get_version():
        return f'Version: beta.0 Config: {app.config["CONFIGURATION_NAME"]}'

    return app


def initialize_extensions(app):
    """Initialize all flask extensions."""
    CORS(app)
    jwt_manager.init_app(app)
    PyMongo(app)
    MongoEngine(app)


def register_blueprints(app):
    """Register blueprints."""
    from app.routes import USER_BP
    app.register_blueprint(USER_BP)
    from app.routes import ROLE_BP
    app.register_blueprint(ROLE_BP)


def initialize_database():
    """Initialize database."""
    create_default_roles()


@jwt_manager.user_loader_callback_loader
def load_user(user_id: str) -> User:
    """Return the current JWT user."""
    return user_domain_logic.get_user(user_id)


__all__ = [
    "jwt_manager"
]
