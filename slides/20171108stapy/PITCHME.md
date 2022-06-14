# いちばんやさしいPythonの学び方の作り方

2017 Nov 8 / みんなのPython勉強会#30 

Takanori Suzuki

Note:
この書籍がタイトルどおり「いちばんやさしい」内容となることを目指して、執筆にどのどのような工夫をしていたかについて語ります。
また、この書籍の執筆やPython研修の中で感じている、初めてのプログラミング言語を学ぶときのポイントについても紹介します。

---

## Who am I?(お前誰よ)

* 鈴木たかのり / Takanori Suzuki
* Twitter: [@takanory](https://twitter.com/takanory)
* [Python mini Hack-a-thon](https://pyhack.connpass.com/)(#pyhack)主催
* [Pythonボルダリング部](https://kabepy.connpass.com/)(#kabepy)部長

![takanory](assets/images/kurokuri.jpg)

---

### 株式会社ビープラウド所属

* https://www.beproud.jp/

![BeProud](assets/images/beproud.png)

+++

### PyQ

* Pythonに特化したオンライン学習サービス
* https://pyq.jp/

![PyQ](assets/images/pyq.png)

+++

### connpass

* IT勉強会支援プラットフォーム
* https://connpass.com/

![connpass](assets/images/connpass.png)

---

### 一般社団法人PyCon JP理事

* https://www.pycon.jp/

![PyCon JP](assets/images/pyconjp_logo.png)

+++

### PyCon JP 2017

* 国内最大のPythonイベント
* https://pycon.jp/2017/ja/

![PyCon JP 2017](assets/images/pyconjp2017-logo.png)

+++

### Python Boot Camp

* 初心者向けPythonチュートリアル
* https://www.pycon.jp/support/bootcamp.html

![Python Boot Camp](assets/images/python-boot-camp-logo.png)

---

## はなすこと

* 「いちばんやさしいPythonの教本」の紹介
  * 執筆チームの紹介
  * この本のつくり方
* プログラミングを学ぶときのポイント

---

## いちばんやさしいPythonの教本

![いちばんやさしいPythonの教本](assets/images/ichiyasa.jpg)

+++

### いちばんやさしいPythonの教本

* 272ページ / 2,376円(税込)
* 著者: 鈴木 たかのり、杉谷 弥月
* 2017年8月10日発売
* https://book.impress.co.jp/books/1116101151

+++

### 「いちばんやさしい教本」シリーズ

- https://book.impress.co.jp/category/series/easybook/
- 「絶対に挫折しない」をコンセプトとした実用書
- 第一線で活躍する講師のセミナーを受けているように学べる

+++?image=20171108stapy/images/easybook.png&size=contain

+++

### 「解説パート」+「手順パート」

+++?image=20171108stapy/images/ichiyasa-sample1.png&size=contain

+++?image=20171108stapy/images/ichiyasa-sample2.png&size=contain

---

### 執筆チーム

* 著者: 鈴木 たかのり([@takanory](https://twitter.com/takanory))、杉谷 弥月
* 社内レビュワー

  * [@shimizukawa](https://twitter.com/shimizukawa)
  * [@haru860](https://twitter.com/haru860)
  * [@okusama27](https://twitter.com/okusama27)

* ヘルプコラミスト

  * [@hirokiky](https://twitter.com/hirokiky)

---

## 書籍の内容

+++

### 目次

* 1章 Pythonを学ぶ準備をしよう
* 2章 コマンドプロンプトに慣れよう
* 3章 基礎を学びながらプログラムを作成しよう
* 4章 繰り返しと条件分岐を学ぼう
* 5章 辞書とファイルの扱いを学ぼう
* 6章 会話botを作ろう
* 7章 ライブラリを使いこなそう
* 8章 サードパーティ製パッケージを使いこなそう
* 9章 Webアプリケーションを作成しよう
* 10章 さらに知識を身に付けるための学び方

Note:
それぞれざーっと構成を説明します

+++

### プログラミング入門

プログラムを書いたことがない人向けの内容

* 1章 Pythonを学ぶ準備をしよう
  * コンピューターの仕組み
  * Python、Atomインストール
* 2章 コマンドプロンプトに慣れよう
  * コマンドでのファイル操作
* 3章 基礎を学びながらプログラムを作成しよう
  * 演算、print()関数
  * 変数、str型、int型
  * リスト、タプル

Note:
PCに環境を構築するところから、プログラミングとは何か、どのようにコンピューターで動作するのかを丁寧に解説しています。

+++

### Python言語入門

プログラムを作る上で欠かせない文法を解説

* 4章 繰り返しと条件分岐を学ぼう
  * for文、if文
* 5章 辞書とファイルの扱いを学ぼう
  * 辞書
  * open()関数

Note:
プログラミングの基本となるfor文(繰り返し)、if文(条件分岐)や、Pythonのデータ型(辞書)、ファイル入出力

+++

### 会話botによるアプリケーション開発

会話botの開発を通してPythonの機能を使いこなす

* 6章 会話botを作ろう
  * in演算子、break文
  * 関数、組込関数
* 7章 ライブラリを使いこなそう
  * モジュール、標準ライブラリ
  * 例外処理
* 8章 サードパーティ製パッケージを使いこなそう
  * pip、venv
  * requests

+++

### はじめてのWebアプリケーション開発

会話botをWebアプリケーション化する。

* 9章 Webアプリケーションを作成しよう
  * Webアプリケーションとは
  * Bottle
  * テンプレート
  * フォーム

+++

### 次のステップ

さらに学ぶための情報源を紹介。

* 10章 さらに知識を身に付けるための学び方
  * 書籍
  * Webサイト
  * コミュニティ
  
---

## この本のつくり方

Note:
初心者向けで気をつけたことと、文章をを書く場合に当たり前のこともあると思います。

+++

### 「いちばんやさしい教本」シリーズ

* 「絶対に挫折しない」をコンセプトとした実用書

+++

### 素早く理解できるように

* 説明していない用語を使わない
* 徐々にできることが増えていく
* 最初にコードとストーリーをレビュー

+++

### 読みやすい日本語

* できるだけ短い表現にする
* 曖昧な用語を使わない、主語をはっきり
* 代名詞をできるだけ使わない
* 表記ゆれをなくす

Note:
脳内のバッファを使わない文章にする。

+++

### 次のステップをサポート

* botプログラムに徐々にコマンドを追加
* botアプリケーションをWeb化


+++

### この本でできないこと

* リファレンス的な使い方

---

## 研修講師の経験をフィードバック

Note:
そこでつまずくかー的なところもサポート

+++

### 自分の場所がわからない問題

Note:
フォルダで場所がわからなくなる

+++?image=20171108stapy/images/ichiyasa-folder.png&size=contain

+++

### 機能分割できない問題

+++?image=20171108stapy/images/ichiyasa-algorithm.png&size=contain

+++

### コードどこ書き換えるのかわからない問題

+++?image=20171108stapy/images/ichiyasa-diff.png&size=contain

+++

### スライスわかりにくい問題

+++?image=20171108stapy/images/ichiyasa-slice.png&size=contain

---

## プログラミングを学ぶときのポイント

+++

### 書籍は自分に合うものを

* 大きい本屋に行ってパラパラとめくってみる
* 自分がなんとなく気に入ったものを買う
* リファレンスとしては使えないと割り切る

+++

### 使うものを作ろう

* 繰り返している作業
* 面倒なことをプログラムにやらせよう

Note:
このあいだ研修で月一回のデータの比較をPythonにしてみたらしい。すごい

+++

### オレ凄えって思う

* 誰かに褒められるともっとうれしい

+++?image=20171108stapy/images/pyconjpbot-image.png&size=contain

+++

### PyQもよろしくね!

* Pythonに特化したオンライン学習サービス
* https://pyq.jp/

![PyQ](assets/images/pyq.png)


---

## ありがとうございました

---

## Question?
