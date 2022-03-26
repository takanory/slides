import os
import re

from jira import JIRA
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ["SLACK_BOT_TOKEN"])

user = os.environ["JIRA_USER"]
token = os.environ["JIRA_TOKEN"]
jira = JIRA("https://pyconjp.atlassian.net/", basic_auth=(user, token))


@app.message(re.compile(r"^jira (.*)$"))
def calc(message, context, say):
    keywords = context["matches"][0]
    jql = f'text ~ "{keywords}" order by created desc'
    text = ""
    # get 5 recent issues
    for issue in jira.search_issues(jql, maxResults=5):
        issue_id = issue.key
        url = issue.permalink()
        summary = issue.fields.summary
        text += f"* <{url}|{issue_id}> {summary}\n"
    else:
        text = "No issues found"
    say(text)


if __name__ == "__main__":
    app_token = os.environ["SLACK_APP_TOKEN"]
    SocketModeHandler(app, app_token).start()
