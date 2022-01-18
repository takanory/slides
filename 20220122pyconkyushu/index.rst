=================================================
 Introduction to **Structural Pattern Matching**
=================================================

Takanori Suzuki

PyCon Kyushu 2022 Kumamoto / 2022 Jan 22

.. イベントの開催おめでとうございます。
   また、私のトークに参加してくれてありがとうございます。
   今日は「...」について話します

Agenda / アジェンダ
===================
* Motivation / モチベーション
* What's New / 更新情報
* Syntax / 構文
* Patterns / パターン

.. トークのアジェンダ。
   モチベーションとゴール。
   Python 3.10の新機能を紹介。
   構造的パターンマッチングの構文。
   様々なパターンをコード例と一緒に説明。

Photos 📷 Tweets 🐦 👍
========================
``#PyConK`` / ``@takanory``

.. 写真やツイートなどご自由に。

Slide 💻
---------
`slides.takanory.net <https://slides.takanory.net>`__

.. スライドは公開済み。
   TwitterでURLも共有済み

Who am I? / お前誰よ 👤
========================
* Takanori Suzuki / 鈴木 たかのり (|twitter| `@takanory <https://twitter.com/takanory>`_)
* `PyCon JP Association <https://www.pycon.jp/>`_: 副代表理事
* `BeProud <https://www.beproud.jp/>`_: 取締役 / Python Climber
* `Python Boot Camp <https://www.pycon.jp/support/bootcamp.html>`_, `Python mini Hack-a-thon <https://pyhack.connpass.com/>`_, `Python Bouldering Club <https://kabepy.connpass.com/>`_

.. image:: /assets/images/sokidan-square.jpg

この発表の **モチベーション** 💪
=================================
* Structural Pattern Matching は **便利そう**
* みんなに **知って**、**使って** みてほしい

.. 本題に入ります。
   Python 3.10にたくさんの新機能がある。
   中でも構造的パターンマッチングはかなり便利そう。
   みんなにも知ってほしい、使ってみてほしい

この発表の **ゴール** 🥅
-------------------------
* **構文** と **基本的な使い方** を知る
* さまざまな **パターン** と、その **使い方** を知る
* 明日から **試せる**

前提条件
--------
* **中級** レベル
* **Pythonの文法** を理解している

  * タプル、リスト、辞書、if、def、isinstance、データクラス、型ヒントなど

.. このトークは中級レベル。
   Pythonの文法を基本的に理解している

質問
====

Python 3.10を使ってますか? 🙋‍♂️
--------------------------------

3.10の新機能を知ってますか? 🙋‍♀️
---------------------------------

**What's New** in Python 3.10 🆕
=================================

.. Python 3.10の新機能について紹介します

**What's New** in Python 3.10 🆕
---------------------------------
* `docs.python.org/3/whatsnew/3.10.html <https://docs.python.org/3/whatsnew/3.10.html>`_

.. image:: images/whatsnew.png
   :alt: What's New in Python 3.10

.. Python公式ドキュメントのWhat's Newに新機能がまとまっている

Python Release Python 3.10.0
----------------------------
`www.python.org/downloads/release/python-3100/ <https://www.python.org/downloads/release/python-3100/>`_

.. image:: images/python3100.png
   :width: 70%
   :alt: Python Release Python 3.10.0

.. Python 3.10は10月4日にリリースされた。
   3.10.2が最新。
   3.10には新機能がたくさんあるが...

お前誰よ? 🐍
----------------
.. image:: https://user-images.githubusercontent.com/11718525/135937807-fd3e0fd2-a31a-47a4-90c6-b0bb1d0704d4.png
   :width: 70%
   :alt: Python 3.10 release logo

.. この画像はPython 3.10 release logo。
   ヘビのまわりに3.10の新機能が書いてある

Python 3.10の **新機能**
------------------------
* Parenthesized Context Managers
* Better Typing Syntax
* Better Error Messages
* Structural Pattern Matching
* Better Debugging

.. 5つの主要な新機能がロゴに書いてある。
   Parenthesized...

