```{eval-rst}
:og:image: _images/20260221shizuoka.png
:og:image:alt: Pydanticで複雑なJSONを一発でValidation

.. |cover| image:: images/20260221shizuoka.png
```

# **Pydantic**で<br />複雑な**JSON**を<br />一発で**Validation**

```{image} images/pycon-mini-shizuoka-logo.png
:width: 50%
```

Takanori Suzuki

PyCon mini Shizuoka 2026 / 2026 Feb 21

## 今日話すこと {nekochan}`nesshou`

* **どんな課題**があったか {nekochan}`yabai`
* Pydanticの**基本** {nekochan}`benkyou`
* Pydanticで**複雑なJSON**を**Validation** {nekochan}`work-moeru`
* JSON SchemaからPydantic**コード生成** {nekochan}`kitai`
* さらなる**Validtionルール** {nekochan}`megane`

## Photos {nekochan}`camera` Tweets {nekochan}`niwatori` {nekochan}`come-on`

`#pyconshizu` / `@takanory`

### {fas}`globe` [`slides.takanory.net`](https://slides.takanory.net/)

![slides.takanory.net](images/slides-takanory-net.png)

## **Who** am I? / お前 **誰よ** 👤

* Takanori Suzuki / 鈴木 たかのり ({fab}`twitter` [@takanory](https://twitter.com/takanory))
* [BeProud](https://www.beproud.jp/) 取締役 / Python Climber
* [PyCon JP Association](https://www.pycon.jp/) 代表理事
* [Python Boot Camp](https://www.pycon.jp/support/bootcamp.html) 講師、[Python mini Hack-a-thon](https://pyhack.connpass.com/) 主催、[Pythonボルダリング部](https://kabepy.connpass.com/) 部長

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

### PyCon JP 2026**共同座長** [^chairs] 🪑🪑

* 日程：2026年8月21日（金）〜23日（日）
* 会場： 広島国際会議場
* 共同座長：佐野浩士、鈴木たかのり

```{image} images/pyconjp2026-chairs.png
:width: 60%
```

[^chairs]: [PyCon JP Blog: PyCon JP 2026 座長発表](https://pyconjp.blogspot.com/2025/10/pyconjp2026-co-chairs.html)

### 主催メンバー**募集中**！！ 🙌

* **イベント企画の具体化**を進めてくれる方募集
* PyCon JP 2026主催メンバー申込フォーム [^form]

![](images/pyconjp2026-form-qr.png)

[^form]: <https://forms.gle/of8NjqkPmUaF8HGR7>

### **BeProud** Inc. 🏢

* [BeProud](https://www.beproud.jp/): Pythonシステム開発、コンサル
* [connpass](https://connpass.com/): IT勉強会支援プラットフォーム
* [PyQ](https://pyq.jp/): Python独学プラットフォーム
* [TRACERY](https://tracery.jp/): システム開発ドキュメントサービス

![BeProud logos](/assets/images/beproud-logos.png)

### BeProud**メンバー募集中** {nekochan}`kamon`

```{image} /assets/images/qr-career.png
:width: 40%
:alt: Pythno求人のQRコード
:target: https://www.beproud.jp/careers/python/
```

```{image} /assets/images/qr-casual-interview.png
:width: 40%
:alt: カジュアル面談のQRコード
:target: https://forms.gle/tM4n2ufKf49MbXsH9
```

## **どんな課題**があったか {nekochan}`yabai`

### 学習教材のWebシステム

* [デジタル教材マナビリア](https://www.meijitosho.co.jp/gakusan/manaviria/)
* 小・中学校向け学習プラットフォーム
* 学習教材を使った勉強がWebでできる

### さまざまな解答**フォーム形式** {nekochan}`good`

* 記述、選択式、並べ替え等

![さまざまな解答形式](/20251204bpstyle/images/manaviria1.png)

### **編集者画面**で教材を作成 {nekochan}`work`

```{image} /20251204bpstyle/images/edit_quiz1.png
:width: 40%
```

```{image} /20251204bpstyle/images/edit_quiz2.png
:width: 40%
```

### フォーム形式ごとに異なる**設定項目** {nekochan}`guruguru`

* 記述式
  * 表紙形式：フォーム幅
  * 解答欄：正解、別解、プレースホルダー
* 選択式
  * 表示形式：ボタンorセレクトボックス、選択肢ラベル
  * 解答欄：選択肢リスト、正解リスト
* 並べ替え他

### **JSON**にしてDBに保存

```{code-block} json
{
    "question": "Python 3.14の新機能はどれ？"
    "answer_format": "choices",
    "display": {"choices_selector": "button", "choices_label": "ABC"}
    "body": {
        "answers": [
            {"answer": "t-string",
             "is_correct": true},
            {"answer": "safe external debugger",
             "is_correct": true},
            {"answer": "lazy import",
             "is_correct": false},
            {"answer": "アノテーションの遅延評価",
             "is_correct": true}
        ]
    }
}
```

### DB保存時にJSONを**Validation**

* 誤ったデータの混入を防ぐ {nekochan}`ng`
* **JSON Schema**でValidationしていた

### **JSON Schema**でValidation {nekochan}`yoshi`

* {fas}`globe` [`json-schema.org`](https://json-schema.org/)
* JSONデータの定義をJSONで書ける
* Pythonのライブラリ([jsonschema](https://python-jsonschema.readthedocs.io/en/stable/))あり

![JSON Schema logo](https://json-schema.org/img/logos/logo-blue.svg)

### JSON Schemaのサンプル [^json-schema-sample]

[^json-schema-sample]: [Creating your first schema](https://json-schema.org/learn/getting-started-step-by-step)

```{code-block} json
{"productId": 5, "productName": "MANAVIRIA"}
```

```{code-block} json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/product.schema.json",
  "title": "Product",
  "description": "A product from Acme's catalog",
  "type": "object",
  "properties": {
    "productId": {
      "description": "The unique identifier for a product",
      "type": "integer"
    },
    "productName": {
      "description": "Name of the product",
      "type": "string"
    }
  }
}
```

### マナビリア**CBT**が爆誕[^cbt] {nekochan}`chudoon`

* 今まではワークのみ
* CBT（テスト機能）が追加（2026年4月）

```{image} https://www.meijitosho.co.jp/db/info/20250801_2.png
:width: 30%
```

[^cbt]: [全問自動採点のCBTサービス開始](https://www.meijitosho.co.jp/info/?id=20250801) 

### 似てるけど**微妙に異なる**JSON仕様 {nekochan}`ase`

* 点数：CBTのみ
* ヒント：ワークのみ
* 解答形式：共通
* ソート順：共通
* などなど

### JSON Schemaで両方に対応する？ {nekochan}`yabai`

* 共通の所は共通の処理にしたい
* コピペで似たJSON Schema管理はやりたくない

### JSON Schema実装のつらみ（私見） {nekochan}`pusupusu`

* Schemaが**長くて**見づらい
* 定義が**JSON**なので読みにくい
  * Pythonコード中に**長いdict**がある
* フォーム形式ごとにバリデーション切り替え
  * Pythonの`if`文とJSON Schemaの**混在**
  
### **Pydantic**に書き換えよう！！ {nekochan}`sore`

## Pydanticの**基本** {nekochan}`benkyou`

### **Pydantic**とは

* {fas}`globe` [`docs.pydantic.dev`](https://docs.pydantic.dev/latest/)
* Python用のデータValidationライブラリ
* dataclass、TypedDictなどをValidation可能
* **型ヒント**を使ってルールを定義 {nekochan}`yoshi`

```{image} https://avatars.githubusercontent.com/u/110818415
:width: 25%
:alt: Pydantic logo
```

### PydanticでValidationの**結論**

* めっちゃ**いい感じ**にできた（自画自賛） {nekochan}`doya`

### Pydanticを**インストール** {nekochan}`kamon`

```{code-block} bash
$ pip install "pydantic"
$ pip install "pydantic[email]"  # email Validationする場合
```

### JSONをValidation[^examples]

```{literalinclude} code/person.json
:language: json
```

```{literalinclude} code/example_model.py
:language: python
```

[^examples]: [Validating File Data - Pydantic Validation](https://docs.pydantic.dev/latest/examples/files/)

### JSONをValidation

* 正しいJSONをValidation {nekochan}`yoshi`

```{literalinclude} code/example.py
:language: python
:lines: 1, 5-10
```

### JSONをValidation

* 正しくないJSONをValidation {nekochan}`ng`
  * `name`がない
  * `age`がマイナス
  * `email`がメールアドレスじゃない

```{literalinclude} code/person_wrong.json
```

### エラーがめちゃ親切 {nekochan}`dai-kansha`

```{literalinclude} code/example.py
:language: python
:lines: 3-4, 12-16
```

```{code-block} text
name
  Field required [type=missing, input_value={'age': -30, 'email': 'not-an-email-address'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing
age
  Input should be greater than 0 [type=greater_than, input_value=-30, input_type=int]
    For further information visit https://errors.pydantic.dev/2.12/v/greater_than
email
  value is not a valid email address: An email address must have an @-sign. [type=value_error, input_value='not-an-email-address', input_type=str]
```

```{revealjs-break}
```

```{revealjs-code-block} text
:data-line-numbers: 2,5,8

name
  Field required [type=missing, input_value={'age': -30, 'email': 'not-an-email-address'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing
age
  Input should be greater than 0 [type=greater_than, input_value=-30, input_type=int]
    For further information visit https://errors.pydantic.dev/2.12/v/greater_than
email
  value is not a valid email address: An email address must have an @-sign. [type=value_error, input_value='not-an-email-address', input_type=str]
```

* `name`は必須のフィールド
* `age`は0より大きい
* `email`の値がメールアドレス形式じゃない

## Pydanticで**複雑なJSON**を<br />**Validation** {nekochan}`work-moeru`
## JSON SchemaからPydantic**コード生成** {nekochan}`kitai`
## さらなる**Validtionルール** {nekochan}`megane`
