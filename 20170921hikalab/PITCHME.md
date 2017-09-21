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

### Python知ってる人?

+++

### Python書いたことある人?

+++

### 他のプログラミング言語使っている人?

---

## 今日のゴール

(ほぼ)標準のPythonのみを使って、

いい感じにプログラムを書けるようになる

ヒントを得る

---

## 今日話すこと

1. 「はじめの一歩」の振り返り
2. pythonの一般的なデバッグ手法(pdb)
3. コーディングスタイルの統一(PEP8, flake8)
4. 自動テスト手法(unittest)
5. Python公式ドキュメントを読みこなそう
6. 文字列メソッドを使いこなそう
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

### なぜデバッガー?

* `print()`デバッグはめんどう
* この変数の値が見たかった
  * 止めてコード書き換えて再実行
* pdbを使おう!

+++

### pdb

* Python標準のデバッガ
* インストール不要
* コマンドラインで操作

+++

### 間違ったfizzbuzz

```python
for num in range(1, 100):
    if num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    elif num % 15 == 0:  # ここがおかしい
        print('FizzBuzz')
    else:
        print(num)
```

+++

### デバッグする

```python
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

```sh
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

* `p`: expression: expressionを評価した結果を表示
* `n`: 次の行に移動
* `c`: 次のブレークポイントまで実行
* `h`: ヘルプを表示
* `l`: ソースコードを表示
* `q`: デバッガを終了する

他のコマンドは[27.3.1. デバッガコマンド](https://docs.python.jp/3/library/pdb.html#debugger-commands "27.3.1. デバッガコマンド")を参照

+++

### まとめ

* pdbでデバッグしよう

[pdb - Python デバッガ](https://docs.python.jp/3/library/pdb.html "27.3. pdb — Python デバッガ — Python 3.6.1 ドキュメント")

---

## 3. コーディングスタイルの統一(PEP8, flake8)

+++

### なぜ統一する?

* Pythonとしての統一ルールがある
* サポートするツールもある
* 統一しておけば揉めない

+++

### PEP8(1/2)

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/ "PEP 8 -- Style Guide for Python Code | Python.org")

* Yes

```python
spam(ham[1], {eggs: 2})
dct['key'] = lst[index]
i = i + 1
submitted += 1
```

* No

```python
spam( ham[ 1 ], { eggs: 2 } )
dct ['key'] = lst [index]
i=i+1
submitted +=1
```

+++

### PEP8(2/2)

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/ "PEP 8 -- Style Guide for Python Code | Python.org")

* Yes

```python
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```

* No

```python
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

+++

### pycodestyle

* PEP8対応のチェックツール
* インストールが必要

[pycodestyle's documentation](http://pycodestyle.pycqa.org/ "pycodestyle’s documentation — pycodestyle 2.3.1 documentation")

```sh
$ pip install pycodestyle  # インストール
$ pycodestyle fizzbuzz.py  # pycodestyleを実行
```

+++

### だめなfizzbuzz.py

```python
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

```sh
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
* インストールが必要

```sh
$ pip install flake8
$ flake8 fizzbuzz.py
```

[Flake8: Your Tool For Style Guide Enforcement](http://flake8.pycqa.org/en/latest/ "Flake8: Your Tool For Style Guide Enforcement — flake8 3.4.1 documentation")

+++

### まとめ

* flake8 を使おう
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

+++?code=20170921hikalab/unittest/fizzbuzz_ng.py&lang=python

### 間違ったfizzbuzz関数

+++?code=20170921hikalab/unittest/test_fizzbuzz.py&lang=python

### テストコード

+++

### 実行結果

```sh
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

