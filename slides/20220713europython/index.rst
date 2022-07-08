======================================================
 Automate the Boring Stuff with **Slackbot** (ver. 2)
======================================================

Takanori Suzuki

EuroPython 2022 / 2022 Jul 13

.. Thank you for coming to my presentation.
   I am very happy to be able to talk in EuroPython.
   My talk title is "Automate the Boring Stuff with Slackbot (ver. 2)"

Agenda
======
* **Background** and **Motivation** for Slackbot
* How to create **simple** bot
* How to create **interactive** bot
* How to **extend** bot using libs and APIs

.. revealjs-notes::

   Today, I will talk about...

Photos 📷 Tweets 🐦 👍
=========================

``#EuroPython`` / ``@takanory``

.. revealjs-notes::

   I'd be happy to take pictures and share them and give you feedback on Twitter.
   Hashtag is #EuroPython

Slide 💻
---------
`slides.takanory.net <https://slides.takanory.net>`__

.. revealjs-notes::

   I've already published this slide on slides.takanory.net.
   And I've already shared this slide URL on Twitter.

Why **ver. 2** in the title?
============================

Back to **2019**
----------------
* Talk in 🇵🇭 🇹🇭 🇲🇾 🇯🇵 🇹🇼 🇸🇬 🇮🇩
* TODO: 各国PyConでの発表のコラージュ

.. image:: images/pyconus2020.png
   :width: 80%

.. revealjs-notes::

   The story goes back to 2019.
   I have given talks on Slackbot at several PyCons.

And the 2022
------------
* Talk **updated** with latest information
* I am very **happy**!!
* **Thanks** to EuroPython staff!!

.. revealjs-notes::

   I've updated the talk with the latest information about Slack and libraries.
   And this is my first talk at an international Python event after COVID-19!
   I am very happy to be able to present in person in front of you all.
   And huge thanks to EuroPython staff.
   By the way, before the main topic,...

Who am I? 👤
=============
* Takanori Suzuki / 鈴木 たかのり (:fab:`twitter` `@takanory <https://twitter.com/takanory>`_)
* Vice Chair of `PyCon JP Association <https://www.pycon.jp/>`_
* Director of `BeProud Inc. <https://www.beproud.jp/>`_
* `Python Boot Camp <https://www.pycon.jp/support/bootcamp.html>`_, `Python mini Hack-a-thon <https://pyhack.connpass.com/>`_, `Python Bouldering Club <https://kabepy.connpass.com/>`_

.. image:: /assets/images/sokidan-square.jpg

.. revealjs-notes::

   Before the main topic,...I will introduce myself.
   I'm Takanori Suzuki. My twitter is "takanory", please follow me.
   I'm Vice-Chairperson of the PyCon JP Association.
   And I'm director of BeProud Inc.
   I'm also active in several Python related communities.

**PyCon JP** 2022 🇯🇵
---------------------
* `2022.pycon.jp <https://2022.pycon.jp/>`_
* Date: 2022 **Oct 14** (Fri) - **16** (Sun)
* Venue: **Tokyo**, Japan (in-person)

.. image:: /assets/images/pyconjp2022logo.png
   :width: 50%

.. revealjs-notes::

   PyCon JP 2022 will be held as an in-person event.
   Please come to Japan!
   Let's get back to the main topic.
   
.. PyCon JP 2022やるよ。ぜひ来てね

**Background** and **Motivation**
=================================

.. revealjs-notes::

   First, I will talk about the Background and Motivation of this talk.

Conference **Tasks**
--------------------
* I held PyCon JP(2014-2016) as Chair
* Conference tasks:

  * 👨‍💻 Keynotes, Talks and Trainings
  * 🎫 Ticket sales and reception
  * 🏬 Venue and facility(WiFi, Video...)
  * 🍱 Foods, ☕️ Coffee, 🧁 Snacks and 🍺 Beers

.. revealjs-notes::

   I held PyCon JP events several years in the past.
   As you can imagine, there are lots of tasks to hold Conference.
   For example, talk arrangements, ticket sales, venue management, food...
   And, ...

Staff ask me the **same things**
--------------------------------
* 40+ staff
* 🐣 NEW staff : 🐔 OLD staff = 50 : 50

