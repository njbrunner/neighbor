from os.path import dirname, join

from dotenv import load_dotenv
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant
from flask import current_app

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def generate_access_token(identity: str):
    token = AccessToken(
        current_app.config['ACCOUNT_SID'],
        current_app.config['API_KEY'],
        current_app.config['API_SECRET'],
        identity=identity)
    chat_grant = ChatGrant(service_sid=current_app.config['CHAT_SERVICE_SID'])
    token.add_grant(chat_grant)
    return token.to_jwt().decode()
