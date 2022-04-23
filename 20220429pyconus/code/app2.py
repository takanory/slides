import os
import random
import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ["SLACK_BOT_TOKEN"])


# match any message contains "Hi"
@app.message("Hi")
def handle_hi_message(message, say):
    say("Hi!!! I am beerbot! :beer:")


# match any message contains "cheers"
@app.message("cheers")
def handle_cheers_mesasge(message, say):
    say("Cheers! :beers:")


if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
