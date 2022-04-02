import os
import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import deepl

app = App(token=os.environ["SLACK_BOT_TOKEN"])

translator = deepl.Translator(os.environ["DEEPL_AUTH_KEY"])


@app.message(re.compile(r"^translate (.*)"))
def calc(message, context, say):
    text = context["matches"][0]
    result = translator.translate_text(text,
                                       target_lang="EN-US")
    say(result.text)


if __name__ == "__main__":
    app_token = os.environ["SLACK_APP_TOKEN"]
    SocketModeHandler(app, app_token).start()
