## いちばんやさしいPython機械学習の教本

### から見る

## 機械学習を学習する課題

### Takanori Suzuki

#stapy 48 / 2019 Aug 8

---

## 今日話すこと

* 書籍の紹介
* この内容になった経緯
* 機械学習を学習する課題

+++

## 最初にお願い

* 撮影📷、ツイート🐦ぜひどうぞ
* スライドは📝公開します
* ぜひ懇親会🍺でフィードバックください

---

## Who am I?(お前誰よ)

* 鈴木たかのり / Takanori Suzuki
* Twitter: [@takanory](https://twitter.com/takanory)
* [一般社団法人PyCon JP](https://www.pycon.jp) 副代表理事: `#pyconjp`
* [株式会社ビープラウド](https://www.beproud.jp) 役員
* [Python mini Hack-a-thon](https://pyhack.connpass.com/) 主催: `#pyhack`
* [Pythonボルダリング部](https://kabepy.connpass.com/) 部長: `#kabepy`

![takanory](assets/images/kurokuri.jpg)

+++

### PyCon JP

* PyCon JP 2019: [pycon.jp/2019](https://pycon.jp/2019/)

![PyCon JP 2019 logo](20190808stapy/images/pyconjp2019.png)

+++

### BeProud

* connpass: [connpass.com](https://connpass.com/)
* PyQ: [pyq.jp](https://pyq.jp/)
* 書籍: Pythonプロフェッショナルプログラミング
* (TODO: 画像入れる)

---

## 書籍の紹介

![](20190808stapy/images/ichiyasaml.jpg)

+++

### いちばんやさしいPython機械学習の教本

* 発売日: 2019年6月21日
* ページ数: 304
* 2,600円+税
* 著者: 鈴木 たかのり、降旗 洋行、平井 孝幸、株式会社ビープラウド

+++?image=20190808stapy/images/amazon.jpg&size=contain

+++

### 対象読者

* 「いちばんやさしいPythonの教本」を読んでいる
* Pythonの基本文法は知っている
* 機械学習学びたい人

+++

### 主な内容

* 1章: 機械学習について知ろう
* 2章: 開発環境の準備
* 3章: スクレイピング(データ収集)
* 4章: 文章自動生成(自然言語処理)
* 5章: 手書き文字認識(機械学習)
* 6章: 表データの前処理
* 7章: 気温予測(回帰分析)
* 8章: 次のステップ

+++

### 特徴

* 1章は完全な読み物
* 3章/4章/5章/6章+7章は好きなところから
* 各章の最後はpybotでコマンド化

+++?image=20190808stapy/images/lesson11.png&size=90% auto

+++?image=20190808stapy/images/overview2.png&size=contain

@snap[south]
@size[x-small](https://shacho.beproud.jp/entry/ichiyasa-pythonml)
@snapend

---

## この内容になった経緯

+++

### 2018年1月10日に打診あり

![](20190808stapy/images/dashin.png)

+++

### 社内的にGO!がでる

* 2018年1月12日: 編集者と打合せ
* 2018年1月18日: 社内でGoがでる
* 2018年1月24日: 平井がjoin
* 2018年2月1日: 第2回目打合せ
* →まずはネタ出しを進める

+++?image=20190808stapy/images/ideathon.png&size=90% auto

+++

### 企画案を編集に伝える

* 2018年7月6日
* 環境構築、pybot準備
* スクレイピングでデータ収集
* マルコフ連鎖で文章生成
* 手書き文字認識
* 前処理と予測
* 回帰分析
* 次のステップ

+++?image=20190808stapy/images/editor-comment.png=90% auto

+++

### ホワイトボードで各要素の関連を説明

![ホワイトボード](20190808stapy/images/whiteboard1.jpg)

+++

### ホワイトボードで各要素の関連を説明

![ホワイトボード](20190808stapy/images/whiteboard2.jpg)

+++

### ホワイトボードで各要素の関連を説明

![ホワイトボード](20190808stapy/images/whiteboard3.jpg)

+++

### そして現在の構成に

![機械学習プロジェクトの全体像](20190808stapy/images/overview.png)

+++

### 長い戦いがはじまった!!!✒️

* 2018年7月31日: 降籏がjoin
* 2018年8月: 執筆開始
  * 8カ月に渡る戦い
* 2019年4月5日: 脱稿
  * 当初は1月中旬で3月発売予定...

+++

### そして出版へ📕

* 2019年4月22日: 著者初校、校閲
* 2019年5月11日: 再校作成(編集)
* 2019年5月20日: 著者
* 2019年5月23日: 念校・仕上げ
* 2019年5月27日: 印刷所入稿
* 2019年05月30日: 校了
* 2019年06月21日: 発売！！

---

## 機械学習を学習する課題

+++

(注)個人的な意見であり、特定の書籍、人物などを批判するものではありません。

+++

### 機械学習だけじゃなにもできない問題

+++

### 機械学習だけじゃなにもできない問題

* 機械学習でなにかを作り上げるにはそれ以外がとても大事
  * 課題の設定
  * データ収集
  * 前処理

+++

### 全体の流れを解説

![全体の流れ](20190808stapy/images/flow.png)

+++

### 最後までがとても長い問題

+++

### 最後までがとても長い問題

* データ収集
* 前処理
* 機械学習
* 精度評価→ここで一旦ゴール

Note:
途中で心折れそう

+++

### それぞれを断片的に体験できる

![各Chapterの範囲](20190808stapy/images/hani.png)

+++

### そのデータ面白くない問題

+++

### そのデータ面白くない問題

* アヤメとかボストンの住宅とか興味ないでしょ?

+++

### イメージが湧きそうなデータを使用

![データ](20190808stapy/images/data.png)

+++

### 用語多過ぎ問題

+++

---

## Thank You!

* Twitter: [@takanory](https://twitter.com/takanory)
* Slides: [github.com/takanory/slides](https://github.com/takanory/slides)
