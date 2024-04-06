```{eval-rst}
:og:image: _images/20240417pythonkansai.png
:og:image:alt: Amazon Pollyで問題文を読み上げ

.. |cover| image:: images/20240417pythonkansai.png
```

# **Amazon Polly** で<br />問題文を読み上げ

Takanori Suzuki

Python Kansai #03 / 2024 Apr 17

## アジェンダ 📜

* 背景とゴール
* Amazon Pollyの基本
* 読み上げをカスタマイズ
* 問題文読み上げでやったこと

## 背景 🏞️

* 学習教材の **電子化** プロジェクト
* **合理的配慮** の一環としてのテキスト読み上げ
* 全盲の人向けではなく、**聴覚優位** の人向け

### 合理的配慮

> 合理的配慮とは、障害者から何らかの助けを求める意思の表明があった場合、過度な負担になり過ぎない範囲で、社会的障壁を取り除くために必要な便宜のことである。 

* [合理的配慮 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%90%88%E7%90%86%E7%9A%84%E9%85%8D%E6%85%AE)

### 聴覚優位

> 子どもたちの情報の取り入れ方を下記の3タイプに分類し、“知覚の優位性”という考え方が世界に広がっていったことに始まります。
>
> 視覚優先型・聴覚優先型・運動感覚/触覚優先型

* [聴覚優位タイプとは？見るより聞くほうが理解しやすい子の勉強方法を専門家が解説](https://soctama.jp/column/67272)

### やりたいこと

* 問題文などを **読み上げ** られる
  * **聴覚優位** の生徒が理解しやすく
* 完全な読み上げじゃなくてもよい

### ちなみに全盲の場合

* OSのアクセシビリティ機能を使う
* PC上のスクリーンリーダーを使用する
* Web側はアクセシビリティに対応する
* 参考: [ウェブアクセシビリティ導入ガイドブック｜デジタル庁](https://www.digital.go.jp/resources/introduction-to-web-accessibility-guidebook/)
* →今回は対象外

## ゴール 🥅

* **Amazon Polly** での音声合成を知る
* Pythonでの **実装方法** を知る
* 読み上げの **カスタマイズ方法** を知る

## Photos 📷 Tweets 🐦 👍

`#pythonkansai` / `@takanory`

### Slides / スライド 💻

[slides.takanory.net](https://slides.takanory.net/)

<!-- ![slides.takanory.net](images/slides-takanory-net.png) -->

## **Who** am I? / お前 **誰よ** 👤

* Takanori Suzuki / 鈴木 たかのり ({fab}`twitter` [@takanory](https://twitter.com/takanory))
* [BeProud](https://www.beproud.jp/) 取締役 / Python Climber
* [PyCon JP Association](https://www.pycon.jp/) 代表理事
* [Python Boot Camp](https://www.pycon.jp/support/bootcamp.html) 講師、[Python mini Hack-a-thon](https://pyhack.connpass.com/) 主催、[Pythonボルダリング部](https://kabepy.connpass.com/) 部長

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

### PyCon JP **Association** 🐍

日本国内のPythonユーザのために、**Pythonの普及及び開発支援**を行うために、継続的にカンファレンス(**PyCon**)を開くことを目的とした **非営利組織**

[`www.pycon.jp`](https://www.pycon.jp)

![pycon jp logo](/assets/images/pyconjp_logo.png)

### PyCon JP **2024** 🇯🇵

* {fas}`globe` [`2024.pycon.jp`](https://2024.pycon.jp/)
* **9月27-29日** に **東京** で開催予定
* 3名の **共同座長**(with 吉田さん、寺田さん)
* **主催メンバー** 募集中
* 詳細: [PyCon JP 2024座長決定のお知らせと主催者グループのメンバー募集](https://pyconjp.blogspot.com/2024/01/pyconjp2024-co-chair.html)

### **BeProud** Inc. 🏢

* [BeProud](https://www.beproud.jp/): Pythonシステム開発、コンサル
* [connpass](https://connpass.com/): IT勉強会支援プラットフォーム
* [PyQ](https://pyq.jp/): Python独学プラットフォーム
* [TRACERY](https://tracery.jp/): システム開発ドキュメントサービス

![BeProud logos](/assets/images/beproud-logos.png)

### PyPro4 📕

* [Python Professional Programming 第4版](https://www.shuwasystem.co.jp/book/9784798070544.html)
* 2024年2月16日発売、468ページ、3300円

![PyPro4](/assets/images/pypro4.jpg)

## Amazon Pollyの基本 🗣️

##  読み上げをカスタマイズ 🔧

## 問題文読み上げでやったこと 📖

## Amazon Pollyの補足情報 🔍

## まとめ 📚

## Thank You 🙏

{fas}`desktop` [slides.takanory.net](https://slides.takanory.net/)

{fab}`twitter` [@takanory](https://twitter.com/takanory)
{fab}`github` [takanory](https://github.com/takanory/)
{fab}`linkedin` [takanory](https://www.linkedin.com/in/takanory/)
{fab}`untappd` [takanory](https://untappd.com/user/takanory/)

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)
