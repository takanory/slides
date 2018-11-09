### Who am I

* Takaori Suzuki
* Twitter: @takanory
* **Program staff** of #ploneconf2018

![takanory](assets/images/kurokuri.jpg)

+++

### Thank you for

* Training management by Philip
* Talk session volunteer by Jim, Kim and others
* All Keynotes, Talks speakers

Note:
At first, I say Thank you...

---

### Who am I

* Takaori Suzuki
* Twitter: @takanory
* Program staff of #ploneconf2018
* **Chair of PyCon JP** 2014, 2015 and 2016

+++

### Conference Tasks

* Keynotes, Talks and Training arrangement
* Ticket sales and reception
* Facility(WiFi, Video...) management
* Foods, Coffee, Snacks and Beers

Note:
I think you know, there are so many tasks to hold a conference

+++

## But Programmer is Lazy

Note:
As you know, programmers dislike routine work.

+++

## I want a Secretary!!!

Note:
to do my tiresome tasks instead

+++

## Let's make it!!

---

## PyCon JP Bot

Chatbot for PyCon JP Slack

Note:
I will talk about PyCon JP Bot.

+++

### Why Chatbot?

* Launching the Slack application at any time
* Easy access to Slack
* To do everything in Slack

![takanory](20181109ploneconf/images/slack.png)

+++

### PyCon JP Bot

* GitHub: https://github.com/pyconjp/pyconjpbot
* based on https://github.com/lins05/slackbot

+++

### PyCon JP Bot

* TODO: 図を入れる

+++

### Example: `$ping` command

```python
from slackbot.bot import respond_to

@respond_to('^ping$')
def ping(message):
    """$ping -> pong"""
    message.send('pong')
```

+++

### Example: `$choice` command

```python
@respond_to('^choice\s+(.*)')
def choice(message, words):
    """$choice spam ham eggs -> ham"""
    word_list = words.split()
    message.send(random.choice(word_list))
```

Note:
Commands can receive parameters using regular expressions

+++

### Commands of PyCon JP Bot

* `

+++

## DEMO