.. revealjs-notes::

   The number of PyCon JP staff is over 40, half of them are new staff.
   New staff ask similar things to me. And I send similar answers repeatedly.
   But, ...

Programmer is **Lazy**
======================
.. revealjs-notes::

   As you know, programmers dislike routine work. I also dislike it VERY much.

Let's create a **secretary**!!
==============================
.. revealjs-notes::

   I want someone to do my bothersome tasks instead of me like a secretary.
   Let's make it.

Goal
====
* How to create **simple** bot
* How to create **interactive** bot
* How to **extend** bot using libs and APIs

.. revealjs-notes::

   The goal of this talk.
   You'll learn how to create simple bot,
   how to create interactive bot,
   how to extend bot using libraries and APIs through various case studies.

Why **Slack** ?
===============
* Launching the Slack app at any time 💻 📱
* **Easy** to access Slack
* To do **everything** in Slack

.. image:: /20190224pyconapac/images/slack.png
   :width: 60%

.. revealjs-notes::

   My secretary is a chatbot of Slack.
   Is there someone using Slack?
   I'm Launching the Slack application at any time on my PC and smartphone.
   So it's easy to access Slack. I want to do everything in Slack.
   Let's make a chatbot on Slack.

You can create **interactive** bot
----------------------------------
.. image:: images/bot-result1.png
   :width: 48%

.. image:: images/bot-result2.png
   :width: 48%

.. revealjs-notes::

   If you listen to the end of this talk, you will be able to create a bot like this.
   For example, the bot will greet, choose randomly, calculate, count, search JIRA issues, create email addresses and more.
   Now let's learn how to create a bot.
   
.. このトークを聞くとこんなbotが作れるようになりますよ。
   あいさつしたり、randomに選んだり、計算したり、カウントしたり、JIRA検索したり、メールアドレスを追加したり。

Simple integration with **Incoming Webhooks** 🪝
================================================

.. revealjs-notes::

   First, I will explain Simple integration with Incoming Webhooks.

System overview
---------------
.. image:: images/diagram-webhook.png

.. revealjs-notes::

   This is a system overview of Incoming Webhooks.
   When a program sends a message to a Webhook URL via HTTPS, the message will be sent to Slack.

**Create** Incoming Webhooks Integration 🔧
===========================================

**Create** Incoming Webhooks Integration
----------------------------------------
* Generate **Webhook URL**

  1. Create a Slack app
  2. Activate Incoming Webhooks in the app
  3. Add Webhook to Workspace
* see: `Sending messages using Incoming Webhooks <https://api.slack.com/messaging/webhooks>`_

.. revealjs-notes::

   How to generate a Webhook URL is as follows....

1. Create a Slack app
---------------------
* https://api.slack.com/apps

.. image:: images/create-webhook1-1.png
   :width: 50%

.. image:: images/create-webhook1-2.png
   :width: 50%

.. revealjs-break::
   :notitle:

* Enter name and choose workspace

.. image:: images/create-webhook2.png
   :width: 50%

.. revealjs-break::
   :notitle:

* Set app icon (optional)

.. image:: images/create-webhook3.png
   :width: 50%

* see: `Beer icons created by Freepik - Flaticon <https://www.flaticon.com/free-icons/beer>`_

2. Activate Incoming Webhooks
-----------------------------
.. image:: images/create-webhook4-1.png
   :width: 50%

3. Add Webhook to Workspace
---------------------------
* Click "Add New Webhook to Workspace"

.. image:: images/create-webhook4-2.png
   :width: 50%

.. revealjs-break::
   :notitle:

* Choose channel → Click "Allow"

.. image:: images/create-webhook5.png
   :width: 50%

.. revealjs-break::
   :notitle:

* Get **Webhook URL**: ``https://hooks.slack.com/...``

.. image:: images/create-webhook6.png
   :width: 50%

.. revealjs-notes::

   At last, we got a webhook URL
   Then let's send a message to Slack with the URL.

Post message via **Webhook URL** 📬
===================================

Post message with **cURL**
--------------------------

.. code-block:: bash

   $ curl -X POST -H 'Content-type: application/json' \
   > --data '{"text":"Hello Slack!"}' \
   > https://hooks.slack.com/services/T000...

