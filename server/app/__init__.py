import os

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo

from app.utilities import create_default_roles


class DevelopmentConfig(object):
    DEBUG = True
    TESTING = True

    # Authentication
    JWT_SECRET_KEY = "enter_secret_here"

    # RetryableWrites are unsupported for mLab MongoDB
    MONGO_URI = "mongodb://localhost:27017/covid-19?retryWrites=false"
    MONGODB_SETTINGS = {
        'host': MONGO_URI
    }


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(DevelopmentConfig)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    initialize_extensions(app)

    register_blueprints(app)

    initialize_database()

    # a simple page that says hello
    @app.route('/')
    def hello():
        return 'Hello, World!'

    return app


def initialize_extensions(app):
    """Initialize all flask extensions."""
    CORS(app)
    JWTManager(app)
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
