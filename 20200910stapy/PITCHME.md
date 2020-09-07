## オンライン時代のプログラミング習得について考える

### Takanori Suzuki

#stapy 61 / 2020 Sep 10

---

## 今日話すこと

* 最近関わった書籍の紹介(宣伝)
* オンライン時代のプログラミング習得について考える

+++

## 最初にお願い

* 撮影📷、ツイート🐦ぜひどうぞ
* スライドは📝公開してます
* ぜひ懇親会🍺でフィードバックください

---

## Who am I?(お前誰よ)

* 鈴木たかのり / Takanori Suzuki
* Twitter: [@takanory](https://twitter.com/takanory)
* [一般社団法人PyCon JP Association](https://www.pycon.jp) 副代表理事: `#pyconjp`
* [株式会社ビープラウド](https://www.beproud.jp) 役員
* [Python mini Hack-a-thon](https://pyhack.connpass.com/) 主催: `#pyhack`
* [Pythonボルダリング部](https://kabepy.connpass.com/) 部長: `#kabepy`

![takanory](assets/images/kurokuri.jpg)

+++

### PyCon JP🐍

* PyCon JP 2019: [pycon.jp/2019](https://pycon.jp/2019/)

![PyCon JP 2019 logo](20190808stapy/images/pyconjp2019.png)

+++

### BeProud

* connpass: [connpass.com](https://connpass.com/)
* PyQ: [pyq.jp](https://pyq.jp/)
* 書籍: Pythonプロフェッショナルプログラミング他

![BeProud](20190808stapy/images/beproud.png)

---

## 書籍の紹介

![いちばんやさしいPython機械学習の教本](20190808stapy/images/ichiyasaml.jpg)

+++?image=20200910stapy/images/ichiyasa2.jpg&position=left&size=25% auto

@snap[east span-70 text-center]
### いちばんやさしいPythonの教本 第2版

* https://book.impress.co.jp/books/1119101162
* 発売日: 2020年8月24日
* ページ数: 272
* 2,200円+税
* 主な内容: あああ
@snapend

+++?image=20200910stapy/images/pattern80.jpg&position=left&size=25% auto

@snap[east span-70 text-center]
### つなげば動く！ Pythonふりがなプログラミング パターン文例80

* https://book.impress.co.jp/books/1119101161
* 発売日: 2020年7月22日
* ページ数: 248
* 2,200円+税
* 主な内容: あああ
@snapend

+++?image=20200910stapy/images/pythnon-excel.jpg&position=left&size=25% auto

@snap[east span-70 text-center]
### できる 仕事がはかどるPython＆Excel自動処理 全部入り。

* https://book.impress.co.jp/books/1119101179
* 発売日: 2020年8月24日
* ページ数: 280
* 2,150円+税
* 主な内容: あああ
@snapend

+++?image=20200910stapy/images/saitan-python1.jpg&position=left&size=25% auto

@snap[east span-70 text-center]
### 最短距離でゼロからしっかり学ぶ Python入門 必修編

* https://gihyo.jp/book/2020/978-4-297-11570-8
* 発売日: 2020年9月2日
* ページ数: 312
* 3,200円+税
* 主な内容: あああ
@snapend

+++?image=20200910stapy/images/saitan-python2.jpg&position=left&size=25% auto

@snap[east span-70 text-center]
### 最短距離でゼロからしっかり学ぶ Python入門 実践編

* https://gihyo.jp/book/2020/978-4-297-11572-2
* 発売日: 2020年9月2日
* ページ数: 344
* 3,300円+税
* 主な内容: あああ
@snapend

+++?image=20190808stapy/images/amazon.jpg&size=90% auto

+++

### シリーズの特徴

![読み方](20190808stapy/images/how-to-read.png)

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

### 本書の特徴

* 1章は完全な読み物
* 3章/4章/5章/6章+7章は好きなところから
* 各章の最後はpybotでコマンド化

+++?image=20190808stapy/images/lesson11.png&size=90% auto

+++?image=20190808stapy/images/overview2.png&size=90% auto

@snap[south]
@size[small](https://shacho.beproud.jp/entry/ichiyasa-pythonml)
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

+++?image=20190808stapy/images/editor-comment.png&size=70% auto

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
* 2019年5月20日: 著者再校
* 2019年5月23日: 念校・仕上げ
* 2019年5月27日: 印刷所入稿
* 2019年05月30日: 校了
* 2019年06月21日: 発売!!🎉

---

## 機械学習を学習する課題

+++

(注)個人的な意見であり、特定の書籍、人物などを批判するものではありません。

+++

### 課題: 機械学習だけじゃなにもできない

+++

### 課題: 機械学習だけじゃなにもできない

* 課題の設定
* データ収集
* 前処理

Note:
* 機械学習でなにかを作り上げるにはそれ以外がとても大事。
* とくに元となるデータを用意するのが超重要。

+++

### そこで: 全体の流れを解説

![全体の流れ](20190808stapy/images/flow.png)

+++

### そこで: 周辺技術も体験

* スクレイピングでデータ収集(Ch.3)
* 日本語の形態素解析(Ch.4)
* データの前処理(Ch.6)
* 精度の評価(Ch.5, 7)

+++

### 課題: 最後までがとても長い

+++

### 課題: 最後までがとても長い

![全体の流れ](20190808stapy/images/flow.png)

Note:
* さきほど全体の流れを示したが、最後までやろうとするととても長い
* 結果が出るまですごい時間がかかる
* 途中で心折れそう

+++

### そこで: 断片的に体験できる

![各Chapterの範囲](20190808stapy/images/hani.png)

+++

### 課題: 達成感がない

+++

### 課題: 達成感がない

* コードを実行してグラフ表示→で?

+++

### そこで: botでアプリケーション化

![bot化](20190808stapy/images/bot1.png)

+++

### そこで: botでアプリケーション化

![bot化](20190808stapy/images/bot2.png)

+++

### 課題: データが面白くない

+++

### 課題: データが面白くない

* アヤメとかボストンの住宅価格とか興味ある?

+++

### そこで: イメージが湧くデータ

![データ](20190808stapy/images/data.png)

+++

### 課題: 用語多過ぎ

+++

### 課題: 用語多過ぎ

欠損値、外れ値、形態素解析、ラベル、教師あり学習、教師なし学習、分類、回帰、クラスタリング、アンサンブル学習、モデル、線形回帰、ロジスティック回帰、サポートベクターマシン、決定木、ランダムフォレスト、混同行列、真陽性、偽陽性、偽陰性、真陰性、正解率、適合率、再現率、F値、、、

+++

### そこで: 用語集を用意

![用語集](20190808stapy/images/glossary.png)

Note:
* どのカテゴリの用語かもわかりやすい
* どのChapterで扱っているかも書いているので便利!!

+++

### 課題: やってみても成果がでない

+++

### 課題: やってみても成果がでない

* 「AIでなんかやって」と無茶振り

+++

### そこで: データがないとだめだよ

![データ収集](20190808stapy/images/data-collect.png)

+++

### そこで: 成果が出ない場合あるよ

![PoC](20190808stapy/images/poc.png)

+++

### そこで: 費用対効果が大事だよ

![PoC](20190808stapy/images/seido.png)

+++

### 課題まとめ

* なにもできない→周辺技術を知って体験
* 最後までが長い→断片的に体験
* 達成感がない→botのコマンド化
* データ面白くない→興味が湧くデータ
* 用語多過ぎ→用語集とLessonの対応
* 成果でない→データ量、成果でないことある、費用対効果

---

## まとめ

* 書籍の紹介
* この内容になった経緯
* 機械学習を学習する課題

---

## Thank You!

* Twitter: [@takanory](https://twitter.com/takanory)
* Slides: [github.com/takanory/slides](https://github.com/takanory/slides)

---

## おまけページ

執筆時の工夫

+++

### アウトラインでレビュー

* 執筆初期にアウトライン状態で著者レビュー
  * 見出し、何を書くつもりか箇条書き
* ストーリー的によさそうかをチェック
* 説明の抜け漏れを防ぐ
* 全体的な流れが統一しやすかった

+++

### レビュー説明会

* BeProud社内から17名のレビュワーが参加
  * 機械学習ﾁｮｯﾄﾃﾞｷﾙ/ﾃﾞｷﾅｲ勢
* レビューの観点、心の持ち方を説明
  * (日本語の)バグを憎んで人を憎まず
  * 思ったらとりあえず書く
  * 指摘が採用されなくても気にしない
* レビューシートでバランス調整

+++

### Adobe Document Cloud

* 前半はPDFをDropboxでレビュー
* コメント増えると重たい問題
* Adobe Document Cloud超便利!!!
  * 依頼者は有料アカウント必要
  * Acrobat Readerでレビューできる
  * 激列に軽い!
  * オフラインでレビューできる!!

---

## Thank You!

* Twitter: [@takanory](https://twitter.com/takanory)
* Slides: [github.com/takanory/slides](https://github.com/takanory/slides)

