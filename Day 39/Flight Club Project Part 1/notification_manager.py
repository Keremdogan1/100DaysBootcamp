import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, message_body):
        self.my_phone_number = os.getenv("DAY39_PHONE_NUMBER")
        self.account_sid = os.getenv("DAY39_ACCOUNT_SID")
        self.auth_token = os.getenv("DAY39_AUTH_TOKEN")
        self.my_phone_number = os.getenv("DAY39_PHONE_NUMBER")
        self.body = message_body

    def send_message(self):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=self.body,
            from_ = 'whatsapp:+14155238886',
            to = self.my_phone_number
        )
        print(message.status)