Python 3.10の **新機能**
------------------------
* Parenthesized Context Managers
* Better Typing Syntax
* Better Error Messages
* **Structural Pattern Matching** 👈
* Better Debugging

.. このトークではStructural Pattern Matchingについて話す

Structural Pattern Matching 🏛
==============================

.. revealjs-break::

* Structural Pattern Matchingの **PEP**

  * `PEP 634 – Specification <https://www.python.org/dev/peps/pep-0634/>`_
  * `PEP 635 – Motivation and Rationale <https://www.python.org/dev/peps/pep-0635/>`_
  * `PEP 636 – Tutorial <https://www.python.org/dev/peps/pep-0636/>`_

.. 機能が大きいため3つのPEPに分かれている。
   Specification、Motivation and Rationale、Tutorial。
   興味のある方は、PEPを読んでみて

モチベーション
--------------
`www.python.org/dev/peps/pep-0635/#motivation <https://www.python.org/dev/peps/pep-0635/#motivation>`_

  (Structural) pattern matching syntax is found in many languages, from Haskell, Erlang and Scala to Elixir and Ruby. (A proposal for JavaScript is also under consideration.)

.. この文章はPEPに書いてあるパターンマッチングのモチベーション

.. revealjs-break::

`www.python.org/dev/peps/pep-0635/#motivation <https://www.python.org/dev/peps/pep-0635/#motivation>`_

  (構造的)パターンマッチの構文は、Haskell、Erlang、ScalaからElixir、Rubyなど、多くの言語で見られます(JavaScriptへの提案も検討中)。

.. 日本語にするとこんな感じ

.. revealjs-break::

.. code-block:: python

   # オブジェクトの型や形を確認する
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

.. if-elif-elseは、オブジェクトの型や形のチェックによく使われる。
   isinstance(), hasattr(), len(), dictのkeyなど。
   match文を使えば、よりエレガントに書くことができる。
   これがStructural Pattern Matchingのモチベーション。
   さて、モチベーションがわかったところで、構文について説明します

構文 |code|
===========
* Pattern Matchingの基本的な構文

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

.. match文は、式を受け取り...その値をcaseブロックの連続したパターンと比較する

**ソフト** キーワード
---------------------
* Python 3.10の **新仕様**
* ``match``、``case``、``_``
* **識別子** に使用可能

.. code-block:: python

   >>> match = 'match'  # OK
   >>> class = 'class'  # NG
     File "<stdin>", line 1
       class = 'class'  # NG
             ^
   SyntaxError: invalid syntax

.. ソフトキーワードは新しい言語仕様。
   match, case, _はソフトキーワード。
   ソフトキーワードは識別子に使用可能。
   では、パターンについて説明します。

パターン |random|
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

.. This is the syntax I introduced before.
   You can specify various patterns after case.
   I will introduce patterns with code examples.

.. これはsyntaxですが、patternにはさまざまなpattensを指定できます。
   いくつかを紹介していきます。

.. これは前に紹介した構文。
   caseの後にいろいろなパターンを指定できる。
   パターンをコード例で紹介する。


**リテラル** パターン
---------------------
.. revealjs-code-block:: python
   :data-line-numbers: 1-9|1-3|1,8-9

   match beer_style:
       case "Pilsner":
           result = "First drink"
       case "IPA":
           result = "I like it"
       case "Hazy IPA":
           result = "Cloudy and cloudy"
       case _:
           result = "I like most beers"

.. 最初はリテラルパターン。リテラルパターンはシンプルなパターン。
   (ページ送り)
   beer_styleの値が"Pilsner"の場合ここが実行される。
   (ページ送り)
   値がどのパターンにもマッチしないと_にマッチする。
   _はワイルドカード。

**OR** パターン
---------------
* ``|`` は OR

.. revealjs-code-block:: python
   :data-line-numbers: 1,4-5

   match beer_style:
       case "Pilsner":
           result = "First drink"
       case "IPA" | "Session IPA":
           result = "I like it"
       case "Hazy IPA":
           result = "Cloudy and cloudy"
       case _:
           result = "I like most beers"

