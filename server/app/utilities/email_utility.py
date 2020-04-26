# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

import os

from flask import current_app
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sendgrid_api_client = SendGridAPIClient(current_app.config['SENDGRID_API_KEY'])
    response = sendgrid_api_client.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as exception:
    print(exception.message)
