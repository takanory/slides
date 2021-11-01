=============================================
 Introduction to Structural Pattern Matching
=============================================

Takanori Suzuki

PyCon APAC 2021 / 2021 Nov 20

.. 見てくれてありがとう。今日はこれについて話すよ的な


Agenda
======
* Motivation
* What's New
* Syntax
* Patterns

.. 今日話すことをざっくり説明

Photos 📷 Tweets 🐦 👍
========================
``#pyconapac`` / ``@takanory``

.. I'd be happy to take pictures and share them and give you feedback on Twitter, etc.
   Hashtag is #pyconapac

Slide
-----
`slides.takanory.net <https://slides.takanory.net>`__

.. This slide available on slides.takanory.net.
   And I've already shared this slide on Twitter.
   Please check it out #pyconapac.

Who am I? 👤
=============
* Takanori Suzuki / 鈴木 たかのり (|twitter| `@takanory <https://twitter.com/takanory>`_)
* `PyCon JP Association <https://www.pycon.jp/>`_
* `BeProud Inc. <https://www.beproud.jp/>`_
* `Python Boot Camp <https://www.pycon.jp/support/bootcamp.html>`_, `Python mini Hack-a-thon <https://pyhack.connpass.com/>`_, `Python Bouldering Club <https://kabepy.connpass.com/>`_

.. image:: /assets/images/sokidan-square.jpg

.. Before the main topic,...I will introduce myself.
   I'm Takanori Suzuki. My twitter is "takanory", please follow me.
   I'm Vice-Chairperson of PyCon JP Association.
   And I'm director of BeProud Inc.
   I'm also active in several Python related communities

Questions
=========

.. First, I have questions

Have you used Python 3.10? 🙋‍♂️
--------------------------------

Do you know the new features? 🙋‍♀️
-----------------------------------
.. Do you know the new features in 3.10?

Motivation of this talk 💪
===========================

.. このトークのモチベーション
   3.10で色々新機能が増えている
   Structural Pattern Matchingはかなり便利そう
   みんなに知って使ってみてほしい

Goal of this talk 🥅
=====================
.. Python 3.10の新機能の概要を知る
   Structural Pattern Matchingの基本的な使い方を知る
   明日から試せる

What's New in Python 3.10 🆕
=============================

.. revealjs-break::

* `docs.python.org/3/whatsnew/3.10.html <https://docs.python.org/3/whatsnew/3.10.html>`_

.. image:: images/whatsnew.png
   :alt: What's New in Python 3.10

.. Before main topic. I will introduce to the new features of 3.10.
   3.10の新機能について紹介します

Python Release Python 3.10.0
----------------------------
* `www.python.org/downloads/release/python-3100/ <https://www.python.org/downloads/release/python-3100/>`_
* Release Date: Oct. 4, 2021

.. image:: images/python3100.png
   :alt: Python Release Python 3.10.0

.. Python 3.10 has many new features...By the way...

Who are You? 🐍
----------------

.. image:: https://user-images.githubusercontent.com/11718525/135937807-fd3e0fd2-a31a-47a4-90c6-b0bb1d0704d4.png
   :alt: Python 3.10 release logo

.. This image is "Python 3.10 release logo".
   You can find the new features of 3.10 around this snake.

Parenthesized Context Managers
------------------------------
.. code-block:: python

   # 3.10
   with (
       open('craftbeer.txt') as f1,
       open('beer-in-kanda.txt') as f2,
   ):
       ...

.. code-block:: python

   # Before 3.10
   with open('craftbeer.txt') as f1, \
        open('beer-in-kanda.txt') as f2
       ...

