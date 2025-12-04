```{eval-rst}
:og:image: _images/20251204bpstyle.png
:og:image:alt: Pydanticで複雑なJSONを一発でValidation

.. |cover| image:: images/20251204bpstyle.png
```

# **Pydantic**で<br />複雑な**JSON**を<br />一発で**Validation** {nekochan}`doya`

Takanori Suzuki

BPStyle 179 / 2025 Nov 4

## はじめに

* プロジェクトで複雑なJSONをバリデーションする必要があった
* いままではJSON Schemaを使っていた
* JSON Schemaのメンテだるそう
* Pydanticに載せ替えたらいい感じになった {nekochan}`yatta`

## システムの概要 {nekochan}`benkyou`

* MANAVIRIA：タブレット対応デジタル教材

<iframe width="560" height="315" src="https://www.youtube.com/embed/oioJJ_-oFEU?si=yUTdqQ5Br4paTPUy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### さまざまな解答**フォーム形式** {nekochan}`good`

* 記述、選択、並べ替え等

![さまざまな解答形式](images/manaviria1.png)

### **編集者画面**で教材を作成 {nekochan}`work`

```{image} images/edit_quiz1.png
:width: 40%
```

```{image} images/edit_quiz2.png
:width: 40%
```

### フォーム形式ごとに異なる**設定項目** {nekochan}`guruguru`

* 記述式
  * 表紙形式：フォーム幅
  * 解答欄：正解、別解、プレースホルダー
* 選択式
  * 表示形式：ボタンorセレクトボックス、選択肢ラベル
  * 解答欄：選択肢リスト、正解リスト
* 並べ替え...

### **JSON**にしてDBに保存

```{code-block} json
{
    "question": "Python 3.14の新機能はどれ？"
    "answer_format": "choices",
    "display": {"choices_selector": "button",
                "choices_label": "ABC"}
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

### 保存時にJSONを**Validation**

* 誤ったデータの混入を防ぐ {nekochan}`ng`

## **JSON Schema**でValidation {nekochan}`miru`

### JSON Schema

* [`json-schema.org`](https://json-schema.org/)
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

### JSON Schema実装のつらみ（私見） {nekochan}`pusupusu`

* Schemaが**長くて**見づらい
* 定義が**JSON**なので読みにくい
  * Pythonコード中に**長いdict**がある
* フォーム形式ごとにバリデーション切り替え
  * Pythonの`if`文とJSON Schemaの**混在**
  
### PythonだけでJSONを**いい感じ**にValidationできないかなー {nekochan}`think`

## **Pydantic**でValidation {nekochan}`mita`

### Pydantic

* [`docs.pydantic.dev`](https://docs.pydantic.dev/latest/)
* Python用のデータValidationライブラリ
* dataclass、TypedDictなどをValidation可能
* **型ヒント**を使ってルールを定義 {nekochan}`yoshi`

```{image} https://avatars.githubusercontent.com/u/110818415
:width: 25%
:alt: Pydantic logo
```

### PydanticでValidationの結論

* めっちゃ**いい感じ**にできた（自画自賛） {nekochan}`doya`

## Pydanticの基本

```{code-block} bash
$ pip install "pydantic"
$ pip install "pydantic[email]"  # email Validationする場合
```

### JSON dataをvalidation[^examples]

```{literalinclude} code/person.json
:language: json
```

```{literalinclude} code/example_model.py
:language: python
```

[^examples]: [Validating File Data - Pydantic Validation](https://docs.pydantic.dev/latest/examples/files/)

### JSON dataをvalidation（続き）

* 正しいJSONをValidation {nekochan}`yoshi`

```{literalinclude} code/example.py
:language: python
:lines: 1, 5-10
```

###  正しくないJSONをValidation

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
