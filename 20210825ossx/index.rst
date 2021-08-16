==========================
 Pythonの現在とこれからと
==========================

Takanori Suzuki

<OSS X Users Meeting> #31 / 2021 Aug 25

TODO
====
* emでfontawesomeが斜体になるのでCSS直す

今日話すこと
============
* Pythonとは(5分)
* Pythonの旬なプロジェクト(5分)
* Python開発の歴史(5分)
* Pythonの現在と今後(10分)
* Pythonの未来(5分)

最初に質問(1分)
===============
* Python知ってる人
* Python使ったことある人

Who am I(お前誰よ)(1分)
=======================
* 鈴木たかのり
* |twitter| `@takanory <https://twitter.com/takanory>`_
* (``#pyconjp``) 副代表理事
* 株式会社BeProud 役員/Python Climber

Pythonとは(5分)
===============
* 汎用のプログラミング言語

  * 動的型付け
* 1991年に0.9がリリース
* 最新バージョンは3.9.6
* Python 2系は2020年1月1日にEOL

読みやすく
----------
* インデントが構文
* PEP8というコーディング規約

.. code-block:: python

   ここにサンプルコード

後方互換性
----------
* 基本的に3.xが更新されてもそのまま動く
* 対応するサードパーティ製パッケージ次第(後述)
* Python 2系→3系ではいくつか広報互換性を犠牲にした

  * そのおかげで移行にかなりかかった

豊富なライブラリ
----------------
* 標準ライブラリでいろいろできる
* 「バッテリー同梱」とも言われる
* ただ多すぎて使われてなさそうなものも...

豊富なサードパーティ製パッケージ
--------------------------------
* PyPIからインストールできる
* いろいろできる
* Webフレームワーク、スクレイピング
* 機械学習、深層学習
* コンピュータービジョン
* データ分析
* https://awesome-python.com/ を紹介

Pythonの特徴まとめ
------------------
* 読みやすい構文
* 後方互換性を維持
* 豊富なライブラリ、パッケージ

Pythonの旬なプロジェクト(5分)
=============================
* GitHubでstarが多めのものから抜粋
* FastAPI
* Django / DRF
* Keras?
* scikit-learn: 1.0が出るっぽい?
* black
* poetry
* (それぞれを1ページずつで紹介予定)

Python開発の歴史(5分)
=====================
* PEPの仕組みを説明(2000年から

  * PEP書いて提案
  * メーリングリストで議論
  * 最後に採用/不採用を判断

* BDFLが採用不採用を判断していた

  * BDFL = Guido
  * BDFL Delegateで他人に判断を委譲できる

* BDFL引退の話

  * セイウチ演算子ですごいもめた?
  * `[python-committers] Transfer of power <https://mail.python.org/pipermail/python-committers/2018-July/005664.html>`_

* Pythonの新しい運営モデル

  * `PEP 8000 -- Python Language Governance Proposal Overview | Python.org <https://www.python.org/dev/peps/pep-8000/>`_ でいくつか提案されて投票
  * `PEP 8016 -- The Steering Council Model | Python.org <https://www.python.org/dev/peps/pep-8016/>`_ が採用

* The Steering Council Model

  * 毎年5名のCouncilメンバーを投票で決める
  * CouncilメンバーがPEPの採用不採用を決定
  * 2019はGuidoはいたが、2020以降は立候補していない
* 今後

  * 継続的に開発は続きそう
  * Council Modelへの移行はいいタイミングだったかも

PyCon JP 2021の宣伝(1分)
========================
* ここで宣伝を入れる
* Python Charity Talksも宣伝するかなぁ

Pythonの現在と今後(10分)
========================
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

Pythonの未来(5分)
=================
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
