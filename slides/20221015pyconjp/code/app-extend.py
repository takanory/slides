import logging
import os
import random
import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ["SLACK_BOT_TOKEN"])

logging.basicConfig(level=logging.DEBUG)

# match any message contains "Hi"
@app.message("Hi")
def handle_hi_message(message, say):
    say("Hi!!! I am beerbot! :beer:")


# match any message contains "cheers"
@app.message("cheers")
def handle_cheers_message(mesasge, say):
    say("Cheers! :beers:")


@app.message("morning")
def handle_morning_message(message, say):
    """reply morning greetings with mention"""
    user = message["user"]  # get user ID
    say(f"Good morning <@{user}>!")


@app.message(re.compile(r"choice (.*)"))
def handle_choice(say, context):
    """random choice from words"""
    # get matched text from context["matches"]
    words = context["matches"][0].split()
    say(random.choice(words))


@app.message(re.compile(r"(\d+)\s*(beer|tea)"))
def handle_beer_or_tea(say, context):
    """serve a specified number of beers or teas"""
    count = int(context["matches"][0])
    beer_or_tea = context["matches"][1]
    say(f":{beer_or_tea}:" * count)


@app.message("follow me")
def handle_follow_me(message, say):
    """send follow me message with icon"""
    blocks = [{
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Takanori Suzuki*\nFollow me! <https://twitter.com/takanory|@takanory>",
        },
        "accessory": {
            "type": "image", "alt_text": "takanory",
            "image_url": "https://pbs.twimg.com/profile_images/192722095/kurokuri_400x400.jpg",
        }}]
    say(blocks=blocks)


@app.message("log")
def handle_log(message, say, logger):
    logger.debug(f"message: {message['text']}")
    say("logs exported!")
    

# A user joined a public or private channel
@app.event("member_joined_channel")
def member_joined(event, say):
    """send a welcome message to a new member"""
    user = event["user"]  # get user ID
    say(f"Welcome <@{user}>! :tada:")


@app.message("beer")
def add_beer_emoji(client, message):
    """add :beer: emoji reaciton"""
    client.reactions_add(
        channel=message["channel"],
        timestamp=message["ts"],
        name="beer",
    )


if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
