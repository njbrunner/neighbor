import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class BaseConfig(object):

    # Authentication
    JWT_SECRET_KEY = "enter_secret_here"

    ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
    API_KEY = os.environ['TWILIO_API_KEY']
    API_SECRET = os.environ['TWILIO_API_SECRET']
    CHAT_SERVICE_SID = os.environ.get('TWILIO_CHAT_SERVICE_SID', None)
    AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']


class DevelopmentConfig(BaseConfig):
    CONFIGURATION_NAME = "DevelopmentConfig"
    DEBUG = True
    TESTING = True

    MONGO_URI = "mongodb://localhost:27017/covid-19?retryWrites=false"
    MONGODB_SETTINGS = {
        'host': MONGO_URI
    }


class ProductionConfig(BaseConfig):
    CONFIGURATION_NAME = "ProductionConfig"
    DEBUG = False
    TESTING = False

    # RetryableWrites are unsupported for mLab MongoDB
    MONGO_URI = os.environ.get('MONGODB_URI')
    if MONGO_URI:
        MONGO_URI = MONGO_URI + "?retryWrites=false"
    MONGODB_SETTINGS = {
        'host': MONGO_URI
    }


class TestingConfig(BaseConfig):
    CONFIGURATION_NAME = "TestingConfig"
    DEBUG = True
    TESTING = True

    MONGO_URI = "mongodb://localhost:27017/covid-19?retryWrites=false"
    MONGODB_SETTINGS = {
        'host': MONGO_URI
    }