.. image:: images/webhook-curl.png

.. revealjs-notes::

   We send a simple message with cURL.
   When we send a message with JSON, the message will be displayed in Slack.

Post message with **Python**
----------------------------
* see: `urllib.request <https://docs.python.org/3/library/urllib.request.html>`_

.. code-block:: python

   import json
   from urllib import request

   url = "https://hooks.slack.com/services/T000..."
   message = {"text": "Hello from Python!"}
   data = json.dumps(message).encode()
   request.urlopen(url, data=data)

.. image:: images/webhook-python.png

.. revealjs-notes::

   But we are pythonista.
   We use urllib.requests module.

Post message with **Requests**
------------------------------
* see: `Requests <https://docs.python-requests.org/en/latest/>`_

.. code-block:: bash

   $ pip install requests

.. code-block:: python

   import requests

   url = "https://hooks.slack.com/services/T000..."
   message = {"text": "Hello from Requests!"}
   r = requests.post(url, json=message)

.. image:: images/webhook-requests.png

.. revealjs-notes::

   It is easier to use Requests.

Post message with **Slack SDK**
-------------------------------
* see: `Python Slack SDK <https://slack.dev/python-slack-sdk/>`_

.. code-block:: bash

   $ pip install slack-sdk

.. code-block:: python

   from slack_sdk.webhook import WebhookClient

   url = "https://hooks.slack.com/services/T000..."
   webhook = WebhookClient(url)
   r = webhook.send(text="Hello from Slack SDK!")

.. image:: images/webhook-slacksdk.png

.. revealjs-notes::

   I also recommend the Python Slack SDK provided by Slack.

.. Slackが提供しているPython Slack SDKもおすすめです。

**Formatting** text
-------------------
* see: `Formatting text for app surfaces <https://api.slack.com/reference/surfaces/formatting>`_

.. revealjs-code-block:: python
   :data-line-numbers: 4-7

   from slack_sdk.webhook import WebhookClient

   url = "https://hooks.slack.com/services/T000..."
   webhook = WebhookClient(url)
   # *bold*, <url|text>, :emoji: and etc.
   r = webhook.send(text="*Hello* from "
     "<https://slack.dev/python-slack-sdk/|Slack SDK>! :beer:")

.. image:: images/webhook-formatting.gif

.. revealjs-notes::

   Text can be formatted as markdown
   If you want to create more complex messages,... use the Block Kit.

.. markdownっぽくテキストがフォーマットできます。

**Block** Kit 🧱
================

.. revealjs-notes::

   use the Block Kit !

**Block** Kit
-------------

.. image:: images/block-kit.png
   :width: 90%

* see: `Block Kit <https://api.slack.com/block-kit>`_

.. revealjs-notes::

   Block Kit is a new UI framework for Slack apps.

**Example** of Block Kit
------------------------
.. code-block:: python

   blocks = [{
       "type": "section",
       "text": {
            "text": "*THANK YOU* for coming to my talk !:tada: Please give me *feedback* about this talk :bow:",
            "type": "mrkdwn"
       },
       "fields": [
            {"type": "mrkdwn", "text": "*Love*"},
            {"type": "mrkdwn", "text": "*From*"},
            {"type": "plain_text", "text": ":beer:, Ferrets, LEGO"},
            {"type": "plain_text", "text": "Japan :jp:"},
       ],
   }]
   response = webhook.send(blocks=blocks)

.. image:: images/webhook-blocks.png

Block Kit **Builder**
---------------------
.. image:: images/block-kit-builder.gif
   :width: 80%

* `app.slack.com/block-kit-builder/ <https://app.slack.com/block-kit-builder/>`_

.. revealjs-notes::

   Block Kit Builder is useful for creating Blocks.
   We can write Block Kit code interactively and see the results visually.

Summary of Incoming **Webhooks**
================================
* **Easy** to post messages from programs 📬
* Create complex messages with **Block Kit** 🧱
* But **one-way** (program➡️Webhook➡️Slack)

.. revealjs-notes::

   I'd like to interact with the bot.
   Next,..

**Interactive** bot 🤝
======================

.. revealjs-notes::

   Next,..I will explain how to make an interactive bot.  

