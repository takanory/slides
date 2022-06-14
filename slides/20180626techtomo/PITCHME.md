## Pythonってどんな言語?

### 導入事例や気になるトレンドについて

2018 Jun 26 / テクトモ #1

Takanori Suzuki

---?include=20180626techtomo/md/about.md

---

## 質問はsli.doへ

* ブラウザのURLに `sli.do`
* イベントコードに `techtomo0626`

---

## 最初に質問

+++

### Python知っている人?

+++

### Python書いたことある人?

+++

### 他のプログラミング言語は書いたことある人?

---

## Pythonの歴史

+++

### Python 0.9.0

* 1991年に公開
* netnewsにソースコードが公開された
* list, dict, str

+++

### Python 1系

* 1994年1月に1.0リリース
* lambda, map, filter, reduce
* Python 1.6が2000年にリリース

+++

### Python 2系

* 2000年10月に2.0がリリース
* 2.7.15が最新(2018年5月5日)
* 2020年1月1日でサポート終了
  * [PEP 404 - Python 2.8 Un-release Schedule](https://www.python.org/dev/peps/pep-0404/)

+++

### Python 3系

* 2008年12月に3.0がリリース
* Python 2系との後方互換性を一部削除
* 3.6.5が最新(2018年5月28日)
* 3.7.0がもうすぐ(2018年6月27日)リリース予定

---

## Pythonの特徴

+++

### 設計思想

* シンプルで読みやすいコードが書けること
* 同じ動作をするプログラムは似たようなコードに

+++

### インデント

* ブロック構造をインデントで表現

```python
for i in range(10):
    if i % 5 == 0:
        print('ham')
    elif i % 3 == 0:
        print('eggs')
    else:
        print('spam')
```

+++

### バッテリー同梱

* [Python 標準ライブラリ](https://docs.python.org/ja/3/library/index.html)
* 多数のライブラリが最初から用意されている

![標準ライブラリ](20180626techtomo/images/library.png)

+++

### PEP: Python Enhanthment Proposal

* Python拡張の提案
* 拡張のアイデアをドキュメント化
  * レビューして採用/不採用を判断
  * [PEP 1 - PEP Purpose and Guidelines](http://sphinx-users.jp/articles/pep1.html)
  * [PEP 1 - PEP Purpose and Guidelines(日本語訳)](http://sphinx-users.jp/articles/pep1.html)
* PEPの一覧ページもPEP
  * [PEP 0 – Index of Python Enhancement Proposals(PEPs)](https://www.python.org/dev/peps/)

+++

### PEP8

* Pythonのコーディング規約
  * [PEP8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
  * [pep8-ja](http://pep8-ja.readthdocs.io/)
* インデントはスペース4つ

+++

### PEP8の例

* Yes

```python
import os
import sys

spam(1)
```

* No

```python
import sys, os

spam (1)
```

+++

### The Zen of Python

* Pythonらしさとはなにか?
* [PEP 20 - The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

---

## 導入事例

+++

### メジャーな企業も利用

* Google: 標準プログラミング言語の1つ
* Pinterest: WebサービスがPython
* Instagram: 同上
* Dropbox: Python開発者が在籍
* Disney: グラフィックス

+++

### US PyConのスポンサー

* Microsoft、Google、AWS、JPMorgan、LinkedIn、Bloombergなどなど
* [About PyCon Sponsors](https://us.pycon.org/2018/sponsors/)

![US PyCon Sponsors](20180626techtomo/images/pycon-sponsors.png)

+++

### 国内の事例

* [PyCon JP スポンサー](https://pycon.jp/2017/ja/sponsors/)

![PyCon JP スポンサー](20180626techtomo/images/pyconjp-sponsors.png)

+++

### SQUEEZE

* https://squeeze-inc.co.jp/services/
* 民泊の運用サポートサービスをPythonで実装

![SQUEEZE](20180626techtomo/images/squeeze.png)

+++

### モノタロウ

* https://www.monotaro.com/
* 工具通販サイトだけでなく、在庫管理など全てPython製

![SQUEEZE](20180626techtomo/images/monotaro.png)

+++

### LINE

* https://line.me/
* フロントは別言語
* ログ管理とかがPython製

![LINE](20180626techtomo/images/line.png)

+++

### Retty

* https://retty.me/
* 各種データ分析、料理画像の機械学習などに利用

![Retty](20180626techtomo/images/retty.png)

+++

### AI学習システム[ＴＲＡＩ]

* http://tekiseicubic.com/about_trai/
* 適性検査の結果を機械学習
* 社員タイプの分類、活躍率、定着率予測など

![Retty](20180626techtomo/images/trai.png)

+++

### ここで次回「テクトモ」の発表内容を紹介

+++

### 深層学習のはじめかたと活用事例(仮)

* 志田 和也 (Shida Kazuya) / [ユニファ株式会社](https://unifa-e.com/)
* 私はもともと iOS/Android のエンジニアで、今年から仕事として深層学習をやりはじめました。はじめるに当たって Python や TensorFlow などのツールや環境の紹介と、実際に弊社での深層学習の活用事例を紹介したいと思います

![志田さんアイコン](20180626techtomo/images/shida.jpg)

+++

### ユニファ株式会社

* 家族のコミュニケーションを豊かにするプラットフォームを創造

![ユニファ](20180626techtomo/images/unifa.png)

---

## Pythonの現在のトレンド

+++

### 機械学習、データ分析

* NumPy: 行列操作と数値演算
* SciPy: 科学技術計算
* pandas: データの探索や加工、集計
* Jupyter Notebook: 対話環境
* Matplotlib: データ可視化
* scikit-learn: 機械学習

+++

### 深層学習

* TensorFlow
* Keras
* Chainer

+++

### 機械学習だけじゃない

+++

### Webスクレイピング

* [Scrapy: A Fast and Powerful Scraping and Web Crawling Framework](https://scrapy.org/)

![Scrapy](20180626techtomo/images/scrapy.png)

+++

### Webアプリケーション

* [Django: The Web framework for perfectionists with deadlines](https://docs.djangoproject.com/)

![Django](20180626techtomo/images/django.png)

+++

### DjangoCongress JP 2018

* 日本初のDjangoに関するConference
* [DjangoCongress JP 2018](https://djangocongress.jp/)

![DjangoCongress JP 2018](20180626techtomo/images/djangocongress.png)

+++

### Awesome Python

* [vinta/awesome-python: A curated list of awesome Python frameworks, libraries, software and resources](https://github.com/vinta/awesome-python)

![Awesome Python](20180626techtomo/images/awesome-python.png)

+++

### Pythonならいろいろできそう

---

## Pythonの今後の展望

+++

### 今後のリリース予定

* 2018年6月27日 Python 3.7.0リリース: [PEP 537](https://www.python.org/dev/peps/pep-0537/)
* 2019年10月20日 Python 3.8.0リリース: [PEP 569](https://www.python.org/dev/peps/pep-0569/)
* 2020年1月1日 Python 2系サポート終了: [PEP 404](https://www.python.org/dev/peps/pep-0404/)

+++

### Python 3.7.0

* [What's New In Python 3.7](https://docs.python.org/ja/3.7/whatsnew/3.7.html)

+++

### breakpoint() 組込関数

* `breakpoint()` と書くと、バッガーが起動
* pdb以外のデバッガーにも対応
* [PEP 553 -- Built-in breakpoint()](https://www.python.org/dev/peps/pep-0553/)

```python
import pdb; pdb.set_trace()  # 今まで

breakpoint()  # Python 3.7以降
```

+++

### dataclaess

* データ格納用のクラス
* [PEP 557 -- Data Classes](https://www.python.org/dev/peps/pep-0557/)

```python
@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0

p = Point(1.5, 2.5)
print(p)   # produces "Point(x=1.5, y=2.5, z=0.0)"
```

+++

### さらに先は

* Python 3.8.0 の新機能は未定
* Python 4系についても未定
* しばらくはPython 3系の最新でよさそう

---

## これからPythonを学ぶには

+++

### 入門書はたくさん

* [ASCII.jp：Python入門書22冊を読み比べてみた](http://ascii.jp/elem/000/001/691/1691531/)
  * 「どの本でもPythonを学び始めることができますが、筆者の出した結論は2冊買いです。図が多い書籍＋ページ数の多い書籍、超初心者向け書籍＋リファレンス系書籍、体験系書籍＋チュートリアル系書籍、出版社Aの本＋出版社Bの本など、どんな組み合わせでも良いので、とりあえず2冊買ってみるのです。」

+++

### PCでの学習

* 動画での学習
* オンライン学習サービス
  * PyQもよろしく!

![PyQ](assets/images/pyq.png)

+++

### コミュニティへの参加

* [Pythonカテゴリイベント](https://connpass.com/category/Python/)
* もくもく会への参加がおすすめ
* 相談できる人を見つけよう

![connpassのPythonカテゴリ](20180626techtomo/images/connpass-python.png)

+++

### PyCon JP 2018

* https://pycon.jp/2018/
* ぜひまた会いましょう!

![PyCon JP 2018](20180626techtomo/images/pyconjp2018.png)

---

## One more thing...

Note:
以上で発表を終わりますが、1つおまけがあります

+++

### 懇親会で書籍プレゼント

* スラスラ読める Pythonふりがなプログラミング
* Pythonプロフェッショナルプログラミング 第3版

![PythonふりがなプログラミングとPythonプロフェッショナルプログラミング](20180626techtomo/images/present.png)

Note:
* Pythonふりがなプログラミングの著者の一人の大津さんが見えてます

---

## ありがとうございました

---

## Question?