```sh
$ python3 -m unittest test_fizzbuzz.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

+++

### 自動テスト: まとめ

* 書ける範囲で書こう
* [26.3. doctest - 対話的な実行例をテストする](https://docs.python.jp/3/library/doctest.html "26.3. doctest — 対話的な実行例をテストする — Python 3.6.1 ドキュメント")もあるよ

---

## 5. Python公式ドキュメントを読みこなそう

+++

### 公式ドキュメント?

* https://docs.python.jp/3/ で公開されている
* 情報がたくさん
  * チュートリアル
  * ライブラリーリファレンス
  * HOWTO
* https://docs.python.org/ja/3/ に移行予定

+++

### 非公式はあくまでヒントに

* Qiita
* teratail, Stack Overflow
* 個人ブログ

+++

### `print()`関数

* `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`

`objects`を`sep`で区切りながらテキストストリーム`file`に表示し、最後に`end`を表示します。`sep`、`end`、`file`、`flush` を与える場合、キーワード引数として与える必要があります。

[print()関数 - 2. 組み込み関数](https://docs.python.jp/3/library/functions.html#print)

+++

### `print()`関数は可変長引数を受け取る

```python
>>> print()

>>> print(1, 2)
1 2
>>> print(1, 2, 3, 4)
1 2 3 4
```

+++

### `sep`引数で区切り文字が変更できる

```python
>>> print(1, 2, 3, 4, sep=",")
1,2,3,4
>>> print(1, 2, 3, 4, sep="|")
1|2|3|4
>>> print(1, 2, 3, 4, sep="✌")
1✌2✌3✌4
```

+++

### `file`引数で出力先を変えられる

```python
>>> with open('sample.txt', 'w') as f:
...     print(1, 2, 3, 4, file=f)
...     print(1, 2, 3, 4, file=f, sep=',')
...
>>> with open('sample.txt') as f:
...     f.read()
... 
'1 2 3 4\n1,2,3,4\n'
```

+++

### ここまで触れたドキュメント

* [pdb - Python デバッガ](https://docs.python.jp/3/library/pdb.html "27.3. pdb — Python デバッガ — Python 3.6.1 ドキュメント")
* [unittest - ユニットテストフレームワーク](https://docs.python.jp/3/library/unittest.html "26.4. unittest — ユニットテストフレームワーク — Python 3.6.1 ドキュメント")
* [doctest - 対話的な実行例をテストする](https://docs.python.jp/3/library/doctest.html "26.3. doctest — 対話的な実行例をテストする — Python 3.6.1 ドキュメント")
* [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/ "PEP 8 -- Style Guide for Python Code | Python.org")
* [pycodestyle's documentation](http://pycodestyle.pycqa.org/ "pycodestyle’s documentation — pycodestyle 2.3.1 documentation")
* [Flake8: Your Tool For Style Guide Enforcement](http://flake8.pycqa.org/en/latest/ "Flake8: Your Tool For Style Guide Enforcement — flake8 3.4.1 documentation")
* [print()関数 - 2. 組み込み関数](https://docs.python.jp/3/library/functions.html#print)

+++ 

### まとめ

* 公式ドキュメント読もう
* 外部ライブラリもドキュメントがちゃんとしているものを使おう

---

## 6. 文字列メソッドを使いこなそう

+++

### なぜ?

* Pythonの文字列はメソッドが豊富
* 正規表現使わなくてもいろいろできる

[4.7. テキストシーケンス型 - str](https://docs.python.jp/3/library/stdtypes.html#text-sequence-type-str "4.7. テキストシーケンス型 — str")

+++

### .format()メソッド使いこなし(1/2)

```python
>>> '{}, {}, {}'.format('a', 'b', 'c')
'a, b, c'
>>> '{2}, {1}, {0}'.format('a', 'b', 'c')  # 順番入れ替え
'c, b, a'
>>> '{lat}, {lng}'.format(lat='37.24N', lng='-115.81W')  # 名前でアクセス
'37.24N, -115.81W'
>>> '{:,}'.format(1234567890)  # 数値にカンマ
'1,234,567,890'
```

[6.1.3.1. 書式指定ミニ言語仕様](https://docs.python.jp/3/library/string.html#format-specification-mini-language "6.1.3.1. 書式指定ミニ言語仕様")

+++ 

### .format()メソッド使いこなし(2/2)

```python
>>> c = 3-5j  # 虚数を定義
>>> '{0.real} {0.imag}'.format(c)  # 属性にアクセス
'3.0 -5.0'
>>> from datetime import datetime
>>> now = datetime.now()
>>> '{:%Y-%m-%d %H:%M:%S}'.format(now)  # 特殊な書式指定
'2017-09-20 17:14:50'
```

[6.1.3.1. 書式指定ミニ言語仕様](https://docs.python.jp/3/library/string.html#format-specification-mini-language "6.1.3.1. 書式指定ミニ言語仕様")

+++

### .endswith()メソッド

* `str.endswith(suffix[, start[, end]])`

文字列が指定された suffix で終わるなら True を、そうでなければ False を返します。 suffix は見つけたい複数の接尾語のタプルでも構いません。

```python
>>> filename = 'hoge.jpg'
>>> filename.endswith('.gif')
False
>>> filename.endswith(('.jpg', '.gif', '.png'))
True
```

+++

### まとめ

* 文字列メソッドは多機能
* 単純な処理は文字列メソッドのみでOK

[4.7. テキストシーケンス型 - str](https://docs.python.jp/3/library/stdtypes.html#text-sequence-type-str "4.7. テキストシーケンス型 — str")

---

## 7. 例外処理の使いどころ

+++

### なぜ?

* エラーは情報の宝庫
* 例外処理は便利
* でもなんでも例外で処理するのは危険

+++

### Tracebackを読もう

```python
Traceback (most recent call last):
  File "traceback_sample.py", line 7, in <module>
    main()
  File "traceback_sample.py", line 5, in main
    return sub()
  File "traceback_sample.py", line 2, in sub
    return int('名前')
