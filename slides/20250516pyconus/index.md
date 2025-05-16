```{eval-rst}
:og:image: _images/20250516pyconus.png
:og:image:alt: How to learn Japanese with Python

.. |cover| image:: images/20250516pyconus.png
```

# How to learn **Japanese** w/ **Python**

Takanori Suzuki

```{image} images/pyconus2025-logo.svg
:alt: PyCon US 2025 logo
:width: 50%
```

PyCon US 2025 / 2025 May 16

## Agenda ✅

* Background and Motivation / Goal
* Japanese is Difficult
* Python supports Japanese leaning

```{revealjs-notes}
* The agenda for this talk is as follows.
* I will talk about Background, Motivation and goal of this talk.
* Next, I will introduce some of the difficulties of the Japanese language.
* In the last part, I will explain how Python supports Japanese language learning, with example codes.
```

### PyCon US 2024

* **Lightning Talk** on the same idea
* I will talk in **more detail**

<iframe width="560" height="315" src="https://www.youtube.com/embed/p_Vx3gDHeUI?si=H6ZHmYQfvvWOn-U4&amp;controls=0&amp;start=530" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

```{revealjs-notes}
I gave a lightning talk on the same idea at PyCon US 2024.
Does anyone remember it?
Today I will talk in more detail.
```

## Background and Motivation 🏞️

```{revealjs-notes}
* Background and Motivation of this talk...
```

### Background and Motivation

* Developing School **Textbook Web** at work
  * Japanese NLP to make it **Easier to Learn**
* NLP libs could help people **Learn Japanese**

```{revealjs-notes}
* Background and Motivation of this talk...
* My team is developing web-based Textbook for junior high school students at work.
* I am using Japanese NLP to make the textbook easier to learn.
* Based on this experience, I thought Python's NPL libraries could help people learn Japanese.
```

### Background and Motivation(cont.)

