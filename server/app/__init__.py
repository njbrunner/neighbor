import os

from flask import Flask, request
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS


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
    # app.config.from_mapping(
    #     SECRET_KEY='dev',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    app.config.from_object(DevelopmentConfig)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    initialize_extensions(app)

    register_blueprints(app)

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
