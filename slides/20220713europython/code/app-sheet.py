import os
import datetime

from jira import JIRA
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ["SLACK_BOT_TOKEN"])

user = os.environ["JIRA_USER"]
token = os.environ["JIRA_TOKEN"]
jira = JIRA("https://pyconjp.atlassian.net/", basic_auth=(user, token))

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SHEET = "1i3YQPObe3ZC_i1Jalo44_2_Ce72tQmIlZLyZ5sjFj4s"


@app.message("create issues")
def creaete_issues(message, say):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET, range="A2:C4").execute()

    # --snip--
    today = datetime.date.today()
    for row in result.get("values", []):
        duedate = today + datetime.timedelta(days=int(row[1]))
        issue_dict = {"project": {"key": "ISSHA"},
                      "summary": row[0],
                      "description": row[2],
                      "duedate": f"{duedate:%Y-%m-%d}",
                      "issuetype": {"name": "Task"}}
        issue = jira.create_issue(fields=issue_dict)
        url = issue.permalink()
        say(f"* Create: <{url}|{issue.key}> {row[0]}\n")


if __name__ == "__main__":
    app_token = os.environ["SLACK_APP_TOKEN"]
    SocketModeHandler(app, app_token).start()
