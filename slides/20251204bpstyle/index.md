```{eval-rst}
:og:image: _images/20251204bpstyle.png
:og:image:alt: Pydanticで複雑なJSONを一発でValidation

.. |cover| image:: images/20251204bpstyle.png
```

# **Pydantic**で<br />複雑な**JSON**を<br />一発で**Validation** {nekochan}`doya`

Takanori Suzuki

BPStyle 179 / 2025 Nov 4

## 背景、モチベーション

* プロジェクトで**複雑なJSON**をValidationする必要があった
* いままでは**JSON Schema**を使っていた
* JSON Schemaの**メンテだるそう**
* **Pydantic**に載せ替えたらいい感じになった {nekochan}`yatta`

## システムの概要 {nekochan}`benkyou`

* MANAVIRIA：タブレット対応デジタル教材

<iframe width="560" height="315" src="https://www.youtube.com/embed/oioJJ_-oFEU?si=yUTdqQ5Br4paTPUy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### さまざまな解答**フォーム形式** {nekochan}`good`

* 記述、選択式、並べ替え等

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
* 並べ替え他

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

### JSON Schema実装のつらみ（私見） {nekochan}`pusupusu`

* Schemaが**長くて**見づらい
* 定義が**JSON**なので読みにくい
  * Pythonコード中に**長いdict**がある
* フォーム形式ごとにバリデーション切り替え
  * Pythonの`if`文とJSON Schemaの**混在**
  
### PythonだけでJSONを**いい感じ**にValidationできないかなー {nekochan}`think`

## **Pydantic**でValidation {nekochan}`mita`

### **Pydantic**

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

## Pydanticの**基本** {nekochan}`benkyou`

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

## **Pydantic**で複雑なJSONをValidation {nekochan}`work-moeru`

### 複数のモデルを**Unions**でまとめる {nekochan}`nakayoshi`

