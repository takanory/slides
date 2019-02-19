## Automate the Boring Stuff with Slackbot

### Takanori Suzuki

PyCon APAC 2019 / 2019 Feb 24
---

## Who am I?

* 鈴木たかのり / Takanori Suzuki
* Twitter: [@takanory](https://twitter.com/takanory)
* Director of [PyCon JP Committee](https://www.pycon.jp): `#pyconjp`
* Director of [BeProud Inc.](https://www.beproud.jp)
* Organizer of [Python mini Hack-a-thon](https://pyhack.connpass.com/): `#pyhack`
* Captain of [Python Bouldering Club](https://kabepy.connpass.com/): `#kabepy`

![takanory](assets/images/kurokuri.jpg)

Note:
(1m)

---

## Back grounds and Motivation

Note:
(2m) First, I will talk about Back grounds and Motivation of this talk.

+++

### Conference Tasks

* I held PyCon JP(2014-2016) as Chairperson
* Conference tasks:
  * Keynotes, Talks and Trainings arrangement
  * Ticket sales and reception
  * Venue and facility(WiFi, Video...) management
  * Foods, Coffee, Snacks and Beers

Note:

* I held PyCon JP several times in the past.
* As you can imagine, lots of tasks to hold Conference. And, ...

+++

### Staff ask me the same things

* 40+ staff each year
* Newcomers:Experienced = 50:50

Note:

* The number of PyCon JP staff is 40 over, half of them are the new staff.
* Newcomers ask similar things to me. And I send similar messages to newcomers.
* But, ...

+++

## Programmer is Lazy

Note:

* As you know, programmers dislike routine work. I also dislike it very much.

+++

## Let's create a secretary!!

Note:

* I want someone to do my bothersome tasks instead of me.

---

## Why Chatbot?

* Launching the Slack application at any time
* Easy to access Slack
* To do everything in Slack

![slack](20190224pyconapac/images/slack.png)

Note:

(1m)

* I'm Launching the Slack application at any time.
* So it's easy to access Slack. I want to do everything in Slack.
* From here, I will explain how to create a chatbot on Slack.

---

## Simple integration with Incoming Webhooks

Note:
(5m)

* First, I will explain Simple integration with Incoming Webhooks.

+++

### System overview

* TODO: 図を入れる

* https://api.slack.com/incoming-webhooks

Note:

* This is system overview of Incoming Webhooks.
* When we send a message to a Webhook URL via HTTP, the message sent to Slack.

+++

### Create Incoming Webhooks Integration

* Generate Webhook URL
  1. Create a Slack app
  2. Enable Incoming Webhooks in the app
  3. Create an Incoming Webhook
* Webhook URL like this:

```
https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
```

* see: [Getting started with Incoming Webhooks](https://api.slack.com/incoming-webhooks#getting-started)

Note:

* How to generate Webhook URL is as follows....

+++

### Post message with cURL

```bash
$ curl -X POST -H 'Content-type: application/json' \
> --data '{"text": "Hello Slack"}' \
> https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXX
```

![Hello Slack from cURL](20190224pyconapac/images/webhook-curl.png)

Note:

* Send a simple message with cURL.
* When we send a message with JSON, a message will be displayed in Slack.

+++

### Post message with Requests

```python
import json
import requests

URL = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXX'
data = json.dumps({'text': 'Hello Slack from Python!'})
requests.post(URL, data=data)
```

![Hello Slack from Requests](20190224pyconapac/images/webhook-requests.png)

Note:

* Using Requests in Python is like this. It's easy to us.

+++

### Complex message with Requests

```python
fields = [{'title': 'Love', 'value': 'Ferrets, :beer:, :beers:', 'short': True},
          {'title': 'From', 'value': 'Japan :jp:', 'short': True}]
data = json.dumps({'attachments': [{
    'pretext': 'Nice to meet you!!',
    'author_name': 'Takanori Suzuki',
    'author_link': 'https://twitter.com/takanory/',
    'text': '*THANK YOU* for coming to my talk !:tada: Please give me *feedback* about this talk :bow:',
    'fields': fields,
}]})
```

![Message Attachments](20190224pyconapac/images/webhook-attachments.png)

Note:
We can send complex messages like this with message attachments.

+++

### Summary of Incoming Webhooks

* **Easy to send** messages from programs
* We can create **complex messages**
* BUT **one way** only(program -> Webhook -> Slack)

Note:
Next, I will explain how to make interactive chatbot.

---

## How to create slackbot

+++

### System overview

* TODO: 図を入れる

+++

### Create bot user on Slack

* Create bot user
  1. Create a Slack app
  2. Enable Bots
  3. Add a Bot User
  4. Install App to Workspace -> Authorize
* Invite Bot User to Slack channel
* 'Bot User OAuth Access Token' like this:

```
xoxb-123467890-XXXXXX-XXXXXXXXXXXXX
```

* see: [Creating a bot user](https://api.slack.com/bot-users#creating-bot-user)

Note:
How to create Bot user is as follow....

+++

### Install slackbot

* https://github.com/lins05/slackbot

```shell
$ mkdir mybot
$ cd mybot
$ python3.6 -m venv env
$ source env/bin/activate
(env) $ pip install slackbot
:
:
Successfully installed certifi-2018.11.29 chardet-3.0.4 idna-2.8 requests-2.21.0 six-1.12.0 slackbot-0.5.3 slacker-0.12.0 urllib3-1.24.1 websocket-client-0.44.0
```

Note:
Then, I make venv and install slackbot.

+++

### Create a simple bot with slackbot

* `slackbot_settings.py`

```python
API_TOKEN = "xoxb-123467890-XXXXXX-XXXXXXXXXXXXX"  # Bot token
PLUGINS = ['mybot.plugins']  # Plugin packages
```

* `run.py`

```python
from slackbot.bot import Bot

def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
```

+++

### Simple Plugin

* `mybot/plugins/__init__.py`

```shell
(env) $ mkdir mybot
(env) $ mkdir mybot/plugins
(env) $ touch mybot/plugins/__init__.py  # empty file
```

* `mybot/plugins/sample.py`

```python
from slackbot.bot import listen_to

@listen_to('Hi')
def hello(message):
    message.send('Hi!!! I am slackbot')
```

Note:

* これで一通りのファイルが揃いました

+++

### Run slackbot

* Files for slackbot

```text
mybot/
├── mybot/plugins/
│   ├── __init__.py
│   └── sample.py
├── run.py
└── slackbot_settings.py
```

```shell
(env) $ python run.py
```

![First Slackbot](20190224pyconapac/images/slackbot-hi.png)

Note:

* 基本的なSlackbotの作りはわかったと思うので、拡張していきます。

---

## Extend slackbot

+++

### `listen_to` / `respond_to` decolator

```python
from slackbot.bot import listen_to, respond_to

@listen_to('Hi')
def hello(message):
    message.send('Hi!!! I am slackbot')

@respond_to('ping')  # mention
def ping(message):
    message.reply('pong!')  # mention
```

![Decolator](20190224pyconapac/images/slackbot-decolator.png)

+++

### emoji reaction

* Use `mesasge.react()` method

```python
# -- snip--

@listen_to('beer')
def beer(message):
    message.react(':beer:')
```

![message.react](20190224pyconapac/images/slackbot-react.png)

+++

### Extract parameters on chat message

* Use regular expression

```python
import random
# -- snip--

@respond_to('choice (.*)')
def choice(message, words):
    word = random.choice(words.split())
    message.send('I chose *{}*'.format(word))
```

![Regular expression](20190224pyconapac/images/slackbot-re.png)

+++

### settings

* slackbot_settings.py

```python
ALIASES = '$'  # Prefix instead of mention (@mybot ping -> $ping)
ERRORS_TO = 'mybot-error'  # Some channel
DEFAULT_REPLY = "Sorry but I didn't understand you"
PLUGIN = ['mybot.plugins', 'other.plugins',]  # Pluing packages
```

![Settings](20190224pyconapac/images/slackbot-settings.png)

* see: [Usage of Slackbot](https://github.com/lins05/slackbot#usage)

Note:
Slackbot has several settings.

+++

### Attachements support

```python
import json
# -- snip--

@respond_to('github', re.IGNORECASE)
def github():
    attachments = [
    {
        'fallback': 'Fallback text',
        'author_name': 'Author',
        'author_link': 'http://www.github.com',
        'text': 'Some text',
        'color': '#59afe1'
    }]
    message.send_webapi('', json.dumps(attachments))
```

* TODO: なんか複雑なメッセージを返すコードとその実行例

+++

### Summary of Slackbot

* We can **communicate** with Slackbot
* Slackbot can handle **arguments** in messages
* Slackbot can send mesages in **various formats**

Note:
I think that you understand Slackbot can do various things.
Next,...

---

## Case studies

Note:
I will show some case studies combining Python libraries and APIs.

---

## Calculator function using SymPy

+++

### Calculator function using SymPy

* Motivation
  * スマートフォンで電卓アプリを呼び出すのが面倒
  * Slackから計算できたら楽じゃね?

+++

### Install SymPy

* SymPy: Python library for symbolic mathematics
* https://www.sympy.org/

```shell
(env) $ pip install sympy
:
Successfully installed mpmath-1.1.0 sympy-1.3
```

+++

* `mybot/plugins/calc.py`

```python
from slackbot.bot import listen_to
from sympy import sympify, SympifyError

@listen_to('([-+*/^%!().\d\s]+)')
def calc(message, formula):
    try:
        result = sympify(formula)
        answer = int(result) if result.is_Integer else float(result)
        message.send(f'{answer:,}')
    except SympifyError:
        pass
```

+++

### Calc command

![calc command](20190224pyconapac/images/slackbot-calc.png)

---

### Karma function using Peewee ORM

---

### Search JIRA issues and display issue

---

### Create multiple issues from a template

---

### Search files from Google Drive

---

### Account management of G Suite

---

## Summary and next steps
