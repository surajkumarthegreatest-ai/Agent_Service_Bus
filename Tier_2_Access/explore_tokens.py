from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def main():

    creds=Credentials.from_authorized_user_file("token.json",["https://www.googleapis.com/auth/gmail.readonly"])
    service=build("gmail","v1",credentials=creds)

    labels=service.users().labels().list(userId="me").execute()

    sent=labels.get("labels",[])[1]
    unread=labels.get("labels",[])[2]

    messages=service.users().messages().list(userId="me").execute()
    print(sent)
    print(unread)
    print(messages)

if __name__ == "__main__":
    main()