from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import base64
import os

def main():

    SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

   
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        print("No token.json found. Please run OAuth flow first.")
        return

   
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())

   
    service = build("gmail", "v1", credentials=creds)

   
    email_body = (
        "From: asb.test.04012026@gmail.com\r\n"
        "To: surajkumarsthegreatest@gmail.com\r\n"
        "Subject: Test Email\r\n\r\n"
        "This is a test email sent via Gmail API."
    )
    raw_message = base64.urlsafe_b64encode(email_body.encode("utf-8")).decode("utf-8")
    
    message = {"raw": raw_message}

    
    try:
        sent_message = service.users().messages().send(userId="me", body=message).execute()
        print(f"Email sent with ID: {sent_message['id']}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()   