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

* I held PyCon JP(2014-1016) as Chairperson
* Conference tasks:
  * Keynotes, Talks and Trainigs arrangement
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
data = json.dumps({
    'attachments': [{
        'pretext': 'Nice to meet you!!',
        'author_name': 'Takanori Suzuki',
        'author_link': 'https://twitter.com/takanory/',
        'text': '*THANK YOU* for coming to my talk !:tada: Please give me *feedback* about this talk :bow:',
        'fields': [{'title': 'From', 'value': 'Japan', 'short': True},
                   {'title': 'Love', 'value': 'Ferrets, :beer:, :beers:', 'short': True}]
    }]
})
```

![Message Attachments](20190224pyconapac/images/webhook-attachments.png)

Note:
We can send complex messages like this with message attachments.

+++

### Summary of Incoming Webhook

* プログラムから簡単にメッセージ送信できる
* メッセージの装飾できる
* BUT one way only

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
* Bot User OAuth Access Token like this:

```
xoxb-123467890-XXXXXX-XXXXXXXXXXXXX
```

* Invite Bot User to Slack channel

* see: [Creating a bot user](https://api.slack.com/bot-users#creating-bot-user)

Note:
Botユーザーをまずは作成します。手順の説明...

+++

### Install slackbot

* https://github.com/lins05/slackbot

```
$ mkdir mybot
$ cd mybot
$ python3.6 -m venv env
$ source env/bin/activate
(env) $ pip install slackbot
```

Note:
Then, I make venv and install slackbot.

+++

### Create a simple bot with slackbot

* slackbot_settings.py

```python
API_TOKEN = "xoxb-123467890-XXXXXX-XXXXXXXXXXXXX"
PLUGINS = ['mybot.plugins']
```

* run.py

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

* mybot/plygins/__init__.py: for module
* mybot/plugins/hello.py

```python
from slackbot.bot import listen_to

@listen_to('Hello')
def hello(message):
    message.send('Hello from slackbot')
```

* TODO: 反応している画像を入れる

---

## Extend slackbot

+++

### listen_to and respond_to decolator

```python
from slackbot.bot import listen_to, respond_to

@listen_to('Hello')
def hello(message):
    message.send('Hello from slackbot')

@respond_to('ping')  # mention
def ping(message):
    message.reply('pong!')  # mention
```

+++

### emoji reaction

* Use `mesasge.react()` method

```python
# -- snip--

@listen_to('beer'):
def beer(message):
    message.react(':beer:')
```

* TODO: 画像を入れる

+++

### Extract parameters on chat message

* Use regular expression

```python
import random
# -- snip--

@listen_to('choice (.*)')
def choice(message, words):
    word = random.choice(words.split())
    message.send('I chose {}'.format(word))
```

* TODO: 画像を入れる

+++

### settings

* slackbot_settings.py

```python
ALIASES = '$'  # Prefix instead of mention (@mybot ping -> $ping)
ERRORS_TO = 'mybot-error'  # Some channel
DEFAULT_REPLY = "Sorry but I didn't understand you"
PLUGIN = ['mybot.plugins', 'other.plugins',]  # Pluing packages
```

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

### Summary of Slackbot

* We can communicate with Slackbot
* Slackbot can handle arguments in messages
* Slackbot can send mesages in various formats

Note:
I think that you understand Slackbot can do various things.
Next,...

---

## Case studies

Note:
I will show some case studies combining Python libraries and APIs.

+++

### Calculator function using SymPy

+++

### Karma function using Peewee ORM

+++

### Search JIRA issues and display issue

+++

### Create multiple issues from a template
+++

### Search files from Google Drive

+++

### Account management of G Suite

---

## Summary and next steps