.. このパターンはIPAまたはSession IPAにマッチする

**wildcardなし** のLiteralパターン
----------------------------------
.. revealjs-code-block:: python

   match beer_style:
       case "Pilsner":
           result = "First drink"
       case "IPA":
           result = "I like it"
       case "Hazy IPA":
           result = "Cloudy and cloudy"
       # case _:
       #     result = "I like most beers"

.. 最後のワイルドカードをコメントアウト。
   beer_styleの値がどれにもマッチしなければなにも起こらない

? 🤔
-----

.. あれ?あんまり便利そうに見えない?

**if** 文で書き換える
---------------------
* ``if`` 文で書いた場合

.. code-block:: python

   if beer_style == "Pilsner":
       result = "First drink"
   elif beer_style == "IPA" or beer_style == "Session IPA":
       result =  "I like it"
   elif beer_style == "Hazy IPA":
       result = "Cloudy and cloudy"
   else:
       result = "I like most beers"

.. if文で書き換えてみると、あんまり変わらないように見える。
   あなたの考えは正しい。
   ですが...

Pattern Matchingは **パワフル** 💪
-----------------------------------
.. ですが...Pattern Matchingはもっとパワフル。
   便利なパターンを紹介する。

リテラルと **変数** パターン
============================

リテラルと **変数** パターン
----------------------------
* 長さ2のタプルが注文を表す

.. revealjs-code-block:: python

   order1 = ("IPA", "nuts")  # ビールとフード
   order2 = ("Pilsner", "")  # ビールのみ
   order3 = ("", "fries")    # フードのみ
   order4 = ("", "")         # なにも注文しない
   
   order_beer_and_food(order1)  # -> I dring IPA with nuts.

リテラルと **変数** パターン
----------------------------
.. revealjs-code-block:: python

   def order_beer_and_food(order: tuple) -> str:
       match (order):
           case ("", ""):
               return "Please order something."
           case (beer, ""):
               return f"I drink {beer}."
           case ("", food):
               return f"I eat {food}."
           case (beer, food):
               return f"I drink {beer} with {food}."
           case _:
               return "one beer and one food only."

.. ビールとフードの注文タプルを受け取る関数を考えてみます。

リテラルと **変数** パターン
----------------------------
.. revealjs-code-block:: python
   :data-line-numbers: 1-4,14

   def order_beer_and_food(order: tuple) -> str:
       match (order):
           case ("", ""):  # match here
               return "Please order something."
           case (beer, ""):
               return f"I drink {beer}."
           case ("", food):
               return f"I eat {food}."
           case (beer, food):
               return f"I drink {beer} with {food}."
           case _:
               return "one beer and one food only."

   order_beer_and_food(("", ""))  # -> Please order something.

.. 注文が(空, 空)の場合、3行目にマッチし戻り値は"Please order something."

リテラルと **変数** パターン
----------------------------
* ``"IPA"`` が ``beer`` に代入

.. revealjs-code-block:: python
   :data-line-numbers: 1-2,5-6,14

   def order_beer_and_food(order: tuple) -> str:
       match (order):
           case ("", ""):
               return "Please order something."
           case (beer, ""):  # match here
               return f"I drink {beer}."
           case ("", food):
               return f"I eat {food}."
           case (beer, food):
               return f"I drink {beer} with {food}."
           case _:
               return "one beer and one food only."

   order_beer_and_food(("IPA", ""))  # -> I drink IPA.

.. 注文が("IPA", 空)の場合、5行目にマッチする。
   そしてタプルの最初の値(IPA)がbeer変数に代入される。
   結果は"I drink IPA."

リテラルと **変数** パターン
----------------------------
* ``"IPA"`` が ``beer`` に代入
* ``"nuts"`` が ``food`` に代入