* フォーム形式（記述、選択式等）ごとにPydanticモデルは必要
* **Unions**を使用すると「いずれかにマッチ」ができる
* [Unions - Pydantic Validation](https://docs.pydantic.dev/latest/concepts/unions/)

```{revealjs-break}
```

```{literalinclude} code/unions_sample.py
:language: python
```

### 複数の**フォーム**をUnionsでまとめる {nekochan}`gattai`

```{revealjs-break}
```

```{mermaid}
---
title: モデルクラスの構成図
---
classDiagram
    BaseForm <|-- WrittenForm
    BaseForm <|-- ChoicesForm
    WrittenForm <-- AnswerForm
    ChoicesForm <-- AnswerForm
    class BaseForm["BaseForm(共通の要素を定義)"] {
        str: question
        str: answer_format
        object: display
        object: body
    }
    class WrittenForm["WrittenForm(記述式のフォーム)"] {
        WrittenDisplay: display
        WrittenBody: body
    }
    class ChoicesForm["ChoicesForm(選択式のフォーム)"] {
        ChoicesDisplay: display
        ChoicesBody: body
    }
    class AnswerForm["AnswerForm(複数フォームをまとめたモデル)"] {
        WritterForm_or_ChoicesForm: answer_form
    }
```

```{revealjs-break}
```

* フォームの**ベースクラス**を定義

```{literalinclude} code/unions_form.py
:language: python
:lines: 1-11
```

```{revealjs-break}
:notitle:
```

* **記述式**のフォームモデルを定義

```{literalinclude} code/unions_form.py
:language: python
:lines: 14-17,19-23,25-29
```

```{revealjs-break}
:notitle:
```

* **選択式**のフォームモデルを定義

```{literalinclude} code/unions_form.py
:language: python
:lines: 32-36,38-42,44-47,49-53
```

```{revealjs-break}
:notitle:
```

* **Unions**で複数のフォームを1つに**まとめる**

```{literalinclude} code/unions_form.py
:language: python
:lines: 25-30,49-54,56-58
```

```{revealjs-break}
:notitle:
```

* 記述式を**Validation**

```{literalinclude} code/unions_form.py
:language: python
:lines: 61-73,91-92
```

```{revealjs-break}
:notitle:
```

* 選択式を**Validation**

```{literalinclude} code/unions_form.py
:language: python
:lines: 74-90,95-96
```

```{revealjs-break}
:notitle:
```

* きちんとValidationできてるーーーー {nekochan}`big-love`

```{code-block} python
# 見やすさのために改行を入れてます
answer_form=WrittenForm(
    question='Pythonの作者は？',
    answer_format='written',
    display=WrittenDisplay(textInputFormat=1),
    body=WrittenBody(answers=['Guido van Rossum'], placeholder='作者名をアルファベットで書いてください'))
answer_form=ChoicesForm(
    question='Python 3.14の新機能はどれ？',
    answer_format='choices',
    display=ChoicesDisplay(choices_selector='button', choices_label='ABC'),
    body=ChoicesBody(answers=[
        ChoicesAnswer(answer='t-string', is_correct=True),
        ChoicesAnswer(answer='safe external debugger', is_correct=True),
        ChoicesAnswer(answer='lazy import', is_correct=False)
    ]))
```

### Pydanticで**一発でValidation**できそう！ {nekochan}`kitakitakitakita-kitakitsune`

## SchemaからPydantic**コード生成** {nekochan}`kitai`

### SchemaからPydantic**コード生成** {nekochan}`kitai`

* 実際のJSON Schemaはもっと**複雑**
* フォーム形式も**6パターン**
* Pydanticのコード書くのは大変そう

### datamodel-code-generator {nekochan}`kami`

* {fas}`globe` [`koxudaxi.github.io/datamodel-code-generator`](https://koxudaxi.github.io/datamodel-code-generator/)
* 各種データ定義からPythonの**コードを生成**
* 入力：OpenAPI、**JSON Schema**、YAML、GraphQL、Python辞書など
* 出力：**Pydantic**、dataclass、TypedDictなど

```{revealjs-break}
```

* 基本的な使い方
* 実際はフォーム形式ごとにJSONファイルを作成し、モデルコードを生成

```{code-block} bash
% pip install datamodel-code-generator
% datamodel-codegen --input scheama.json \
  --input-file-type jsonschema \
  --output-model-type pydantic_v2.BaseModel \
  --output model.py
```

### 生成コードで各フォームの<br />**Pydanticモデル**ができた！ {nekochan}`dai-kansha`

## さらにValidation**ルールを追加** {nekochan}`mada`

### さらにValidation**ルールを追加** {nekochan}`mada`

* データを意味的に解釈してチェックしたい
* 複数の項目の組み合わせでチェックしたい
* →**Constraints**追加、**Validator**の**作成**

### **任意の値**のみ選択可能にする

* Enumで定義した値のみ指定可 [^enums]

```{code-block} python
from enum import Enum

class TextInputFormat(Enum):
    """記述式のテキスト入力形式"""
    HALF_WIDTH = 1  # 幅50%
    FULL_WIDTH = 2  # 幅100%（1行）
	
class WrittenDisplay(BaseModel):
    """記述式の表示形式"""
    text_input_format: TextInputFormat
```

[^enums]: <https://docs.pydantic.dev/latest/api/standard_library_types/#enums>

### **数値の範囲**や**文字数**を指定

* `Field()`に数値の範囲[^integers]、文字数[^strings]などの条件を指定できる

```{code-block} python
class WrittenDisplay(BaseModel):
    # 数値の上限を指定
    max_length: PositiveInt = Field(..., le=100)
    # 文字数の範囲を指定
    question: str = Field(..., min_length=20, max_length=500)
```

 [^integers]: <https://docs.pydantic.dev/latest/api/standard_library_types/#integers>
 [^strings]: <https://docs.pydantic.dev/latest/api/standard_library_types/#strings>

### 選択肢の中に**正解があるか**

* `@model_validator`でValidatorを定義 [^validators]

[^validators]: <https://docs.pydantic.dev/latest/concepts/validators/>

```{code-block} python
class ChoicesAnswer(BaseModel):  # 選択式の1つの選択肢
    answer: str  # 選択肢
    is_correct: bool  # 正解フラグ

class ChoicesBody(BaseModel):  # 選択式
    answers: list[ChoicesAnswer]  # 複数の選択肢
	
    @model_validator(mode="after")
    def at_least_one_correct(self) -> Self:
        """answersに1つ以上のis_correct: Trueがあるか"""
        if not any(a.is_correct for a in self.answers):
            raise ValueError("正解の選択肢がありません")
        return self
```

### 他にもいろいろできるんで<br />詳しくは**ドキュメント**読んでね {nekochan}`megane`

{fas}`globe` [`docs.pydantic.dev`](https://docs.pydantic.dev/latest/)

## **複雑なデータ**をValidation<br />→**Pydantic**を検討しよう！ {nekochan}`kyapi`

## Thank You {nekochan}`pray`

{fas}`desktop` [slides.takanory.net](https://slides.takanory.net/)
{fas}`code` [20251204bpstyle/code](https://github.com/takanory/slides/tree/master/slides/20251204bpstyle/code)

{fab}`twitter` [takanory](https://twitter.com/takanory)
{fab}`github` [takanory](https://github.com/takanory/)
{fab}`linkedin` [takanory](https://www.linkedin.com/in/takanory/)
{fab}`untappd` [takanory](https://untappd.com/user/takanory/)

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)
