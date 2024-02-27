# **Python開発の変遷**

をPythonプロフェッショナルプログラミングの

**改訂の歴史** から知る

Takanori Suzuki

BPStudy #198 / 2024 Feb 28

## アジェンダ

* Pythonプロフェッショナルプログラミング(以下: PyPro)出版の歴史
* ◯◯の歴史と比較
* 

## お前誰よ 👤

* Takanori Suzuki / 鈴木 たかのり ({fab}`twitter` [@takanory](https://twitter.com/takanory))
* [BeProud](https://www.beproud.jp/) 取締役 / Python Climber
* [PyCon JP Association](https://www.pycon.jp/) 代表理事
* [Python Boot Camp](https://www.pycon.jp/support/bootcamp.html) 講師、[Python mini Hack-a-thon](https://pyhack.connpass.com/) 主催、[Pythonボルダリング部](https://kabepy.connpass.com/) 部長

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

### PyCon JP **Association** 🐍

日本国内のPythonユーザのために、**Pythonの普及及び開発支援**を行うために、継続的にカンファレンス(**PyCon**)を開くことを目的とした **非営利組織**

* [`www.pycon.jp`](https://www.pycon.jp)

![pycon jp logo](/assets/images/pyconjp_logo.png)

### PyCon JP **2024**

* **9月** 後半に **東京** で開催予定
* 3名の **共同座長**(with 吉田さん、寺田さん)
* **主催メンバー** 募集中
* 詳細: [PyCon JP 2024座長決定のお知らせと主催者グループのメンバー募集](https://pyconjp.blogspot.com/2024/01/pyconjp2024-co-chair.html)

### **BeProud** Inc. 🏢

* [BeProud](https://www.beproud.jp/): Pythonシステム開発、コンサル
* [connpass](https://connpass.com/): IT勉強会支援プラットフォーム
* [PyQ](https://pyq.jp/): Python独学プラットフォーム
* [TRACERY](https://tracery.jp/): システム開発ドキュメントサービス

![BeProud logos](/assets/images/beproud-logos.png)

### Pythonプロフェッショナルプログラミング

* **ビープラウド** が執筆した書籍
* ビープラウドに新たに **加わったメンバー** が、開発プロジェクトに **円滑に参加** するためのガイド
  * **Python** で開発する **チーム** に役立つはず
  * **当時の開発スタイル** が見えてくる

## PyPro出版の **歴史** 📚

### PyPro出版の **歴史** 📚

* **初版**(PyPro): 2012年3月27日
* **第2版**(PyPro2): 2015年2月27日
* **第3版**(PyPro3): 2018年6月12日
* **第4版**(PyPro4): 2024年2月16日

### どれくらい **間があいた** のか

```python
>>> from datetime import date
>>> pypro = date(2012, 3, 27)
>>> pypro2 = date(2015, 2, 27)
>>> pypro3 = date(2018, 6, 12)
>>> pypro4 = date(2024, 2, 16)
>>> pypro2 - pypro
datetime.timedelta(days=1067)
>>> pypro3 - pypro2
datetime.timedelta(days=1201)
>>> pypro4 - pypro3
datetime.timedelta(days=2075)
```

### [PyPro](https://www.shuwasystem.co.jp/book/9784798032948.html) (黒)

* 発売日: 2012年3月27日
* 464ページ
* 本体: 2,800円+税

![pypro1](images/pypro1.jpg)

### [PyPro](https://www.shuwasystem.co.jp/book/9784798032948.html) 著者

* リーダー: 清水川貴之
* 岡野真也、池田洋介、畠弥峰、drillbits、cactusman、東健太、tell-k、今川館、ナツ、文殊堂、aita、冨田洋祐

![pypro1](images/pypro1.jpg)

### [2012年](https://ja.wikipedia.org/wiki/2012%E5%B9%B4)のできごと

* [Python 3.3](https://peps.python.org/pep-0398/)、[Python 2.7.3](https://peps.python.org/pep-0373/)
* [Django 1.4](https://docs.djangoproject.com/en/5.0/releases/1.4/)
* 渋谷ヒカリエ、東京スカイツリー開業
* ロンドンオリンピック開催
* Wii U発売

### [PyPro2](https://www.shuwasystem.co.jp/book/9784798043159.html) (黒+赤)

* 発売日: 2015年2月27日
* 472ページ
* 本体: 2,800円+税

![pypro2](images/pypro2.jpg)

### [PyPro2](https://www.shuwasystem.co.jp/book/9784798043159.html) 著者

* リーダー: 清水川貴之
* 岡野真也、drillbits、cactusman、東健太、tell-k、文殊堂、冨田洋祐、**aodag**、**鈴木たかのり**、**清原弘貴**

![pypro2](images/pypro2.jpg)

### [2015年](https://ja.wikipedia.org/wiki/2015%E5%B9%B4)のできごと

* [Python 3.5](https://peps.python.org/pep-0478/)、[Python 2.7.10](https://peps.python.org/pep-0373/)
* [Django 1.8](https://docs.djangoproject.com/en/5.0/releases/1.8/)
* Windows 10リリース
* マイナンバー法が施行
* 北陸新幹線が開業
* Apple Watch発売

### [PyPro3](https://www.shuwasystem.co.jp/book/9784798053820.html) (黒+青)

* 発売日: 2018年6月12日
* 488ページ
* 本体: 2,800円+税

![pypro3](images/pypro3.jpg)

### [PyPro3](https://www.shuwasystem.co.jp/book/9784798053820.html) 著者

* リーダー: 鈴木たかのり
* 清水川貴之、tell-k、清原弘貴、**James Van Dyne**、**的場達矢**、**吉田花春**、**新木雅也**、**altnight**、川村愛美、**石上晋**

![pypro3](images/pypro3.jpg)

### [2018年](https://ja.wikipedia.org/wiki/2018%E5%B9%B4)のできごと

* [Python 3.7](https://peps.python.org/pep-0537/)、[Python 2.7.15](https://peps.python.org/pep-0373/)
* [Django 2.1](https://docs.djangoproject.com/en/5.0/releases/2.1/)
* 平昌冬季オリンピック
* ロシアワールドカップ
* ZOZOSUITがリリース
* Google Home、Amazon Echo発売開始

### [PyPro4](https://www.shuwasystem.co.jp/book/9784798070544.html) (黒+緑)

* 発売日: 2024年2月16日
* 468ページ
* 本体: 3,000円+税

![pypro4](images/pypro4.jpg)

### [PyPro4](https://www.shuwasystem.co.jp/book/9784798070544.html) 著者

* リーダー: 石上晋
* **鈴木駿**、altnight、鈴木たかのり、**Yukie**、**荻野真志**、吉田花春、**降籏洋行**、川村愛美、的場達矢

![pypro4](images/pypro4.jpg)

### [2024年](https://ja.wikipedia.org/wiki/2024%E5%B9%B4)のできごと

* [Python 3.12.2](https://peps.python.org/pep-0693/)、[Python 3.13](https://peps.python.org/pep-0719/)(10月)
* [Django 5.0.2](https://docs.djangoproject.com/en/5.0/releases/5.0.2/)
* Python 3.7以前は[EOL](https://endoflife.date/python)、Django 3.2が[4月にEOL](https://endoflife.date/django)
* Apple Vision Pro発売開始(2月)
* 日本銀行券が刷新(7月)
* パリオリンピック開催(7月)

### PyPro出版の歴史のまとめ

* **12年** で **4回** 出版
* **メンバー** も **入れ替え** ながら
* 執筆 **リーダー** も **代わり** ながら

![pypro1](images/pypro1.jpg)
![pypro2](images/pypro2.jpg)
![pypro3](images/pypro3.jpg)
![pypro4](images/pypro4.jpg) 

## 改訂の歴史を **遡る**

## Pythonのセットアップ 🐍

### PyPro3 → PyPro4

![PyPro3](images/pypro3.jpg)
![PyPro4](images/pypro4.jpg)

### Docker / Docker Composeの採用

* Python開発環境として[Docker](https://www.docker.com/)を採用
* PyPro3では[VirtualBox](https://www.virtualbox.org/) / [Vagrant](https://www.vagrantup.com/) 上のUbuntu
  * Pythonをソースからインストール

### Black / Ruff / mypy

* 開発に便利なツールの最新化
* [Black](https://black.readthedocs.io/): コード整形ツール。2018年リリース
* [Ruff](https://docs.astral.sh/ruff/): Pythonリンター。2022年リリース
* [mypy](https://www.mypy-lang.org/): 型ヒントの静的型チェッカー
  * PyPro3ではリンターの[Flake8](https://github.com/pycqa/flake8)のみ紹介

### PyPro2 → PyPro3

![PyPro2](images/pypro2.jpg)
![PyPro3](images/pypro3.jpg)

### Pythonが2.7系

* インストールするPythonバージョンが2.7.6
  * PyPro3では3.6.4
* 仮想環境用に[virtualenv](https://github.com/pypa/virtualenv)をインストール
  * [venv](https://docs.python.org/ja/3/library/venv.html)モジュールはPython 3.3から
  
### バージョン管理がMercurial

* 当時はバージョン管理に[Mercurial](https://www.mercurial-scm.org/)を使用
  * サーバーも自前でたてていた
  * [Bitbucket](https://bitbucket.org/)も軽く紹介
  * PyPro3からGit/GitHub

### PyPro → PyPro2

![PyPro](images/pypro1.jpg)
![PyPro2](images/pypro2.jpg)

### get-pip.py

* `pip` コマンドはPythonに含まれていない
* `get-pip.py` をダウンロード→インストール

```bash
$ wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
$ sudo python get-pip.py
```

* ↑このURLは404 Not Found

### Flake8 → PEP8とPyFlakes

* Flake8 = PEP8 + PyFlakes + MaCabe
  * まだFlake8は使っていなかった
* `pep8` コマンドは現在は [pycodestyle](https://pypi.org/project/pycodestyle/)

## Webアプリケーション 🕸️

### PyPro3 → PyPro4

* WebアプリケーションからWeb APIへ
  * [Django](https://www.djangoproject.com/)でHTML生成ではなく、**APIのみ** 提供
  * フロントは[Vue.js](https://vuejs.org/)
  * [FastAPI](https://fastapi.tiangolo.com/)にも軽く触れている

### PyPro2 → PyPro3

* Flaskで乗りログ
  * [Flask](https://flask.palletsprojects.com/en/3.0.x/)でWebアプリ構築
  * お題は乗りログ（電車の乗車記録）

### PyPro → PyPro2

* Flaskでゲストブック
  * フレームワークは[Flask](https://flask.palletsprojects.com/en/3.0.x/)
  * お題はゲストブック

## データサイエンス 📊

### PyPro3 → PyPro4

* 機械学習からデータサイエンスへ
  * Jupyter Notebookから[JupyterLab](https://jupyterlab.readthedocs.io/en/latest/)に
  * **数理最適化** を紹介

### PyPro2 → PyPro3

* 機械学習の章が初登場
* 機械学習プロジェクトの進め方を紹介

## チーム開発のためのツール 🛠️

### PyPro3 → PyPro4

* **複数** の課題管理システムを紹介
  * Redmine、Backlog、JIRA、GitHub Projects
* Slackの使いこなしを追加
* **ビデオ、音声会議** を追加
* **Googleカレンダー**、**1Password** を追加
  * Dropbox、Dropbox Paperを削除

### PyPro2 → PyPro3

* 課題管理はRedmine一択
  * **Redmine** のインストールはあっさり

### PyPro → PyPro2

* **Redmine** のインストールはしっかり
  * PyProではTracで課題管理
* Mercurialとの連携
* チャットシステムは **Slack** (2013年リリース)
  * PyProではSkype

## 課題管理とレビュー 🎫

### PyPro3 → PyPro4

* Redmineの画面イメージを削除
  * 複数の課題管理システムに対応するため
* Backlog、Jira、GitHubでのテンプレート設定
* チケットテンプレート例がreST→ **markdown**

### PyPro → PyPro2

* **チケットテンプレート** が追加
* コードレビューには[rietveld](https://github.com/rietveld-codereview/rietveld)を使用
  * App Engine上で動くレビューツール
  
## ソースコード管理 🐙

### PyPro3 → PyPro4

* `git swtich` コマンドを紹介
* GUIクライアントの紹介を削除
  * エディタからの操作が増えた

### PyPro2 → PyPro3

* Git/GitHubに変更
  * ブランチ作成
  * マージ、リベース
  * GitHub Flow
  * GitHubのTips

### PyPro → PyPro2

* Mercurialでのソースコード管理
  * サーバー上の管理と設定
  * フックの活用
  * BeProud Mercurial Workflow

## 開発ドキュメント 📝

### PyPro3 → PyPro4

* 普遍的な開発ドキュメントの話に変更
* ビープラウドでは[TRACERY](https://tracery.jp/)を使用
  * [2022年リリース](https://prtimes.jp/main/html/rd/p/000000006.000025386.html)
* [Sphinx](https://www.sphinx-doc.org/)はあまり使われなくなった

## 単体テスト ✅

### PyPro3 → PyPro4

* [pytest](https://docs.pytest.org/)と各種pytestプラグイン
* Djangoのテストは[pytest-django](https://pytest-django.readthedocs.io/)
* pandasのテストとスナップショットテスト
  * 過去の実行結果を次回のテストで使う

### PyPro2 → PyPro3

* [unittest](https://docs.python.org/ja/3/library/unittest.html)とテストランナーにpytestの組み合わせ
* Webのテストは[WebTest](https://docs.pylonsproject.org/projects/webtest/)
  * [最終リリース](https://pypi.org/project/WebTest/)が2021年8月

### PyPro

* テストランナーが[nose](https://nose.readthedocs.io/)
  * [最終リリース](https://pypi.org/project/nose/)が2015年6月

## 継続的インテグレーション 🤵‍♂️

### PyPro3 → PyPro4

* [GitHub Actions](https://github.co.jp/features/actions)に改訂 ([2019年リリース](https://github.blog/jp/2019-11-14-universe-day-one/))
  * チェックアウト、Docker、ユニットテスト、静的解析
  * 結果のSlack通知

### PyPro2 → PyPro3

* [CircleCI](https://circleci.com/ja/)で継続的インテグレーション
  * ユニットテスト
  * Slack通知
  * Sphinxドキュメントのビルド

### PyPro → PyPro2

* [Jenkins](https://www.jenkins.io/)で継続的インテグレーション
  * Jenkinsのインストール
  * ユニットテスト
  * Sphinxドキュメントのビルド