.. revealjs-code-block:: python
   :data-line-numbers: 1-2,9-10,14

   def order_beer_and_food(order: tuple) -> str:
       match (order):
           case ("", ""):
               return "Please order something."
           case (beer, ""):
               return f"I drink {beer}."
           case ("", food):
               return f"I eat {food}."
           case (beer, food):  # match here
               return f"I drink {beer} with {food}."
           case _:
               return "one beer and one food only."

   order_beer_and_food(("IPA", "nuts"))  # -> I drink IPA with nuts.

.. 注文が("IPA", "nuts")の場合、9行目にマッチ。
   最初の値(IPA)がbeer変数に代入、2番目の値(nuts)がfood変数に代入。
   結果は"I drink IPA with nuts."

リテラルと **変数** パターン
----------------------------
* タプルの長さが一致しない

.. revealjs-code-block:: python
   :data-line-numbers: 1-2,11-14

   def order_beer_and_food(order: tuple) -> str:
       match (order):
           case ("", ""):
               return "Please order something."
           case (beer, ""):
               return f"I drink {beer}."
           case ("", food):
               return f"I eat {food}."
           case (beer, food):
               return f"I drink {beer} with {food}."
           case _:  # match here
               return "one beer and one food only."

   order_beer_and_food(("IPA", "nuts", "spam"))  # -> one beer and one food only.

.. 注文が("IPA", "nuts", "spam")の場合、タプルの長さが2じゃないのでワイルドカードにマッチする。
   結果は"one beer and one food only."

**if** 文で書き換える
---------------------
.. code-block:: python

   def order_beer_and_food(order: tuple) -> str:
       if len(order) == 2:
           beer, food = order
           if beer == "" and food == "":
               return  "I'm full."
           elif beer != "" and food == "":
               return f"I drink {beer}."
           elif beer == "" and food != "":
               return f"I eat {food}."
           else:
               return f"I drink {beer} with {food}."
       else:
           return  "one beer and one food only."

.. if文で書き換えてみる。このコードは少しわかりにくいと思う。

どっちが好み?
-------------
* Structural Pattern Matching
* ``if`` 文

**順番** は重要 ⬇️
==================
.. revealjs-code-block:: python
   :data-line-numbers: 3-4,14

   def order_beer_and_food(order: tuple) -> str:
       match (order):
           case (beer, food):  # match here
               return f"I drink {beer} with {food}."
           case ("", ""):  # never reach
               return "Please order something."
           case (beer, ""):  # never reach
               return f"I drink {beer}."
           case ("", food):  # never reach
               return f"I eat {food}."
           case _:
               return "one beer and one food only."

   order_beer_and_food(("IPA", ""))  # -> I drink IPA with .

.. 注意点が1つある。caseの順番が重要。
   パターンは上から順に比較するので、こう書くと最初のパターンにマッチする。
   その結果、他のパターンに到達しない。

**クラス** パターン
===================

**クラス** パターン
-------------------
.. code-block:: python

   @dataclass
   class Order:  # Order(beer="IPA"), Order("Ale", "nuts")...
       beer: str = ""
       food: str = ""

.. code-block:: python

   def order_with_class(order: Order) -> str:
       match (order):
           case Order(beer="", food=""):
               return "Please order something."
           case Order(beer=beer, food=""):
               return f"I drink {beer}."
           case Order(beer="", food=food):
               return f"I eat {food}."
           case Order(beer=beer, food=food):
               return f"I drink {beer} with {food}."
           case _:
               return "Not an order."

.. Order class has beer and food attributes.
   First case is the pattern matches when beer and food are empty.
   Second case is the pattern matches when only food is empty.
   Then the value of order.beer will be assignend to beer variable.
   3rd case is order.food value assigned to food variable.
   4th case is order.beer and order.food value assignend beer and food.

.. beerとfoodを属性に持つorderクラスを作ります

クラスパターンの **実行結果**
-----------------------------

.. code-block:: python

   >>> order_with_class(Order())
   'Please order something.'
   >>> order_with_class(Order(beer="Ale"))
   'I drink Ale.'
   >>> order_with_class(Order(food="fries"))
   'I eat fries.'
   >>> order_with_class(Order("Ale", "fries"))
   'I drink Ale with fries.'
   >>> order_with_class("IPA")
   'Not an order.'

