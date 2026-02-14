```{eval-rst}
:og:image: _images/20260219startpython.png
:og:image:alt: ネコチャン絵文字をドキュメント**に入れよう！

.. |cover| image:: images/20260219startpython.png
```

#  🐱**絵文字**を**ドキュメント**に入れよう！

Takanori Suzuki

```{image} images/startpython-logo.png
:alt: Start Python Club logo
:width: 15%
```

みんなのPython勉強会#120 / 2026 Feb 19

## **Who** am I? / お前 **誰よ** 👤

* Takanori Suzuki / 鈴木 たかのり ({fab}`twitter` [@takanory](https://twitter.com/takanory))
* [BeProud](https://www.beproud.jp/) 取締役 / Python Climber
* [PyCon JP Association](https://www.pycon.jp/) 代表理事
* [Python Boot Camp](https://www.pycon.jp/support/bootcamp.html) 講師、[Python mini Hack-a-thon](https://pyhack.connpass.com/) 主催、[Pythonボルダリング部](https://kabepy.connpass.com/) 部長

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

### PyCon JP 2026**共同座長** [^chairs] 🪑🪑

* {fas}`globe` [`2026.pyconjp`](https://2026.pycon.jp/)
* 日程：2026年8月21日（金）〜23日（日）
* 会場：[広島国際会議場](https://www.pcf.city.hiroshima.jp/icch/)
* 共同座長：佐野浩士、鈴木たかのり

```{image} /20251108tokai/images/pyconjp2026-chairs.png
:width: 40%
```

[^chairs]: [PyCon JP Blog: PyCon JP 2026 座長発表](https://pyconjp.blogspot.com/2025/10/pyconjp2026-co-chairs.html)

### 主催メンバー**募集中**！！ 🙌

* **企画の具体化**を一緒に進める方大歓迎
* PyCon JP 2026主催メンバー申込フォーム [^form]

![](/20251108tokai/images/pyconjp2026-form-qr.png)

[^form]: <https://forms.gle/of8NjqkPmUaF8HGR7>

## **ネコ**は好きですか？ 🐱

Do you like **Cats** 🐱?

### **プログラマー**の多くは**ネコ好き**<br />🧑‍💻 👩‍💻 ❤️ 🐱

IMO, Many **Programmers** like **Cats**

（個人の意見です）

### 例 / For example

![LGTMeow](images/lgtmeow.png) [^lgtmeow]

[^lgtmeow]: <https://lgtmeow.com/>

### 私も**猫が好き** 🐈

I **like cats** too

### **フェレット**がもっと好き！ 😍

But I like **Ferrets** even more!

```{image} /20251108tokai/images/fchan.jpg
:alt: f-chan
:width: 32%
```

```{image} /20251108tokai/images/nia-and-seven.jpg
:alt: nia-chan and seven-chan
:width: 32%
```

```{image} /20251108tokai/images/seven.jpg
:alt: seven-chan
:width: 32%
```

## **ネコチャン絵文字**について 🐱

About **Cat Emojis**

### **Slack**と**Discord**用ネコチャン絵文字 🐈‍⬛

Cat Emojis for **Slack** & **Discord**

* **しかまつ**([@shi_ka_ma_tsu](https://x.com/shi_ka_ma_tsu))さんが**作成**、**配布**

```{image} https://assets.st-note.com/production/uploads/images/111036040/rectangle_large_type_2_8d02bf693e68eb6eefb92eb427a577d2.png?width=2000&height=2000&fit=bounds&quality=85
:width: 80%
```

```{revealjs-break}
```

* 会社やコミュニティのSlackで**毎日使って**いる
* I **use** it **every day** in company / community Slack

```{image} /20251108tokai/images/nekochan-react1.png
:width: 48%
```

```{image} /20251108tokai/images/nekochan-react2.png
:width: 30%
```

```{revealjs-break}
```

* ネコチャン絵文字を**ダウンロード**できます！
* [note.com/shikamatsu/n/nd217dc0617db](https://note.com/shikamatsu/n/nd217dc0617db) [^guide]

```{image} /20251108tokai/images/download-nekochan-emojis.png
:alt: Download Nekochan emojis
:width: 50%
```

[^guide]: [ネコチャン絵文字の利用に関するおやくそくなど｜しかまつ(ネコチャン絵文字職人)](https://note.com/shikamatsu/n/n8818bb5ebea1#8b38f78f-1883-46c6-a596-63d9bf4c69da)

## **ドキュメント**に<br />ネコチャン絵文字 🐱 📄

Cat Emojis in **Documents**

### モチベーション / Motivation

* **スライド**でネコチャン絵文字を使用したい
* 絵文字画像を**Copy & Paste**すれば可能

```{image} /20251108tokai/images/emoji-copy-paste.gif
:alt: Copy and Paste Cat Emoji
:width: 75%
```

### プログラマーは**怠惰** 🥱<br />Programmer is **Lazy**

絵文字をたくさんCopy & Pasteするのは**退屈**

Copy & Paste lots of Emojis is **Boring**

### 私たちには**Python**がある {fab}`python`<br />We have **Python**

退屈なことはPythonで**簡単に**しよう

**Simplify** the Boring Stuff with Python

## **sphinx-nekochan** 🔧

### **sphinx-nekochan** 🔧

* ドキュメントに**ネコチャン絵文字**を追加する**Sphinx拡張**
* **Sphinx extension** for adding **Cat emoji** to docs
* {fas}`globe` [sphinx-nekochan.readthedocs.io](https://sphinx-nekochan.readthedocs.io/)

```{image} images/sphinx-nekochan-web.png
:alt: sphinx-nekochan web page
:width: 60%
```

### Sphinx 👁️‍🗨️

* {fas}`globe` [www.sphinx-doc.org](https://www.sphinx-doc.org/)
* きれいなドキュメントが簡単に作成できる
* [docs.python.org](https://docs.python.org/3/)はSphinxを使っている

```{image} /20251108tokai/images/docs-python-org.png
:alt: docs.python.org
:width: 60%
```

### やってみよう / Get Started 👈 

```bash
$ pip install sphinx-nekochan  # sphinxもインストールされる
$ sphinx-quickstart  # ベースファイルを生成
```

* **conf.py**に拡張を追加

```{code-block} python
extensions = [
    ...
    "sphinx_nekochan",
]
```

```{revealjs-break}
```

* ドキュメントで **`nekochan`** ロールを使用

````{tab-set-code}
```markdown
I love {nekochan}`beer`
```

```rst
I love :nekochan:`beer`
```
````

* HTMLドキュメントを**ビルド**

```bash
$ make html
$ open build/html/index.html  # HTMLファイルを開く
```

```{revealjs-break}
```

* ネコチャン絵文字が**表示された**！！ 🎉
* Cat Emoji **displayed** in the document!! 🎉

```{image} /20251108tokai/images/sphinx-nekochan-sample.png
:alt: sphinx-nekochan sample document
:width: 100%
```

### ネコチャン絵文字の**名前**を**探す** 🔎

* [List of Nekochan emoji](https://sphinx-nekochan.readthedocs.io/nekochan_emojis.html)
* [List of Nekochan emoji without text](https://sphinx-nekochan.readthedocs.io/nekochan_emojis_without_text.html)

```{image} https://sphinx-nekochan.readthedocs.io/_images/nekochan-search.gif
:width: 70%
```

## **スライド**でsphinx-nekochan 💻

sphinx-nekochan on **slides**

### sphinx-revealjs 💻

* {fas}`globe` [sphinx-revealjs.readthedocs.io](https://sphinx-revealjs.readthedocs.io/)
* [Reveal.js](https://revealjs.com/)スライドを生成するSphinx拡張

<iframe height="400" src="https://attakei.github.io/sphinx-revealjs/en/index.html" title="Introduction of sphinx-revealjs" width="600"></iframe>

### sphinx-revealjsでsphinx-nekochan

* **同じコード**でネコチャン絵文字が表示
* **Same code** will display Cat Emoji

````{tab-set-code}
```markdown
I love {nekochan}`beer`
```

```rst
I love :nekochan:`beer`
```
````

I love {nekochan}`beer`

## 絵文字を**カスタマイズ** {nekochan}`work`

**Customize** emoji

### 絵文字の**大きさ**を変更 {nekochan}`nobita` [^height]

````{tab-set-code}
```markdown
* 大きいクマー {nekochan}`bear;1.5em` 普通クマー {nekochan}`bear`
* 巨大ダパーネコチャン {nekochan}`dapaa;100px`
```

```rst
* 大きいクマー :nekochan:`bear;1.5em` 普通クマー :nekochan:`bear`
* 巨大ダパーネコチャン :nekochan:`dapaa;100px`
```
````

* 大きいクマー {nekochan}`bear;1.5em` 普通クマー {nekochan}`bear`
* 巨大ダパーネコチャン {nekochan}`dapaa;100px`

[^height]: <https://sphinx-nekochan.readthedocs.io/#customize-emoji-height-and-alt-text>

### 絵文字を**回転** {nekochan}`sushi` [^transform]

````{tab-set-code}
```markdown
* {nekochan}`skip` 90度回転 {nekochan}`skip;;;rotate-90`
* {nekochan}`yoshi` 左右反転 {nekochan}`yoshi;;;flip-horizontal`
```

```rst
* :nekochan:`skip` 90度回転 :nekochan:`skip;;;rotate-90`
* :nekochan:`yoshi` 左右反転 :nekochan:`yoshi;;;flip-horizontal`
```
````

* {nekochan}`skip` 90度回転 {nekochan}`skip;;;rotate-90`
* {nekochan}`yoshi` 左右反転 {nekochan}`yoshi;;;flip-horizontal`

[^transform]: <https://sphinx-nekochan.readthedocs.io/#transform-emoji>

### **大きさ変更**、**Alt指定**、**回転**

````{tab-set-code}
```markdown
{nekochan}`mou-dounidemo-nare;256px;もうどうにでもな～れ;rotate-180`
```

```rst
:nekochan:`mou-dounidemo-nare;256px;もうどうにでもな～れ;rotate-180`
```
````

{nekochan}`mou-dounidemo-nare;256px;もうどうにでもな～れ;rotate-180`

## **Enjoy** sphinx-nekochan {nekochan}`yatta`

* {nekochan}`work` [sphinx-nekochan.readthedocs.io](https://sphinx-nekochan.readthedocs.io)
* {nekochan}`octpus` [takanory/sphinx-nekochan](https://github.com/takanory/sphinx-nekochan)
  * 気に入ったら**GitHub star**してね！ {nekochan}`kitai`
* {nekochan}`snake` [pypi.org/project/sphinx-nekochan](https://pypi.org/project/sphinx-nekochan/)

```{revealjs-break}
:notitle:
```

{nekochan}`akeome-nya`
{nekochan}`ame-nya`
{nekochan}`amefoot-nya`
{nekochan}`angel-nya`
{nekochan}`ari-nya`
{nekochan}`asa-nya`
{nekochan}`ase-nya`
{nekochan}`atama-paan-nya`
{nekochan}`atsui-nya`
{nekochan}`autumn-nya`
{nekochan}`azarashi-nya`
{nekochan}`badminton-nya`
{nekochan}`bakushou-nya`
{nekochan}`banban-nya`
{nekochan}`banya-nya`
{nekochan}`banzai-nya`
{nekochan}`barista-nya`
{nekochan}`barrier-nya`
{nekochan}`basketball-nya`
{nekochan}`beam-nya`
{nekochan}`beer-nya`
{nekochan}`big-love-nya`
{nekochan}`bikkuri-chicken-nya`
{nekochan}`bikkuri-nya`
{nekochan}`book-mark-nya`
{nekochan}`bow-nya`
{nekochan}`bow-nya2`
{nekochan}`buriburiburiburi-muchaburi-nya`
{nekochan}`buta-nya`
{nekochan}`buttobu-nya`
{nekochan}`byebye-nya`
{nekochan}`calendar-nya`
{nekochan}`camera-nya`
{nekochan}`cat-rareta-nya`
{nekochan}`chira-nya`
{nekochan}`choo-choo-train-nya`
{nekochan}`chudoon-nya`
{nekochan}`clap-nya`
{nekochan}`clarinet-nya`
{nekochan}`css-kanzen-ni-rikai-sita-nya`
{nekochan}`dai-kansha-nya`
{nekochan}`daijoubu-nya`
{nekochan}`dancing-nya`
{nekochan}`dapaa-nya`
{nekochan}`darudarudarudaru-darumesian-nya`
{nekochan}`densha-nya`
{nekochan}`docchidemo-ii-nya`
{nekochan}`donburako-nya`
{nekochan}`done-nya`
{nekochan}`donmai-nya`
{nekochan}`doron-nya`
{nekochan}`doya-nya`
{nekochan}`drum-nya`
{nekochan}`eiei-o-nya`
{nekochan}`fire-nya`
{nekochan}`flute-nya`
{nekochan}`freeze-nya`
{nekochan}`fukurou-nya`
{nekochan}`gattai-nya`
{nekochan}`gerokowa-nya`
{nekochan}`gessori-nya`
{nekochan}`gohan-nya`
{nekochan}`gohan-taberu-nya`
{nekochan}`good-nya`
{nekochan}`goron-goron-nya`
{nekochan}`gorua-nya`
{nekochan}`gugigi-nya`
{nekochan}`guiter-nya`
{nekochan}`guruguru-nya`
{nekochan}`ha-nya`
{nekochan}`hachi-nya`
{nekochan}`hai-nya`
{nekochan}`haniwa-nya`
{nekochan}`haniwa-nya-noroi`
{nekochan}`haniwa-nya-purupuru`
{nekochan}`haniwa-nya-shousei`
{nekochan}`haniwa-nya-shutudo`
{nekochan}`haniwa-nya-spin`
{nekochan}`haniwa-nya-yatta`
{nekochan}`hansei-nya`
{nekochan}`hare-nya`
{nekochan}`hate-hate-nya`
{nekochan}`hate-nya`
{nekochan}`hebi-nya`
{nekochan}`help-nya`
{nekochan}`hige-nya`
{nekochan}`hirameita-nya`
{nekochan}`hituji-nya`
{nekochan}`hiza-ni-ya-wo-ukete-simatte-nya`
{nekochan}`ho-nya`
{nekochan}`hokkori-nya`
{nekochan}`holiday-nya2`
{nekochan}`holiday-nya3`
{nekochan}`hospital-nya`
{nekochan}`hotcake-nya`
{nekochan}`hueta-nya`
{nekochan}`hug-nya`
{nekochan}`huhuhu-nya`
{nekochan}`hyoui-nya`
{nekochan}`hyun-nya`
{nekochan}`ie-nya`
{nekochan}`ika-nya`
{nekochan}`inai-nya`
{nekochan}`inosisi-nya`
{nekochan}`inu-nya`
{nekochan}`isogu-nya`
{nekochan}`issue-mada-nai-nya`
{nekochan}`itabasami-nya`
{nekochan}`itadakimasu-nya`
{nekochan}`itsumo-sumanai-nya`
{nekochan}`ittari-kitari-nya`
{nekochan}`iwa-nyai-nya`
{nekochan}`ji-nya`
{nekochan}`jii-nya2`
{nekochan}`jikan-nya`
{nekochan}`jiken-nya`
{nekochan}`jinrou-nya`
{nekochan}`jito-nya`
{nekochan}`juutai-nya`
{nekochan}`kahun-nya`
{nekochan}`kaisan-nya`
{nekochan}`kami-nya`
{nekochan}`kaminari-nya`
{nekochan}`kamo-nya`
{nekochan}`kamon-nya`
{nekochan}`karai-nya`
{nekochan}`kata-koru-nya`
{nekochan}`kaze-tuyoi-nya`
{nekochan}`kenkou-shindan-nya`
{nekochan}`kick-nya`
{nekochan}`kika-nyai-nya`
{nekochan}`kiku-nya`
{nekochan}`kiriri-nya`
{nekochan}`kitaeru-nya`
{nekochan}`kitai-nya`
{nekochan}`kitakitakitakita-kitakitsune-nya`
{nekochan}`kito-nya`
{nekochan}`kochira-nya`
{nekochan}`komata-nya`
{nekochan}`kosame-nya`
{nekochan}`kossori-nya`
{nekochan}`kouji-nya`
{nekochan}`kuchibue-nya`
{nekochan}`kuhuhu-nya`
{nekochan}`kuma-nya`
{nekochan}`kumori-nya`
{nekochan}`kuro-bow-nya`
{nekochan}`kuro-juutai-nya`
{nekochan}`kuro_ng`
{nekochan}`kuro_ok`
{nekochan}`kusa-nya`
{nekochan}`kushami-nya`

## Thank you {nekochan}`pray`

{fas}`desktop` [slides.takanory.net](https://slides.takanory.net/)

{fas}`globe` [sphinx-nekochan.readthedocs.io](https://sphinx-nekochan.readthedocs.io/)

{fab}`twitter` [takanory](https://twitter.com/takanory)
{fab}`github` [takanory](https://github.com/takanory/)
{fab}`linkedin` [takanory](https://www.linkedin.com/in/takanory/)
{fab}`untappd` [takanory](https://untappd.com/user/takanory/)

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

