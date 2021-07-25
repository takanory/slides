### Pythonの特徴と
### 注目ライブラリのご紹介

< OSS X Users Meeting > #19 Python

Takanori Suzuki / 2017-06-29

---

### Who am I?(お前誰よ)

* 鈴木たかのり / Takanori Suzuki
* Twitter: [@takanory](https://twitter.com/takanory)
* [株式会社ビープラウド](https://www.beproud.jp/)
* [一般社団法人PyCon JP](https://www.pycon.jp/) 理事
* [Pythonボルダリング部](https://kabepy.connpass.com/)(#kabepy)部長

![BeProud](assets/images/beproud.png)

---

### 今日話すこと

* Pythonとは
* Pythonの特徴
* 注目ライブラリ
* Pythonを学ぶには

+++

### 最初に質問

* Python知ってる人?

+++

### 最初に質問

* Python書いたことある人?

+++

### 最初に質問

* 他のプログラミング言語は知ってる人?

---

### Pythonとは

+++

### Pythonとは

* マルチプラットフォーム
* マルチパラダイム
* Python 3
* 豊富なライブラリ

+++

### マルチプラットフォーム

* Windows
* macOS
* Linux
* 他

+++

### マルチパラダイム

* オブジェクト指向
* 命令形
* 手続き型
* 関数型

+++

### Python 3

* 今から使うならPython 3一択
* 最新バージョンは 3.6.1
* 日本語の文字コードに悩まされにくい

```python
print('こんにちは世界!') # Python 3系
print 'こんにちは世界!' # Python 2系
```

+++

### 豊富なライブラリ

* 400弱の標準ライブラリ
* https://docs.python.jp/3/library/index.html

![標準ライブラリ](20170629ossx/images/standard-library.png)

+++

### 豊富なサードパーティ製パッケージ

* 多数のパッケージ
* https://pypi.python.org/pypi

![PyPI](20170629ossx/images/pypi.png)

---

### Python の特徴

+++

### Python の特徴

* 読みやすいコード
* PEP8: コーディングスタイル
* PEP: 拡張提案
* Pythonでできること

+++

### 読みやすいコード

* 構造(ブロック)をインデントで表現

```python
for num in range(1,101):
    if num % 15 == 0:
        print('Fizz Buzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
```

+++

### PEP8: コーディングスタイル

* PEP 8: Style Guide for Python Code
* https://www.python.org/dev/peps/pep-0008/

```python
spam(ham[1], {eggs: 2})        # Good
spam( ham[ 1 ], { eggs: 2 } )  # Bad
dct['key'] = lst[index]        # Good
dct ['key'] = lst [index]      # Bad
```

+++

### PEP8: コーディングスタイル

* 各種サポートツール
  * pycodestyle: PEP8のチェック
  * autopep8: 自動的に書き換える
  * flake8: pycodestyle + 論理チェック

+++

### PEP: Pythonの拡張提案

* Python Enhancement Proposal
* https://www.python.org/dev/peps/

![PEP](20170629ossx/images/peps.png)

+++

### Pythonでできること

* コマンドラインツール
* バッチ処理
* Web開発
* データサイエンス
* 構成管理
* ドキュメンテーション
* その他いろいろ

---

### 注目ライブラリ

+++

### 注目ライブラリ

* Pythonライブラリ厳選レシピ
* Awesome Python

  * Web開発
  * データサイエンス
  * 構成管理
  * ドキュメンテーション
  * その他

+++

### Pythonライブラリ厳選レシピ

* http://gihyo.jp/book/2015/978-4-7741-7707-6
* 「これだけは知っていてほしい」を厳選

  * 標準ライブラリ
  * サードパーティ製パッケージ

![Pythonライブラリ厳選レシピ](assets/images/recipe.jpg)

+++

### Awesome Python

* https://github.com/vinta/awesome-python

![Awesome Python](20170629ossx/images/awesome-python.png)

+++

### Web開発

* Webフレームワーク

  * Django: https://www.djangoproject.com/
  * Bottle: https://bottlepy.org/

* Webスクレイピングフレームワーク

  * Scrapy: https://scrapy.org/

+++

### データサイエンス

* NumPy, SciPy: 数値計算、科学計算
* pandas: データ解析
* scikit-learn: 機械学習
* Matplotlib, Bokeh: 可視化
* Keras, Caffe, TensorFlow: ディープラーニング
* NLTK: 自然言語処理
* 詳細は次のセッションで

+++

### 構成管理

* Ansible: https://www.ansible.com/
  * YAMLで記述

![Ansible](20170629ossx/images/ansible.png)

+++

### ドキュメンテーション

* Sphinx: http://www.sphinx-doc.org/
  * reStructuredText または Markdown で記述

![Sphinx](20170629ossx/images/sphinx.png)

+++

### その他

* OpenPyXL: https://openpyxl.readthedocs.io/
  * Excelファイルの読み書き
* Slackbot: https://github.com/lins05/slackbot
  * Slack(チャット)のbotフレームワーク
* awscli: https://aws.amazon.com/jp/cli/
  * AWSのコマンドラインツール
  
---

### Pythonを学ぶには

+++

### Pythonを学ぶには

* Webサイト
* 学習サイト
* Q&Aサイト
* 書籍
* コミュニティ

+++

### Webサイト

* Python公式ドキュメント
  * 標準ライブラリ: http://docs.python.jp/3/library/
  * チュートリアル: http://docs.python.jp/3/tutorial/
  * HOWTO: http://docs.python.jp/3/howto/
* Dive into Python 3日本語版: http://diveintopython3-ja.rdy.jp/

+++

### 学習サイト

* Paiza: https://paiza.jp/
* ProjectEuler: https://projecteuler.net/
* CheckIO: https://checkio.org/

+++

### 学習サイト

* PyQ: https://pyq.jp/

![PyQ](assets/images/pyq.png)

+++

### Q&Aサイト

* Stack Overflow: https://ja.stackoverflow.com/
* teratail: https://teratail.com/

+++

### 書籍

* [Pythonスタートブック](http://gihyo.jp/book/2010/978-4-7741-4229-6)
* [Pythonチュートリアル](https://www.oreilly.co.jp/books/9784873117539/)
* [Pythonプロフェッショナルプログラミング第2版](http://www.shuwasystem.co.jp/products/7980html/4315.html)
* [Pythonライブラリ厳選レシピ](http://gihyo.jp/book/2015/978-4-7741-7707-6)

+++

### 書籍(雑誌)

* [Software Design 2017年6月号](http://gihyo.jp/magazine/SD/archive/2017/201706)
  * 第2特集 今すぐはじめるPython

![Software Design 2017年6月号](assets/images/softwaredesign.jpg)

+++

### 書籍(雑誌)

* 懇親会で1冊プレゼント!!!

![Software Design 2017年6月号](assets/images/softwaredesign.jpg)

+++

### コミュニティ

* python.jp: https://www.python.jp/
* PyCon JP: http://pycon.jp
* Python mini Hack-a-thon: https://pyhack.connpass.com/
* PyData.Tokyo: https://pydata.tokyo/
* PyLadies Tokyo: http://tokyo.pyladies.com/

+++

### コミュニティのSlack

* python.jp: https://www.python.jp/community/
* PyCon JP: http://pyconjp-fellow.herokuapp.com/
* Python mini Hack-a-thon: http://pyhack.herokuapp.com/
* PyData-JP: https://pydata-jp.herokuapp.com/
* PyLadies Japan: [Slackアカウント申請フォーム](https://docs.google.com/forms/d/e/1FAIpQLSelRdBGus7o6MsijTZiTt1kFAoFYQlwYgrBPQOrGVwGlAmHNg/viewform "Slackアカウント申請 - PyLadies Japan")

+++

### PyCon JP

* https://pycon.jp/2017
* 2017年9月開催
* 700名以上が参加
* 有料(一般 10,000円)
* 早割は売り切れ

![PyCon JP 2017](assets/images/pyconjp2017-logo.png)

---

### Question?

---

### Thank you
