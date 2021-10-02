# 2要素認証について知ろう

2020 May XXX / Takanori Suzuki

---

## 目的

* 認証にどういう種類があるか知る
* 2要素認証がどういうものか知る
* それぞれのメリットデメリットを知る

+++

## お品書き

* パスワード認証
  * パスワード認証の問題
  * パスワード管理ソフト
* 2要素認証(2FA)
  * 2要素認証どうやるの
  * Slackで2FAを設定

---

## 最初に質問

+++

### パスワード管理ソフト使っている人? 🙋‍♀️

+++

### 2要素認証がどういうものか説明できる人? 🙋‍♂️

+++

### 2要素認証を導入している人? 🙋‍♀️

---

## パスワード認証

+++

### パスワード認証とは

* IDとパスワードの組み合わせでの本人確認手段
* IDとパスワードを知っている人
  * →本人

+++

### Q: パスワード認証にはどんな問題がありますか?

+++

### パスワードが漏れるとこうなる

* 参考: [WIRED記者の悲劇から学ぶ「セキュリティ9つの常識」](https://wired.jp/2012/08/14/how-not-to-become-mat-honan/)

+++

### パスワードが漏れるとこうなる

* iPhoneのデータが全削除
* MacBookのデータが全削除
* Twitterを乗っ取られる
* 8年分のGMailを全削除

+++

### アシュレイ・マディソン

* 不倫マッチングサイトのデータがクラッキングされて流出
* 11,000,000件のパスワードがクラックされた

* 参考: [「123456」がダントツ人気パスワード、CEO辞任も依然としてユーザー増加中など不倫SNS「アシュレイ・マディソン」情報流出騒動をめぐるあれこれ総まとめ](https://gigazine.net/news/20150914-ashley-madison-password-lesson/)

+++

### パスワードTop5

1. `123456`
2. `12345`
3. `password`
4. `DEFAULT`
5. `123456789`

+++

### パスワード流出をチェック

* [`haveibeenpwned.com`](https://haveibeenpwned.com/) : メールアドレス
* [`haveibeenpwned.com/Passwords`](https://haveibeenpwned.com/Passwords) : パスワード

![have i been pwned](201908-2fa/images/haveibeenpwned.png)

+++

### パスワード認証の問題

* 複数のサイトで共通のパスワード使うと危険
  * 1つバレたら全部バレる
* サイトごとにパスワードのルールが異なる
  * 文字数、文字種(英字、数字、記号)
* でもそんなの人は覚えられない

+++

### パスワード管理ソフト

* IDとパスワードを管理するソフト
  * [1Password](https://1password.com/)
  * [LastPass](https://www.lastpass.com/ja)
  * [Dashlane](https://www.dashlane.com/)
  * [Bitwarden](https://bitwarden.com/)

+++

### パスワード認証の問題(その2)

* 漏洩のリスク
* 悪意のある中の人
* 総当たり攻撃
  * [参考Tweet](https://twitter.com/yamatosecurity/status/1155289692268457985)

+++?image=201908-2fa/images/password-recovery-times.jpg&size=contain 90%

+++

## そこで

## 2要素認証

---

### 2要素認証とは

* 2FA(Two-factor Authentication)
* 2種類の要素で認証する

+++

### 2種類の要素って?

* 以下の3要素のうち2つ
  * 本人だけが知っていること
  * 本人だけが所有しているもの
  * 本人自身の特性
* Q: それそれどんな認証が例として考えられますか?
* 参考: [二要素認証とは？セキュリティを向上させる5つのポイント](https://japan.norton.com/two-factor-authentication-8528)

+++

### 認証の例

* 本人だけが知っていること: パスワード
* 本人だけが所有しているもの: トークン、スマートフォン
* 本人自身の特性: 指紋、顔認証

+++

### 2段階認証

* 2要素認証≠2段階認証
* Q: 違いを説明できますか?

+++

### 2要素認証≠2段階認証

* 例: ネットバンキングなど
  * ログインパスワード(1段階)
  * 振り込み時に秘密の質問(2段階)
* どちらも「本人だけが知っていること」なので1要素

---

## 2要素認証(2FA)どうやるの

+++

## 2要素認証(2FA)どうやるの

* Webサービス + スマートフォンアプリ
* 引用元: [多要素認証とは？パスワードだけでは守りきれないクラウドのセキュリティ](https://www.secure-sketch.com/blog/multi-factor-authentication)

![多要素認証実施までの流れ](https://www.secure-sketch.com/hs-fs/hubfs/blog_GRCP%E5%AF%84%E7%A8%BF/201810_MFA%EF%BC%88%E5%B1%B1%E7%94%B0%EF%BC%89/MFA2.jpg)

+++

### 2FAに対応しているサービス(例)

* Googleアカウント
* Dropbox
* Slack
* Evernote
* Facebook
* Twitter
* GitHub
* AWS
* PayPal

+++

### 2FAの認証クライアント

* スマートフォンにインストールして使う
  * [Authy](https://authy.com/)
  * [Google Authenticator](https://support.google.com/accounts/answer/1066447?co=GENIE.Platform%3DAndroid&hl=ja&oco=0)
  * [LastPass Authenticator](https://lastpass.com/auth/)
  * [IIJ SmartKey](https://www.iij.ad.jp/smartkey/)

+++

### TOTP

* Time-based One-Time Password
  * ワンタイムパスワードの1種
  * 時間単位(だいたい30秒)でパスワードが払い出される
* [RFC 6238 - TOTP: Time-Based One-Time Password Algorithm](https://tools.ietf.org/html/rfc6238)	
* 参考: [ワンタイムパスワード](https://ja.wikipedia.org/wiki/%E3%83%AF%E3%83%B3%E3%82%BF%E3%82%A4%E3%83%A0%E3%83%91%E3%82%B9%E3%83%AF%E3%83%BC%E3%83%89)

+++

### pyotp: OTPのPython実装

* [pyauth/pyotp](https://github.com/pyauth/pyotp)

```python
totp = pyotp.TOTP('base32secret3232')
totp.now() # => '492039'

# OTP verified for current time
totp.verify('492039') # => True
time.sleep(30)
totp.verify('492039') # => False
```

+++

### ハードウェアキー

* (私は使ったことありません)
* [YubiKey](https://yubikey.yubion.com/)
* [Titanセキュリティキー](https://cloud.google.com/titan-security-key/?hl=ja)
* FIDO(Fast IDentity Online)という認証技術

  * 参考: [FIDO (認証技術) - Wikipedia](https://ja.wikipedia.org/wiki/FIDO_(%E8%AA%8D%E8%A8%BC%E6%8A%80%E8%A1%93%29)
  * 参考: [FIDO エコシステム | YubiOn](https://www.yubion.com/solution/fido/)

---

## Slackで2FAを設定

---

## まとめ

* 認証にどういう種類があるか
  * →パスワード管理、2FA
* 2要素認証がどういうものか知る
  * →2種類の要素で認証する
* それぞれのメリットデメリットを知る
  * →サービスごとに使い分けてもいいかもね
