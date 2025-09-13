```{eval-rst}
:og:image: _images/20250920pyconcn-lt.png
:og:image:alt: Put 🐱 Cat Emojis in your Documents!

.. |cover| image:: images/20250920pyconcn-lt.png
```

# Put 🐱 Cat Emojis in your Documents!
```{revealjs-section}
:data-background-image: images/pyconchina-background1.png
```

Takanori Suzuki

PyCon China 2025 / 2025 Sep 20

## Do you **like cats**? 🐱
```{revealjs-section}
:data-background-image: images/pyconchina-background2.png
```

### IMO, **Many programmers** like Cats <br /> 🧑‍💻 👩‍💻 ❤️ 🐱

### For example

![cat programmer](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjU3OHZhZnVqdTAwZ2RwYTMxZWdpZmt0YWxxb2ZxNm8xeTFrMDB5ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/heIX5HfWgEYlW/giphy.gif) [^cat-programmer]

[^cat-programmer]: <https://giphy.com/gifs/cat-laptop-document-heIX5HfWgEYlW>

### I **like cats** too 🐈

### But I like **Ferrets** even more! 😍

```{image} images/fchan.jpg
:alt: f-chan
:width: 32%
```

```{image} images/nia-and-seven.jpg
:alt: nia-chan and seven-chan
:width: 32%
```

```{image} images/seven.jpg
:alt: seven-chan
:width: 32%
```

## About **Cat Emojis** 🐱
```{revealjs-section}
:data-background-image: images/pyconchina-background2.png
```

### Cat Emojis for **Slack** & **Discord** 💬

