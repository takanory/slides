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

![Overview of Incoming Webhook](20190224pyconapac/images/webhook-overview.png)

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

![Overview of Slackbot](20190224pyconapac/images/slackbot-overview.png)

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

```python
@respond_to('choice (.*)')
def choice(message, words):
    word = random.choice(words.split())
    message.send('I chose *{}*'.format(word))
```

![Regular expression](20190224pyconapac/images/slackbot-re.png)

+++

### settings(`slackbot_settings.py`)

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

@listen_to(r'^([-+*/^%!().\d\s]+)$')
def calc(message, formula):
    try:
        result = sympify(formula)
        answer = int(result) if result.is_Integer else float(result)
        message.send(f'{answer:,}')
    except SympifyError:
        pass
```

+++?image=20190224pyconapac/images/slackbot-calc.png&size=auto

---

## Plusplus function using Peewee ORM

+++

### Karma function using Peewee ORM

* Motivation
  * スタッフに感謝し合う感じにしたい

---

## Search JIRA issues and display issue

+++

### Search JIRA issues and display issue

* Motivation
  * WebのJIRAの画面が重い
  * Webで見ずに詳細を確認したい

+++

### Install Python JIRA

* Python library to work with JIRA APIs
* https://jira.readthedocs.io/

```shell
(env) $ pip install jira
:
Successfully installed asn1crypto-0.24.0 cffi-1.12.1 cryptography-2.5 defusedxml-0.5.0 jira-2.0.0 oauthlib-3.0.1 pbr-5.1.2 pycparser-2.19 pyjwt-1.7.1 requests-oauthlib-1.2.0 requests-toolbelt-0.9.1
```

+++

### Authentication

```python
from jira import JIRA

URL = 'https://jira.atlassian.com/'
jira = JIRA(URL, basic_auth=('user', 'pass'))
```

* See: [2.1.2. Authentication](https://jira.readthedocs.io/en/master/examples.html#authentication)

+++

### Get Issue object

```python
@listen_to(r'(ISSHA-[\d]+)')  # Issue id pattern
def jira_issue(message, issue_id):
    issue = jira.issue(issue_id)
    summary = issue.fields.summary
    status = issue.fields.status.name
    assignee = issue.fields.assignee.name
    issue_url = issue.permalink()
    attachments = [{
        'pretext': f'<{issue_url}|{issue_id}> {summary}',
        'fields': [{'title': 'Assignee', 'value': assignee},
                   {'title': 'Status', 'value': status}],
    }]
    message.send_webapi('', json.dumps(attachments))
```

* See: [2.1.3 Issues](https://jira.readthedocs.io/en/master/examples.html#issues)

+++

![JIRA issue](20190224pyconapac/images/slackbot-jira-issue.png)

+++

### Search issues

```python
@respond_to('jira (.*)')
def jira_search(message, keywords):
    jql = f'project=ISSHA and text ~ "{keywords}" order by created desc'
    text = ''
    for issue in jira.search_issues(jql, maxResults=5):
        id = issue.key
        url = issue.permalink()
        summary = issue.fields.summary
        text += f'- <{url}|{id}> {summary}\n'
    message.send(text)
```

* See: [2.1.5 Searching](https://jira.readthedocs.io/en/master/examples.html#searching)
* JQL: JIRA Query Language
* see: [Advanced searching - Atlassian Documentation](https://confluence.atlassian.com/jiracoreserver073/advanced-searching-861257209.html)

+++

![JIRA search](20190224pyconapac/images/slackbot-jira-search.png)

---

## Create multiple issues from a template

+++

### Create multiple issues from a template

* Motivation
  * イベント開催ごとに20くらいのJIRA issueが必要
  * コピーするのだるい
  * JIRAの画面が重い

+++

### System Overview

* TODO: 図を入れる

+++

### Google Authorization is VERY Complex(1/2)

* create Google Cloud Platform project
  * enable API(in this case: Google Sheets API)
  * download `credentials.json`
* Install Google Client Library

```shell
(venv) $ pip install google-api-python-client google-auth-oauthlib
:
Successfully installed cachetools-3.1.0 google-api-python-client-1.7.8 google-auth-1.6.3 google-auth-httplib2-0.0.3 httplib2-0.12.1 pyasn1-0.4.5 pyasn1-modules-0.2.4 rsa-4.0 uritemplate-3.0.0
```

+++

### Google Authorization is VERY Complex(2/2)

* craete `quickstart.py`
  * [quickstart.py on GitHub](https://github.com/gsuitedevs/python-samples/blob/master/sheets/quickstart/quickstart.py)
* run `quickstart.py`
  * select your Google account in Web browser
  * Click the Accept button
  * get `token.pickle` file(finish!!)

```shell
(venv) $ python quickstart.py
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&.....
Name, Major:
Alexandra, English
:
Will, Math
```

* See: [Python Quickstart | Sheets API | Google Developers](https://developers.google.com/sheets/api/quickstart/python)

Note:

* でもGoogleのAPI使えると強力なのでがんばろう

+++

---

## Search files from Google Drive

---

## Account management of G Suite

+++

### Account management of G Suite

* Motivation
  * G Suiteの管理画面たまにしか開かない
  * 使い方忘れる

---

## Summary and next steps
