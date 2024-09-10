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

<ruby>すもも<rt>su mo mo</rt></ruby>,
<ruby><ruby>パイソン<rt>pa i so n</rt></ruby>

```html
<ruby>すもも<rt>su mo mo</rt></ruby>,
<ruby><ruby>パイソン<rt>pa i so n</rt></ruby>,
```

### Indicate **pronunciation** with `<ruby>`

* **Hiragana** annotation: Readings
* ふりがな: Furigana

<ruby><ruby>パイソン<rt>ぱいそん</rt></ruby>
<ruby>
  <ruby>日曜日<rt>にちようび</rt></ruby>
  <rt>ni chi yo u bi</rt>
</ruby>

```html
<ruby><ruby>パイソン<rt>ぱいそん</rt></ruby>,
<ruby>
  <ruby>日曜日<rt>にちようび</rt></ruby>
  <rt>ni chi yo u bi</rt>
</ruby>
```

## **Hiragana** and **Katakana** (あ / ア)

### **Hiragana** and **Katakana**

* Hiragana and Katakana are **phonogram**
* 1 character represent a phoneme(speech sound)
  * Like a Japanese **alphabet**
* Hiragana: <ruby>あかさたな<rt>a ka sa ta na</rt></ruby>...
* Katakana: <ruby>アカサタナ<rt>a ka sa ta na</rt></ruby>...

### **Hiragana** and **Katakana**

* Basically use Hiragana
  * <ruby>にちようび<rt>ni chi yo u bi</rt></ruby>
* Katakana is used for foreign words
  * <ruby><ruby>パイソン<rt>pa i so n</rt></ruby> (Python)

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

```python
>>> import jaconv
>>> jaconv.kana2alphabet("にちようび")  # Hiragana
'nichiyoubi'
>>> jaconv.kata2alphabet("パイソン")  # Katakana
'paison'
```
