# Sample code of Automate the Boring Stuff with Slackbot (ver. 2)

* Create venv

```bash
$ python3.11 -m venv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
```

* Generate an app-level token
  * See: [Socket Mode | Slack](https://api.slack.com/apis/connections/socket)
* Generate a bot token
  * See: [Enabling interactions with bots | Slack](https://api.slack.com/bot-users)
* Run bot app

```bash
(env) $ export SLACK_APP_TOKEN=xapp-...
(env) $ export SLACK_BOT_TOKEN=xoxb-...
(env) $ python app-hoge.py
```
