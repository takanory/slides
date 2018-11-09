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
I think you know, there are so many tasks to hold a conference.
But,...

+++

## Programmer is Lazy

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

a Chat bot for PyCon JP Slack

Note:
I will talk about PyCon JP Bot.

+++

### Why Chatbot?

* Launching the Slack application at any time
* Easy to access Slack
* To do everything in Slack

![slack](20181109ploneconf/images/slack.png)

Note: 
I'am Launching the Slack application at any time
So it's easy to access Slack
I want to do everything in Slack

+++

### PyCon JP Bot

* GitHub: https://github.com/pyconjp/pyconjpbot
* based on Slackbot: https://github.com/lins05/slackbot
* Slack API: https://api.slack.com/

+++

### PyCon JP Bot

![architecture](20181109ploneconf/images/architecture.png)

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

command |
--- | ---
`$google` | search google
`$jira` | search JIRA issue
`$wikipedia` | search Wikipedia
`$weather` | weather forecast
`$translate` | translation
`$gadmin` | manage google admin
`$lgtm` | generate LGTM image

Note:
There are examples of comannds of PyCon JP Bot

+++

## DEMO

Note:
I'll show you DEMO.
How I will reducing bothersome tasks.

$ping
> Bot is active.

> Participants asked me "Do you have any recommendded Japanese food?" at reecption desk.
$choice ramen gyoza gyoza gyoza gyoza sushi

> He asked "Where is the gyoza restaurant?"
$google kamata gyoza

> Then, He said "I don't know gyoza"
> "OK, I'll show you"
$image gyoza

> "Please tell me more about gyoza"
$wikipedia gyoza
$wikipedia -en gyoza

> They ate gyoza.
> At the time of payment, the ammount of money was 26,000 yen for 8 people
26000 / 8
"3,250 yen for each person"

> "BTW, I will move to Kyoto tomorrow. Is Kyoto cold?"
$weather 京都
> "I can't read!"
$translate 明日 は :sunny:晴れ 最低気温13℃ 最高気温22℃

Bot answered all questions!!
I reduced my bothersome tasks.

$translate ありがとうございました
$translate -de ありがとうございました
$translate -es ありがとうございました
