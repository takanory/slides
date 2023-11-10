import os
import re

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from sympy import sympify, SympifyError

app = App(token=os.environ["SLACK_BOT_TOKEN"])


@app.message(re.compile(r"^([-+*/^%!().\d\s]+)$"))
def calc(message, context, say):
    try:
        formula = context["matches"][0]
        result = sympify(formula)  # Simplifies formula
        if result.is_Integer:
            answer = int(result)  # Convert to integer
        else:
            answer = float(result)  # Convert to float
        say(f"{answer:,}")
    except SympifyError:
        pass


if __name__ == "__main__":
    app_token = os.environ["SLACK_APP_TOKEN"]
    SocketModeHandler(app, app_token).start()
