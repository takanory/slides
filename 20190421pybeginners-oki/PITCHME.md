## Slackbot: PyCon JP Botの紹介

2018 Apr 21 / PythonBeginners沖縄 22

Takanori Suzuki

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

* https://www.pycon.jp/
* 年に一回Pythonのカンファンレンスを開催(今年は9月に東京)
* 昨日のOSC沖縄に出展するために沖縄に来た
* 16:30の飛行機で帰ります(お先に失礼します)

+++

### BeProud

* https://www.beproud.jp/
* メインはPythonで受託
* connpassの運営会社
* オンライン学習サービスPyQの運営会社
  * https://pyq.jp/

+++

### おみやげ

* 各種ステッカー、PyQのお試しコードなど

(写真)

---

### Conferenceのタスク

* キーノート、トーク、チュートリアルの計画
* チケット発売と受付
* 設備(無線LAN、ビデオ等)の管理
* 食事、コーヒー、おやつ、ビール🍺

Note:

* PyCon JPを運営していましたが、カンファレンスにはたくさんのタスクがあります

+++

## プログラマーは怠惰

Note:

* プログラマーはルーチンワークが嫌い。私も大嫌いです

+++

## 誰か助けて!!!

Note:

* 面倒な作業を誰か代わりにやってほしい

+++

## そうだ作ろう!!

---

## Slackbot: PyCon JP Botの紹介

* PyCon JP Slack用チャットBot

+++

### なぜチャットBot?

* Slackアプリは常に起動
* すぐにSlackにアクセスできる
* Slackでなんでもやろう

![Slack](20190421pybeginners-oki/images/slack.png)

+++

### PyCon JP Bot

* GitHub: https://github.com/pyconjp/pyconjpbot
* Slackbotベース: https://github.com/lins05/slackbot
* Slack API: https://api.slack.com/

+++

### PyCon JP Bot

![architecture](20190421pybeginners-oki/images/architecture.png)

+++

### `$ping` コマンド

```python
from slackbot.bot import respond_to

@respond_to('ping')
def ping(message):
    """$ping -> pong"""
    message.send('pong')
```

Note:

* respond_to デコレーターで指定したコマンドに応答します

+++

### `$choice` コマンド

```python
@respond_to('^choice\s+(.*)')
def choice(message, words):
    """$choice spam ham eggs -> ham"""
    word_list = words.split()
    message.send(random.choice(word_list))
```

Note:

正規表現を使用してコマンドからパラメーターを取り出せます

+++

コマンド | 説明
--- | ---
`$google` | google検索
`$image` | google画像検索
`$jira` | JIRAの課題を検索
`$wikipedia` | Wikipediaを検索
`$weather` | 天気予報
`$translate` | 機械翻訳
`$gadmin` | Google adminでの管理
`$lgtm` | LGTM画像の生成

Note:

PyCon JP Botに実装されているコマンドの一例です

---

## デモ

Note:

* `$ping`
* `$choice タコライス 沖縄そば ゴーヤーチャンプルー`
* `$image 沖縄そば`
* `$wikipedia 沖縄そば`
* `$wikipedia -en okinawa soba`
* `$google 沖縄そば 那覇 おすすめ`
* `12300 / 8`
* `$weather`
* `$weather 那覇`
* `$lgtm create https://pbs.twimg.com/media/D4hCiW-X4AIUUFn.jpg THANK YOU !`

+++?image=20190421pybeginners-oki/images/demo1.png&size=auto 100%

+++?image=20190421pybeginners-oki/images/demo2.png&size=auto 100%

+++?image=20190421pybeginners-oki/images/demo3.png&size=auto 100%

+++?image=20190421pybeginners-oki/images/demo4.png&size=auto 100%

