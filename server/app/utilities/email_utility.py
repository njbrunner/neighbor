# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python

from http import client
from urllib import parse

from flask import current_app
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content


def send_email():
    # from_email = Email("test@example.com")
    # to_email = To("test@example.com")
    # subject = "Sending with SendGrid is Fun"
    # content = Content("text/plain", "and easy to do anywhere, even with Python")
    # mail = Mail(from_email, to_email, subject, content)
    # # message = Mail(
    # #     from_email='from_email@example.com',
    # #     to_emails='to@example.com',
    # #     subject='Sending with Twilio SendGrid is Fun',
    # #     html_content='<strong>and easy to do anywhere, even with Python</strong>')

    # sendgrid_api_client = SendGridAPIClient(api_key=current_app.config['SENDGRID_API_KEY'])
    # print(sendgrid_api_client)
    # # response = sendgrid_api_client.send(message.get())
    # response = sendgrid_api_client.client.mail.send.post(request_body=mail.get())
    # print(response.status_code)
    # print(response.body)
    # print(response.headers)

    connection = client.HTTPConnection('api.sendgrid.com/v3/mail')
    params = parse.urlencode({
        "personalizations": [
            {
                "to": [
                    {
                        "email": "example@example.com"
                    }
                ],
                "subject": "Hello, World!"
            }
        ],
        "from": {
            "email": "from_address@example.com"
        },
        "content": [
            {
                "type": "text/plain",
                "value": "Hello, World!"
            }
        ]
    })
    headers = {
        "Content-type": "application/json",
        "Authorization": "Bearer " + current_app.config['SENDGRID_API_KEY']
    }

    connection.request("POST", "/send", params, headers)
    response = connection.getresponse()
    print(response)