ValueError: invalid literal for int() with base 10: '名前'
```

+++

### 例外を握りつぶしちゃう

```python
try:
    # なんか
    # 処理
except Exception:
    pass
```

+++

### どこで発生する例外かわかりにくい

```pytho
try:
    # とっても
    # とっても
    # 長い
    # 処理
except ValueError:
    # 対応する例外処理
except IndexError:
    # 対応する例外処理
```

+++

### 例外の発生する可能性のある個所のみを対象に

```python
try:
    # とっても
except ValueError:
    # 対応する例外処理
    return
try:
    # とっても
except IndexError:
    # 対応する例外処理
# 長い
# 処理
```

+++

### 可能なら前もってチェックする

```python
try:
    num = int(num_str)
except ValueError:
    # 数値の文字列じゃないときの処理
```

```python
if num_str.isdigit():
    num = int(num_str)
else:
    # 数値の文字列じゃないときの処理
``

+++

### まとめ

* Tracebackを読もう
* 例外を握りつぶさない
* 全体を大きく囲まない
* 先にわかるものはそこでチェック

[5. 組み込み例外 — Python 3.6.1 ドキュメント](https://docs.python.jp/3/library/exceptions.html "5. 組み込み例外 — Python 3.6.1 ドキュメント")

---

## 8. 内包表記、ジェネレーター式を使いこなそう

---

## 9. 次のステップ

+++

### Python言語入門から

![いちばんやさしいPythonの教本](assets/image/ichiyasa.jpg)

[いちばんやさしいPythonの教本](https://book.impress.co.jp/books/1116101151 "いちばんやさしいPythonの教本 人気講師が教える基礎からサーバサイド開発まで - インプレスブックス")

+++

### Pythonで何か作ってみたい

![Pythonエンジニアファーストブック](assets/image/pyfirst.jpg)

[Pythonエンジニア ファーストブック](http://gihyo.jp/book/2017/978-4-7741-9222-2 "Pythonエンジニア ファーストブック：書籍案内｜技術評論社")

+++

### ライブラリを使いこなしたい

![Python ライブラリ厳選レシピ](assets/image/recipe.jpg)

[Python ライブラリ厳選レシピ](http://gihyo.jp/book/2015/978-4-7741-7707-6 "Python ライブラリ厳選レシピ：書籍案内｜技術評論社")

+++

## Question?

---

## ありがとうございました