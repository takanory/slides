```{eval-rst}
:og:image: _images/20240307bpstyle.png
:og:image:alt: Amazon Pollyで問題文を読み上げ

.. |cover| image:: images/20240307bpstyle.png
```

# **Amazon Polly** で<br />問題文を読み上げ

Takanori Suzuki

BPStyle #158 / 2024 Mar 7

## 背景

* 某案件で学習教材の電子化をやっている
* **合理的配慮** の一環としてテキスト読み上げを実現したい
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

* 問題文等を読み上げられるようにする
  * 聴覚優位の生徒が理解しやすくする
* 完全に読み上げられなくてもある程度しょうがない

### ちなみに全盲の場合

* OSのアクセシビリティ機能を使う
* PC上のスクリーンリーダーを使用する
* Web側はアクセシビリティに対応する
* 参考: [ウェブアクセシビリティ導入ガイドブック｜デジタル庁](https://www.digital.go.jp/resources/introduction-to-web-accessibility-guidebook/)
* →今回は対象外

## Amaozon Polly

### Amaozon Polly

* [Amazon Polly（深層学習を使用したテキスト読み上げサービス）| AWS](https://aws.amazon.com/jp/polly/)
* **数十の言語** で高品質で自然な人間の声を展開
* 12ヶ月間、 毎月 **500万文字が無料**
* クラウド型コールセンターのAmazon Connectでも使える

### Amazon Pollyのデモ

* [テキスト読み上げ機能 | Amazon Polly | ap-northeast-1](https://ap-northeast-1.console.aws.amazon.com/polly/home/SynthesizeSpeech)
* 多分ytakashimaさんは平成狸合戦ぽんぽこが好き（適当）([nibu.mp3](nibu.mp3))
* Maybe ytakashima-san likes Heisei Raccoon War Ponpoko (appropriate) ([nibu-en.mp3](nibu-en.mp3))

### PythonからAmazon Pollyを実行

```bash
(env) $ pip install boto3
(env) $ export AWS_ACCESS_KEY_ID=AKI...
(env) $ export AWS_SECRET_ACCESS_KEY=ZoWb...
(env) $ export AWS_DEFAULT_REGION=ap-northeast-1
```

* Boto3をインストール
* APIを使うための環境変数を設定

```{revealjs-break}
```

```{literalinclude} code/polly.py
```

* [Polly - Boto3 1.34.56 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html)
* [AWSでAIサービスを使ってみる〜第3回polly編〜 #Python - Qiita](https://qiita.com/AInosukey/items/cb86c1012d40747b9dda)

```{revealjs-break}
```

* mp3ファイルができた！！ 🎉
* [masashinji.mp3](masashinji.mp3)

## Amazon Pollyカスタマイズ

### 言語の変更

* 言語と音声は`VoiceId`引数を変更する
* [Amazon Polly の音声 - Amazon Polly](https://docs.aws.amazon.com/ja_jp/polly/latest/dg/voicelist.html)
* 日本語: Mizuki, Takumi, Kazuha, Tomoko
* 英語: Ivy, Salli, Joey, Justin...など

```{literalinclude} code/polly2.py
:lines: 7-8
```

* [hajimo.mp3](hajimo.mp3)
