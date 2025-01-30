```{eval-rst}
:og:image: _images/20250213stapy.png
:og:image:alt: エラーはともだちこわくないよ

.. |cover| image:: images/20250213stapy.png
```

# **エラー**は**ともだち** こわくないよ

Takanori Suzuki

```{image} images/stapy-logo.png
:alt: Start Python Club logo
:width: 15%
```


みんなのPython勉強会 #112 / 2025 Feb 13

## 今日**はなすこと**

* Pythonのエラーってなに？
* よくあるエラーのパターン
* 例外処理
* おまけ：better error messages

### 今日の**ゴール**

* Pythonのエラーが怖くなくなる
* エラーと仲良くなれる

## Photos 📷 Tweets 🐦 👍

`#stapy` / `@takanory`

### [slides.takanory.net](https://slides.takanory.net/) 💻

![slides.takanory.net](images/slides-takanory-net.png)

## **Who** am I? / お前 **誰よ** 👤

* Takanori Suzuki / 鈴木 たかのり ({fab}`twitter` [@takanory](https://twitter.com/takanory))
* [BeProud](https://www.beproud.jp/) 取締役 / Python Climber
* [PyCon JP Association](https://www.pycon.jp/) 代表理事
* [Python Boot Camp](https://www.pycon.jp/support/bootcamp.html) 講師、[Python mini Hack-a-thon](https://pyhack.connpass.com/) 主催、[Pythonボルダリング部](https://kabepy.connpass.com/) 部長

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

### PyCon JP **Association** 🐍

日本国内のPythonユーザのために、**Pythonの普及及び開発支援**を行うために、継続的にカンファレンス(**PyCon**)を開くことを目的とした **非営利組織**

[`www.pycon.jp`](https://www.pycon.jp)

![pycon jp logo](/assets/images/pyconjp_logo.png)

### PyCon JP **2025**

* {fas}`globe` [`2025.pycon.jp`](https://2025.pycon.jp/)
* 🗓️ 2025年**9月26日(金)-27日(土)**
* ⛩️ [**広島**国際会議場](https://www.pcf.city.hiroshima.jp/icch/)
  * **旅費の支援**も多分あるよ

### **BeProud** Inc. 🏢

* [BeProud](https://www.beproud.jp/): Pythonシステム開発、コンサル
* [connpass](https://connpass.com/): IT勉強会支援プラットフォーム
* [PyQ](https://pyq.jp/): Python独学プラットフォーム
* [TRACERY](https://tracery.jp/): システム開発ドキュメントサービス

![BeProud logos](/assets/images/beproud-logos.png)

## Pythonのエラーってなに {nekochan}`hate-nya`

### エラー好きな人？ {nekochan}`hai`

### Pythonには**2つのエラー**

* 構文エラー（syntax error）
* 例外（exception）
* 参考：[8. エラーと例外 — Python公式ドキュメント](https://docs.python.org/ja/3.13/tutorial/errors.html)

### 構文エラー（syntax error）

* Pythonの**構文**として**正しくない**
* 構文解析時にエラーが発生

```pycon
>>> for i in range(10)
  File "<python-input-1>", line 1
    for i in range(10)
                      ^
SyntaxError: expected ':'
```

### 例外（exception）

* 構文が正しいが**実行時に発生**するエラー

```{code-block} python3
>>> 1 / 0
Traceback (most recent call last):
  File "<python-input-0>", line 1, in <module>
    1 / 0
    ~~^~~
ZeroDivisionError: division by zero
```

## よくあるエラーのパターン

## 例外処理

## おまけ：better error messages

## まとめ  {nekochan}`good`

## お知らせ

* Sphinxドキュメントにネコチャン絵文字を簡単に入れられる拡張[sphinx-nekochan](https://sphinx-nekochan.readthedocs.io/)をリリースしました {nekochan}`banzai`
* 参考：[【2024.08追加】SlackやDiscordで使えるネコチャン絵文字を配布しています♪｜しかまつ(ネコチャン絵文字職人)](https://note.com/shikamatsu/n/nd217dc0617db)

## Thank You {nekochan}`pray`

{fas}`desktop` [slides.takanory.net](https://slides.takanory.net/)

{fab}`twitter` [takanory](https://twitter.com/takanory)
{fab}`github` [takanory](https://github.com/takanory/)
{fab}`linkedin` [takanory](https://www.linkedin.com/in/takanory/)
{fab}`untappd` [takanory](https://untappd.com/user/takanory/)

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