.. The results are here.
   It works in the same way as the previous tuple case.

.. 先程のタプルと同じように動作します

クラスパターン
--------------
.. code-block:: python

   def order_with_class(order: Order) -> str:
       match (order):
           case Order(beer="", food=""):
               return "Please order something."
           case Order(beer=beer, food=""):
               return f"I drink {beer}."
           case Order(beer="", food=food):
               return f"I eat {food}."
           case Order(beer=beer, food=food):
               return f"I drink {beer} with {food}."
           case _:
               return "Not an order."

.. Rewrite this code of classes pattern with if statement.

**if** 文で書き換える
---------------------
.. code-block:: python

   def order_with_class(order: Order) -> str:
       if isinstance(order, Order):
           if order.beer == "" and order.food == "":
               return  "Please order something."
           elif order.beer != "" and order.food == "":
               return f"I drink {order.beer}."
           elif order.beer == "" and order.food != "":
               return f"I eat {order.food}."
           else:
               return f"I drink {order.beer} with {order.food}."
       else:
           return "Not an order."

.. I rewrote that code  with if statements.
   It looks a little cluttered.
   And, Classes patterns are much more powerful.

.. if文で書いてみるとこんな感じになります。ちょっとごちゃごちゃしてますね。
   まだまだあります

**注文用** クラス
-----------------
.. code-block:: python

   @dataclass
   class Beer:  # Beer("IPA", "Pint")
       style: str
       size: str

   @dataclass
   class Food:  # Food("nuts")
       name: str

   @dataclass
   class Water:  # Water(4)
       number: int

.. There are three classes representing order of beer, food, and water.
   Each classes has attributes beer style and size, food name, and the number of glasses of water.

.. ビール、フード、水の注文を表すそれぞれのクラスがあるとします。

**クラス** パターン
-------------------
* **複数** のクラス

.. code-block:: python

   def order_with_classes(order: Beer|Food|Water) -> str:
       match (order):
           case Beer(style=style, size=size):
               return f"I drink {size} of {style}."
           case Food(name=name):
               return f"I eat {name}."
           case Water(number=number):
               return f"{number} glasses of water, please."
           case _:
               return "Not an order."

.. This code written in classes patterns with multiple classess.
   It is easy to recognize because it branches based on the type of classes.

.. classes patternsで書くとこうなります。
   それぞれのクラスの型で分岐するのでわかりやすいです。

**if** 文で書き換える
---------------------
.. code-block:: python

   def order_with_classes(order: Beer|Food|Water) -> str:
       if isinstance(order, Beer):
           return f"I drink {order.size} of {order.style}."
       elif isinstance(order, Food):
           return f"I eat {order.name}."
       elif isinstance(order, Water):
           return f"{order.number} glasses of water, please."
       else:
           return "Not an order."

.. I rewrite that code  with if statements. It looks like this.
   The match case is cleaner and readable, don't you think?

.. match caseで書いた方がすっきりして読みやすいと思いませんか?

**シーケンス** パターン ➡️
==========================

**シーケンス** パターン ➡️
--------------------------
* 注文のテキストをパース
* 例:

.. code-block:: python

   order_text = "beer IPA pint"
   order_text = "food nuts"
   order_text = "water 3"
   order_text = "bill"

.. Next, I will explain about Sequense pattens.
   In this caes, I'll parse the order text.
   For example...

.. 次はシーケンスのマッチについて解説します。
   ここでは注文のテキストを解析します。
   In this caes, I'll parse the order text.

複数のパターンにマッチ
----------------------
* シーケンスの **長さ** でマッチ

.. code-block:: python

   match order_text.split():
       case [action]:  # match "bill"
           ...
       case [action, name]:  # match "food nuts", "water 3"
           ...
       case [action, name, size]:  # match "beer IPA pint"
           ...

.. This code can match the patterns of multiple sequences.
   In this case, there are patterns with list lengths of 1, 2, and 3.

.. 複数のシーケンスのパターンにマッチできます。
   この場合はリストの長さが1、2、3のパターンがあります。

