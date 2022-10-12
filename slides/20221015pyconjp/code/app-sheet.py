import os

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ["SLACK_BOT_TOKEN"])

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SHEET = "SHEET_ID..."
SHEET = os.environ["SHEET_ID"]


@app.message("create issues")
def create_issues(message, say):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET, range="A2:C4").execute()
    for row in result.get("values", []):
        say(f"* Title: {row[0]}, Delta: {row[1]}")


if __name__ == "__main__":
    app_token = os.environ["SLACK_APP_TOKEN"]
    SocketModeHandler(app, app_token).start()
