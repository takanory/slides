```{eval-rst}
:og:image: _images/20240921pycontw.png
:og:image:alt: How to learn Japanese with Python

.. |cover| image:: images/20240921pycontw.png
```

# How to learn **Japanese** w/ **Python**

Takanori Suzuki

![PyCon Taiwan logo](images/pycontw-logo.jpg)

PyCon Taiwan 2024 / 2024 Sep 21

## Agenda ✅

* Background and Motivation / Goal
* 日本語の難しさ
* fuga

## Background and Motivation 🏞️

### Background and Motivation

* 仕事で中学生向けの学習教材を言語的に処理する開発をしている
* →より学習しやすくするために
* その中で、Pythonライブラリが日本語学習の助けになるのではと考えた

### Background and Motivation(cont.)

* [FSI language difficulty](https://www.fsi-language-courses.org/blog/fsi-language-difficulty/)
* 日本語は英語話者にとってもっと学習が難しい言語("super-hard languages")
* 他はMandarin, Cantonese, Korean and Arabic

### Goal

* 日本語の難しさを理解
* 各種ライブラリの使い方を理解
* 日本語の勉強をサポートできるかも

## Photos 📷 Tweets 🐦 👍

`#pycontw` / `@takanory`

### Slides 💻

[slides.takanory.net](https://slides.takanory.net)

## Who am I? 👤

```{revealjs-break}
:notitle:
```

- Takanori Suzuki / 鈴木 たかのり ({fab}`twitter` [@takanory](https://twitter.com/takanory))
- [PyCon JP Association](https://www.pycon.jp/committee/english.html/): Chair
- [BeProud Inc.](https://www.beproud.jp/): Director / Python Climber
- [Python Boot Camp](https://www.pycon.jp/support/bootcamp.html), [Python mini Hack-a-thon](https://pyhack.connpass.com/), [Python Bouldering Club](https://kabepy.connpass.com/)
- Love: Ferrets, LEGO, 🍺 / Hobby: 🎺, 🧗‍♀️

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

```{revealjs-notes}
I'm Takanori Suzuki. My X(Twitter) is "takanory", please follow me.
I'm a Chairperson of PyCon JP Association.
Also, I'm a director of BeProud Inc and my title is "Python CLimber".
I'm also active in several Python related communities in Japan.
```

### PyCon **JP** 2024

* [`2024.pycon.jp`](https://2024.pycon.jp)
* Date: 2024 **Sep 27**(Fri)-**29**(Sun)
* Place: **Tokyo**, Japan
* **English talks** are available

```{image} images/pyconjp2024logo.png
:alt: PyCon JP 2024 logo
:width: 70%
```

## Questions 🙋‍♂️

### Have you **learned** Japanese? 🙋‍♀️

### Are you **interested** in Japanese? 🙋‍♂️

### Would you like to **visit** Japan? 🙋‍♀️ 🙋‍♂️

### PyCon **JP** 2024

* [`2024.pycon.jp`](https://2024.pycon.jp)
* Date: 2024 **Sep 27**(Fri)-**29**(Sun)
* Place: **Tokyo**, Japan
* **English talks** are available

```{image} images/pyconjp2024logo.png
:alt: PyCon JP 2024 logo
:width: 70%
```

## Japanese is **Difficult** 😫

(日本語の難しい点をいくつか紹介するよ)

* **3 Types** of Characters
* **No Spaces** between Words
* **Multiple Readings** of Kanji

### **3 Types** of Characters

English | Snake | Beer
-- | -- | --
Pronounciation | hebi | biːru
Hiragana | へび | びーる
Katakana | ヘビ | ビール
Kanji | 蛇 | 麦酒

### **No Spaces** between Words

<ruby>すもももももももものうち<rt> su mo mo mo mo mo mo mo mo no u chi </rt></ruby>

### **No Spaces** between Words

すもももももももものうち

↓

すもも/も/もも/も/もも/の/うち

"Plums and peaches are part of peaches"

### **Multiple Readings** of Kanji

* **日**: day, sun
* Taiwanese pronounciation: ri(?)

### **Multiple Readings** of Kanji

* **日**: day, sun
* Taiwanese pronounciation: ri(?)
* **Japanese**-style reading(訓読み)
  * にち(nichi)、ひ(hi)
* **Chinese**-style reading(音読み)
  * じつ(jitsu)、か(ka)

### **Multiple Readings** of Kanji

* **Japanese**-style reading: にち(nichi)、ひ(hi)
* **Chinese**-style reading: じつ(jitsu)、か(ka)
* How to read?
  * 日曜日 (Sunday)
  * 前日 (Previous day)

### <ruby>日<rt>**nichi**</rt></ruby><ruby>曜<rt>yo</rt></ruby><ruby>日<rt>**bi**</rt></ruby> (Sunday) / <ruby>前<rt>zen</rt></ruby><ruby>日<rt>**jitsu**</rt></ruby> (Previous day)

* **Japanese**-style reading: にち(nichi)、ひ(hi)
* **Chinese**-style reading: じつ(jitsu)、か(ka)

### Japanese is **Difficult**!! 😱

## {fab}`python` Python supports Japanese leaning

## **`<ruby>`** HTML Tag 💎
### **`<ruby>`** HTML Tag 💎

* `<ruby>` represents **small annotations**
* `<rt>` specifies the **ruby text** component

<ruby>PyCon<rt>Python Conference</rt></ruby>
<ruby>TW<rt>Taiwan</rt></ruby>
2024

```html
<ruby>PyCon<rt>Python Conference</rt></ruby>
<ruby>TW<rt>Taiwan</rt></ruby>
2024

```

* see: [`<ruby>`: The Ruby Annotation element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby)

### Indicate **pronunciation** with `<ruby>`

* **Alphabet** annotation: Pronounciation

<ruby>パイコン<rt>pa i ko n</rt></ruby>
<ruby>たいわん<rt>ta i wa n</rt></ruby>
(PyCon Taiwan)

```html
<ruby>パイコン<rt>pa i ko n</rt></ruby>
<ruby>たいわん<rt>ta i wa n</rt></ruby>
```

### Indicate **pronunciation** with `<ruby>`

* **Hiragana** annotation: Readings
* ふりがな: **Furigana**

<ruby>パイコン<rt>ぱいこん</rt></ruby>
<ruby>台湾<rt>たいわん</rt></ruby>
(PyCon Taiwan)

```html
<ruby>パイコン<rt>ぱいこん</rt></ruby>
<ruby>台湾<rt>たいわん</rt></ruby>
```

## **Hiragana** and **Katakana** (あ / ア)

hebi / へび / ヘビ

### **Hiragana** and **Katakana**

* Hiragana and Katakana are **phonogram**
* 1 character represent a phoneme(speech sound)
  * Like a Japanese **alphabet**
* Hiragana: <ruby>あかさたな<rt>a ka sa ta na</rt></ruby>...
* Katakana: <ruby>アカサタナ<rt>a ka sa ta na</rt></ruby>...

### **Hiragana** and **Katakana**

* Basically use Hiragana
  * <ruby>たいわん<rt>ta i wa n</rt></ruby>
* Katakana is used for foreign words
  * <ruby><ruby>パイコン<rt>pa i ko n</rt></ruby> (PyCon)

### **Romanization** of Japanese (Romaji)

* 日本語の読みを表すためにアルファベットで書く
* 地名の看板とかローマ字を使っている
* ローマ字に変換してひらがなを勉強しよう

![Ikebukuro station](images/ikebukuro.jpg)

### jaconv

* [jaconv](https://github.com/ikegami-yukino/jaconv): interconverter for Hiragana, Katakana, alphabet and etc.

```bash
$ python3.12 -m venv env
$ . env/bin/activate
(env) pip install jaconv
```

```pycon
>>> import jaconv
>>> jaconv.kana2alphabet("たいわん")  # Hiragana -> alphabet
'taiwan'
>>> jaconv.kata2alphabet("パイコン")  # Katakana -> alphabet
'paikon'
```

### Add **Romaji** annotation

* kana2roman.py

```{revealjs-literalinclude} code/kana2roman.py
```

### Add **Romaji** annotation

```bash
$ python kana2roman.py パイコンたいわん
<ruby>パイコンたいわん<rt>paikontaiwan</rt></ruby>
```

<ruby>パイコンたいわん<rt>paikontaiwan</rt></ruby>

### Can read Hiragana and Katakana 🎉

## **No Spaces** between Words

<ruby>すもももももももものうち<rt> su mo mo mo mo mo mo mo mo no u chi </rt></ruby>

### **No Spaces** between Words

* 日本語は単語がスペースで分割されていない
* 辞書ベースで単語を分割する
* 日本語の形態素解析ライブラリが必要

### Japanese **morphological analyzer**

* SudachiPy: [pypi.org/project/SudachiPy](https://pypi.org/project/SudachiPy/)
* SudachiDcit: [pypi.org/project/SudachiDict-core](https://pypi.org/project/SudachiDict-core/)

```bash
$ pip install sudachipy sudachidict_core
```

### SudachiPy

* Rust製で速い
* 辞書が複数ある(small, core, full)
  * ここではcoreを使用

### **Word Segmentation**

* 辞書データを元に単語に分割するよ

```pycon
>>> from sudachipy import Dictionary
>>> tokenizer = Dictionary().create()
>>> text = "すもももももももものうち"
>>> for token in tokenizer.tokenize(text):
...     print(token)
... 
すもも
も
もも
も
もも
の
うち
```

### **Word Segmentation** with Romaji

* word_segmentation.py

```{revealjs-literalinclude} code/word_segmentation.py
```

### **Word Segmentation** with Romaji

```bash
$ python word_segmentation.py すもももももももものうち
<ruby>すもも<rt>sumomo</rt></ruby> / <ruby>も<rt>mo</rt></ruby> / <ruby>もも<rt>momo</rt></ruby> / <ruby>も<rt>mo</rt></ruby> / <ruby>もも<rt>momo</rt></ruby> / <ruby>の<rt>no</rt></ruby> / <ruby>うち<rt>uchi</rt></ruby>
```

<ruby>すもも<rt>sumomo</rt></ruby> / <ruby>も<rt>mo</rt></ruby> / <ruby>もも<rt>momo</rt></ruby> / <ruby>も<rt>mo</rt></ruby> / <ruby>もも<rt>momo</rt></ruby> / <ruby>の<rt>no</rt></ruby> / <ruby>うち<rt>uchi</rt></ruby>


## **Multiple Readings** of Kanji

<ruby>日曜日<rt>nichi you bi</rt></ruby>、<ruby>前日<rt>zen jitsu</rt></ruby>
