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
Yes, I hate too.

+++

## I want someone!!!

Note:
to do my bothersome tasks on my behalf

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

![slack](20181109ploneconf/images/slack.png)

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

@respond_to('ping')
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

* `$google`: search google
* `$jira`: search JIRA issue
* `$wikipedia`
* `$weather`: weather forecast
* `$translate`
* `$gadmin`: manage google admin(account and group)
* `$lgtm`: generate LGTM image
* ...and so on

Note:
There are examples of comannds of PyCon JP Bot

+++

## DEMO

Note:
I'll show you DEMO.
How I will reducing bothersome tasks.

$ping
> Bot is active.

> Participants asked me "Do you have any recommendded Japanese food?".
$choice ramen gyoza gyoza gyoza gyoza sushi

> Where is the gyoza restaurant?
$google kamata gyoza

> "I don't know gyoza"
> "I'll show you"
$image gyoza

> "Please tell me more about gyoza"
$wikipedia gyoza
$wikipedia -en gyoza

> "OK Looks good to me."
$lgtm create https://pbs.twimg.com/media/DrdPY1fU0AAzpGV.jpg

> They ate gyoza.
> At the time of payment, the ammount of money was 26,000 yen for 8 people
26000 / 8
"3,250 yen for each person"

> "BTW, I will move to Kyoto tomorrow. How do I get to Kyoto?"
$google 京急蒲田から京都

> "Is Kyoto cold?"
$weather 京都
> "I can't read!"
$translate 明日 は :sunny:晴れ 最低気温13℃ 最高気温22℃

Bot answered all questions!!
I reduced my bothersome tasks.