Better Error Messages
---------------------
.. code-block:: python

   # Brackets are not closed
   beer_types = ['Pilsner', 'Ale', 'IPA', 'Hazy IPA'
   print(beer_types)

.. revealjs-code-block:: text
   :data-line-numbers: 3-5

   $ python3.10 beer_styles.py
     File ".../beer_styles.py", line 2
       beer_styles = ['Pilsner', 'Ale', 'IPA', 'Hazy IPA'
                     ^
   SyntaxError: '[' was never closed

.. revealjs-code-block:: text
   :data-line-numbers: 3-5

   $ python3.9 beer_styles.py
     File ".../beer_styles.py", line 3
       print(beer_styles)
       ^
   SyntaxError: invalid syntax

Better Error Messages
---------------------
.. revealjs-code-block:: python
   :data-line-numbers: 3-6

   # 3.10
   >>> if beer_syle = 'IPA':
     File "<stdin>", line 1
       if beer_syle = 'IPA':
          ^^^^^^^^^^^^^^^^^
   SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

.. revealjs-code-block:: python
   :data-line-numbers: 3-5

   # Before 3.10
   >>> if beer_syle = 'IPA':
     File "<stdin>", line 1
       if beer_syle = 'IPA':
                    ^
   SyntaxError: invalid syntax

Better Typing Syntax
--------------------
* `PEP 604 <https://www.python.org/dev/peps/pep-0604>`_: New Type Union Operator

  * ``Union[X, Y]`` → ``X | Y``
  * ``Optional[X]`` → ``X | None``

.. revealjs-code-block:: python
   :data-line-numbers: 2

   # 3.10
   def drink_beer(number: int | float) -> str | None
       if am_i_full(number):
           return 'I'm full'

.. revealjs-code-block:: python
   :data-line-numbers: 2

   # Before 3.10
   def drink_beer(number: Union[int, float]) -> Optional[str]
       if am_i_full(number):
           return 'I'm full'

.. revealjs-break::

* `PEP 613 <https://www.python.org/dev/peps/pep-0613>`_: TypeAlias

.. code-block:: python

   # 3.10
   BeerStr: TypeAlias = 'Beer[str]'  # a type alias
   LOG_PREFIX = 'LOG[DEBUG]'  # a module constant

.. code-block:: python

   # Before 3.10
   BeerStr = 'Beer[str]'  # a type alias
   LOG_PREFIX = 'LOG[DEBUG]'  # a module constant

.. revealjs-break::

.. revealjs-code-block:: python
   :data-line-numbers: 2, 4

   # Python 3.7-3.9
   from __future__ import annotations

   def drink_beer(number: int | float) -> str | None
       if am_i_full(number):
           return 'I'm full'

What's New in Python 3.10 🆕
----------------------------
* Parenthesized Context Managers
* Better Error Messages
* Better Typing Syntax
* **Structural Pattern Matching**

Structural Pattern Matching 🏛
==============================

.. revealjs-break::

* `PEP 634 – Structural Pattern Matching: Specification <https://www.python.org/dev/peps/pep-0634/>`_
* `PEP 635 – Structural Pattern Matching: Motivation and Rationale <https://www.python.org/dev/peps/pep-0635/>`_
* `PEP 636 – Structural Pattern Matching: Tutorial <https://www.python.org/dev/peps/pep-0636/>`_

Motivation
----------
`www.python.org/dev/peps/pep-0635/#motivation <https://www.python.org/dev/peps/pep-0635/#motivation>`_

  (Structural) pattern matching syntax is found in many languages, from Haskell, Erlang and Scala to Elixir and Ruby. (A proposal for JavaScript is also under consideration.)

.. revealjs-break::
   :notitle:

.. code-block:: python

   if isinstance(x, tuple) and len(x) == 2:
       host, port = x
       mode = "http"
   elif isinstance(x, tuple) and len(x) == 3:
       host, port, mode = x

.. code-block:: python

   # Structural Pattern Matching
   match x:
       case host, port:
           mode = "http"
       case host, port, mode:
           pass

.. isinstance()で型をチェックして中身を見て、みたいなのをよくやるけど、それがもっとエレガントに書ける
   
Syntax |code|
=============
Generic syntax of pattern matching

.. revealjs-code-block:: python
   :data-line-numbers: 1|2-9

   match subject:
       case <pattern_1>:
           <action_1>
       case <pattern_2>:
           <action_2>
       case <pattern_3>:
           <action_3>
       case _:
           <action_wildcard>

.. A match statement takes an expression ... and compares its value to successive patterns given as one or more case blocks

Soft keywords
-------------
* New in Pytohn 3.10
* ``match``, ``case`` and ``_``
* Can be used identifier names

.. code-block:: python

   >>> match = 'match'  # Soft keyword
   >>> class = 'class'  # Keyword
     File "<stdin>", line 1
       class = 'class'
             ^
   SyntaxError: invalid syntax

.. 新しくソフトキーワードができた。
   match, case, _はソフトキーワード。
   ソフトキーワードは識別子に使用できる
   では、実際の書き方を説明していきます。

Patterns |random|
=================
.. revealjs-break::

.. code-block:: python

   match subject:
       case <pattern_1>:
           <action_1>
       case <pattern_2>:
           <action_2>
       case <pattern_3>:
           <action_3>
       case _:
           <action_wildcard>

.. これはsyntaxですが、patternにはさまざまなpattensを指定できます。
   いくつかを紹介していきます。

Simple pattern
--------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-7|1,8-9

   match beer_style:
       case "Pilsner":
           return "First drink"
       case "IPA":
           return "I like it"
       case "Hazy IPA":
           return "Cloudy and cloudy"
       case _:
           return "I like most beers"

.. beer_styleの中身がXXXならYYYを返します。
   どれもマッチしなければワイルドカードの _ にマッチします。

.. revealjs-break::

* ``|`` is OR   

.. revealjs-code-block:: python
   :data-line-numbers: 4-5

   match beer_style:
       case "Pilsner":
           return "First drink"
       case "IPA" | "Session IPA":
           return "I like it"
       case "Hazy IPA":
           return "Cloudy and cloudy"
       case _:
           return "I like most beers"

.. revealjs-break::

* without whildcard

.. revealjs-code-block:: python

   match beer_style:
       case "Pilsner":
           return "First drink"
       case "IPA":
           return "I like it"
       case "Hazy IPA":
           return "Cloudy and cloudy"

.. 最後のワイルドカードを削除する。
   それ以外を選んだらなにも起こらない。
