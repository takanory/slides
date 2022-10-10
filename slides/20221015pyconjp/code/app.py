import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ["SLACK_BOT_TOKEN"])

# match any message contains "Hi"
@app.message("Hi")
def handle_hi_message(message, say):
    say("Hi!!! I am beerbot! :beer:")

if __name__ == "__main__":
    app_token = os.environ["SLACK_APP_TOKEN"]
    SocketModeHandler(app, app_token).start()
