import json

from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant
from twilio.rest import Client
from flask import current_app


def generate_access_token(identity: str):
    token = AccessToken(
        current_app.config['ACCOUNT_SID'],
        current_app.config['API_KEY'],
        current_app.config['API_SECRET'],
        identity=identity)
    chat_grant = ChatGrant(service_sid=current_app.config['CHAT_SERVICE_SID'])
    token.add_grant(chat_grant)
    return token.to_jwt().decode()


def create_twilio_user(unique_identity: str, name: str):
    """Create a user with the Twilio Client."""
    twilio_client = Client(
        current_app.config['ACCOUNT_SID'],
        current_app.config['AUTH_TOKEN']
    )

    twilio_client.chat.services(current_app.config['CHAT_SERVICE_SID']).users.create(
        identity=unique_identity,
        friendly_name=name,
        attributes=json.dumps({
            'name': name
        })
    )
