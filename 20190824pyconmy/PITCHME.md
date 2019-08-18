## Automate the Boring Stuff with Slackbot

### Takanori Suzuki

PyCon Malaysia / 2019 Aug 24

Note:

* Thank you for coming to my presentation.
* I am very happy to be able to make a presentation in PyCon Malaysia.

---

## Agenda

* Background and Motivation
* How to create **simple chatbot**
* How to create **interactive bot**
* How to **extend bot** using libs and APIs

Note:
Today, I will talk about...

---

## Before my talk

### Photo 📷 Tweet 🐦 👍

### Memo 📝 🙅‍♂️

Note:
* 撮影OK、Tweetしてね
* スライドは公開するからメモ、撮影しなくていいよ

---

## Who am I?

* Takanori Suzuki / 鈴木 たかのり
* Twitter: [@takanory](https://twitter.com/takanory)
* Vice-Chair of [PyCon JP Committee](https://www.pycon.jp): `#pyconjp`
* Director of [BeProud Inc.](https://www.beproud.jp)
* Organizer of [Python mini Hack-a-thon](https://pyhack.connpass.com/): `#pyhack`
* Captain of [Python Bouldering Club](https://kabepy.connpass.com/): `#kabepy`

![takanory](assets/images/sokidan-square.jpg)

Note:
(1m)
* I'm Takanori Suzuki from Japan. My twitter is takanory please follow me.
* I'm Vice-Chairperson of PyCon JP Committee.
* Have you ever been to Japan? If you have never visited Japan,

+++

## PyCon JP 2019

* [pycon.jp/2019/](https://pycon.jp/2019/)
* Date: 2019 Sepember 14(Sa)-17(Tu)
* Place: Tokyo, Japan

![PyCon JP 2019](assets/images/pyconjp2019.png)

Note:

* PyCon JP is a very good opportunity for you.
* PyCon JP will be held in middle of September.
* I'm looking forward to seeing YOU again in PyCon JP.

+++

## World PyCon Tour 2019🌏

* Feb: PyCon APAC 🇵🇭
* May: US PyCon 🇺🇸
* Jun: PyCon Thailand 🇹🇭
* Jul: EuroPython 🇨🇭
* Aug: PyCon Malaysia 🇲🇾 👈 Now!!!
* Sep: PyCon JP 🇯🇵
* Sep: PyCon Taiwan 🇹🇼
* Oct: PyCon Singapore 🇸🇬

Note:
* 今年は世界中のPyConに応募して発表することに挑戦している
* マレーシアが今年5カ所目、PyConマレーシアでの参加も発表は初めてです
* Well then, let's talk about the main topic.

---
## Background and Motivation

Note:
(2m)
* First, I will talk about the Background and Motivation of this talk.

+++

### Conference Tasks

* I held PyCon JP(2014-2016) as Chair
* Conference tasks:
  * 👨‍💻 Keynotes, Talks and Trainings arrangement
  * 🎫 Ticket sales and reception
  * 🏬 Venue and facility(WiFi, Video...) management
  * 🍱 Foods, ☕️ Coffee, 🧁 Snacks and 🍺 Beers

Note:

* I held PyCon JP event several years in the past.
* As you can imagine, lots of tasks to hold Conference. And, ...

+++

### Staff ask me the same things

* 40+ staff
* **New** staff : **Old** staff = 50 : 50

Note:

* The number of PyCon JP staff is 40 over, half of them are the new staff.
* Newcomers ask similar things to me. And I send similar messages to newcomers.
* But, ...

+++

## Programmer is Lazy

Note:

* As you know, programmers dislike routine work. I also dislike it VERY much.

+++

## Let's create a secretary!!

Note:

* I want someone to do my bothersome tasks instead of me.
* Let's make it.

---

## Goal

* How to create **simple chatbot**
* How to create **interactive bot**
* How to **extend bot** using libs and APIs

Note:
(1m)
* The goal of this talk.
* You'll learn how to create simple chatbot,
* how to create interactive bot,
* how to extend bot using libraries and APIs through various case studies.

---

## Why Slackot

* Launching the Slack application at any time
* Easy to access Slack
* To do everything in Slack

![slack](20190224pyconapac/images/slack.png)
	
Note:
(1m)

* My secretary is chatbot of Slack.
  * Is there someone using Slack?
* I'm Launching the Slack application at any time on PC and smartphone.
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

Note:

* This is system overview of Incoming Webhooks.
* When program send a message to a Webhook URL via HTTPS, the message will send to Slack.

+++

### Create Incoming Webhooks Integration

* Generate Webhook URL
  1. Create a Slack app
  2. Enable Incoming Webhooks in the app
  3. Create an Incoming Webhook
* Webhook URL like this:

  `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`


* see: [Incoming Webhooks](https://api.slack.com/incoming-webhooks)

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

### Post message with Python

```python
import json
from urllib import request

URL = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXX'
data = {'text': 'Hello from Python!'}
jsoned = json.dumps(data).encode('utf-8')
req = request.Request(URL, data=jsoned, method='POST')
request.urlopen(req)
```

![Hello from Python!](20190615pyconth/images/webhook-python.png)

Note:

* Using rullib.requests in Python is like this.

+++

### Post message with Requests

```python
import requests

URL = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXX'
data = {'text': 'Hello from Requests!'}
requests.post(URL, json=data)
```

![Hello from Requests!](20190615pyconth/images/webhook-requests.png)

Note:

* Using Requests in Python is like this. It's easy to us.

+++

### Complex message with Requests

```python
fields = [{'title': 'Love', 'value': 'Ferrets, :beer:, LEGO', 'short': True},
          {'title': 'From', 'value': 'Japan :jp:', 'short': True}]
data = {'attachments': [{
    'pretext': 'Nice to meet you!!',
    'author_name': 'Takanori Suzuki',
    'author_link': 'https://twitter.com/takanory/',
    'text': '*THANK YOU* for coming to my talk !:tada: Please give me *feedback* about this talk :bow:',
    'fields': fields}]}
requests.post(URL, json=data)
```

![Message Attachments](20190224pyconapac/images/webhook-attachments.png)

Note:
We can send complex messages like this with message attachments.

+++

### How to create complex message

* Block-Kit: new UI framework
* Introducing Block Kit
  * https://api.slack.com/block-kit
* Block Kit Builder
  * https://api.slack.com/tools/block-kit-builder

Note:

* Block-Kit is a new UI framework on Slack.
* and Block Kit Builder is interactive prototype builder.

+++?image=20190615pyconth/images/block-kit-builder.png&size=contain

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
  3. Add a **Bot User**
  4. Install App to Workspace -> **Authorize**
* Invite Bot User to Slack channels
* **Bot User OAuth Access Token** like this: `xoxb-123467890-XXXXXX-XXXXXXXXXXXX`

* see: [Creating a bot user](https://api.slack.com/bot-users#creating-bot-user)

Note:
* I describe how to create interactive bot.
* At first, we craete bot user on Slack.

+++

### Install slackbot

```shell
$ mkdir mybot; cd mybot
$ python3.7 -m venv env
$ . env/bin/activate
(env) $ pip install slackbot
:
(env) $ pip list | grep slackbot
slackbot         0.5.3   
```

* [github.com/lins05/slackbot](https://github.com/lins05/slackbot)

Note:
* Then, I make venv and install slackbot library.
* slackbot is chatbot framework.

+++

### Create a simple bot with slackbot

* slackbot_settings.py

```python
API_TOKEN = "xoxb-123467890-XXXXXX-XXXXXXXXXXXXX"  # Bot token
PLUGINS = ['mybot.plugins']  # Plugin packages
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

Note:
* The simplest slackbot consists of 4 files.

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

* That's all.

+++

### File structure

--- | ---
mybot/ | Project dir
mybot/env/ | venv
mybot/plugins/__init__.py | 
mybot/plugins/sample.py | Sample plugin
mybot/run.py | Main script
mybot/slackbot_settings.py | Settings

Note:
* たった4つのファイルで完成です
 
+++

### Run slackbot

```shell
(env) $ python run.py
```

![First Slackbot](20190224pyconapac/images/slackbot-hi.png)

Note:

* ではbotを動かしてみましょう
* I guess you understood the basic way to make Slackbot, so we will extend it.

---

## Extend slackbot

+++

### `listen_to` / `respond_to` decorator

```python
from slackbot.bot import listen_to, respond_to

@listen_to('Hi')
def hello(message):
    message.send('Hi!!! I am slackbot')

@respond_to('ping')  # mention
def ping(message):
    message.reply('pong!')  # mention
```

+++

### `listen_to` / `respond_to` decorator

![Decorator](20190224pyconapac/images/slackbot-decolator.png)

+++

### emoji reaction

* `mesasge.react()` method

```python
@listen_to('beer')
def beer(message):
    message.react(':beer:')
```

![message.react](20190615pyconth/images/slackbot-react.png)

+++

### Extract parameters on message

* Use regular expressions

```python
@respond_to('choice (.*)')  # choice pizza beer sushi
def choice(message, words):  # -> words='pizza beer sushi'
    word = random.choice(words.split())
    message.send('I chose *{}*'.format(word))
```

+++

### Extract parameters on message

![Regular expression](20190224pyconapac/images/slackbot-re.png)

+++

### Settings: `slackbot_settings.py`

```python
ALIASES = '$'  # Prefix instead of mention (@mybot ping -> $ping)
ERRORS_TO = 'mybot-error'  # Error reporting channel
DEFAULT_REPLY = "Sorry but I didn't understand you"
PLUGIN = ['mybot.plugins', 'other.plugins',]  # Pluing packages
```

![Settings](20190224pyconapac/images/slackbot-settings.png)

* see: [Usage of Slackbot](https://github.com/lins05/slackbot#usage)

Note:
Slackbot has several settings.

+++

### Attachments support

```python
import json

@respond_to('follow me')
def followme(message):
    attachments = [{
        'author_name': 'Takanori Suzuki',
        'text': 'Follow me! <https://twitter.com/takanory|@takanory>',
        'color': '#59afe1'
    }]
    message.send_webapi('', json.dumps(attachments))
```

![Attachments](20190224pyconapac/images/slackbot-attachments.png)

+++

### Summary of Slackbot

* We can **communicate** with Slackbot
* Slackbot can handle **arguments** in messages
* Slackbot can send messages in **various formats**

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
  * I feel heavy to call a caluclator app on my smartphone
  * It seems useful if Slack as a calculator

+++

### Install SymPy

* SymPy: Python library for symbolic mathematics
  * [www.sympy.org](https://www.sympy.org/)
* Install: `$ pip install sympy`

+++

* `mybot/plugins/calc.py`

```python
from slackbot.bot import listen_to
from sympy import sympify, SympifyError

@listen_to(r'^([-+*/^%!().\d\s]+)$')  # Formula like pattern
def calc(message, formula):
    try:
        result = sympify(formula)  # Simplifies the formula
	if result.is_Integer:
	    answer = int(result)  # Convert to interger value
	else:
	    answer = float(result)  # Convert to float value
        message.send(f'{answer:,}')
    except SympifyError:
        pass
```

+++?image=20190224pyconapac/images/slackbot-calc.png&size=auto

---

## Plusplus function using Peewee ORM

+++

### Plusplus function using Peewee ORM

* Motivation
  * In PyCon JP, I want to make a culture that appreciates each other staff

+++

### Install Peewee

* simple and small ORM.
  * a small, expressive ORM
  * python 2.7+ and 3.4+ (developed with 3.6)
  * supports sqlite, mysql and postgresql
* [docs.peewee-orm.com](http://docs.peewee-orm.com/en/latest/)
* Install: `$ pip install peewee`

+++

### Plusplus model

```python
from pathlib import Path
from peewee import SqliteDatabase, Model, CharField, IntegerField

dbpath = Path(__file__).parent / 'plusplus.db')
db = SqliteDatabase(dbpath)

class Plusplus(Model):
    name = CharField(primary_key=True)
    counter = IntegerField(default=0)

    class Meta:
        database = db

db.connect()
db.create_tables([Plusplus], safe=True)
```

+++

### Plusplus command

```
from slackbot.bot import listen_to

from .plusplus_model import Plusplus

@listen_to(r'^(\w+)\+\+')
def plusplus(message, name):
    target = name.lower()
    # Get or create object
    plus, created = Plusplus.get_or_create(
        name=target, defaults={'counter': 0})
    plus.counter += 1
    plus.save()
    message.send(f'Thank you {name}! (count: {plus.counter})')
```

+++

![Plusplus](20190615pyconth/images/slackbot-plusplus.png)

---

## Display JIRA issue and Search issues

+++

### Display JIRA issue and Search issues

* Motivation
  * JIRA is very useful
  * JIRA Web is **very heavy**
  * I want to check issue details without JIRA Web

+++

### System Overview

![Overview of JIRA](20190224pyconapac/images/jira-overview.png)

+++

### Install Python JIRA

* Python library to work with JIRA APIs
  * [jira.readthedocs.io](https://jira.readthedocs.io/)
* Install: `$ pip install jira`			

+++

### Authentication

```python
from jira import JIRA

URL = 'https://jira.atlassian.com/'
jira = JIRA(URL, basic_auth=('user', 'pass'))
```

* see: [2.1.2. Authentication](https://jira.readthedocs.io/en/master/examples.html#authentication)

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

* see: [2.1.3 Issues](https://jira.readthedocs.io/en/master/examples.html#issues)

+++

![JIRA issue](20190224pyconapac/images/slackbot-jira-issue.png)

+++

### Search issues

```python
@respond_to('jira (.*)')
def jira_search(message, keywords):
    # make JQL query string
    jql = f'project=ISSHA and text ~ "{keywords}" order by created desc'
    text = ''
    # get 5 recent issues
    for issue in jira.search_issues(jql, maxResults=5):
        id = issue.key
        url = issue.permalink()
        summary = issue.fields.summary
        text += f'- <{url}|{id}> {summary}\n'
    message.send(text)
```

* see: [2.1.5 Searching](https://jira.readthedocs.io/en/master/examples.html#searching)
* JQL: JIRA Query Language
* see: [Advanced searching - Atlassian Documentation](https://confluence.atlassian.com/jiracoreserver073/advanced-searching-861257209.html)

+++

![JIRA search](20190224pyconapac/images/slackbot-jira-search.png)

---

## Create multiple issues from a template

+++

### Create multiple issues from a template

* Motivation
  * In pycamp event, **20+ issues** are required for each event
  * It is very painful for me to **copy issues** manually
  * JIRA Web is **very heavy**(again)

Note:
* PyCon JP hold pycamp every month.

+++

### System Overview

![Ovierview of template](20190224pyconapac/images/template-overview.png)

+++

### Google Authorization is VERY Complex(1/2)

* create Google Cloud Platform project
  * enable API(in this case: Google Sheets API)
  * download `credentials.json`
* Install Google Client Library
  * `$ pip install google-api-python-client google-auth-oauthlib`

Note:
* At firest, we make Google Authorized token.

+++

### Google Authorization is VERY Complex(2/2)

* download `quickstart.py`
  * [quickstart.py on GitHub](https://github.com/gsuitedevs/python-samples/blob/master/sheets/quickstart/quickstart.py)
* run `quickstart.py`
  * select your Google account in Web browser
  * Click the Accept button
  * get `token.pickle` file(finish!!)

```shell
(env) $ python quickstart.py
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&.....
Name, Major:
Alexandra, English
:
Will, Math
```

* see: [Python Quickstart | Sheets API | Google Developers](https://developers.google.com/sheets/api/quickstart/python)

Note:

* But, if we can use Google's API, we can do many things

+++

### Get Spreadsheet Data

```python
from googleapiclient.discovery import build
SHEET_ID = '1LEtpNewhAFSXXXXXXXXXXXXX'

creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# build service
service = build('sheets', 'v4', credentials=creds)
# get data from Spreadsheet
result = service.spreadsheets().values().get(
    spreadsheetId=SHEET_ID, range='sheet_name!A:G').execute()
for row in result.get('value', []):
    print(row[0], row[1])  # Cell A and B
```

* see: [Method: spreadsheets.values.get](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get)

+++

### Create JIRA Issue

```python
duedate = datetime.date.today + datetime.timedelta(days + 14)
issue_dict = {
    'project': {'key': PROJECT},
    'components': [{'name': COMPONENT}],
    'summary': SUMMARY_TEXT,
    'description': LONG_DESCRIPTION,
    'assignee': {'name': NAME_OF_ASSIGNEE},
    'reporter': {'name': NAME_OF_REPORTER},
    'duedate': '{:%Y-%m-%d}'.format(duedate),
}
issue = jira.create_issue(fields=issue_dict)  # create issue
```

* see: [2.1.3 Issues](https://jira.readthedocs.io/en/master/examples.html#issues)

+++

### Sample of template command

* `$pycamp create`: Create issues for pycamp event

![Sample of Template command](20190224pyconapac/images/template-bot-sample.png)

+++?image=20190224pyconapac/images/template-pycamp-template.png&size=contain

Note:

* Here is the pycamp issue template.

+++?image=20190224pyconapac/images/template-created-issues.png&size=contain

Note:

* As you can see, I can create many tickets for pycamp in one command.
* I am very happy.

+++

### Source code of pycamp command

* see: https://github.com/pyconjp/pyconjpbot/blob/master/pyconjpbot/plugins/pycamp.py

+++

### I never have to copy issues again 🎉

---

## Account management of G Suite

+++

### Account management of G Suite

* Motivation
  * PyCon JP use `pycon.jp` domain with G Suite
  * I only use Google Admin web occasionally
  * I forgot to use admin screen

Note:

* create a new staff account
* add email address to groups

+++

### System Overview

![Overview of gadmin](20190224pyconapac/images/gadmin-overview.png)

+++

### Update Google Authorization

* update Google Cloud Platform project
  * add G Suite Admin API
  * re-download `credentials.json`
* re-run `quickstart.py`
  * get new `token.pickle`

```shell
(env) $ python quickstart.py
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&.....
Name, Major:
Alexandra, English
:
Will, Math
```

Note:

* If we use the new API we need to re-authenticate

+++

### Get user list

```python
# build service
DOMAIN = 'pycon.jp'
service = build('admin', 'directory_v1', credentials=creds)

# get user list
users_list = service.users().list(orderBy='email', domain=DOMAIN).execute()
for user in users_list.get('users', []):
    email = user['primaryEmail']
    fullname = user['name']['fullName']
    print(f'{email} {fullname}')
```

* see: [Users: list | Directory API](https://developers.google.com/admin-sdk/directory/v1/reference/users/list)

+++

### Insert user

```python
body = {
    'primaryEmail': EMAIL_ADDRESS,
    'password': PASSWORD,
    'name': {
        'givenName': FIRST_NAME,
        'familyName': LAST_NAME,
    },
}
try:
    service.users().insert(body=body).execute()
except:
    pass  # fail
```

* see: [Users: insert | Directory API](https://developers.google.com/admin-sdk/directory/v1/reference/users/insert)

+++

### Suspend, Resume, Delete user

```python
suspend = {'suspended': True}
service.users().update(userKey=EMAIL, body=suspend).execute()

resume = {'suspended': False}
service.users().update(userKey=EMAIL, body=resume).execute()

service.users().delete(userKey=email).execute()
```

* see: [Users: update | Directory API](https://developers.google.com/admin-sdk/directory/v1/reference/users/update)
* see: [Users: delete | Directory API](https://developers.google.com/admin-sdk/directory/v1/reference/users/delete)

+++?image=20190224pyconapac/images/gadmin-help.png&size=contain

+++?image=20190224pyconapac/images/gadmin-user-list.png&size=contain

+++?image=20190224pyconapac/images/gadmin-member-list.png&size=contain

+++

### I can completely forget Google Admin web site 🎉

+++

### Source code of gadmin command

* see: https://github.com/pyconjp/pyconjpbot/blob/master/pyconjpbot/google_plugins/gadmin.py

---

## Summary

* Incoming Webhooks
* Slackbot
* Slackbot with Libraries
* Slackbot with APIs

+++

## Next steps

* Let's make **your own Slackbot**
* Let's connect with libraries and APIs
* Automate your Boring Stuff with Slackbot

Note:

Then you will have more free time so you can do other creative things more.

+++

## Thank you! 🙏

## Terima kasih! 🙏

* Twitter: [@takanory](https://twitter.com/takanory)
* Slides: [github.com/takanory/slides](https://github.com/takanory/slides)