Connection protocols
--------------------
* Events API over HTTP
* Socket Mode
* see: `Choosing a protocol to connect to Slack <https://api.slack.com/apis/connections>`_

.. revealjs-notes::

   Slack provides 2 protocols for interacting.

.. Slackは2種類のプロトコルを用意しています

Events API over HTTP
--------------------

.. image:: images/diagram-eventsapi.png

* see: `Using the Slack Events API <https://api.slack.com/apis/connections/events-api>`_

.. revealjs-notes::

   In "Events API over HTTP",
   User messages will be Events API and Events API directly over HTTP.
   The protocol requires a public HTTP endpoint.


Socket Mode
-----------

.. image:: images/diagram-socketmode.png

* see: `Intro to Socket Mode <https://api.slack.com/apis/connections/socket>`_

.. revealjs-notes::

   On the other hand, Socket Mode does not require a static HTTP endpoint.
   Socket Mode allows you to receive Events API through a private WebSocket.

Connection protocols
--------------------
* Events API over HTTP
* **Socket Mode** 👈

.. revealjs-notes::

   I chose Socket Mode for this talk, because it is easy to develop locally.

.. * 公開するエンドポイントを用意するのが難しい場合はSocket Modeが便利
   * ここではSocket Modeで説明をしていく

**Create** bot user 🤖
======================

**Create** bot user
-------------------
* Create bot user with **Socket Mode**

  1. Create a Slack app (same procedure)
  2. Enable Socket Mode
  3. Subscribe bot event
  4. Add Bot Token Scopes
  5. Install App to Workspace
* Invite bot user to Slack channels

.. revealjs-notes::

   I describe how to create an interactive bot.
   At first, we create bot user on Slack.

1. Create a Slack app
---------------------
* Open https://api.slack.com/apps

.. image:: images/create-webhook1-1.png
   :width: 50%

.. image:: images/create-webhook1-2.png
   :width: 50%

.. revealjs-break::
   :notitle:

* Enter name and choose workspace

.. image:: images/create-bot2.png
   :width: 50%

.. revealjs-break::
   :notitle:

* Set app icon (optional)

.. image:: images/create-bot3.png
   :width: 50%

* see: `Beer icons created by Freepik - Flaticon <https://www.flaticon.com/free-icons/beer>`_

2. Enable Socket Mode
---------------------
* Select "Socket Mode" → Turn toggle on

.. image:: images/create-bot4.png
   :width: 70%

.. revealjs-break::
   :notitle:

* Enter token name → Click "Generate"

.. image:: images/create-bot5.png
   :width: 50%

.. revealjs-break::
   :notitle:

* Get **app-level token**: ``xapp-...``

.. image:: images/create-bot6.png
   :width: 50%

3. Subscribe bot event
----------------------
* Select "Event Subscriptions" → Turn toggle on

.. image:: images/create-bot3-1.png
   :width: 70%

.. revealjs-break::
   :notitle:

* Add "message.channels" to bot events

.. image:: images/create-bot3-2-1.png
   :width: 50%

.. image:: images/create-bot3-2-2.png
   :width: 50%

4. Add Bot Token Scopes
-----------------------
* Select "OAuth & Permissions"

.. image:: images/create-bot7.png
   :width: 80%

.. revealjs-break::
   :notitle:

* Click "Add on OAuth Scope"

.. image:: images/create-bot8.png
   :width: 80%

.. revealjs-break::
   :notitle:

* Add "chat:write" to Bot Token Scopes

.. image:: images/create-bot9.png
   :width: 50%

.. image:: images/create-bot10.png
   :width: 50%

5. Install App to Workspace
---------------------------
* Select "Install App" → Click "Install to Workspace"

.. image:: images/create-bot11.png
   :width: 80%

.. revealjs-break::
   :notitle:

* Switch OAuth screen → Click "Allow" button

.. image:: images/create-bot12.png
   :width: 50%

.. revealjs-break::
   :notitle:

* Get **Bot Token**: ``xoxb-...``

.. image:: images/create-bot13.png
   :width: 50%

Invite bot user to channels
---------------------------
.. image:: images/invite-bot.png
   :width: 50%

**Long** and **Complex** !! 🤯
===============================