* Cat Emojis are **Created** and **Distributed** by **Shikamatsu-san**([@shi_ka_ma_tsu](https://x.com/shi_ka_ma_tsu))

```{image} https://assets.st-note.com/production/uploads/images/111036040/rectangle_large_type_2_8d02bf693e68eb6eefb92eb427a577d2.png?width=2000&height=2000&fit=bounds&quality=85
:width: 60%
```

```{revealjs-break}
```

* I **use** it **every day** in company / community Slack

```{image} images/nekochan-react1.png
:width: 48%
```

```{image} images/nekochan-react2.png
:width: 30%
```

```{revealjs-break}
```

* You **can download** Cat Emojis!!
* [note.com/shikamatsu/n/nd217dc0617db](https://note.com/shikamatsu/n/nd217dc0617db) [^guide]

```{image} images/download-nekochan-emojis.png
:alt: Download Nekochan emojis
:width: 60%
```

[^guide]: [Guidelines for Using Cat Emojis](https://note.com/shikamatsu/n/n8818bb5ebea1#8b38f78f-1883-46c6-a596-63d9bf4c69da)

## Cat Emojis in **Documents** 🐱 📄
```{revealjs-section}
:data-background-image: images/pyconchina-background2.png
```

### Motivation 💪

* Use Cat Emojis on **My Slides**
* Can do it by **Copy & Paste** Emoji image

```{image} images/emoji-copy-paste.gif
:alt: Copy and Paste Cat Emoji
:width: 75%
```

### **Programmer is Lazy** 🫠

Copy & Paste lots of Emojis is **Boring**

### We have **Python** {fab}`python`

**Simplify** the Boring Stuff with Python

## **sphinx-nekochan** 🔧
```{revealjs-section}
:data-background-image: images/pyconchina-background2.png
```

("Nekochan" is Cat in Japanese)

### **sphinx-nekochan** 🔧

* **Sphinx extension** for adding **Cat emoji** to docs
* {fas}`globe` [sphinx-nekochan.readthedocs.io](https://sphinx-nekochan.readthedocs.io/)

```{image} images/sphinx-nekochan-web.png
:alt: sphinx-nekochan web page
:width: 60%
```

### Sphinx 👁️‍🗨️

* {fas}`globe` [www.sphinx-doc.org](https://www.sphinx-doc.org/)
* Easy to create intelligent and beautiful docs
* [docs.python.org](https://docs.python.org/3/) using Sphinx

```{image} images/docs-python-org.png
:alt: docs.python.org
:width: 50%
```

### Get Started 🏃

```bash
# sphinx is also install
(env) % pip install sphinx-nekochan
# generates Sphinx base files
(env) % sphinx-quickstart
```

* add `sphinx_nekochan` extension in **conf.py**

```{code-block} python
extensions = [
    ...
    "sphinx_nekochan",
]
```

```{revealjs-break}
```

* Use **`nekochan`** role in the document

````{tab-set-code}
```markdown
I love {nekochan}`beer`
```

```rst
I love :nekochan:`beer`
```
````

* **Build** html documents

```bash
(env) % make html
(env) % open build/html/index.html
```

```{revealjs-break}
```

* Cat Emoji **displayed** in the document!! 🎉

```{image} images/sphinx-nekochan-sample.png
:alt: sphinx-nekochan sample document
:width: 130%
```

### **Find** the **Name** of Cat Emoji 🔎

* [List of Nekochan emoji](https://sphinx-nekochan.readthedocs.io/nekochan_emojis.html)
* [List of Nekochan emoji without text](https://sphinx-nekochan.readthedocs.io/nekochan_emojis_without_text.html)

```{image} https://sphinx-nekochan.readthedocs.io/_images/nekochan-search.gif
:width: 70%
```

## sphinx-nekochan on **slides** 💻
```{revealjs-section}
:data-background-image: images/pyconchina-background2.png
```

### sphinx-revealjs 

* {fas}`globe` [sphinx-revealjs.readthedocs.io](https://sphinx-revealjs.readthedocs.io/)
* Sphinx extension to generate [Reveal.js](https://revealjs.com/) slides

<iframe height="400" src="https://attakei.github.io/sphinx-revealjs/en/index.html" title="Introduction of sphinx-revealjs" width="600"></iframe>

### sphinx-revealjs with sphinx-nekochan

* **Same code** will display Cat Emoji in slides

````{tab-set-code}
```markdown
* I love {nekochan}`beer
* I want to see {nekochan}`panda`
```

```rst
* I love :nekochan:`beer`
* I want to see :nekochan:`panda`
```
````

* I love {nekochan}`beer`
* I want to see {nekochan}`panda`

## **Customize** emoji {nekochan}`memo`
```{revealjs-section}
:data-background-image: images/pyconchina-background2.png
```

### Customize emoji **Height** {nekochan}`nobita` [^height]

````{tab-set-code}
```markdown
* Big bear {nekochan}`bear;1.5em` default {nekochan}`bear`
* Huge hot-sprint nekochan {nekochan}`hot-spring;100px`
```

```rst
* Big bear :nekochan:`bear;1.5em` default :nekochan:`bear`
* Huge hot-sprint nekochan :nekochan:`hot-spring;100px`
```
````

* Big bear {nekochan}`bear;1.5em` default {nekochan}`bear`
* Huge hot-sprint nekochan {nekochan}`hot-spring;100px`

[^height]: <https://sphinx-nekochan.readthedocs.io/#customize-emoji-height-and-alt-text>

### **Transform** emoji {nekochan}`goron-goron` [^transform]

````{tab-set-code}
```markdown
* {nekochan}`skip` rotate {nekochan}`skip;;;rotate-90`
* {nekochan}`yoshi` flip horizontal
{nekochan}`yoshi;;;flip-horizontal`
```

```rst
* :nekochan:`skip` rotate :nekochan:`skip;;;rotate-90`
* :nekochan:`yoshi` flip horizontal
:nekochan:`yoshi;;;flip-horizontal`
```
````

* {nekochan}`skip` rotate {nekochan}`skip;;;rotate-90`
* {nekochan}`yoshi` flip horizontal
{nekochan}`yoshi;;;flip-horizontal`

[^transform]: <https://sphinx-nekochan.readthedocs.io/#transform-emoji>

## **Enjoy** sphinx-nekochan {nekochan}`yatta`
```{revealjs-section}
:data-background-image: images/pyconchina-background2.png
```

* {nekochan}`work` [sphinx-nekochan.readthedocs.io](https://sphinx-nekochan.readthedocs.io)
* {nekochan}`octpus` [takanory/sphinx-nekochan](https://github.com/takanory/sphinx-nekochan)
  * Please **GitHub star** if you like it! {nekochan}`kitai`
* {nekochan}`snake` [pypi.org/project/sphinx-nekochan](https://pypi.org/project/sphinx-nekochan/)

```{revealjs-break}
:notitle:
```

{nekochan}`akeome-nya`
{nekochan}`ame-nya`
{nekochan}`amefoot-nya`
{nekochan}`angel-nya`
{nekochan}`ase-nya`
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
{nekochan}`benkyou`
{nekochan}`big-love-nya`
{nekochan}`bikkuri-nya`
{nekochan}`bow-nya`
{nekochan}`bow-nya2`
{nekochan}`buriburiburiburi-muchaburi-nya`
{nekochan}`buttobu-nya`
{nekochan}`byebye-nya`
{nekochan}`calendar-nya`
{nekochan}`camera-nya`
{nekochan}`cat-rareta-nya`
{nekochan}`chira-nya`
{nekochan}`choo-choo-train-nya`
{nekochan}`chudoon-nya`
{nekochan}`clap-nya`
{nekochan}`css-kanzen-ni-rikai-sita-nya`
{nekochan}`dai-kansha-nya`
{nekochan}`daijoubu-nya`
{nekochan}`dancing-nya`
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
{nekochan}`freeze-nya`
{nekochan}`gattai-nya`
{nekochan}`gerokowa-nya`
{nekochan}`gessori-nya`
{nekochan}`gohan-nya`
{nekochan}`gohan-taberu-nya`
{nekochan}`good-nya`
{nekochan}`goron-goron-nya`
{nekochan}`gorua-nya`
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
{nekochan}`itsumo-sumanai-nya`
{nekochan}`ittari-kitari-nya`
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
{nekochan}`kamon-nya`
{nekochan}`karai-nya`
{nekochan}`kata-koru-nya`
{nekochan}`kaze-tuyoi-nya`
{nekochan}`kenkou-shindan-nya`
{nekochan}`kick-nya`
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
{nekochan}`kuma-nya`
{nekochan}`kuro-bow-nya`
{nekochan}`kuro-juutai-nya`
{nekochan}`kuro_ng`
{nekochan}`kuro_ok`
{nekochan}`kusa-nya`
{nekochan}`kyapi-nya`
{nekochan}`kyomu-nya`
{nekochan}`kyomu-nya2`
{nekochan}`kyun-desu-nya`
{nekochan}`lgtm-nya`
{nekochan}`lion-nya`
{nekochan}`love-nya`
{nekochan}`maccho-nya`
{nekochan}`mada-nya`
{nekochan}`magic-nya`
{nekochan}`maguro-no-osushi-nya`
{nekochan}`mail-nya`
{nekochan}`manpuku-nya`
{nekochan}`mask-nya`
{nekochan}`massage-nya`
{nekochan}`maturi-nya`
{nekochan}`mawaru-nya`
{nekochan}`mechanaki-nya`
{nekochan}`medetai-nya`
{nekochan}`melty-nya`

## Thank you {nekochan}`pray`
```{revealjs-section}
:data-background-image: images/pyconchina-background1.png
```

{fas}`desktop` [slides.takanory.net](https://slides.takanory.net/)

{fas}`globe` [sphinx-nekochan.readthedocs.io](https://sphinx-nekochan.readthedocs.io/)

{fab}`twitter` [takanory](https://twitter.com/takanory)
{fab}`github` [takanory](https://github.com/takanory/)
{fab}`linkedin` [takanory](https://www.linkedin.com/in/takanory/)
{fab}`untappd` [takanory](https://untappd.com/user/takanory/)

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

