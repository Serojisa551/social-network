# import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from mailbox import Message
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.errors import Error
import base64
from email.mime.text import MIMEText

# # Replace with the path to your client_secret.json file
# CLIENT_SECRET_FILE = 'configs1.json'

# # The scopes for the Gmail API
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']


# def get_credentials():
#     print("lol")
#     flow = InstalledAppFlow.from_client_secrets_file(
#         CLIENT_SECRET_FILE, SCOPES)
#     credentials = flow.run_local_server(port=0)
#     print("adg")
#     return credentials


# credentials = get_credentials()
# print(credentials.refresh_token)


def send_email(message):
    try:
        # Set up the Gmail API client
        creds = Credentials.from_authorized_user_file(
            'configs1.json', ['https://www.googleapis.com/auth/gmail.send'])
        service = build('gmail', 'v1', credentials=creds)

        # Define the message to be sent
        to = message['to']
        subject = message['subject']
        body = message['body']
        message = Message()
        message['to'] = to
        message['subject'] = subject
        message.set_payload(body)

        # Send the message
        create_message = {'raw': base64.urlsafe_b64encode(
            message.as_bytes()).decode()}
        send_message = (service.users().messages().send(
            userId="me", body=create_message).execute())

        return send_message

    except HttpError as error:
        print('An error occurred: %s' % error)
        return None

    except Error as error:
        print('An error occurred: %s' % error)
        return None


# Call this function to obtain an access token and refresh token