.. revealjs-notes::

   The steps are long and complex !!
   Is there a better way ?
   I recommend... App Manifest.

.. ステップが長くて難しいですか?

App **Manifest** ⚙️
===================

.. revealjs-notes::

   I recommend... App Manifest.

App **Manifest**
----------------
* YAML-formatted configuration for Slack apps
* see: `Create and configure apps with manifests <https://api.slack.com/reference/manifests>`_

.. revealjs-notes::

   App Manifests are YAML-formatted configuration bundles for Slack apps.
   We can share and reuse manifests.

Example of App Manifest
-----------------------
.. code-block:: yaml

   display_information:
     name: beerbot2
   features:
     bot_user:
       display_name: beerbot2
       always_online: false
   oauth_config:
     scopes:
       bot:
         - channels:history
         - chat:write
   settings:
     event_subscriptions:
       bot_events:
         - message.channels
     interactivity:
       is_enabled: true
     org_deploy_enabled: false
     socket_mode_enabled: true
     token_rotation_enabled: false

Get App Manifest
----------------
* Select "App Manifest" menu

.. image:: images/get-app-manifest.png
   :width: 70%

Create new app with App Manifest
--------------------------------
* Select "From an app manifest"
* Select workspace → Click "Next"

.. image:: images/app-manifest1.png
   :width: 40%

.. image:: images/app-manifest2.png
   :width: 40%

.. revealjs-break::
   :notitle:

* Enter app manifest YAML

.. image:: images/app-manifest3.png
   :width: 46%

.. revealjs-break::
   :notitle:

* Review app summary → Click "Create"

.. image:: images/app-manifest4.png
   :width: 35%

.. image:: images/app-manifest5.png
   :width: 35%

.. image:: images/app-manifest6.png
   :width: 35%

.. revealjs-break::
   :notitle:

* Install App to Workspace

.. image:: images/app-manifest7.png
   :width: 70%

.. revealjs-break::
   :notitle:

* Generate App-Level Token

.. image:: images/app-manifest8.png
   :width: 45%

.. image:: images/app-manifest9.png
   :width: 45%


**Short** and **Reusable** !! 🥳
=================================

.. revealjs-notes::

   App Manifest makes steps shorter and reusable.
   Now we are ready to start creating an interactive bot.

Create bot with **Bolt** ⚡️
============================

.. revealjs-notes::

   Let's create a bot with Bolt !
   What is Bolt?

Bolt for Python
---------------
* Python framework to build Slack app in a **flash**
* Developped by **Slack**
* :fab:`github` `github.com/slackapi/bolt-python <https://github.com/slackapi/bolt-python>`_
* see:

  * `Bolt for Python <https://slack.dev/bolt-python/concepts>`_
  * `The Bolt family of SDKs <https://api.slack.com/tools/bolt>`_ (JavaScript, Java)

.. revealjs-notes::

   Bolt is a Python ... flash.
   Slack also provides Bolt for JavaScript and Java.

**Install** Bolt for Python
---------------------------
.. code-block:: bash

   $ mkdir beerbot
   $ cd beerbot
   $ python3.10 -m venv env
   $ . env/bin/activate
   (env) $ pip install slack-bolt

**Create** a simple bot with Bolt
---------------------------------
.. literalinclude:: code/app1.py
   :language: python
   :caption: app.py

.. revealjs-notes::

   When the bot receives the string "Hi", bot sends a greeting message.

**Running** bot
---------------
.. code-block:: bash

   # Set 2 tokens in environment variables
   (env) $ export SLACK_APP_TOKEN=xapp-...
   (env) $ export SLACK_BOT_TOKEN=xoxb-...
   (env) $ python app.py
   ⚡️ Bolt app is running!

.. image:: images/bot-hi.png

.. revealjs-notes::

   Set 2 tokens in environment variables, then run app.py.
   When I write a message "Hi" on Slack, the bot responds!

I can **interact** with the bot ! 🎉
-------------------------------------

.. image:: images/bot-hi.png

.. revealjs-notes::

   But this is simple enough, so...

**Extend** bot 🛠
=================

.. revealjs-notes::

   so I will extend the bot.

``@app.message()`` decolator
----------------------------
.. literalinclude:: code/app-extend.py
   :lines: 13-23

