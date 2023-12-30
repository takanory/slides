# Pythonで<br />**日本語処理** 入門

**〜フリガナプログラムを作ろう〜**

Takanori Suzuki 

Open Source Conference Osaka 2024 / 2024 Jan 27

## アジェンダ 📋

* 自然言語処理とは
  * **形態素解析** について
* **Janome** でフリガナプログラム
* **SudachiPy** でフリガナプログラム
* LLM(大規模言語モデル)については **話しません**

### ゴール 🥅

* 自然言語処理がどういうものか知る
* JanomeまたはSudachiPyを使った日本語処理ができそう

## Photos 📷 Tweets 🐦 👍

`#oscosk2024` / `@takanory`

### Slide / スライド 💻

[slides.takanory.net](https://slides.takanory.net)

## **Who** am I? / お前 **誰よ** 👤

- Takanori Suzuki / 鈴木 たかのり ({fab}`twitter` [@takanory](https://twitter.com/takanory))
- [PyCon JP Association](https://www.pycon.jp/) 代表理事
- [BeProud](https://www.beproud.jp/) 取締役 / Python Climber
- [Python Boot Camp](https://www.pycon.jp/support/bootcamp.html) 講師、[Python mini Hack-a-thon](https://pyhack.connpass.com/) 主催、[Pythonボルダリング部](https://kabepy.connpass.com/) 部長

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

### PyCon JP **Association** 🐍

日本国内のPythonユーザのために、**Pythonの普及及び開発支援**を行うために、継続的にカンファレンス(**PyCon**)を開くことを目的とした **非営利組織**

* [`www.pycon.jp`](https://www.pycon.jp)

![pycon jp logo](/assets/images/pyconjp_logo.png)

### PyCon JP **Association** の主な活動

* PyCon JP: 年1の大規模カンファレンス
* [Python Boot Camp](https://www.pycon.jp/support/bootcamp.html): 初心者向けチュートリアル
* [Pythonコミュニティのサポート](https://www.pycon.jp/support/community.html)
* [PyCon JP TV](https://tv.pycon.jp/): YouTubeライブ

### PyCon JP Associationブース

* PyCon JP 2024スタッフ募集
* Python Boot Campの紹介
* PyLadies Caravanの紹介
* その他Python・コミュニティ関連相談

### **BeProud** Inc. 🏢

* [BeProud](https://www.beproud.jp/) :Pythonシステム開発、コンサル
* [connpass](https://connpass.com/): IT勉強会支援プラットフォーム
* [PyQ](https://pyq.jp/): Python独学プラットフォーム
* [TRACERY](https://tracery.jp/): システム開発ドキュメントサービス

![BeProud logos](/assets/images/beproud-logos.png)

## **自然言語処理** とは 🗣️

### **自然言語処理** とは 🗣️

* NLP(Natural Language Processing)
* 自然言語(日本語、英語等)は厳格な構文がない
  * Pythonは[言語仕様](https://docs.python.org/ja/3/reference/index.html)があるので機械的に処理がしやすい
* NLP(自然言語処理)用のライブラリが必要

### NLPライブラリ

* [NLTK: Natural Language Toolkit](https://www.nltk.org/)
* [Gensim](https://radimrehurek.com/gensim/index.html)
* [spaCy](https://spacy.io/)
* [Pytorch-NLP](https://pytorchnlp.readthedocs.io/en/latest/)
* そのままでは **日本語を処理できない** ものも

* [Awesome Python](https://awesome-python.com/#natural-language-processing)より

### 日本語の特徴

* 単語が **スペースで区切られていない**

  * 「すもももももももものうち」

* 一つの漢字に **複数の読み方**

  * 「一月一日は元日で昨日は大晦日」
  
* 文脈で **単語の分かれ目** が違う

  * 「東京都と神奈川の小京都」

## **形態素解析** 💬

### **形態素解析** 💬

* 自然言語(日本語)を **形態素** に分割

  * 形態素=単語などの要素
* **品詞** などの情報を付加
* 日本語の **辞書データ** が必要

### 品詞、原形、読み

* 形態素解析が付加する主な情報
* 例：「とても美味しいビールを飲みたい」
* **品詞**: とても(副詞)美味しい(形容詞)ビール(副詞)...
* **原形**: 飲み→飲む
* **読み**: 美味しい→おいしい、飲み→のみ

### 形態素解析の用途

* 検索エンジンの検索インデックス
* 文章の分類
* 単語の数で文章の特徴を表す(**Bag of Words**)
* 単語の重要度を調べる(**TF-IDF**)

### **目的**：フリガナを振る

* 形態素解析ライブラリを使ったプログラム

```bash
$ ./furigana.py "美味しい麦酒を飲もう" > result.html && cat result.html
<ruby><rb>美味</rb><rt>おい</rt></ruby>しい
<ruby><rb>麦酒</rb><rt>びーる</rt></ruby>を
<ruby><rb>飲</rb><rt>の</rt></ruby>もう
```

![result](images/result.png)

## **Janome** で形態素解析 👀

### **Janome** とは

* [mocobeta.github.io/janome/](https://mocobeta.github.io/janome/)
* **Pure Python** で書かれた **辞書内包** の形態素解析器
  * OSに依存しない
  * すぐ使い始められる

### Janomeをインストール

* `pip install janome` でインストール

```bash
$ python3.11 -m venv env  # venvモジュールで仮想環境作成
$ . env/bin/activate
(env) $ pip install janome
...
Successfully installed janome-0.5.0
```

### Janomeで形態素解析

* `janome` コマンドで形態素解析

```bash
(env) $ echo "美味しい麦酒を飲もう" | janome
美味しい	形容詞,自立,*,*,形容詞・イ段,基本形,美味しい,オイシイ,オイシイ
麦酒	名詞,一般,*,*,*,*,麦酒,ビール,ビール
を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
飲も	動詞,自立,*,*,五段・マ行,未然ウ接続,飲む,ノモ,ノモ
う	助動詞,*,*,*,不変化型,基本形,う,ウ,ウ
```

### 形態素解析の結果

* 「表層形	品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音」の形式

```
美味しい	形容詞,自立,*,*,形容詞・イ段,基本形,美味しい,オイシイ,オイシイ
麦酒	名詞,一般,*,*,*,*,麦酒,ビール,ビール
を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
飲も	動詞,自立,*,*,五段・マ行,未然ウ接続,飲む,ノモ,ノモ
う	助動詞,*,*,*,不変化型,基本形,う,ウ,ウ
```

### プログラムで形態素解析

```{code-block} pycon
(env) $ python
>>> from janome.tokenizer import Tokenizer
>>> t = Tokenizer()
>>> for token in t.tokenize("美味しい麦酒を飲もう"):
...     print(token)
... 
美味しい	形容詞,自立,*,*,形容詞・イ段,基本形,美味しい,オイシイ,オイシイ
麦酒	名詞,一般,*,*,*,*,麦酒,ビール,ビール
を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
飲も	動詞,自立,*,*,五段・マ行,未然ウ接続,飲む,ノモ,ノモ
う	助動詞,*,*,*,不変化型,基本形,う,ウ,ウ
```

### Janomeで分かち書き

* `tokenize()` メソッドで分かち書きモード（`wakati=True`）を指定

```{code-block} pycon
>>> tokens = t.tokenize("美味しい麦酒を飲もう", wakati=True)
>>> tokens
<generator object Tokenizer.__tokenize_stream at 0x10055e9d0>
>>> list(tokens)
['美味しい', '麦酒', 'を', '飲も', 'う']
```

### 読みなど任意の情報を取得

```{code-block} pycon
>>> tokens = list(t.tokenize("飲もう"))
>>> tokens[0].surface  # 表層系
'飲も'
>>> tokens[0].part_of_speech  # 品詞情報
'動詞,自立,*,*'
>>> tokens[0].base_form  # 原形
'飲む'
>>> tokens[0].reading  # 読み
'ノモ'
>>> tokens[0].phonetic  # 発音
'ノモ'
>>> tokens = list(t.tokenize("縮む"))  # 読みと発音が異なる例
>>> tokens[0].reading, tokens[0].phonetic
('チヂム', 'チジム')
```

## Janome でフリガナ

### Janome でフリガナ

```{literalinclude} code/furigana1.py
```

```{revealjs-break}
```

* すべての文字にフリガナが振られている

```bash
(env) $ python furigana1.py "美味しい麦酒を飲もう"
<ruby><rb>美味しい</rb><rt>オイシイ</rt></ruby><ruby><rb>麦酒</rb><rt>ビール</rt></ruby><ruby><rb>を</rb><rt>ヲ</rt></ruby><ruby><rb>飲も</rb><rt>ノモ</rt></ruby><ruby><rb>う</rb><rt>ウ</rt></ruby>
```

![実行結果1](images/result1.png)

### フリガナをひらがなにする

* [jaconv](https://github.com/ikegami-yukino/jaconv)を利用

```bash
(env) $ pip install jaconv
```

```{revealjs-literalinclude} code/furigana2.py
:lines: 1-12
:data-line-numbers: 2, 11
```

```{revealjs-break}
```

* フリガナが **ひらがな** になった

```bash
(env) $ python furigana2.py "美味しい麦酒を飲もう"
<ruby><rb>美味しい</rb><rt>おいしい</rt></ruby><ruby><rb>麦酒</rb><rt>びーる</rt></ruby><ruby><rb>を</rb><rt>を</rt></ruby><ruby><rb>飲も</rb><rt>のも</rt></ruby><ruby><rb>う</rb><rt>う</rt></ruby>
```

![フリガナがひらがなに](images/result2.png)

### 漢字が含まれる場合のみを対象に

* `surface` に **漢字が含まれる** 場合のみ対象
  * 参考: [note.nkmk.me](https://note.nkmk.me/python-re-regex-character-type/)

```{revealjs-literalinclude} code/furigana3.py
:lines: 1, 5-18
:data-line-numbers: 1, 3, 10-14
```

```{revealjs-break}
```

* 「を」「う」のフリガナが消えた

```bash
(env) $ python furigana3.py "美味しい麦酒を飲もう"
<ruby><rb>美味しい</rb><rt>おいしい</rt></ruby><ruby><rb>麦酒</rb><rt>びーる</rt></ruby>を<ruby><rb>飲も</rb><rt>のも</rt></ruby>う
```

![「を」「う」のフリガナが消えた](images/result3.png)

### 送りがなに対応

* 「美味しい」の「美味」にフリガナを振る
* `ruby()` 関数を作成し送りがな処理を追加

```{revealjs-literalinclude} code/furigana4.py
:lines: 7-17
```

```{revealjs-break}
```

* `ruby()` 関数を呼び出すように変更

```{revealjs-literalinclude} code/furigana4.py
:lines: 19-28
:data-line-numbers: 7
```

```{revealjs-break}
```

* 送りがなが処理できるようになった

```bash
(env) $ python furigana4.py "美味しい麦酒を飲もう"
<ruby><rb>美味</rb><rt>おい</rt></ruby>しい<ruby><rb>麦酒</rb><rt>びーる</rt></ruby>を<ruby><rb>飲</rb><rt>の</rt></ruby>もう
```

![送りがなに対応](images/result4.png)

### 辞書をカスタマイズ

## SudachiPyで形態素解析

### SudachiPyとは

### SudachiPyで形態素解析

### SucahiPyで分かち書き

### 送り仮名のさらなる改善

### 辞書をカスタマイズ

### 辞書のコスト調整

### フリガナレベル対応

* [学年別漢字配当表 - Wikipedia](https://ja.wikipedia.org/wiki/%E5%AD%A6%E5%B9%B4%E5%88%A5%E6%BC%A2%E5%AD%97%E9%85%8D%E5%BD%93%E8%A1%A8)
* [別表　学年別漢字配当表：文部科学省](https://www.mext.go.jp/a_menu/shotou/new-cs/youryou/syo/koku/001.htm)

## まとめ
