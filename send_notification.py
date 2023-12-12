import os
import requests

from dotenv import load_dotenv

def get_token():
    """
    get token from .env
    """
    load_dotenv(verbose=True)

    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    token = os.environ.get("TOKEN")
    return token

def notify_changing(notification_message):
    """
    notifies a message by line 
    """
    token = get_token()

    send_message(token, notification_message)

def send_message(token, notification_message):
    """
    notifies a message by line 
    """
    # Depending on notification service, change following the code 
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)