.. image:: images/bot-decolator.png
   :width: 30%

.. revealjs-notes::

   app.message() decolator executes the function when it matches the pattern.

mention
-------
.. literalinclude:: code/app-extend.py
   :lines: 25-30

.. image:: images/bot-mention.png
   :width: 30%

.. revealjs-notes::

   The bot can send mentions

Using regular expression
------------------------
.. literalinclude:: code/app-extend.py
   :lines: 3-4,31-38

.. image:: images/bot-choice.png
   :width: 30%

.. revealjs-notes::

   Bolt can handle parameters.
   We use regular expressions in app.message() decolator, you can extract matched strings from context["matches"]

.. revealjs-break::

.. literalinclude:: code/app-extend.py
   :lines: 39-45

.. image:: images/bot-beers.png
   :width: 70%

Block Kit support
-----------------
.. literalinclude:: code/app-extend.py
   :lines: 46-61

.. image:: images/bot-followme.png
   :width: 60%

Logging
-------
.. literalinclude:: code/app-extend.py
   :lines: 1,11,78-83

.. code-block:: bash

   $ python app.py
   ⚡️ Bolt app is running!
   DEBUG:app.py:handle_log:message: log
   DEBUG:app.py:handle_log:message: please write log

.. image:: images/bot-logging.png
   :width: 25%

**Events** and **Scopes** 🔭
============================

Events and Scopes
-----------------
* Can only receive events in **Bot Events**
* Can only execute APIs allowed by **Bot Token Scopes**
  
.. revealjs-notes::

   Events and Scopes are important concepts in Slack Bots.
   Bot can only receive events in **Bot Events**.
   Bot aan only execute APIs allowed by **Bot Token Scopes**.

Current Bot Events and Scopes
-----------------------------

* Events

  :message.channels: message posted to **public channels**

* Scopes

  :channels:history: View messages in **public channels**
  :chat:write: Post message

.. revealjs-notes::

   For example, the current bot event is message.channel, bot scopes are channels:history and chat:write only.

.. revealjs-break::

* Cannot read/write messages on **private channels**

.. image:: images/bot-private-cannot-view.png
   :width: 50%

.. revealjs-notes::

   So, the bot cannot read/write messages on private channels.
   I invited the bot to a private channel and sent a "Hi" message but no response!
   What shoud I do?

Add Events and Scopes for private channels
------------------------------------------

* Select "Event Subscriptions" → Click "Add Bot User Event"
* Add **message.groups** event→ Click "Save Changes"

.. image:: images/add-events-and-scopes1.png
   :width: 50%

.. revealjs-notes::

   I need to add events and scopes for private channels.
   I added a "message.groups" event.

.. revealjs-break::

* Select "OAuth & Permissions"
* **groups:history** scope is automatically added

.. image:: images/add-events-and-scopes2.png
   :width: 50%

.. revealjs-notes::

   "groups:history" scope is automatically added

.. revealjs-break::

* **Reinstall** app to workspace

.. image:: images/add-events-and-scopes3.png
   :width: 50%

.. image:: images/add-events-and-scopes4.png
   :width: 40%

.. revealjs-notes::

   I will reinstall the app because of the change in events and scopes.

.. revealjs-break::

* Bot can read/write messages in **private channel**

.. image:: images/add-events-and-scopes6.png
   :width: 40%

.. revealjs-notes::

   Then, the bot can read/write messages in **private channel**

To know user joined a channel
-----------------------------
* Add **member_joined_channel** event → Reinstall app

.. literalinclude:: code/app-extend.py
   :emphasize-lines: 1-2
   :lines: 60-66

.. image:: images/event-member-joined.png
   :width: 40%

.. revealjs-notes::

   If you want to know when a user joins a channel, add a "member_joind_channel" event.
   And You can handle the event with @app.event decorator.

Add Emoji reaction
------------------
* Add **reactions:write** scope → Reinstall app

.. literalinclude:: code/app-extend.py
   :language: python
   :lines: 67-76

.. image:: images/scope-reactions-write.png
   :width: 50%

.. revealjs-notes::

   If you want to add emoji reactions, add a "reactions:write" scope.

