```{eval-rst}
:og:image: _images/20241211apacreport.png
:og:image:alt: 現地セッションの傾向 Web技術編

.. |cover| image:: images/20241211apacreport.png
```

# 現地セッションの<br />傾向: **Web技術**編 🕸️

Takanori Suzuki

```{image} images/pyconapac2024.png
:width: 100
```

PyCon APAC 2024 参加報告会 / 2024 Dec 11

## 今日話すこと、ゴール 💡

* PyCon APAC 2024の**Web技術系**トーク紹介
* ワンチャン **自分いけんじゃね？** と思う
* 海外PyConに**Proposal出したくなる**

## Photos 📷 Tweets 🐦 👍

`@takanory`

### {fas}`globe` [`slides.takanory.net`](https://slides.takanory.net/)

![slides.takanory.net](images/slides-takanory-net.png)

## **Who** am I? / お前**誰よ** 👤

* Takanori Suzuki / 鈴木 たかのり ({fab}`twitter` [@takanory](https://twitter.com/takanory))
* [PyCon JP Association](https://www.pycon.jp/) 代表理事
* [BeProud](https://www.beproud.jp/) 取締役 / Python Climber
* [Python Boot Camp](https://www.pycon.jp/support/bootcamp.html) 講師、[Python mini Hack-a-thon](https://pyhack.connpass.com/) 主催、[Pythonボルダリング部](https://kabepy.connpass.com/) 部長

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)

## 現地セッションの傾向: <br />**Web技術**編 🕸️

### [2024-apac.pycon.id/schedule](https://2024-apac.pycon.id/schedule)

```{image} images/schedule.png
:width: 90%
```

### **Webっぽい**タイトルを抜き出してみる

* Optimizing **Web** Presence: Building an SEO Analyzer with **Flask** & NLP-ID / Alysia Alfi
* Streamlining Full-Stack Development: Building OpenAPI-Powered APIs with **FastAPI** and Integrating with Next.js Using TypeScript and React Query / Ryan Elian
* Database replication with **Django** and Postgres / Marcin Gębala

```{revealjs-break}
```

* **FastAPI** Deconstructed: Anatomy of a Modern **ASGI** Framework / Rafiqul Hasan
* Practical **GraphQL** Server Development with **FastAPI** and **Strawberry** / Takayuki Kawazoe
* Supercharge Your Python **Web App** Security Using Logto.io as Your Authentication Service / Rizqon Sadida

```{revealjs-break}
```

* **Structlog** in Practice / Takayuki Shimizukawa
* **GraphQL** in Python / Marcin Gębala
* Pythonic Ways to Build **Serverless** Apps in AWS and how to migrate from Frameworks / Arnel Jan Sarmiento / Arnel Jan Sarmiento

## 9 / 72本 = **12.5%**

### Optimizing **Web** Presence: Building an SEO Analyzer with **Flask** & NLP-ID

* {fab}`github` [alysialfi/pycon-seo-optimizer](https://github.com/alysialfi/pycon-seo-optimizer)
* WebサイトのSEO分析をするためのツールをFlaskと[NLP-ID](https://github.com/kumparan/nlp-id)（インドネシア語のNLP）で作った話
* Googleのページランクと、Webサイトのキーワードを出してくれるらしい


### Streamlining Full-Stack Development: Building OpenAPI-Powered APIs with **FastAPI** and Integrating with Next.js Using TypeScript and React Query

* {fab}`github` [ryanelian/pycon-apac-2024](https://github.com/ryanelian/pycon-apac-2024)
* スライド: [pycon-apac-2024/PyCon APAC 2024.pdf](https://github.com/ryanelian/pycon-apac-2024/blob/main/PyCon%20APAC%202024.pdf)
* FastAPIとNext.jsのプロジェクトを作成し、OpenAPIを使っていい感じに連携するという話

### Database replication with **Django** and Postgres

* スライド: [Database replication with Django and Postgres](https://speakerdeck.com/maarcingebala/database-replication-with-django-and-postgres)
* PostgreSQLでDBのレプリカ作成して、DjangoでDB route使って複数DBを切り替えて使う話

### **FastAPI** Deconstructed: Anatomy of a Modern **ASGI** Framework

* スライド: [FastAPI Deconstructed - Anatomy of a Modern ASGI Framework.pdf](https://github.com/shopnilsazal/fastapi-deconstructed/blob/main/FastAPI%20Deconstructed%20-%20Anatomy%20of%20a%20Modern%20ASGI%20Framework.pdf)
* FastAPIの構成要素としてASGI、Uvicorn、Starlette、Pydantic、Depends、OpenAPIのそれぞれについて解説する話

### Practical **GraphQL** Server Development with **FastAPI** and **Strawberry**

* {fab}`github`: [zoetaka38/poc-fastapi-strawberry-api](https://github.com/zoetaka38/poc-fastapi-strawberry-api)
* 参考: [FastAPI と Strawberry で作る GraphQL Server ~SQLAlchemy を添えて~ #Python - Qiita](https://qiita.com/zoetaka38/items/a4c269d316009a66c3af)
* FastAPIと[Strawberry](https://strawberry.rocks/)を組み合わせてGraphQLサーバーを作成する話
  * REST APIも併用している
  * GraphQLのパフォーマンス対策も
  
### Supercharge Your Python **Web App** Security Using Logto.io as Your Authentication Service

* {fab}`github` [rizqon/Pycon2024Demo](https://github.com/rizqon/Pycon2024Demo) 
* [Logto.io](https://logto.io/)という認証サービスをDjangoに組み込む話

### **Structlog** in Practice

* {fab}`github` [shimizukawa/structlog-example](https://github.com/shimizukawa/structlog-example)
* スライド(日本語版): [実践structlog](https://docs.google.com/presentation/d/1aST5f0rpdS4jS4pmKC4hbWydHkGCpYpuLwKrZ6u3nb0/pub#slide=id.g30314fac8ae_0_0)
* Django、Celery、Sentryと一緒に[structlog](https://www.structlog.org/)を使用して、ログを追跡しやすくする話
* 詳しく知りたい人はshimizukawaまで

### **GraphQL** in Python

* {fab}`github` [maarcingebala/ariadne-demo](https://github.com/maarcingebala/ariadne-demo)
* スライド: [GraphQL in Python](https://speakerdeck.com/maarcingebala/graphql-in-python)
* GraphQLの概要を紹介し、2つのアプローチをコード例を交えながら紹介する話
  * スキーマファースト: [Ariadne](https://ariadnegraphql.org/)
  * コードファースト: [Graphene](https://graphene-python.org/)

### Pythonic Ways to Build **Serverless** Apps in AWS and how to migrate from Frameworks

* Webアプリケーションをサーバーレスアプリにしようという話
* [mangum](https://github.com/Kludex/mangum)、[AWS Chalice](https://aws.github.io/chalice/)、[Powertools for AWS Lambda](https://docs.powertools.aws.dev/lambda/python/latest/)とかが紹介されていた
* 参考: [The Pythonic Way to Build Serverless Apps with AWS Chalice and CDK: A Guide to Migrating from Micro-frameworks](https://towardsaws.com/the-pythonic-way-to-build-serverless-apps-with-aws-chalice-and-cdk-migrating-from-micro-frameworks-2c80b7a17a9d)

## 現地セッションの **傾向**

* 「Web技術＋**なにか**」という話
* **実際にやっている**こと
* **コード例**を公開している人が多い

## **自分いけんじゃね**と思った？ 😎

### 海外PyConに**興味湧いた**？ ✈️

### 出そう**Proposal**！！

* [PyCon APAC 2025](https://pycon-apac.python.ph/): Mar 1-2, Manila, Philippines
  * [pretalx.com/pycon-apac-2025](https://pretalx.com/pycon-apac-2025/): 12月15日まで
* [PyCon US 2025](https://us.pycon.org/2025/): May 16-18, Pittsburgh, PA
  * [pretalx.com/pyconus2025](https://pretalx.com/pyconus2025/): 12月19日まで
  
### Python Conference **Deadlines**

* {fas}`globe` [`pythondeadlin.es`](https://pythondeadlin.es/)

```{image} images/pythondeadlin.png
:alt: Python Conference Deadlines
:width: 65%
```

### **不安**はあると思いますが

### **通ってから**考えよう！！

飛行機、ホテル、現地の移動、言語、食事、

お金、ビール、観光、お土産、など

### [`gihyo.jp`](https://gihyo.jp/)「PyCon レポート」で検索

```{image} images/pycon-reports.png
:width: 90%
```

### **#pycon-overseas**チャンネル

* 海外PyConに**興味がある人**のチャンネル
* Python mini Hack-a-thon(pyhack) Slack
* [pyhack.connpass.com](https://pyhack.connpass.com/)から参加

```{image} images/pyhack.png
:width: 60%
```

## See you at **PyCon somewhere** 🌏

## Thank You 🙏

{fas}`desktop` [slides.takanory.net](https://slides.takanory.net/)

{fab}`twitter` [@takanory](https://twitter.com/takanory)
{fab}`github` [takanory](https://github.com/takanory/)
{fab}`linkedin` [takanory](https://www.linkedin.com/in/takanory/)
{fab}`untappd` [takanory](https://untappd.com/user/takanory/)

![takanory profile](/assets/images/sokidan-square.jpg)
![kuro-chan and kuri-chan](/assets/images/kurokuri.jpg)
