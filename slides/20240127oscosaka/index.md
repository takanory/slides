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

### Janomeで形態素解析

```bash
$ python3.11 -m venv env
$ . env/bin/activate
(env) $ pip install janome
Successfully installed janome-0.5.0
```

### Janomeで分かち書き

### Janomeでフリガナを振る

### 送り仮名に対応

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
