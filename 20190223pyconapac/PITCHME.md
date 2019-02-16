## Automate the Boring Stuff with Slackbot

### Takanori Suzuki

PyCon APAC 2019 / 2019 Feb 23

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
(2m) First, I will talk about ...

+++

### Conference Tasks

* I held PyCon JP(2014-1016) as Chairperson
* Conference tasks:
  * Keynotes, Talks and Trainigs arrangement
  * Ticket sales and reception
  * Venue and facility(WiFi, Video...) management
  * Foods, Coffee, Snacks and Beers

Note:
I held PyCon JP several times in the past.
As you can imagine, lots of tasks to hold Conference.

+++

### Staff ask me the same things

* 40+ staff each year
* Newcomers:Experienced = 50:50

Note:
The number of PyCon JP staff is 40 over, half of them are the first staff.
Newcomers ask similar things. And I send similar messages to newcomers.
But, ...

+++

## Programmer is Lazy

Note:
As you know, programmers dislike routine work. I also dislike it very much.

+++

## Let's create a secretary!!

Note:
I want someone to do my bothersome tasks instead of me.

---

## Why Chatbot?

* Launching the Slack application at any time
* Easy to access Slack
* To do everything in Slack

![slack](20190223pyconapac/images/slack.png)

Note:
(1m) I'am Launching the Slack application at any time. So it's easy to access Slack. I want to do everything in Slack.
From here, I will explain how to create a chatbot on Slack.

---

## Simple integration with Incoming Webhook

* https://api.slack.com/incoming-webhooks

Note:
(5m)
まずはSimple integration with Incoming Webhookについて説明します。

+++

### System overview

* TODO: 図を入れる

Note:
This is system overview of Incoming Webhook.
プログラムからWebhookに対してメッセージを送信すると、Slackにメッセージがポストされます。

+++

### Create Incoming Webhooks Integration on Slack

* 

Note:
URLを取得する

+++

### Post message with cURL

```bash
$ curl -XXX
$ curl -X POST -H 'Content-type: application/json' \
> --data '{"text": "Hello Slack"}' \
> https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXX
```

Note:
なんか説明

+++

### Post message with cURL

* TODO: ここに送信された画像を入れる

Note:
送信したメッセージがSlackに表示されます!

+++

### Post message with Requests

```python
import json
import requests

URL = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXX'
data = json.dumps({'text': 'Hello Slack'})
requests.post(URL, data=data)
```

Note:
PythonでRequests使うとこんな感じだよ。簡単だよね。

+++

### Complex message with Requests

```python
-- snip --
data = json.dumps({'text': 'Hello Slack'})
requests.post(URL, data=data)
```

* TODO: 画像を入れる

Note:
複雑なメッセージもこんな感じで送れるよ。

---

## How to create slackbot

+++

### System overview

+++

### Create bot user on Slack

+++

### Install slackbot

+++

### Create a simple bot with slackbot

---

## Extend slackbot

+++

### listen_to and respond_to decolator

+++

### emoji reaction(message.react() method)

+++

### Extract parameters on chat message

+++

### settings

+++

### Attachements support

---

## Case study

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
