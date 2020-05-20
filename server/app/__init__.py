import os
from os.path import dirname, join

from dotenv import find_dotenv, load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo

from app.utilities import create_default_roles
from app.domain_logic import user_domain_logic
from app.models import User

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
jwt_manager = JWTManager()

class DevelopmentConfig(object):
    DEBUG = True
    TESTING = True

    # Authentication
    JWT_SECRET_KEY = "enter_secret_here"

    # RetryableWrites are unsupported for mLab MongoDB
    MONGO_URI = os.environ.get('MONGODB_URI')
    if MONGO_URI:
        MONGO_URI = MONGO_URI + "?retryWrites=false"
    MONGODB_SETTINGS = {
        'host': MONGO_URI
    }
    # MONGO_URI = "mongodb://localhost:27017/covid-19?retryWrites=false"
    # MONGODB_SETTINGS = {
    #     'host': MONGO_URI
    # }

    ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
    API_KEY = os.environ['TWILIO_API_KEY']
    API_SECRET = os.environ['TWILIO_API_SECRET']
    CHAT_SERVICE_SID = os.environ.get('TWILIO_CHAT_SERVICE_SID', None)
    AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']


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

    create_default_roles()

    # a simple page that says hello
    @app.route('/version')
    def get_version():
        return 'Version: beta.0'

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