**特定の値** にマッチ
---------------------
* 特定の行動(bill, food...)にマッチ

.. code-block:: python

   match order_text.split():
       case ["bill"]:  # match "bill"
           calculate_amount()
       case ["food", food]:  # match "food nuts"
           tell_kitchen(food)
       case ["water", number]:  # match "water 3"
           grass_of_water(number)
       case ["beer", style, size]:  # match "beer IPA pint"
           tell_beer_master(style, size)

.. Also, if you write the pattern like this, any value in the list will be matched with a specific string(bill, food...).
   This is a combination of sequence patterns and literal patterns.

.. また、このようにパターンを書くと、リストの任意の値が特定の文字列とマッチします

マッチした **サブパターン** を捕まえる
--------------------------------------
* 有効なビールサイズ: ``"Pint"``、``"HalfPint"``
* ``"beer IPA 1-liter"`` は無効

.. code-block:: python

   match order_text.split():
       ...
       case ["beer", style, ("Pint" | "HalfPint")]:
           # ビールのサイズがわからない

.. Valid beer sizes are Pint or Half Pint only.
   For example, "beer IPA 1-liter" is invalid.
   Using the OR patterns in this way, you can match any value.
   But I don't know beer size. How do I get the value of size.

.. 有効なビールのサイズはPintとHalfPintのみだとします

マッチした **サブパターン** を捕まえる
--------------------------------------

* **as** パターンを使う
* サイズ(``"Pint"``、``"HalfPint"``)を ``size`` に代入

.. code-block:: python

   match order_text.split():
       ...
       case ["beer", style, ("Pint" | "HalfPint") as size]:
           tell_beer_master(style, size)

.. In this case, use as patterns.
   Assign the size value(Pint or HalfPint) to the size variable.


**複数の値** にマッチ
---------------------
* 複数の料理の注文に対応する
* 例:

  * ``"food nuts fries pickles"``

.. code-block:: python

   order_text = "food nuts fries pickles"

   match order_text.split():
       ...
       case ["food", food]:  # 1つの値をキャプチャ
           tell_kitchen(food)

.. I want to order multiple food items at once.
   For example "food nuts fries pickles",
   But this sequence pattern can handle single food.

**複数の値** にマッチ
----------------------------
* 変数名に **\*** を追加

.. code-block:: python

   order_text = "food nuts fries pickles"

   match order_text.split():
       ...
       case ["food", *foods]:  # 複数の値をキャプチャ
           for food in foods:  # ("nuts", "fries", "pickles")
               tell_kitchen(name)

.. If I add * to the variable name(foods), multiple values will be assigned.
   Now I can order multiple food items at once!

.. これで一度に複数のフードを注文できるようになりました!

**マッピング** パターン 📕
===========================
.. Last patterns is Mapping pattens.

**マッピング** パターン 📕
--------------------------
* **辞書** 用のパターン
* **JSON** の解析に便利

.. code-block:: python

   order_dict = {"beer": "IPA", "size": "Pint"}

   match order_dict:
       case {"food": food}:
           tell_kitchen(food)
       case {"beer": style, "size": ("Pint" | "HalfPint") as size}:
           tell_beer_master(style, size)
       case {"beer": style, "size": _}:
           print("Unknown beer size")
       case {"water": number}:
           grass_of_water(number)
       case {"bill": _}:
           calculate_amount()

.. The pattern is matched by map types such as dictionaries.
   The mapping pattern is useful for analyzing a JSON-loaded dictionary.

**組み込み** クラスにマッチ
---------------------------
* **str()**、**int()** などを使う

.. code-block:: python

   order_dict = {"water": 3}
   # order_dict = {"water": "three"}  # Doesn't match

   match order_dict:
       case {"food": str(food)}:
           tell_kitchen(food)
       case {"beer": str(style), "size": ("Pint" | "HalfPint") as size}:
           tell_beer_master(style, size)
       case {"beer": str(style), "size": _}:
           print("Unknown beer size")
       case {"water": int(number)}:
           grass_of_water(number)
       case {"bill": _}:
           calculate_amount()

