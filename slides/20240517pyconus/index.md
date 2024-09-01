```{eval-rst}
:og:image: _images/cover.png
:og:image:alt: Learn Japanese 🇯🇵 with Python

.. |cover| image:: images/cover.png
```

# Learn **Japanese** 🇯🇵 with **Python {fab}`python`**

Takanori Suzuki

PyCon US 2024 / 2024 May 17

## PyCon JP 2024 **CfP** is Open

* [2024.pycon.jp](https://2024.pycon.jp/)
* Proposal Deadline: **May 31** (English is welcome!!)
* Date: Sep 27-29
* Place: Tokyo, Japan

## Questions 🙋

### Have you **learned** Japanese? 🙋‍♂️

### Are you **interested** in Japanese? 🙋‍♀️

## Japanese is **difficult** 🤔

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

### 😨
  
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

### 😱 😱
  
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

## 🤯 🤯 🤯

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

## Want to hear **audio**? 🗣️

### Text to **Speech**

* [Amazon Polly - AWS](https://aws.amazon.com/polly/)
* [Polly - Boto3 1.34.106 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html)

```{literalinclude} code/polly.py
:language: python
```

## Sample app

* [github.com/takanory/learn-jp-with-python](https://github.com/takanory/learn-jp-with-python)

```{image} images/sample-app.png
:width: 65%
```

## Thank you 🙏

{fas}`desktop` [slides.takanory.net](https://slides.takanory.net/)
{fas}`code` [code](https://github.com/takanory/slides/tree/master/slides/20240517pyconus/code)

{fab}`twitter` [@takanory](https://twitter.com/takanory)
{fab}`github` [takanory](https://github.com/takanory/)
{fab}`linkedin` [takanory](https://www.linkedin.com/in/takanory/)
{fab}`untappd` [takanory](https://untappd.com/user/takanory/)

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

