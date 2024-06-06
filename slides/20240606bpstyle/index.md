```{eval-rst}
:og:image: _images/20240606bpstyle.png
:og:image:alt: MathMLを解釈して数式読み上げ

.. |cover| image:: images/20240606bpstyle.png
```

# **MathML** を解釈して数式読み上げ

Takanori Suzuki

BPStyle #161 / 2024 Jun 6

## 前回のあらすじ

* 某案件で学習教材の電子化をやっている
* **合理的配慮** の一環としてテキスト読み上げを実現したい
* **Amazon Polly** でテキスト読み上げ
* スライド: [Amazon Polly で問題文を読み上げ](https://slides.takanory.net/slides/20240307bpstyle/#/)

## 問題文の中の数式

* どうやっているか説明

### **Mathjax** で数式を描画

* `$$` または `$` で数式を囲む

```
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$

次の式を解きなさい $(5x＋4)(5x＋1)$ 
```

$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$

次の式を解きなさい $(5x＋4)(5x＋1)$ 

### **どんな数式** が書ける？

* LaTeXで書けるのは全部できる(はず)
* 参考: [Easy Copy Mathjax](https://easy-copy-mathjax.nakaken88.com/)

\begin{eqnarray}
\triangle ABC \equiv \triangle DEF
\end{eqnarray}

\begin{eqnarray}
\varliminf_{ n \to \infty } A_n
 = \bigcup_{ n = 1 }^{ \infty } \bigcap_{ k = n }^{ \infty } A_k
 = \bigcup_{ n \in \mathbb{ N } } \bigcap_{ k \geqq n } A_k
\end{eqnarray}

\begin{eqnarray}
\int_0^1 x dx
= \left[ \frac{x^2}{2} \right]_0^1
= \frac{1}{2}
\end{eqnarray}

### **どうやって変換** してる?

* 原稿はMarkdownの中に`$`、`$$`で囲んだ数式
* Markdown変換: [markdown-it](https://github.com/markdown-it/markdown-it)
* Mathjax変換: [markdown-it-mathjax3](https://github.com/tani/markdown-it-mathjax3)
  * markdown-itのプラグイン
  * 内部では[mathjax-full](https://www.npmjs.com/package/mathjax-full)を使用

### ブラウザで数式を **どう表示** している？

$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$

```html
<mjx-container class="MathJax CtxtMenu_Attached_0" jax="SVG" display="true" style="position: relative;" tabindex="0" ctxtmenu_counter="11">
  <svg style="vertical-align: -1.575ex;" xmlns="http://www.w3.org/2000/svg" width="20.765ex" height="5.291ex" role="img" focusable="false" viewBox="0 -1642.5 9178 2338.5" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true">
    <defs>
      <path id="MJX-1-TEX-I-1D465" d="M52 289Q59 331 106 386T222 442Q257 442 286 424T329 379Q371 442 430 442Q467 442 494 420T522 361Q522 332 508 314T481 292T458 288Q439 288 427 299T415 328Q415 374 465 391Q454 404 425 404Q412 404 406 402Q368 386 350 336Q290 115 290 78Q290 50 306 38T341 26Q378 26 414 59T463 140Q466 150 469 151T485 153H489Q504 153 504 145Q504 144 502 134Q486 77 440 33T333 -11Q263 -11 227 52Q186 -10 133 -10H127Q78 -10 57 16T35 71Q35 103 54 123T99 143Q142 143 142 101Q142 81 130 66T107 46T94 41L91 40Q91 39 97 36T113 29T132 26Q168 26 194 71Q203 87 217 139T245 247T261 313Q266 340 266 352Q266 380 251 392T217 404Q177 404 142 372T93 290Q91 281 88 280T72 278H58Q52 284 52 289Z"></path>
      <path id="MJX-1-TEX-N-3D" d="M56 347Q56 360 70 367H707Q722 359 722 347Q722 336 708 328L390 327H72Q56 332 56 347ZM56 153Q56 168 72 173H708Q722 163 722 153Q722 140 707 133H70Q56 140 56 153Z"></path>
      <path id="MJX-1-TEX-N-2212" d="M84 237T84 250T98 270H679Q694 262 694 250T679 230H98Q84 237 84 250Z"></path>
      <path id="MJX-1-TEX-I-1D44F" d="M73 647Q73 657 77 670T89 683Q90 683 161 688T234 694Q246 694 246 685T212 542Q204 508 195 472T180 418L176 399Q176 396 182 402Q231 442 283 442Q345 442 383 396T422 280Q422 169 343 79T173 -11Q123 -11 82 27T40 150V159Q40 180 48 217T97 414Q147 611 147 623T109 637Q104 637 101 637H96Q86 637 83 637T76 640T73 647ZM336 325V331Q336 405 275 405Q258 405 240 397T207 376T181 352T163 330L157 322L136 236Q114 150 114 114Q114 66 138 42Q154 26 178 26Q211 26 245 58Q270 81 285 114T318 219Q336 291 336 325Z"></path><path id="MJX-1-TEX-N-B1" d="M56 320T56 333T70 353H369V502Q369 651 371 655Q376 666 388 666Q402 666 405 654T409 596V500V353H707Q722 345 722 333Q722 320 707 313H409V40H707Q722 32 722 20T707 0H70Q56 7 56 20T70 40H369V313H70Q56 320 56 333Z"></path><path id="MJX-1-TEX-N-221A" d="M95 178Q89 178 81 186T72 200T103 230T169 280T207 309Q209 311 212 311H213Q219 311 227 294T281 177Q300 134 312 108L397 -77Q398 -77 501 136T707 565T814 786Q820 800 834 800Q841 800 846 794T853 782V776L620 293L385 -193Q381 -200 366 -200Q357 -200 354 -197Q352 -195 256 15L160 225L144 214Q129 202 113 190T95 178Z"></path><path id="MJX-1-TEX-N-32" d="M109 429Q82 429 66 447T50 491Q50 562 103 614T235 666Q326 666 387 610T449 465Q449 422 429 383T381 315T301 241Q265 210 201 149L142 93L218 92Q375 92 385 97Q392 99 409 186V189H449V186Q448 183 436 95T421 3V0H50V19V31Q50 38 56 46T86 81Q115 113 136 137Q145 147 170 174T204 211T233 244T261 278T284 308T305 340T320 369T333 401T340 431T343 464Q343 527 309 573T212 619Q179 619 154 602T119 569T109 550Q109 549 114 549Q132 549 151 535T170 489Q170 464 154 447T109 429Z"></path><path id="MJX-1-TEX-N-34" d="M462 0Q444 3 333 3Q217 3 199 0H190V46H221Q241 46 248 46T265 48T279 53T286 61Q287 63 287 115V165H28V211L179 442Q332 674 334 675Q336 677 355 677H373L379 671V211H471V165H379V114Q379 73 379 66T385 54Q393 47 442 46H471V0H462ZM293 211V545L74 212L183 211H293Z"></path><path id="MJX-1-TEX-I-1D44E" d="M33 157Q33 258 109 349T280 441Q331 441 370 392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412 234T374 68Q374 43 381 35T402 26Q411 27 422 35Q443 55 463 131Q469 151 473 152Q475 153 483 153H487Q506 153 506 144Q506 138 501 117T481 63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336 5T306 36L300 51Q299 52 296 50Q294 48 292 46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351 334 346 350T323 385T277 405Q242 405 210 374T160 293Q131 214 119 129Q119 126 119 118T118 106Q118 61 136 44T179 26Q217 26 254 59T298 110Q300 114 325 217T351 328Z"></path><path id="MJX-1-TEX-I-1D450" d="M34 159Q34 268 120 355T306 442Q362 442 394 418T427 355Q427 326 408 306T360 285Q341 285 330 295T319 325T330 359T352 380T366 386H367Q367 388 361 392T340 400T306 404Q276 404 249 390Q228 381 206 359Q162 315 142 235T121 119Q121 73 147 50Q169 26 205 26H209Q321 26 394 111Q403 121 406 121Q410 121 419 112T429 98T420 83T391 55T346 25T282 0T202 -11Q127 -11 81 37T34 159Z"></path></defs><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="scale(1,-1)"><g data-mml-node="math"><g data-mml-node="mi"><use data-c="1D465" xlink:href="#MJX-1-TEX-I-1D465"></use></g><g data-mml-node="mo" transform="translate(849.8,0)"><use data-c="3D" xlink:href="#MJX-1-TEX-N-3D"></use></g><g data-mml-node="TeXAtom" data-mjx-texclass="ORD" transform="translate(1905.6,0)"><g data-mml-node="mfrac"><g data-mml-node="mrow" transform="translate(220,676)"><g data-mml-node="mo"><use data-c="2212" xlink:href="#MJX-1-TEX-N-2212"></use></g><g data-mml-node="mi" transform="translate(778,0)"><use data-c="1D44F" xlink:href="#MJX-1-TEX-I-1D44F"></use></g><g data-mml-node="mo" transform="translate(1429.2,0)"><use data-c="B1" xlink:href="#MJX-1-TEX-N-B1"></use></g><g data-mml-node="msqrt" transform="translate(2429.4,0)"><g transform="translate(853,0)"><g data-mml-node="msup"><g data-mml-node="mi"><use data-c="1D44F" xlink:href="#MJX-1-TEX-I-1D44F"></use></g><g data-mml-node="mn" transform="translate(462,289) scale(0.707)"><use data-c="32" xlink:href="#MJX-1-TEX-N-32"></use></g></g><g data-mml-node="mo" transform="translate(1087.8,0)"><use data-c="2212" xlink:href="#MJX-1-TEX-N-2212"></use></g><g data-mml-node="mn" transform="translate(2088,0)"><use data-c="34" xlink:href="#MJX-1-TEX-N-34"></use></g><g data-mml-node="mi" transform="translate(2588,0)"><use data-c="1D44E" xlink:href="#MJX-1-TEX-I-1D44E"></use></g><g data-mml-node="mi" transform="translate(3117,0)"><use data-c="1D450" xlink:href="#MJX-1-TEX-I-1D450"></use></g></g><g data-mml-node="mo" transform="translate(0,106.5)"><use data-c="221A" xlink:href="#MJX-1-TEX-N-221A"></use></g><rect width="3550" height="60" x="853" y="846.5"></rect></g></g><g data-mml-node="mrow" transform="translate(3121.7,-686)"><g data-mml-node="mn"><use data-c="32" xlink:href="#MJX-1-TEX-N-32"></use></g><g data-mml-node="mi" transform="translate(500,0)"><use data-c="1D44E" xlink:href="#MJX-1-TEX-I-1D44E"></use></g></g><rect width="7032.4" height="60" x="120" y="220"></rect></g></g></g></g>
  :
  </svg>
</mjx-container>
```


### **SVG** じゃん... 😇

## 数式って **読み上げられない** の？ 🤔

### 数式って **読み上げられない** の？ 🤔

* 数式を読み上げられなかったら数学の勉強ができない
* まさか対応してないわけないだろ
* 調べる

### MathJaxに **Accessibility機能** あった！

* [Accessibility Features - Screen Reader Support](https://docs.mathjax.org/en/latest/basic/accessibility.html#screen-reader-support)

  The `assistive-mml` extension embeds visually hidden MathML alongside MathJax's visual rendering while hiding the visual rendering from assistive technology (AT) such as screenreaders.

### どういうこと？

* `assistive-mml`拡張によって視覚的なレンダリングの横に、**隠されたMathML**を埋め込む
* スクリーンリーダーなどはそのMathMLを読む

### **最新のMathJax** で確認

$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}$$

```html
<mjx-container class="MathJax CtxtMenu_Attached_0" jax="SVG" display="true" style="position: relative;" tabindex="0" ctxtmenu_counter="11"><svg style="vertical-align: -1.575ex;" xmlns="http://www.w3.org/2000/svg" width="20.765ex" height="5.291ex" role="img" focusable="false" viewBox="0 -1642.5 9178 2338.5" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true"><defs><path id="MJX-1-TEX-I-1D465" d="M52 289Q59 331 106 386T222 442Q257 442 286 424T329 379Q371 442 430 442Q467 442 494 420T522 361Q522 332 508 314T481 292T458 288Q439 288 427 299T415 328Q415 374 465 391Q454 404 425 404Q412 404 406 402Q368 386 350 336Q290 115 290 78Q290 50 306 38T341 26Q378 26 414 59T463 140Q466 150 469 151T485 153H489Q504 153 504 145Q504 144 502 134Q486 77 440 33T333 -11Q263 -11 227 52Q186 -10 133 -10H127Q78 -10 57 16T35 71Q35 103 54 123T99 143Q142 143 142 101Q142 81 130 66T107 46T94 41L91 40Q91 39 97 36T113 29T132 26Q168 26 194 71Q203 87 217 139T245 247T261 313Q266 340 266 352Q266 380 251 392T217 404Q177 404 142 372T93 290Q91 281 88 280T72 278H58Q52 284 52 289Z"></path><path id="MJX-1-TEX-N-3D" d="M56 347Q56 360 70 367H707Q722 359 722 347Q722 336 708 328L390 327H72Q56 332 56 347ZM56 153Q56 168 72 173H708Q722 163 722 153Q722 140 707 133H70Q56 140 56 153Z"></path><path id="MJX-1-TEX-N-2212" d="M84 237T84 250T98 270H679Q694 262 694 250T679 230H98Q84 237 84 250Z"></path><path id="MJX-1-TEX-I-1D44F" d="M73 647Q73 657 77 670T89 683Q90 683 161 688T234 694Q246 694 246 685T212 542Q204 508 195 472T180 418L176 399Q176 396 182 402Q231 442 283 442Q345 442 383 396T422 280Q422 169 343 79T173 -11Q123 -11 82 27T40 150V159Q40 180 48 217T97 414Q147 611 147 623T109 637Q104 637 101 637H96Q86 637 83 637T76 640T73 647ZM336 325V331Q336 405 275 405Q258 405 240 397T207 376T181 352T163 330L157 322L136 236Q114 150 114 114Q114 66 138 42Q154 26 178 26Q211 26 245 58Q270 81 285 114T318 219Q336 291 336 325Z"></path><path id="MJX-1-TEX-N-B1" d="M56 320T56 333T70 353H369V502Q369 651 371 655Q376 666 388 666Q402 666 405 654T409 596V500V353H707Q722 345 722 333Q722 320 707 313H409V40H707Q722 32 722 20T707 0H70Q56 7 56 20T70 40H369V313H70Q56 320 56 333Z"></path><path id="MJX-1-TEX-N-221A" d="M95 178Q89 178 81 186T72 200T103 230T169 280T207 309Q209 311 212 311H213Q219 311 227 294T281 177Q300 134 312 108L397 -77Q398 -77 501 136T707 565T814 786Q820 800 834 800Q841 800 846 794T853 782V776L620 293L385 -193Q381 -200 366 -200Q357 -200 354 -197Q352 -195 256 15L160 225L144 214Q129 202 113 190T95 178Z"></path><path id="MJX-1-TEX-N-32" d="M109 429Q82 429 66 447T50 491Q50 562 103 614T235 666Q326 666 387 610T449 465Q449 422 429 383T381 315T301 241Q265 210 201 149L142 93L218 92Q375 92 385 97Q392 99 409 186V189H449V186Q448 183 436 95T421 3V0H50V19V31Q50 38 56 46T86 81Q115 113 136 137Q145 147 170 174T204 211T233 244T261 278T284 308T305 340T320 369T333 401T340 431T343 464Q343 527 309 573T212 619Q179 619 154 602T119 569T109 550Q109 549 114 549Q132 549 151 535T170 489Q170 464 154 447T109 429Z"></path><path id="MJX-1-TEX-N-34" d="M462 0Q444 3 333 3Q217 3 199 0H190V46H221Q241 46 248 46T265 48T279 53T286 61Q287 63 287 115V165H28V211L179 442Q332 674 334 675Q336 677 355 677H373L379 671V211H471V165H379V114Q379 73 379 66T385 54Q393 47 442 46H471V0H462ZM293 211V545L74 212L183 211H293Z"></path><path id="MJX-1-TEX-I-1D44E" d="M33 157Q33 258 109 349T280 441Q331 441 370 392Q386 422 416 422Q429 422 439 414T449 394Q449 381 412 234T374 68Q374 43 381 35T402 26Q411 27 422 35Q443 55 463 131Q469 151 473 152Q475 153 483 153H487Q506 153 506 144Q506 138 501 117T481 63T449 13Q436 0 417 -8Q409 -10 393 -10Q359 -10 336 5T306 36L300 51Q299 52 296 50Q294 48 292 46Q233 -10 172 -10Q117 -10 75 30T33 157ZM351 328Q351 334 346 350T323 385T277 405Q242 405 210 374T160 293Q131 214 119 129Q119 126 119 118T118 106Q118 61 136 44T179 26Q217 26 254 59T298 110Q300 114 325 217T351 328Z"></path><path id="MJX-1-TEX-I-1D450" d="M34 159Q34 268 120 355T306 442Q362 442 394 418T427 355Q427 326 408 306T360 285Q341 285 330 295T319 325T330 359T352 380T366 386H367Q367 388 361 392T340 400T306 404Q276 404 249 390Q228 381 206 359Q162 315 142 235T121 119Q121 73 147 50Q169 26 205 26H209Q321 26 394 111Q403 121 406 121Q410 121 419 112T429 98T420 83T391 55T346 25T282 0T202 -11Q127 -11 81 37T34 159Z"></path></defs><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="scale(1,-1)"><g data-mml-node="math"><g data-mml-node="mi"><use data-c="1D465" xlink:href="#MJX-1-TEX-I-1D465"></use></g><g data-mml-node="mo" transform="translate(849.8,0)"><use data-c="3D" xlink:href="#MJX-1-TEX-N-3D"></use></g><g data-mml-node="TeXAtom" data-mjx-texclass="ORD" transform="translate(1905.6,0)"><g data-mml-node="mfrac"><g data-mml-node="mrow" transform="translate(220,676)"><g data-mml-node="mo"><use data-c="2212" xlink:href="#MJX-1-TEX-N-2212"></use></g><g data-mml-node="mi" transform="translate(778,0)"><use data-c="1D44F" xlink:href="#MJX-1-TEX-I-1D44F"></use></g><g data-mml-node="mo" transform="translate(1429.2,0)"><use data-c="B1" xlink:href="#MJX-1-TEX-N-B1"></use></g><g data-mml-node="msqrt" transform="translate(2429.4,0)"><g transform="translate(853,0)"><g data-mml-node="msup"><g data-mml-node="mi"><use data-c="1D44F" xlink:href="#MJX-1-TEX-I-1D44F"></use></g><g data-mml-node="mn" transform="translate(462,289) scale(0.707)"><use data-c="32" xlink:href="#MJX-1-TEX-N-32"></use></g></g><g data-mml-node="mo" transform="translate(1087.8,0)"><use data-c="2212" xlink:href="#MJX-1-TEX-N-2212"></use></g><g data-mml-node="mn" transform="translate(2088,0)"><use data-c="34" xlink:href="#MJX-1-TEX-N-34"></use></g><g data-mml-node="mi" transform="translate(2588,0)"><use data-c="1D44E" xlink:href="#MJX-1-TEX-I-1D44E"></use></g><g data-mml-node="mi" transform="translate(3117,0)"><use data-c="1D450" xlink:href="#MJX-1-TEX-I-1D450"></use></g></g><g data-mml-node="mo" transform="translate(0,106.5)"><use data-c="221A" xlink:href="#MJX-1-TEX-N-221A"></use></g><rect width="3550" height="60" x="853" y="846.5"></rect></g></g><g data-mml-node="mrow" transform="translate(3121.7,-686)"><g data-mml-node="mn"><use data-c="32" xlink:href="#MJX-1-TEX-N-32"></use></g><g data-mml-node="mi" transform="translate(500,0)"><use data-c="1D44E" xlink:href="#MJX-1-TEX-I-1D44E"></use></g></g><rect width="7032.4" height="60" x="120" y="220"></rect></g></g></g></g></svg>
<mjx-assistive-mml unselectable="on" display="block">
  <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
    <mi>x</mi><mo>=</mo>
    <mrow data-mjx-texclass="ORD">
      <mfrac>
        <mrow><mo>−</mo><mi>b</mi><mo>±</mo><msqrt><msup><mi>b</mi><mn>2</mn></msup><mo>−</mo><mn>4</mn><mi>a</mi><mi>c</mi></msqrt></mrow>
        <mrow><mn>2</mn><mi>a</mi></mrow>
      </mfrac>
    </mrow>
  </math>
</mjx-assistive-mml>
</mjx-container>
```

### なんか読めそう！！👍

### **MathML** だけ取り出す

```html
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mi>x</mi><mo>=</mo>  # x =
  <mrow data-mjx-texclass="ORD">
    <mfrac>  # 分数(fraction)
      <mrow>  # 分子
        <mo>−</mo><mi>b</mi><mo>±</mo>  # -b±
        <msqrt>  # ルート(sqrt)
          <msup><mi>b</mi><mn>2</mn></msup>  # b 2乗
          <mo>−</mo><mn>4</mn><mi>a</mi><mi>c</mi>  # -4ac
        </msqrt>
      </mrow>
      <mrow><mn>2</mn><mi>a</mi></mrow>  # 分母
    </mfrac>
  </mrow>
</math>
```

## **MathML** とは 

### **MathML** とは

* 数式を記述するためのマークアップ言語
* [Mathematical Markup Language - Wikipedia](https://ja.wikipedia.org/wiki/Mathematical_Markup_Language)
* [MathML の記述 - MathML | MDN](https://developer.mozilla.org/ja/docs/Web/MathML/Authoring)
* [MathML 要素リファレンス - MathML | MDN](https://developer.mozilla.org/ja/docs/Web/MathML/Element)

### MathMLの **主な要素**

* `<mi>`: 識別子(a, b, x, y等)
* `<mo>`: 演算子(+、-等)
* `<mn>`: 数字
* `<mfrac>`: 分数
* `<msqrt>`: ルート
* `<msup>`、`<msub>`: 上付き、下付き
* `<mover>`: 弧で使用

## **読み上げテキスト** 作成 💪

* MathMLを読み上げられるテキストにする

### **BeautifulSoup 4**で解析

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(text, "html.parser")
for math in soup.find_all("math"):
    # ここで変換処理
```

### **記号の読み** を入れる

```python
# 識別子、演算子と読みの対応表
OPEROTORS = {
    "(": "括弧",
    ")": "括弧閉じ",
    "±": "プラスマイナス",
    "×": "掛ける",
    "÷": "割る",
    :
}

# 識別子、演算子を変換
for mo_mi in math.find_all(["mo", "mi"]):
    if mo_mi.text in OPERATORS:
        mo_mi.replace_with(OPERATORS[mo_mi.text])
```

### **分数** に対応

* 分数は出現順と日本語の語順が逆

```xml
<mfrac><mn>1</mn><mn>2</mn></mfrac>  # 2ぶんの1
```

```python
for mfrac in math.find_all("mfrac"):
    # 直下に2つの要素があるので、逆順にする
    bunshi, bunbo = mfrac.contents
    mfrac.clear()
    mfrac.append(bunbo)
    mfrac.append("ぶんの")
    mfrac.append(bunshi)
```

### `<msup>2</msup>`を **2乗** と読む

```python
for msup in math.find_all("msup"):
    if msup.contents[1].name == "mn":  # 数字か?
        mn = msup.contents[1]
        mn.replace_with(f"{mn.text}乗")
```

### `<msqrt>`を **ルート** と読む

```python
for msqrt in math.find_all("msqrt"):
    msqrt.insert(0, "ルート")
```

### **その他記号** の対応

```python
math_text = math.text
math_text = math_text.replace("//", "平行")
math_text = math_text.replace("∘C", "℃")
math_text = math_text.replace("∘", "度")
```

### **単位** をいい感じに読ませる

* Amazon Pollyは**単位**を読んでくれる
* `英字+単位`は正しく読まれない(例: `acm`)
  * `a cm` と英字が連続して後ろが単位っぽいときはスペースを空ける
  * `1cm` など数字は大丈夫
* `km2` は「平方キロメートル」と読む
  * `単位[23]乗` のときは「乗」を削除する
  
## 成果物のデモ

### そこそこ **いい感じ** に読まれてる 🎉