.. You can use builtin classes to specify the type of the value.
   In this code, food and beer style are string, and the number of water is an integer only.
   If the value of water is string, it will not match the pattern.

.. このコードでは、料理やビールの種類は文字列で、水の数は整数のみとなります。
   もしwaterの値が文字のthreeの場合は、パターンにマッチしません。

ガード 💂‍♀️
============

.. Finally, let me introduce Guards.

.. 最後にガードについて説明します。

ガード 💂‍♀️
------------
* パターンの後ろに **if** 文

.. code-block:: python

   order_list = ["water", 3]  # -> 3 glasses of water, please.
   # order_list = ["water", 15]  # -> You can only order 1-9 glasses of water.

   match order_list:
       case ["water", int(number)] if 0 < number < 10:
           print(f"{number} glasses of water, please.")
       case ["water", _]:
           print("You can only order 1-9 glasses of water.")

.. If you write an if statement after the pattern, it becomes a guard.
   This code will match if the second value of order_list is an integer.
   After that, a guard checks if the number is in the range of 1-9.

.. パターンの後ろにif文を書くとguardになります。

まとめ
=======
.. revealjs-break::

* モチベーション 💪
* 構文 |code|

  * ソフトキーワード: ``match``、``case``、``_``
* パターン |random|

  * リテラル、変数、クラス、シーケンス、マッピング
  * ワイルドカード、OR、AS、ガード

.. Summary of this talks.
   I tald about ...

Structural Pattern Matching に **挑戦** 👍
-------------------------------------------
.. If you think pattern matching looks good, give it a try!!

.. もしパターンマッチよさそうだなと思ったら、挑戦してみてください

参考資料 📚
------------
* `What's New In Python 3.10 <https://docs.python.org/ja/3.10/whatsnew/3.10.html>`_
* `Python Release Python 3.10.0 <https://www.python.org/downloads/release/python-3100/>`_
* `PEP 634 -- Structural Pattern Matching: Specification <https://www.python.org/dev/peps/pep-0634/>`_
* `PEP 635 -- Structural Pattern Matching: Motivation and Rationale <https://www.python.org/dev/peps/pep-0635/>`_
* `PEP 636 -- Structural Pattern Matching: Tutorial <https://www.python.org/dev/peps/pep-0636/>`_

.. References are here

Thank you !! 🙏
===============
Takanori Suzuki (|twitter| `@takanory <https://twitter.com/takanory>`_)

`slides.takanory.net <https://slides.takanory.net/>`_

.. image:: /assets/images/sokidan-square.jpg

.. Thank you for your attention.
   I hope to see you at PyCon held onsite somewhere.

What's New in Python 3.10 🆕
=============================
.. revealjs-break::

* **Parenthesized Context Managers** 👈
* **Better Error Messages** 👈
* **Better Typing Syntax** 👈
* Structural Pattern Matching
* Better Debugging

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

.. revealjs-code-block:: python
   :data-line-numbers: 3-6

   $ python3.10 beer_styles.py
     File ".../beer_styles.py", line 2
       beer_styles = ['Pilsner', 'Ale', 'IPA', 'Hazy IPA'
                     ^
   SyntaxError: '[' was never closed
   # Easy to understand!!

.. revealjs-code-block:: python
   :data-line-numbers: 3-5

   $ python3.9 beer_styles.py
     File ".../beer_styles.py", line 3
       print(beer_styles)
       ^
   SyntaxError: invalid syntax

Better Error Messages
---------------------
.. revealjs-code-block:: python
   :data-line-numbers: 3-7

   # 3.10
   >>> if beer_syle = 'IPA':
     File "<stdin>", line 1
       if beer_syle = 'IPA':
          ^^^^^^^^^^^^^^^^^
   SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
   # Very friendly!!

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

* Can use Python 3.7 - 3.9

.. code-block:: python

   from __future__ import annotations

   def drink_beer(number: int | float) -> str | None
       if am_i_full(number):
           return 'I'm full'

Try Python 3.10 👍
-------------------