**Summary** of Events and Scopes
--------------------------------
* To receive new events
* To use new API with new scopes
* Add **events** and/or **scopes** → Reinstall app
* see: `Events API types <https://api.slack.com/events>`_
* see: `Permission scopes <https://api.slack.com/scopes>`_

Case studies 📚
================

Calculator function using **SymPy** 🔢
=======================================

Calculator function using **SymPy**
-----------------------------------

* Motivation

  * I feel heavy to call a calculator app on my smartphone
  * It seems useful if **Slack as a calculator**

System overview
---------------
.. image:: images/diagram-sympy.png

about **SymPy**
---------------
.. image:: https://www.sympy.org/static/images/logo.png

* **SymPy**: Python library for symbolic mathematics
* `www.sympy.org <https://www.sympy.org>`_

.. code-block:: bash

   $ pip install sympy

**calc()** function using Sympy
-------------------------------

.. literalinclude:: code/app-sympy.py
   :language: python
   :lines: 6,10-24

Slack as a **calculator** !!
----------------------------

.. image:: images/case-sympy.png
   :width: 30%

Plus-plus feature using **Peewee ORM** 👍
==========================================

Plus-plus feature using **Peewee ORM**
--------------------------------------
* Motivation

  * In PyCon JP, I want to make a culture that **appreciates** each other staff 👍

System overview
---------------
.. image:: images/diagram-peewee.png

about **Peewee**
----------------
.. image:: https://docs.peewee-orm.com/en/latest/_images/peewee3-logo.png
   :width: 40%

* Simple and small ORM.

  * a small, expressive ORM
  * supports sqlite, mysql and postgresql

* `docs.peewee-orm.com <https://docs.peewee-orm.com/>`_

.. code-block:: bash

   $ pip install peewee

plusplus_model.py
-----------------
.. literalinclude:: code/plusplus_model.py

**plusplus()** function using Peewee
------------------------------------
.. literalinclude:: code/app-plusplus.py
   :language: python
   :lines: 6, 10-22

I can **appreciate** it!
------------------------

.. image:: images/case-peewee.png
   :width: 40%

Search issues with **Jira APIs** 🔎
====================================

Search issues with **Jira APIs**
--------------------------------
* Motivation

  * Jira is very useful
  * Jira Web is **slow**
  * Search issues **without Jira Web**

System overview
---------------
.. image:: images/diagram-jira.png

about **Python Jira**
---------------------
* Python library to work with Jira APIs
* `jira.readthedocs.io <https://jira.readthedocs.io/>`_

.. code-block:: bash

   $ pip install jira

Authentication
--------------
* Create an API token

  * see: `Manage API tokens for your Atlassian account <https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/>`_

.. code-block:: python

   from jira import JIRA

   url = 'https://jira.atlassian.com/'
   jira = JIRA(url, basic_auth=('email', 'API token'))

* see: `2.1.2. Authentication <https://jira.readthedocs.io/examples.html#authentication>`_

Search issues
-------------
.. literalinclude:: code/app-jira.py
   :lines: 15-29

* see: `2.1.6. Searching <https://jira.readthedocs.io/examples.html#searching>`_
* see: `JQL: Get started with advanced search in Jira <https://www.atlassian.com/software/jira/guides/expand-jira/jql#advanced-search>`_

**Free** from Jira web!
-----------------------
.. image:: images/bot-jira.png
   :width: 60%

Create **multiple issues** from a template 📝
=============================================

Create **multiple issues** from a template
------------------------------------------
* Motivation

  * In pycamp event, **20+ issues** are required for each event
  * Copying issues by hand is **painful**
  * Jira Web is **slow** (again)

System overview
---------------
.. image:: images/diagram-template.png

Google Authorization is Complex
-------------------------------
* Create a Google Cloud project

  * Enable API(in this case: Google Sheets API)
  * Download ``credentials.json``
* Install Google Client Library

  .. code-block:: bash

     $ pip install google-api-python-client \
       google-auth-httplib2 google-auth-oauthlib

* Download `quickstart.py <https://github.com/googleworkspace/python-samples/blob/master/sheets/quickstart/quickstart.py>`_ from GitHub

.. revealjs-break::

* Run ``quickstart.py``

  * Select your Google account in Web browser
  * Click "Accept" button
  * Get ``token.json`` (finish!!)

