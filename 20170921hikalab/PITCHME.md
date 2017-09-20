## 「Python言語」
## 二歩目を踏み出そう！

#### 脱初心者になるためのポイントを伝授します

Takanori Suzuki / ヒカ☆ラボ / 2017年9月21日

---

## Who am I?(お前誰よ)

* 鈴木たかのり / Takanori Suzuki
* Twitter: [@takanory](https://twitter.com/takanory)
* [Pythonボルダリング部](https://kabepy.connpass.com/)(#kabepy)部長

![takanory](assets/image/kurokuri.jpg)

+++ 

### 株式会社ビープラウド所属

* [株式会社ビープラウド](https://www.beproud.jp/)

![BeProud](assets/image/beproud.png)

+++ 

### 一般社団法人PyCon JP理事

* [一般社団法人PyCon JP](https://www.pycon.jp/)

![PyCon JP](assets/image/pyconjp_logo.png)

---

## 最初に質問

+++

### Python 書いたことある人?

---

## 今日のゴール

標準のPythonのみを使って、いい感じに書けるようになるヒントを知る

---

## 今日話すこと

1. 「はじめの一歩」の振り返り
2. pythonの一般的なデバッグ手法(pdb)
3. コーディングスタイルの統一(PEP8, flake8)
4. 自動テスト手法(unittest)
5. Python公式ドキュメントを読みこなそう
6. 文字列メソッドを使いこなそう(format, startswithなど)
7. 例外処理の使いどころ
8. 内包表記、ジェネレーター式を使いこなそう
9. 次のステップ

---

## 1. 「はじめの一歩」の振り返り

[「Python言語」はじめの一歩 / First step of Python](https://www.slideshare.net/takanory/python-first-step-of-python)

<iframe src="//www.slideshare.net/slideshow/embed_code/key/xFxV1pZ3q2nmDq" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/takanory/python-first-step-of-python" title="「Python言語」はじめの一歩 / First step of Python" target="_blank">「Python言語」はじめの一歩 / First step of Python</a> </strong> from <strong><a href="https://www.slideshare.net/takanory" target="_blank">Takanori Suzuki</a></strong> </div>

+++

### 1.1 Pythonの特徴

* まぁ、なんでもできる
* きれいに書きやすい
* 保守しやすい
* 20年以上開発してる
* Python 2 と 3 がある

+++

### 1.2 言語の特徴

* インデントでブロック構造
* 対話モード
* たくさんの標準ライブラリ
* 豊富な外部パッケージ

+++

### 1.3 インストール

* 公式からインストールしよう

+++

### 1.4 言語仕様

* データ型: int, float, str, bytes
* コレクション: list, tuple, dict, set
* 分岐: if, elif, else
* 繰り返し: for, while
* ファイル操作: open(), with open
* モジュール: import

+++

### 1.5 Python 2と3の違い

* printが文→関数
* 文字列がUnicodeに統一
* intの割り算の結果がfloat
* 標準ライブラリの再構成

+++

### 1.6 よく使う標準ライブラリ

* re: 正規表現
* sys, os: システムパラメータとOS
* datetime: 日付と時刻
* math, random: 数学関数と乱数
* itertools: イテレータ生成関数
* shutil: 高レベルなファイル操作
* json: JSONエンコーダ、デコーダ

+++

### 1.7 よく使うサードパーティ製パッケージ

* pip と venv(virtualenv)
* dateutil: 日時操作の強力な拡張
* Requests: HTTPクライアント
* BeautifulSoup4: HTML, XMLパーサ
* Pillow: 画像処理ライブラリ
* PEP8: pycodestyle, flake8

+++

### 1.8 どうやって学ぶか

* 書籍紹介
* Web上のテキスト
* コミュニティに参加

--- 

## 2. pythonの一般的なデバッグ手法(pdb)

+++

### なぜ pdb?

* printデバッグはめんどう
* この変数の値が見たかった
  * 止めてコード書き換えて再実行
* pdbを使おう!

+++

### pdb

* Python標準のデバッガ
* インストール不要
* コマンドラインで操作

詳しくは[pdb - Python デバッガ](https://docs.python.jp/3/library/pdb.html "27.3. pdb — Python デバッガ — Python 3.6.1 ドキュメント")を参照

+++

### 間違ったfizzbuzz

```
for num in range(1, 100):
    if num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 15 == 0:
        print('FizzBuzz')
    else:
        print(num)
```

+++

### デバッグする

```
for num in range(1, 100):
    import pdb; pdb.set_trace()  # 追加
    if num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 15 == 0:
        print('FizzBuzz')
    else:
        print(num)
```

+++

### 実行

```
$ python3 fizzbuzz.py
(env) Takanoris-MacBook-Pro:pycamp.pycon.jp takanori$ python fizzbuzz.py
> /Users/takanori/fizzbuzz.py(3)<module>()
-> if num % 3 == 0:
(Pdb) p num
1
(Pdb) n
> /Users/takanori/fizzbuzz.py(5)<module>()
-> elif num % 5 == 0:
(Pdb) c
1
> /Users/takanori/fizzbuzz.py(2)<module>()
-> import pdb; pdb.set_trace()  # 追加
(Pdb) p num
2
(Pdb)
```

+++

### 主なコマンド

* p expression: expressionを評価した結果を表示
* n: 次の行に移動
* c: 次のブーレくポイントまで実行
* h: ヘルプを表示
* l: ソースコードを表示
* q: デバッガを終了する

他のコマンドは[27.3.1. デバッガコマンド](https://docs.python.jp/3/library/pdb.html#debugger-commands "27.3.1. デバッガコマンド")を参照

---

## 3. コーディングスタイルの統一(PEP8, flake8)

+++

### なぜ統一する?

* Pythonとしての統一ルールがある
* サポートするツールもある
* 統一しておけば揉めない

+++

### PEP8

[PEP 8 -- Style Guide for Python Code | Python.org](https://www.python.org/dev/peps/pep-0008/ "PEP 8 -- Style Guide for Python Code | Python.org")

```
spam(ham[1], {eggs: 2})  # Yes
spam( ham[ 1 ], { eggs: 2 } )  # No

dct['key'] = lst[index]  # Yes
dct ['key'] = lst [index]  # No

i = i + 1  # Yes
submitted += 1  # Yes
i=i+1  # No
submitted +=1  # No

def complex(real, imag=0.0):  # Yes
    return magic(r=real, i=imag)

def complex(real, imag = 0.0):  # No
    return magic(r = real, i = imag)
```

+++

### pycodestyle

* PEP8対応のチェックツール
* インストールが必要

[pycodestyle](https://pypi.python.org/pypi/pycodestyle "pycodestyle 2.3.1 : Python Package Index")

```
$ pip install pycodestyle
$ pycodestyle fizzbuzz.py
```

### だめなfizzbuzz.py

```
for num in range(1, 100) :
    if num % 15 == 0:
        print( 'FizzBuzz' )
    elif num%3 == 0:
        print('Fizz')
    elif num % 5 == 0:
         print('Buzz')
    else:
        print(num)
```

+++

### 実行結果

```
$ pycodestyle fizzbuzz.py 
fizzbuzz.py:1:25: E203 whitespace before ':'
fizzbuzz.py:3:15: E201 whitespace after '('
fizzbuzz.py:3:26: E202 whitespace before ')'
fizzbuzz.py:4:13: E228 missing whitespace around modulo operator
fizzbuzz.py:7:10: E111 indentation is not a multiple of four
```

+++

### flake8

* pycodestylesに加えてpyflakesのチェックが入る
* importしてるけど使ってない
* 宣言した変数を使ってない
* `from module import *` している

[flake8](https://pypi.python.org/pypi/flake8 "flake8 3.4.1 : Python Package Index")

+++

### コーディングスタイルの統一: まとめ

* pycodestyle は使おう
* flake8 も使えるとよい
* エディターでもチェックしてくれるよ

---

## 4. 自動テスト手法(unittest)

+++

### なぜ自動テスト?

* 関数単位で仕様が明確になる
* リファクタリングしても安心

+++

### unittest

* Pythonの標準ライブラリ
* テストコードを書いて実行できる

[26.4. unittest - ユニットテストフレームワーク](https://docs.python.jp/3/library/unittest.html "26.4. unittest — ユニットテストフレームワーク — Python 3.6.1 ドキュメント")

+++?code=unittest/fizzbuzz_ng.py

### 間違ったfizzbuzz関数

+++?code=unittest/test_fizzbuzz.py

### テストコード

+++

### 実行結果

```
$ python3 -m unittest test_fizzbuzz.py
..F.
======================================================================
FAIL: test_fizzbuzz (test_fizzbuzz.TestFizzbuzz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/takanori/unittest/test_fizzbuzz.py", line 12, in test_fizzbuzz
    self.assertEqual(fizzbuzz(30), 'FizzBuzz')
AssertionError: 'Fizz' != 'FizzBuzz'
- Fizz
+ FizzBuzz


----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=1)
```

+++

### 修正して再実行

```
$ python3 -m unittest test_fizzbuzz.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

+++

### 自動テスト: まとめ

* 書ける範囲で書こう

---

## 5. Python公式ドキュメントを読みこなそう

---

## 6. 文字列メソッドを使いこなそう(format, startswithなど)

---

## 7. 例外処理の使いどころ

---

## 8. 内包表記、ジェネレーター式を使いこなそう

---

## 9. 次のステップ

---

## Question?

---

## ありがとうございました