```{eval-rst}
:og:image: _images/20250718euro.png
:og:image:alt: Learn Japanese 🇯🇵 with Python

.. |cover| image:: images/20250718euro.png
```

# Learn **Japanese** 🇯🇵 with **Python {fab}`python`**

Takanori Suzuki

```{image} images/ep2025-logo-and-caption.svg
:width: 60%
```

EuroPython 2025 / 2025 Jul 18

## PyCon JP 2025

* {fas}`globe` [`2025.pycon.jp`](https://2025.pycon.jp/)
* Date: 2025 **Sep 26**(Fri)-**27**(Sat)
* Place: **Hiroshima**, Japan
* There are **English talks**

```{image} ../20250516pyconus/images/pyconjp2025-in-hiroshima.jpg
:alt: PyCon JP 2025 in Hiroshima
:width: 60%
```

## Questions {nekochan}`hai`

### Have you **learned** Japanese?  {nekochan}`study`

### Are you **interested** in Japanese? {nekochan}`miru`

## Japanese is **difficult** {nekochan}`yabai`

* **3 Types** of Characters(Hiragana, Katakana, Kanji)
* **No Spaces** between Words
* **Multiple Readings** of Kanji

### **3 Types** of Characters

| Emoji | 🐍 | 🍺 |
| -- | -- | -- |
| Hiragara | へび | びーる |
| Katakana | ヘビ | ビール |
| Kanji |  蛇 | 麦酒 |

### **No Spaces** between Words

* すもももももももものうち

### **No Spaces** between Words

* すもももももももものうち
* すもも/も/もも/も/もも/の/うち
* Plums and peaches are part of peaches

### **Multiple Readings** of Kanji

* **日**: day, sun
  * **Japanese**-style reading: にち(nichi)、ひ(hi)
  * **Chinese**-style reading: じつ(jitsu)、か(ka)
  
### **Multiple Readings** of Kanji

* **日**: day, sun
  * **Japanese**-style reading: にち(nichi)、ひ(hi)
  * **Chinese**-style reading: じつ(jitsu)、か(ka)
* 日曜日 (**nichi** you **bi**): Sunday
* 前日 (zen **jitsu**): previous day

### {nekochan}`pokan`
  
### **Multiple Readings** of Kanji

* Same combination but **different readings**
* **一日**: first day, one day
  * **一日** 目: Day 1
  * 一月 **一日**: Jan 1st

### **Multiple Readings** of Kanji

* Same combination but **different readings**
* 一日: first day, one day
  * **一日** 目 (**ichi nichi** me): Day 1
  * 一月 **一日** (ichi gatsu **tsuitachi**): Jan 1st

### {nekochan}`yabai;1.5em` {nekochan}`yabai;1.5em`
  
### **Multiple Readings** of Kanji

* **Special readings** of Kanji idioms
* 今 **日**: today
* 昨 **日**: yesterday
* 明 **日**: tomorrow

### **Multiple Readings** of Kanji

* **Special readings** of Kanji idioms
* 今日 (**kyou**): today
* 昨日 (**kinou**): yesterday
* 明日 (**asu**): tomorrow

### {nekochan}`scream;2em` {nekochan}`scream;2em` {nekochan}`scream;2em`

## Learn Japanese with **Python**

## **No Spaces** between Words

* すもももももももものうち
* すもも/も/もも/も/もも/の/うち

### Japanese morphological analyzer

* SudachiPy: [pypi.org/project/SudachiPy](https://pypi.org/project/SudachiPy/)
* SudachiDict: [pypi.org/project/SudachiDict-core](https://pypi.org/project/SudachiDict-core/)

```bash
$ pip install sudachipy sudachidict_core
```

### Word **Segmentation**

```{literalinclude} code/word_segmentation.py
:language: python
```

## **Multiple Readings** of Kanji

* 今 **日** は一月一 **日** で **日** 曜 **日**
* Today is January 1st, Sunday

### Morphological **Analysis**

```{literalinclude} code/analysis.py
:language: python
```

### Get **Readings**

```{literalinclude} code/readings.py
:language: python
```

### Can't read **Katakana**?

### **Convert** Japanese Character

* jaconv: [pypi.org/project/jaconv](https://pypi.org/project/jaconv)

```{literalinclude} code/convert.py
:language: python
:lines: 9-17
```

## Want to hear **audio**? {nekochan}`kiku`

### Text to **Speech**

* [Amazon Polly - AWS](https://aws.amazon.com/polly/)
* [Polly - Boto3 1.34.106 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html)

```{literalinclude} code/polly.py
:language: python
```

## Sample app

* [github.com/takanory/learn-jp-with-python](https://github.com/takanory/learn-jp-with-python)

```{image} ../20240517pyconus/images/sample-app.png
:width: 65%
```

## Full talk at PyCon US 2025

<iframe width="800" height="450" src="https://www.youtube.com/embed/3wQxP-GfT-A?si=Xgnos7wi9ZRzm-Dj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Thank you {nekochan}`pray`

{fas}`desktop` [slides.takanory.net](https://slides.takanory.net/)
{fas}`code` [code](https://github.com/takanory/slides/tree/master/slides/20250718euro/code)

{fab}`twitter` [@takanory](https://twitter.com/takanory)
{fab}`github` [takanory](https://github.com/takanory/)
{fab}`linkedin` [takanory](https://www.linkedin.com/in/takanory/)
{fab}`untappd` [takanory](https://untappd.com/user/takanory/)

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