* [FSI language difficulty](https://www.fsi-language-courses.org/blog/fsi-language-difficulty/)
  * Japanese is "**super-hard languages**" for English speakers to learn
  * Catevory V* (More than 88 weeks)
  
```{revealjs-notes}
* "FSI language difficulty" reports Japanese is ...
```

```{revealjs-break}
:notitle:
```
  
<blockquote class="reddit-embed-bq" style="height:500px" data-embed-height="740"><a href="https://www.reddit.com/r/MapPorn/comments/1f97r63/language_difficulty_rankings_for_native_english/">Language difficulty rankings (for native English speakers)</a><br> by<a href="https://www.reddit.com/user/Homesanto/">u/Homesanto</a> in<a href="https://www.reddit.com/r/MapPorn/">MapPorn</a></blockquote><script async="" src="https://embed.reddit.com/widgets.js" charset="UTF-8"></script>
  

### Goal

* What is **difficult** about Japanese
* How to use **Japanese NLP** libs and APIs
* How Python can support **Japanese learning**

```{revealjs-notes}
* The goals of this talk are
* You know what is difficult about the Japanese language,
* You know how to use the Japanese NLP libraries and APIs and
* You understand how Python can support Japanese language 
```

## Photos 📷 Share 🐦 👍

`#PyConUS` / `@takanory`

```{revealjs-notes}
I would be happy to take pictures and share them on SNS.
Hashtag is #pyconus
```

### [`slides.takanory.net`](https://slides.takanory.net) 💻

```{image} images/slides-takanory-net.png
:alt: slides.takanory.net
:width: 85%
```

```{revealjs-notes}
This slide has been published.
Please visit slides.takanory.net or via QR code and click on the "Slides" link!
```

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
I'm a Chair of PyCon JP Association.
And I'm a director of BeProud Inc and my title is "Python CLimber".
I'm also active in several Python related communities in Japan.
```

### PyCon JP Association

{fas}`globe` [`www.pycon.jp`](https://www.pycon.jp/committee/english.html)

**Nonprofit** organization for **Python users** in Japan, to **promote Python** and supports its development. Further it is **our goal** to hold an annual **PyCon JP**.

```{revealjs-notes}
PyCon JP Association is a nonprofit...
We hold PyCon JP every year.
Do you know PyCon JP?
```

![PyCon JP Association](/assets/images/pyconjp_logo.png)

### PyCon JP **2025**

* {fas}`globe` [`2025.pycon.jp`](https://2025.pycon.jp/)
* Date: 2025 **Sep 26**(Fri)-**27**(Sat)
* Place: **Hiroshima**, Japan
* There are **English talks**

```{image} images/pyconjp2025-in-hiroshima.jpg
:alt: PyCon JP 2025 in Hiroshima
:width: 60%
```

```{revealjs-notes}
PyCon JP 2025 will be held in Hiroshima at the end of September.
This is the first PyCon JP to be held outside of Tokyo.
Do you know Hiroshima?...
```

### Hiroshima? ⛩️

* Fukuoka - **Hiroshima** - Kyoto - Tokyo - Hokkaido
* [Direct flights to Hiroshima - HIJ, Japan](https://www.directflights.com/to/HIJ)
  * Seoul, Taipei, Shanghai, Hong Kong, Dalian, Hanoi

```{image} https://maps.directflights.com/directflights/800/HIJ.jpg
:alt: Direct flights to Hiroshima
:width: 40%
```

```{revealjs-notes}
Do you know Hiroshima?...
Hiroshima is west of Tokyo and Kyoto.
Hiroshima has several direct flights from overseas, but sorry, no direct flights from US.
```

## Questions {nekochan}`hai`

### Have you **learned** Japanese? {nekochan}`study`

### Are you **interested** in Japanese? {nekochan}`miru`

### Would you like to **visit** Japan? {nekochan}`travel`

```{revealjs-notes}
Almost everyone.
There is a very good opportunity for you...
```

### PyCon JP **2025**

* 2025 **Sep 26**(Fri)-**27**(Sat)
* {nekochan}`yoshi;;;flip-horizontal` **Hiroshima**, Japan

```{image} images/pyconjp2025-in-hiroshima.jpg
:alt: PyCon JP 2025 in Hiroshima
:width: 80%
```

```{revealjs-notes}
PyCon JP 2025 will be held in Hiroshima in September.
See you again at PyCon JP 2025.
```

## Japanese is **Difficult** {nekochan}`yabai`

* **3 Types** of Characters
* **No Spaces** between Words
* **Multiple Readings** of Kanji

```{revealjs-notes}
Back to the main topic.
I will show you 3 difficult points of the Japanese language.
```

### **3 Types** of Characters

English | Peach(🍑) | Snake(🐍)
-- | -- | --
Pronounciation | momo | hebi
Hiragana | もも | へび
Katakana | モモ | ヘビ
Kanji | 桃 | 蛇

```{revealjs-notes}
Japanese language has 3 types of characters: hiragana, katakana, and kanji.
This table shows 3 different characters for each peach and snake.
```

### **No Spaces** between Words

<ruby>すもももももももものうち<rt> su mo mo mo mo mo mo mo mo no u chi </rt></ruby>

```{revealjs-break}
```

すもももももももものうち

↓

すもも/も/もも/も/もも/の/うち

"Plums and peaches are part of peaches"

```{revealjs-notes}
This sentence "すもももももももものうち" is a play on words, but it is correct Japanese.
Most Japanese can correctly break this sentence into words.
```

### **Multiple Readings** of Kanji

* **人**: person, people

```{revealjs-notes}
For example, this kanji character means peason and people.
```

```{revealjs-break}
```

* 2 **styles of readings**
* **Japanese**-style reading(<ruby>訓読み<rt>kun yomi</rt></ruby>)
* **Chinese**-style reading(<ruby>音読み<rt>on yomi</rt></ruby>)

```{revealjs-notes}
Many kanji caracter have 2 styles of readings.
```
  
```{revealjs-break}
```

* **人**: person, people
* **Japanese**-style reading: ひと(hito)、びと(bito)
* **Chinese**-style reading: じん(jin)、にん(nin)

```{revealjs-notes}
The kanji caracter has a total of four different readings.
```

```{revealjs-break}
```

* Japanese-style reading: ひと(hito)、びと(bito)
* Chinese-style reading: じん(jin)、にん(nin)
* Can you read?
  * 小人 (Small person)
  * 日本人 (Japanese)

```{revealjs-notes}
What do you think these idioms read?
```

```{revealjs-break}
```

* <ruby>小<rt>ko</rt></ruby><ruby>人<rt>**bito**</rt></ruby> (Samll person)
  * Japanese-style reading: ひと(hito)、びと(bito)
* <ruby>日<rt>ni</rt></ruby><ruby>本<rt>hon</rt></ruby><ruby>人<rt>**jin**</rt></ruby> (Japanese)
  * Chinese-style reading: じん(jin)、にん(nin)
  
```{revealjs-notes}
The 1st one is Japanese-style reading, "Kobito".
The 2nd one is Chinese-style reading, "Nihonjin".
```
  

### Japanese is **Difficult**!! {nekochan}`scream`

* **3 Types** of Characters
* **No Spaces** between Words
* **Multiple Readings** of Kanji

```{revealjs-notes}
Japanese is Difficult!! But...
```

## {fab}`python` **Python** supports **Japanese** leaning

```{revealjs-notes}
We have Python!!
```

## **`<ruby>`** HTML Tag 💎

```{revealjs-notes}
I will explain the ruby tag before I talk about Python
```

### What is **Ruby** ?

* <ruby>ルビ<rt>ruby</rt></ruby> characters are **small annotation** [^ruby]
* Usually placed **above** the text
* (Not a Programming Language)

[^ruby]: [Ruby character - Wikipedia](https://en.wikipedia.org/wiki/Ruby_character)

### **`<ruby>`** HTML Tag 💎

* `<ruby>` represents **small annotations** [^ruby-tag]
* `<rt>` specifies the **ruby text** component

<ruby>PyCon<rt>Python Conference</rt></ruby>
<ruby>US<rt>United States</rt></ruby>
2025

```html
<ruby>PyCon<rt>Python Conference</rt></ruby>
<ruby>US<rt>United States</rt></ruby>
2025
```

[^ruby-tag]: [`<ruby>`: The Ruby Annotation element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby)

```{revealjs-notes}
If I write a ruby tag like this, it will be displayed like this in a web browser
```

### Indicate **pronunciation** with `<ruby>`

* **Alphabet** annotation: Pronunciation

<ruby>パイコン<rt>pa i ko n</rt></ruby>
<ruby>あめりか<rt>a me ri ka</rt></ruby>
(PyCon America)

```html
<ruby>パイコン<rt>pa i ko n</rt></ruby>
<ruby>あめりか<rt>a me ri ka</rt></ruby>
```

```{revealjs-notes}
This slide uses the ruby tag to indicate pronunciation with alphabets.
```

```{revealjs-break}
```

* **Hiragana** annotation: Readings
* <ruby>ふりがな<rt>fu ri ga na</rt></ruby>

<ruby>アメリカ<rt>あめりか</rt></ruby>
<ruby>合衆国<rt>がっしゅうこく</rt></ruby>
(The United States of America)

```html
<ruby>アメリカ<rt>あめりか</rt></ruby>
<ruby>合衆国<rt>がっしゅうこく</rt></ruby>
```

```{revealjs-notes}
The ruby tag is also used for Furigana, the reading of other characters in hiragana.
```

### Figured out **`<ruby>`** Tag {nekochan}`naruhodo`

```{revealjs-notes}
Now we have figured out the the ruby tag, let's move on to Python.
```

## **Hiragana** and **Katakana** (あ / ア)

Snake(🐍) / hebi / へび / ヘビ

### **Hiragana** and **Katakana**

* Hiragana and Katakana are **phonogram**
* 1 character represent a phoneme(speech sound)
  * Like a Japanese **alphabet**
* Hiragana: <ruby>あかさたな<rt> a ka sa ta na</rt></ruby>...
* Katakana: <ruby>アカサタナ<rt> a ka sa ta na</rt></ruby>...

```{revealjs-break}
```

* Basically use Hiragana
  * <ruby>あめりか<rt> a me ri ka</rt></ruby> (America)
* Katakana is used for foreign words
  * <ruby><ruby>パイコン<rt>pa i ko n </rt></ruby> (PyCon)

### **Romanization** of Japanese (Romaji)

* **Alphabet** to represent Japanese
* **Romaji** is often used on **Information Sign**

![Ikebukuro station](images/ikebukuro.jpg)

* Learn **Hiragana**/**Katakana** using Romaji

### jaconv

* [jaconv](https://github.com/ikegami-yukino/jaconv): interconverter for Hiragana, Katakana, alphabet and etc.

```bash
$ python3.12 -m venv env
$ . env/bin/activate
(env) pip install jaconv
```

```pycon
>>> import jaconv
>>> jaconv.kana2alphabet("あめりか")  # Hiragana -> alphabet
'amerika'
>>> jaconv.kata2alphabet("パイコン")  # Katakana -> alphabet
'paikon'
```

### Add **Romaji** annotation

kana2roman.py

```{revealjs-literalinclude} code/kana2roman.py
:data-line-numbers: 2,4-7|9-12
```

```{revealjs-break}
```

```bash
(env) $ python kana2roman.py "パイコン あめりか"
<ruby>パイコン あめりか<rt>paikon amerika</rt></ruby>
```

<ruby>パイコン あめりか<rt>paikon amerika</rt></ruby>

### Can read **Hiragana** and **Katakana** {nekochan}`good`

## **No Spaces** between Words

<ruby>すもももももももものうち<rt> su mo mo mo mo mo mo mo mo no u chi </rt></ruby>

```{revealjs-break}
```

* Japanese has **no spaces** between words
* Use **Dictionary** to **Recognise** words
* Japanese **Morphological Analyzer** library required

### Japanese **Morphological Analyzer**

* see: {fab}`github` [taishi-i/awesome-japanese-nlp-resources](https://github.com/taishi-i/awesome-japanese-nlp-resources?tab=readme-ov-file#morphology-analysis)

```{image} images/japanese-nlp.png
:alt: Japanese Morphological Analyzers
:width: 60%
```

```{revealjs-notes}
There are many morphological analyzer libraries for Japanese.
```

### Japanese **Morphological Analyzer**

* SudachiPy: [pypi.org/project/SudachiPy](https://pypi.org/project/SudachiPy/)
* SudachiDcit: [pypi.org/project/SudachiDict-core](https://pypi.org/project/SudachiDict-core/)

```bash
(env) $ pip install sudachipy sudachidict_core
```

```{revealjs-notes}
In this case, I use SudachiPy and SudachiDict
```

### SudachiPy

* Made with **Rust**, Very **Fast**
* **Three Types** of Dictionaries
  * Small: small vocabulary
  * **Core**: basic vocabulary (**default**)
  * Full: miscellaneous proper nouns

```{revealjs-notes}
SudachiPy is made by Rust and is very fast.
SudachiDict has three types of different dictionaries with different numbers of vocabularies.
Here I use core dictionary, the default.
```

### **Word Segmentation**

* **Split** the words using **Dictionary**

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

### **Word Segmentation**

word_segmentation.py

```{revealjs-literalinclude} code/word_segmentation.py
:data-line-numbers: 2,4|6-11
```

```{revealjs-break}
```

```bash
(env) $ python word_segmentation.py すもももももももものうち
すもも / も / もも / も / もも / の / うち
```

すもも / も / もも / も / もも / の / うち

* **Cannot read** Hiragana?

### **Word Segmentation** with Romaji

word_segmentation_with_ruby.py

```{revealjs-literalinclude} code/word_segmentation_with_ruby.py
:data-line-numbers: 3,10
```

```{revealjs-break}
```

```bash
(env) $ python word_segmentation_with_ruby.py すもももももももものうち
<ruby>すもも<rt>sumomo</rt></ruby> / <ruby>も<rt>mo</rt></ruby> / <ruby>もも<rt>momo</rt></ruby> / <ruby>も<rt>mo</rt></ruby> / <ruby>もも<rt>momo</rt></ruby> / <ruby>の<rt>no</rt></ruby> / <ruby>うち<rt>uchi</rt></ruby>
```

<ruby>すもも<rt>sumomo</rt></ruby> / <ruby>も<rt>mo</rt></ruby> / <ruby>もも<rt>momo</rt></ruby> / <ruby>も<rt>mo</rt></ruby> / <ruby>もも<rt>momo</rt></ruby> / <ruby>の<rt>no</rt></ruby> / <ruby>うち<rt>uchi</rt></ruby>

### Can **split** into **Words** {nekochan}`clap`

```{revealjs-notes}
You can correctly split Japanese text into words!
```

## **Multiple Readings** of Kanji

<ruby>小<rt>ko</rt></ruby><ruby>人<rt>bito</rt></ruby> (Small person)

<ruby>日<rt>ni</rt></ruby><ruby>本<rt>hon</rt></ruby><ruby>人<rt>jin</rt></ruby> (Japanese)

### **Multiple Readings** of Kanji

* **人**: person, people
* 🇯🇵 **Japanese**-style reading(<ruby>訓読み<rt>kun yomi</rt></ruby>):
  * <ruby>ひと<rt>hi to</rt></ruby>、<ruby>びと<rt>bi to</rt></ruby>
* 🇨🇳 **Chinese**-style reading(<ruby>音読み<rt>on yomi</rt></ruby>):
  * <ruby>じん<rt>ji n</rt></ruby>、<ruby>にん<rt>ni n</rt></ruby>

```{revealjs-break}
```

* 小**人** (Small person): 
  🇯🇵 <ruby>こ<rt>ko</rt> <ruby>**びと**<rt>bi to</rt>
* 日本**人** (Japanese):
  🇨🇳 <ruby>に<rt>ni</rt> <ruby>ほん<rt>ho n</rt> <ruby>**じん**<rt>jin</rt>
  
### {nekochan}`pokan`

```{revealjs-notes}
It's difficult, but not only this.
```

### Multiple Readings of **Kanji idioms**

* Same combination but **different readings**
* **一人**: One person
  * **一人** (One person)
  * **一人**前 (One serving)

```{revealjs-break}
```

* Same combination but **different readings**
* **一人**: One person
  * **一人** (One person): <ruby>**ひとり**<rt>hi to ri</rt></ruby> 🇯🇵
  * **一人**前 (One serving): <ruby>**いちにん**<rt>i chi ni n</rt></ruby> <ruby>まえ<rt>ma e</rt></ruby> 🇨🇳

### {nekochan}`yabai;1.5em` {nekochan}`yabai;1.5em`

```{revealjs-notes}
Terrible...
And there is more...
```

### **Special readings** of Kanji idioms

* 一 **人** (One person): <ruby>**ひとり**<rt>hi to ri</rt></ruby> 🇯🇵
* 二 **人** (Two people)
* 三 **人** (Three people)

```{revealjs-break}
```

* 一 **人** (One person): <ruby>**ひとり**<rt>hi to ri</rt></ruby> 🇯🇵
* 二 **人** (Two people): <ruby>**ふたり**<rt>fu ta ri</rt></ruby> 🇯🇵
* 三 **人** (Three people): <ruby>**さんにん**<rt>sa n ni n</rt></ruby> 🇨🇳

```{revealjs-notes}
These are special readings of Kanji idioms.
```

```{revealjs-break}
```

* Other special readings
* 大人: <ruby>**おとな**<rt>o to na</rt></ruby> (Adult)
* 玄人: <ruby>**くろうと**<rt>ku ro u to </rt></ruby> (Professional)
* 防人: <ruby>**さきもり**<rt>sa ki mo ri</rt></ruby> (soldiers garrisoned at strategic posts in Kyushu in ancient times)

### {nekochan}`scream;2em` {nekochan}`scream;2em` {nekochan}`scream;2em`

```{revealjs-notes}
Oh my gosh
```

## Get **Reading** of Kanji

<ruby>一**人**<rt>one person</rt>の<ruby>日本**人**<rt>Japanese</rt></ruby>の<ruby>大**人**<rt>adult</rt></ruby>が<ruby>一**人**前<rt>one serving</rt></ruby>の<ruby>ラーメン<rt>🍜</rt></ruby>を<ruby>食べる<rt>eat</rt></ruby>

One Japanese adult eats one serving of ramen

```{revealjs-notes}
There are 4 same kanji character, all with different readings.
```

### Get **Reading** of Kanji

* Use **SudachiPy** and **SudachiDict** again
* `reading_form()`: Reading in Katakana

```pycon
>>> from sudachipy import Dictionary
>>> tokenizer = Dictionary().create()  # Make tokenizer
>>> text = "一人の日本人の大人が一人前のラーメンを食べる"
>>> for token in tokenizer.tokenize(text):  # Word segmentation
...     (str(token), token.reading_form())  # Get reading
... 
('一人', 'ヒトリ')
('の', 'ノ')
('日本人', 'ニホンジン')
('の', 'ノ')
('大人', 'オトナ')
...
```

```{revealjs-break}
```

* Looks good {nekochan}`good`
* Cannot read **Katakana**?

```pycon
('一人', 'ヒトリ')
('の', 'ノ')
('日本人', 'ニホンジン')
('の', 'ノ')
('大人', 'オトナ')
...
```

```{revealjs-break}
```

* Cannot read **Katakana**? Use **jaconv**!

```
>>> from jaconv import kata2hira, kata2alphabet
>>> for token in tokenizer.tokenize(text):
...     reading = token.reading_form()
...     hiragana = kata2hira(reading)  # to Hiragana
...     romaji = kata2alphabet(reading)  # to Alphabet(romaji)
...     (str(token), reading, hiragana, romaji)
... 
('一人', 'ヒトリ', 'ひとり', 'hitori')
('の', 'ノ', 'の', 'no')
('日本人', 'ニホンジン', 'にほんじん', 'nihonjin')
('の', 'ノ', 'の', 'no')
('大人', 'オトナ', 'おとな', 'otona')
...
```

### Can get **Reading** to **Kanji** {nekochan}`yatta`

### **Add Reading** to Kanji

kanji_reading.py

```{revealjs-literalinclude} code/kanji_reading.py
:data-line-numbers: 3,5|7-13
```

```{revealjs-break}
```

<ruby>一人<rt>ひとり</rt></ruby>
<ruby>の<rt>の</rt></ruby>
<ruby>日本人<rt>にほんじん</rt></ruby>
<ruby>の<rt>の</rt></ruby>
<ruby>大人<rt>おとな</rt></ruby>
<ruby>が<rt>が</rt></ruby>
<ruby>一人前<rt>いちにんまえ</rt></ruby>
<ruby>の<rt>の</rt></ruby>
<ruby>ラーメン<rt>らーめん</rt></ruby>
<ruby>を<rt>を</rt></ruby>
<ruby>食べる<rt>たべる</rt></ruby>

```bash
(env) $ python kanji_reading.py 一人の日本人の大人が一人前のラーメンを食べる
<ruby>一人<rt>ひとり</rt></ruby>
<ruby>の<rt>の</rt></ruby>
<ruby>日本人<rt>にほんじん</rt></ruby>
<ruby>の<rt>の</rt></ruby>
<ruby>大人<rt>おとな</rt></ruby>
...
```

```{revealjs-break}
```

kanji_reading_romaji.py

```{revealjs-literalinclude} code/kanji_reading_romaji.py
:data-line-numbers: 11,12
```

```{revealjs-break}
```

<ruby>一人<rt>hitori</rt></ruby>
<ruby>の<rt>no</rt></ruby>
<ruby>日本人<rt>nihonjin</rt></ruby>
<ruby>の<rt>no</rt></ruby>
<ruby>大人<rt>otona</rt></ruby>
<ruby>が<rt>ga</rt></ruby>
<ruby>一人前<rt>ichininmae</rt></ruby>
<ruby>の<rt>no</rt></ruby>
<ruby>ラーメン<rt>raーmen</rt></ruby>
<ruby>を<rt>wo</rt></ruby>
<ruby>食べる<rt>taberu</rt></ruby>

```bash
(env) $ python kanji_reading_romaji.py 一人の日本人の大人が一人前のラーメンを食べる
<ruby>一人<rt>hitori</rt></ruby>
<ruby>の<rt>no</rt></ruby>
<ruby>日本人<rt>nihonjin</rt></ruby>
<ruby>の<rt>no</rt></ruby>
<ruby>大人<rt>otona</rt></ruby>
```

### Can read **Kanji** {nekochan}`medetai`
 
## Kanji **level** support {nekochan}`tunda`

### Kanji **level** support {nekochan}`tunda`

 * If you study Japanese, you may know the **JLPT** [^jlpt]
* JLPT has **N1**(difficult) ~ **N5**(easy) levels [^jlpt-level]

```{image} https://www.jlpt.jp/e/resource/img_common/logo.gif
:alt: JLPT logo
:target: https://www.jlpt.jp/e/index.html
```

[^jlpt]: [What is the Japanese-Language Proficiency Test? Index | JLPT Japanese-Language Proficiency Test](https://www.jlpt.jp/e/about/index.html)
[^jlpt-level]: [N1-N5: Summary of Linguistic Competence Required for Each Level | JLPT Japanese-Language Proficiency Test](https://www.jlpt.jp/e/about/levelsummary.html)

### Readings corresponding to **Kanji levels** {nekochan}`kamon`

```{revealjs-notes}
I want to create readings corresponding to kanji levels.
```

### **Kanji list** for each level

* [jiten](https://pypi.org/project/jiten/) has JLPT Kanji lists
  * <https://github.com/obfusk/jiten/tree/master/jiten/res/jlpt>

### Make JLPT **Kanji level dict**

make_jlpt_kanji_dict.py

```{revealjs-literalinclude} code/make_jlpt_kanji_dict.py
:language: python
:data-line-numbers: 2-10|1,12-13
```

```{revealjs-break}
```

* Kanji dict is ready!! {nekochan}`naosu`

```bash
% python make_jlpt_kanji_dict.py
```

```{revealjs-literalinclude} code/JLPT_kanji.json
```

### Get reading with **Kanji level**

* `-a`: Alphabet annotation(default: Hiragana)
* `-l`: Kanji level option

```text
% python kanji_reading_with_level.py -h
usage: kanji_reading_with_level.py [-h] [-a] [-l {1,2,3,4,5}] text

Add Furigana to Japanese text

positional arguments:
  text            text to add furigana annotation

options:
  -h, --help      show this help message and exit
  -a              Alphabet(Romaji) annotation(default: Hiragana)
  -l {1,2,3,4,5}  set kanji level
```

```{revealjs-notes}
I have created an annotation script that supports Kanji levels.
```

```{revealjs-break}
```

```bash
% python kanji_reading_with_level.py 日本語を勉強する
```

<ruby>日本語<rt>にほんご</rt></ruby>
<ruby>を<rt>を</rt></ruby>
<ruby>勉強<rt>べんきょう</rt></ruby>
<ruby>する<rt>する</rt></ruby>
(default)

```bash
% python kanji_reading_with_level.py -a 日本語を勉強する
```

<ruby>日本語<rt>nihongo</rt></ruby>
<ruby>を<rt>wo</rt></ruby>
<ruby>勉強<rt>benkyou</rt></ruby>
<ruby>する<rt>suru</rt></ruby>
(Alphabet(romaji))

```bash
% python kanji_reading_with_level.py -l 5 日本語を勉強する
```

日本語
を
<ruby>勉強<rt>べんきょう</rt></ruby>
する
(N5 level)

```{revealjs-notes}
I will explain the code.
```

### Parse arguments

* Process `-a` and `-l` with **argparse**
* Call `add_reading()` function

```{revealjs-literalinclude} code/kanji_reading_with_level.py
:data-line-numbers: 70-79|80
```

### Get **Kanji set** with level

* Get Kanji set with `get_kanji_set(level)`

```{revealjs-literalinclude} code/kanji_reading_with_level.py
:data-line-numbers: 53-55
```

```{revealjs-notes}
In add_reading() func, to get the Kanji set, specify the level argument to the get_kanji_set() func.
```

```{revealjs-break}
```

* Load `"JLPT_kanji.json"`
* Create a Kanji set is **easier than level**

```{revealjs-literalinclude} code/kanji_reading_with_level.py
:data-line-numbers: 26-32|33-37
```

```{revealjs-notes}
get_kanji_set() func reads Kanjis per level from JSON.
Then Create a Kanji set that is easier than the level.
```

### Is **ruby required**?

* **Ruby / not Ruby** with `is_ruby_required()`

```{revealjs-literalinclude} code/kanji_reading_with_level.py
:data-line-numbers: 53,57-59
```

```{revealjs-notes}
Determine if ruby is required or not with the is_ruby_required() function for each token.
```

```{revealjs-break}
```

* Get all Kanjis -> `kanji_in_surface`
* Kanjis are **within** the level or **above**

```{revealjs-literalinclude} code/kanji_reading_with_level.py
:data-line-numbers: 40-45|46-50
```

```{revealjs-notes}
In the function, I get all Kanjis in the token and assign them to kanji_in_surface.
Next, determine if there is a Kanji and if Kanjis are within the level or above the level.
```

### Add **Ruby text**

* `is_ruby_required() == True`: add Ruby
* `alphabet`: Alphabet or Hiragana(default)

```{revealjs-literalinclude} code/kanji_reading_with_level.py
:data-line-numbers: 57-67|60-63
```

```{revealjs-notes}
Finally, if is_ruby_required() is True, add ruby text.
And, depending on the value of alphabet, ruby is converted to alphabet or hiragana
```

### Can handle **Kanji level**!! {nekochan}`yatta`

No Level: <ruby>日本語<rt>にほんご</rt></ruby>
<ruby>を<rt>を</rt></ruby>
<ruby>勉強<rt>べんきょう</rt></ruby>
<ruby>する<rt>する</rt></ruby>

N5: 日本語
を
<ruby>勉強<rt>べんきょう</rt></ruby>
する

N4: 日本語
を
勉強
する

```{revealjs-notes}
Now, We can handle Kanji level.
You can learn Kanji at your own Japanese level.
```

## **Sample** App {nekochan}`work`

* {fab}`github` [learn_jp_pyconus.py](https://github.com/takanory/learn-jp-with-python/blob/main/learn_jp_pyconus.py)

```bash
% git clone https://github.com/takanory/learn-jp-with-python.git
% cd learn-jp-with-python/
% python3.12 -m venv env
% . env/bin/activate
(env) % pip install -r requirements.txt
(env) % streamlit run learn_jp_pyconus.py
```

```{revealjs-break}
:notitle:
```

```{image} images/streamlit_demo.gif
:width: 85%
```

## **Summary** {nekochan}`juutai`

* Japanese is **Difficult**
  * 3 Characters, No spaces, Kanji readings
* Python supports Japanese learning
  * **jaconv**: Interconverter
  * **SudachiPy**: Morphological analyzer
* **Kanji level** support
  
## 🇯🇵 ❤️ {fab}`python`

Learn **Japanese** with **Python**

```{revealjs-notes}
You can learn Japanese with Python.
Please try to create your own Japanese learning tool!
```

## Thank you {nekochan}`pray`

{fas}`desktop` [slides.takanory.net](https://slides.takanory.net/)
{fas}`code` [sample code](https://github.com/takanory/slides/tree/master/slides/20250516pyconus/code)

{fab}`twitter` [takanory](https://twitter.com/takanory)
{fab}`github` [takanory](https://github.com/takanory/)
{fab}`linkedin` [takanory](https://www.linkedin.com/in/takanory/)
{fab}`untappd` [takanory](https://untappd.com/user/takanory/)

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)
