import os
import re

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ["SLACK_BOT_TOKEN"])

SCOPES = ["https://www.googleapis.com/auth/admin.directory.user"]


@app.message("user_list")
def user_list(message, say, client):
    # get user info: https://api.slack.com/methods/users.info
    response = client.users_info(user=message["user"])
    user = response.data["user"]
    if not user["is_admin"]:
        say("You are not an admin!")
        return

    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    service = build("admin", "directory_v1", credentials=creds)

    users_list = service.users().list(
        orderBy="email", maxResults=10, customer="my_customer").execute()

    for user in users_list.get("users", []):
        email = user["primaryEmail"]
        fullname = user["name"]["fullName"]
        say(f"* {email} {fullname}")


@app.message(re.compile(r"user_add (\w+) (\w+) (\w+) (\w+)"))
def insert_user(message, say, context):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    service = build("admin", "directory_v1", credentials=creds)

    body = {
        "primaryEmail": context["matches"][0] + "@pycon.jp",
        "password": context["matches"][1],
        "name": {
            "givenName": context["matches"][2],
            "familyName": context["matches"][3]
        }}
    service.users().insert(body=body).execute()
    say(f"User {body['primaryEmail']} created")


if __name__ == "__main__":
    app_token = os.environ["SLACK_APP_TOKEN"]
    SocketModeHandler(app, app_token).start()
