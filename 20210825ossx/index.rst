==========================
 Pythonの現在とこれからと
==========================

Takanori Suzuki

<OSS X Users Meeting> #31 / 2021 Aug 25

今日話すこと 🗣
===============
* Pythonとは(5分)
* Pythonの旬なプロジェクト(5分)
* Python開発の歴史(5分)
* Python言語アップデート(10分)
* Pythonの未来(5分)

スクショ 📸 ツイート 🐦 👍
==========================
* ``#ossx`` / ``@takanory``

スライド 💻
===========
👉 `slides.takanory.net <https://slides.takanory.net>`_

最初に質問
==========

Python知ってる人🙋‍♂️
---------------------

Python使ったことある人🙋‍♀️
---------------------------

Python今使っている人🙋‍♂️
-------------------------

Who am I(お前誰よ) 👤
=====================
* 鈴木たかのり(`@takanory <https://twitter.com/takanory>`_)
* PyCon JP Association 副代表理事
* 株式会社BeProud 役員/Python Climber
* 好き：フェレット、🍺、LEGO／趣味：🎺、🧗

.. image:: /assets/images/sokidan-square.jpg

Pythonとは 🐍
==============

.. revealjs-break::

* 汎用のプログラミング言語

  * 動的型付け
* 1991年に0.9がリリース
* 最新バージョンは3.9.6
* Python 2系は2020年1月1日にEOL

読みやすく
----------
* インデントが構文
* **PEP 8** というコーディング規約

  * https://www.python.org/dev/peps/pep-0008/

.. code-block:: python

   for num in range(1, 101):
       if num % 15 == 0:
           print('FizzBuzz')
       elif num % 5 == 0:
           print('Fizz')
       elif num % 3 == 0:
           print('Buzz')
       else:
           print(num)

後方互換性
----------
* 3.9で書いたプログラム→基本3.10で動く
* 利用するサードパーティライブラリ次第(後述)
* Python 2系→3系では後方互換性を犠牲に

  * 移行にかなりかかった

豊富な標準ライブラリ
--------------------
* 標準ライブラリでいろいろできる
* 「バッテリー同梱」とも言われる
* ただ多すぎて使われてなさそうなものも...
* https://docs.python.org/ja/3/library/

