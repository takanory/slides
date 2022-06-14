import os
import re
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from plusplus_model import Plusplus

app = App(token=os.environ["SLACK_BOT_TOKEN"])


# match "word++" pattern
@app.message(re.compile(r"^(\w+)\+\+"))
def plusplus(say, context):
    name = context["matches"][0]
    # Get or create object
    plus, created = Plusplus.get_or_create(
        name=name.lower(),
        defaults={'counter': 0}
    )
    plus.counter += 1
    plus.save()
    say(f"Thank you {name}! (count: {plus.counter})")


if __name__ == "__main__":
    app_token = os.environ["SLACK_APP_TOKEN"]
    SocketModeHandler(app, app_token).start()