.. code-block:: bash

   $ python quickstart.py
   Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?....
   Name, Major:
   Alexandra, English
   :

* see: `Python Quickstart | Sheets API <https://developers.google.com/sheets/api/quickstart/python>`_

Issue template
--------------
.. image:: images/bot-issue-template.png

Get Spreadsheet data
--------------------
.. code-block:: python

   from google.oauth2.credentials import Credentials
   from googleapiclient.discovery import build

   SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
   SHEET = "1i3YQPObe3ZC_i1Jalo44_2_..."

   @app.message("create issues")
   def creaete_issues(message, say):
       creds = Credentials.from_authorized_user_file('token.json', SCOPES)
       service = build('sheets', 'v4', credentials=creds)
       sheet = service.spreadsheets()
       result = sheet.values().get(spreadsheetId=SHEET, range="A2:C4").execute()
       for row in result.get("values", []):
           say(f"* Title: {row[0]}, Delta: {row[1]}")

* see: `Method: spreadsheets.values.get | Sheets API <https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values/get>`_

.. revealjs-break::

.. image:: images/bot-sheet1.png
   :width: 50%

Create Jira issues
------------------
.. literalinclude:: code/app-sheet.py
   :lines: 21, 27-39
   :language: python

* see: `2.1.4. Issues <https://jira.readthedocs.io/examples.html#issues>`_

**Free** from copying issues!
-----------------------------
.. image:: images/bot-sheet2.png
   :width: 30%

.. image:: images/bot-sheet3.png
   :width: 70%

**Account management** of Google Workspace 👥
==============================================

**Account management** of Google Workspace
------------------------------------------
* Motivation

  * PyCon JP Association use ``pycon.jp`` domain with Google Workspace
  * I only use Google Admin web occasionally
  * I **forgot** to use admin screen

System overview
---------------
.. image:: images/diagram-directory.png

Update Google Authorization
---------------------------
* Update a Google Cloud project

  * add **Directory API**
  * re-download ``credentials.json``
* Remove ``token.json``
* Add **Directory API** ``quickstart.py``

  * Re-run ``quickstart.py``
  * Get new ``token.json``

Get user list
-------------
.. literalinclude:: code/app-admin.py
   :language: python
   :lines: 11, 13-26

* see: `Method: users.list | Directory API <https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/list>`_

.. revealjs-break::

.. image:: images/bot-user-list.png
   :width: 50%

Add user
--------
.. literalinclude:: code/app-admin.py
   :language: python
   :lines: 28-42

* see: `Method: users.insert | Directory API <https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/insert>`_

.. revealjs-break::

.. image:: images/bot-user-add.png
   :width: 40%

.. image:: images/bot-user-add2.png
   :width: 80%

I can **forget** Google Admin!
------------------------------

Summary 
=======
* Simple bot using **Incoming Webhooks**
* Interactive bot using **Bolt** for Python
* Extend bot using **libraries** and **APIs**

Next Step 🪜
============

* Let's make **your Slackbot**
* Let's connect with **libraries** and **APIs**
* **Automate your Boring Stuff** with Slackbot

.. Then you will have more free time so you can do other creative things more.

Thank you! 🙏
==============
.. image:: images/bot-translate.png
   :width: 80%

:fab:`twitter` `@takanory <https://twitter.com/takanory>`_

:fas:`desktop` `slides.takanory.net <https://slides.takanory.net>`__

:fas:`code` `github.com/takanory/slides/tree/master/slides/20220713europython/code <https://github.com/takanory/slides/tree/master/slides/20220713europython/code>`__

translate command
-----------------
.. code-block:: bash

   $ pip install deepl

.. literalinclude:: code/app-deepl.py
   :lines: 6, 9-10, 12-18

Thank you! 🙏
--------------
.. image:: images/bot-translate.png
   :width: 80%

:fab:`twitter` `@takanory <https://twitter.com/takanory>`_

:fas:`desktop` `slides.takanory.net <https://slides.takanory.net>`__

:fas:`code` `github.com/takanory/slides/tree/master/slides/20220713europython/code <https://github.com/takanory/slides/tree/master/slides/20220713europython/code>`__