豊富なサードパーティライブラリ
--------------------------------
* PyPI(https://pypi.org/)からインストール

.. image:: images/pypi.png
   :width: 80%
   :alt: PyPI

.. revealjs-break::

* Webフレームワーク、スクレイピング
* 行列計算、機械学習、深層学習
* コンピュータービジョン、画像処理
* データ分析、可視化

.. revealjs-break::

* Awesome Python(https://awesome-python.com/)

.. image:: images/awesome-python.png
   :width: 80%
   :alt: Awesome Python

他のツールの組み込み言語
------------------------
* 3DCG

  * blender, Mayaなど
* ゲームエンジン

  * Unreal Engine

Pythonとは 🐍 - まとめ
----------------------
* 読みやすい構文
* 後方互換性を維持
* 豊富な標準ライブラリ、サードパーティ

Pythonの旬なプロジェクト 🔥
===========================
* 旬っぽいプロジェクトをいくつか紹介

FastAPI
-------
* API構築のWebフレームワーク
* URL: https://fastapi.tiangolo.com/ja/

.. image:: images/fastapi.png
   :width: 70%

.. Pythonの標準である型ヒントに基づいてAPIを構築するための、モダンで、高速(高パフォーマンス)な、Web フレームワーク

JupyterLab
----------
* Webベースのプログラムの対話型実行環境
* https://jupyterlab.readthedocs.io/

.. image:: images/jupyterlab.png
   :width: 70%

PyCaret
-------
* ローコードのMLライブラリ(AutoMLサポート)
* https://pycaret.org/

.. image:: images/pycaret.png
   :width: 70%

AWS CLI / Google Cloud SDK
--------------------------
* クラウドを管理するコマンド群
* https://aws.amazon.com/cli/
* https://cloud.google.com/sdk

Black
-----
* 妥協のないコードフォーマッター
* https://black.readthedocs.io/

.. image:: images/black.png
   :width: 70%

Poetry
------
* パッケージの依存関係の管理、構築
* https://python-poetry.org/

.. image:: images/poetry.png
   :width: 65%

Pythonの旬なプロジェクト 🔥 - まとめ
------------------------------------
* 気になるものがあったら試してみて
* FastAPI
* JupyterLab
* PyCaret
* AWSCLI / Google Cloud SDK
* Black
* Poetry

Python開発の歴史 🕰
==================

Pythonの拡張はPEPで提案
-----------------------
* PEP: Python Enhancement Proposal
* 2000年頃から運用

  * PEPを書いて提案
  * メーリングリストで議論
  * 最後に採用/不採用を判断
* `PEP 1 -- PEP Purpose and Guidelines <https://www.python.org/dev/peps/pep-0001/>`_

BDFL: 優しい終身の独裁者
------------------------
* BDFLが採用不採用を最終決定

  * BDFL = Guido van Rossum
  * BDFL Delegateで他人に判断を委譲可能

BDFLの引退
----------
* セイウチ演算子ですごいもめたのがきっかけ?

  * `PEP 572 -- Assignment Expressions <https://www.python.org/dev/peps/pep-0572/>`_
* 2018年7月にBDFLを引退するというメールを送信

  * `[python-committers] Transfer of power <https://mail.python.org/pipermail/python-committers/2018-July/005664.html>`_

.. revealjs-break::

.. image:: images/transfer-of-power.png
   :width: 80%

Pythonの新しい運営モデル
------------------------
* `PEP 8000 -- Python Language Governance Proposal Overview <https://www.python.org/dev/peps/pep-8000/>`_

  * 複数のガバナンスモデルが提案され投票
* `PEP 8016 -- The Steering Council Model <https://www.python.org/dev/peps/pep-8016/>`_

  * この案が採用された

The Steering Council Model
--------------------------
* 毎年5名のCouncilメンバーを投票で決める
* CouncilメンバーがPEPの採用不採用を決定
* 2019年はGuidoがいたが、2020以降は立候補していない
* 投票結果: `2019 <https://www.python.org/dev/peps/pep-8100/>`_, `2020 <https://www.python.org/dev/peps/pep-8101/>`_, `2021 <https://www.python.org/dev/peps/pep-8102/>`_

2021 Councilメンバー
--------------------
* C.Willing, T.Wouters, B.Cannon, P.Galindo Salgado, B.Warsaw

.. image:: images/council.png
   :width: 80%

Python開発の歴史 🕰 - まとめ
---------------------------
* 2018年に大きく運営方針が変わった
* 今後も継続的に開発は続きそう
* Council Modelへの移行はいいタイミングだったかも

宣伝 📺
=======
* ここで休憩がてらコミュニティ活動の宣伝

PyCon JP
--------
* 国内最大のPythonイベント(`2021.pycon.jp <https://2021.pycon.jp/>`_)
* 2021年10月15日(金)、16日(土)

.. image:: images/pyconjp.png
   :width: 80%

PyCon JP TV
-----------
* Pythonについて月1ライブ配信(`tv.pycon.jp <https://tv.pycon.jp/>`_)
* 次回は2021年9月3日(金)

.. image:: images/pyconjptv.png
   :width: 70%

Python Boot Camp
----------------
* 日本中で開催する初心者向けチュートリアル
* https://www.pycon.jp/support/bootcamp.html

.. image:: images/pycamp.png
   :width: 80%

Python Charity Talks in Japan
-----------------------------
* 今回は地域コミュニティ祭り
* https://pyconjp.connpass.com/event/218154/
* 2021年9月11日(土)

.. image:: images/pycharity.png

宣伝ここまで
------------
* 興味があるものに参加してみてください

Python言語アップデート 🆕
============================
* 現在はPython 3.9.6
* 2021年10月に3.10.0がリリース予定
* 今後は年1回マイナーバージョンが上がる
* サポートは5年間

最近の主な新機能
----------------
* 3.9: 辞書の和集合演算子
* 3.8: 代入式
* 3.7: データクラス
* 3.6: フォーマット済み文字列リテラル
* (コード例を出す)

型ヒント
--------
* 動的型付け言語だが型ヒントが付けられる
* 別なツールでチェックできる
* (コード例を付ける)

Python 3.10の主な新機能
-----------------------
* Better error messages
* Structural Pattern Matching
* (コード例を出す)

Python言語アップデート 🆕 - まとめ
----------------------------------

Pythonの未来 🚀
===============
* 2021のPyConでのLanuguage SummitでGuioが発表

  * コロナでひまでMSに入った
  * Pythonをスピードアップしていく
  * 1年(0.1あがる)ごとに1.5倍
  * 4年で5倍を目指す
* Python 4の予定はない

  * 出すとしても2→3のようにはしない

まとめ
======
* 30年くらいたってる
* なんやかんやあったけど体制は維持されている
* 今もちょっとずつよくなっていってる
* 今後は高速化にも期待
