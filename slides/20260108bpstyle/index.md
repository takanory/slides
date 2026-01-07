```{eval-rst}
:og:image: _images/20260108pstyle.png
:og:image:alt: django-import-exportはインポート・エクスポートできるだけじゃない カスタマイズと使いこなし

.. |cover| image:: images/20260108pstyle.png
```

```{raw} html
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11.12.1/dist/mermaid.esm.min.mjs";
mermaid.registerIconPacks([
  {
    name: 'logos',
    loader: () =>
      fetch('https://unpkg.com/@iconify-json/logos@1/icons.json').then((res) => res.json()),
  },
  {
    name: 'vscode-icons',
    loader: () =>
      fetch('https://unpkg.com/@iconify-json/vscode-icons@1/icons.json').then((res) => res.json()),
  },
]);
</script>
```

# **django-import-export**は

インポート・エクスポートできる**だけじゃない**

〜カスタマイズと使いこなし〜

Takanori Suzuki

BPStyle 180 / 2026 Jan 8

## はなすこと {nekochan}`kiriri`

* なんのために？ {nekochan}`hate`
* django-import-exportの**基本** {nekochan}`work`
* django-import-exportの**使いこなし** {nekochan}`work-moeru`

## なんのために？ {nekochan}`hate`

### 明治図書のマナビリア案件で必要 {nekochan}`naruhodo`

* [MANAVIRIA（マナビリア）](https://www.learning-innovation.go.jp/db/ed0207/)
* 教材データを原稿作成環境から本番環境に<br />**コピー**するため

### **教材データ**とは {nekochan}`benkyou`

* 以下のようなデータがDBに入っている
* 学習教材の目次構成
* 問題文
* 解答形式
* 正解

### 教材データのコピーが必要 {nekochan}`hueta`

* 作成中の教材は間違いがある
* レビューして修正
* レビューOKな教材のみが本番にある
* 別環境で作成した教材データを<br />**本番環境にコピー**する運用 {nekochan}`yoshi`

### 既存の教材データコピー {nekochan}`tako`

* 原稿作成環境(Edit)から本番環境(Production)にExcelファイルで教材データをコピー

```{mermaid}
architecture-beta
    service stg(logos:aws-ecs)[Edit]
    service excel(vscode-icons:file-type-excel)[Excel]
    service prd(logos:aws-ecs)[Production]

    stg:R --> L:excel
    excel:R --> L:prd
```

### 運用できていたわけですが... {nekochan}`good`

### **マナビリアCBT**が爆誕！！ [^cbt] {nekochan}`paaan`

```{image} images/manaviria-cbt.png
:alt: マナビリアCBT
:width: 75%
```

[^cbt]: <https://www.meijitosho.co.jp/gakusan/special/digital_learning/>

### **新しい**教材データコピーが必要 {nekochan}`ha`

* 教材データの構成は似ているが**微妙に違う**
* Excelで実装すると工数が...テストも...

### django-import-exportで**省力化に挑戦** {nekochan}`totugeki`

## django-import-exportの**基本** {nekochan}`work`

### django-import-exportとは {nekochan}`hate`

* {fas}`globe` [django-import-export.readthedocs.io](https://django-import-export.readthedocs.io/en/latest/)
* Django Admin画面にインポート・エクスポート機能を追加する拡張

![](https://django-import-export.readthedocs.io/en/latest/_images/django-import-export-change.png)

### インストールと有効化 [^install]

```code-block {bash}
pip install django-import-export
```

```{code-block} python
:caption: settings.pyで有効化

INSTALLED_APPS = (
    ...
    'import_export',
)
```

[^install]: Installation and configuration: <https://django-import-export.readthedocs.io/en/latest/installation.html>

### リソースクラスを作成 [^resource]

* リソースクラスで対象となる**モデルを指定**

```{code-block} python
:caption: app/admin.py

from import_export import resources
from core.models import Book

class BookResource(resources.ModelResource):
    class Meta:
        model = Book
```

[^resource]: Creating a resource: <https://django-import-export.readthedocs.io/en/latest/getting_started.html#creating-a-resource>

### Django Adminに適用 [^integration]

* 親クラスを変更
* リソースクラスを指定

```{code-block} python
:caption: app/admin.py

from django.contrib import admin
from .models import Book
from import_export.admin import ImportExportModelAdmin

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    resource_classes = [BookResource]
```

[^integration]: Admin integration: <https://django-import-export.readthedocs.io/en/latest/admin_integration.htmla>

### Django Admin画面で<br />**インポート**・**エクスポート**できる！ {nekochan}`yatta`

![](https://django-import-export.readthedocs.io/en/latest/_images/django-import-export-change.png)

### 対象フォーマットは以下

* csv, xlsx, tsv, json, yaml, html

### しかし、このままでは教材データの<br />コピーには**使えない**... {nekochan}`work-yabai`

## django-import-exportの<br />**使いこなし** {nekochan}`work-moeru`

### **対象フィールド**の指定

* 作成日時、更新日時等は不要

```{mermaid}
erDiagram
    Work["Work(教材)"] {
        int id PK
        string code "コード"
        int textbook_id FK "教科書ID"
        int subject_id FK "教科ID"
        string name "教材名"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
        int updated_by FK "更新者"
        str updated_by_name "更新者名"
    }
```

```{revealjs-break}
```

* リソースで対象フィールドを指定 [^declare]

```{code-block} python
class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        # 対象フィールドを指定
        fields = ("id", "name", "price")
```

```{code-block} python
class BookResource(resources.ModelResource):
    class Meta:
        model = Book
        # 対象外フィールドを指定
        exclude = ("created_at", "updated_at")
```

[^declare]: Declare fields: <https://django-import-export.readthedocs.io/en/latest/advanced_usage.html#declare-fields>

```{revealjs-break}
```

* 今回は`exclude`を選択
* フィールドが**増えて**も**自動**で対応

```{code-block} python
class WorkResource(resources.ModelResource):
    class Meta:
        model = Work
        exclude = ("id", "created_at", "updated_at",
                   "updated_by")
```

### **主キー**の変更

* デフォルトでは`id`を使って追加、更新する
* 環境が異なるため`id`がずれる

```{mermaid}
erDiagram
    Work["Work(教材)"] {
        int id PK
        string code "コード"
        int textbook_id FK "教科書ID"
        int subject_id FK "教科ID"
        string name "教材名"
        datetime created_at "作成日時"
        datetime updated_at "更新日時"
        int updated_by FK "更新者"
        str updated_by_name "更新者名"
    }
```

```{revealjs-break}
```

* データを一意に識別するフィールドを指定 [^idfields]
* `code`というユニークな文字列を使用

```{code-block} python
class WorkResource(resources.ModelResource):
    class Meta:
        model = Work
        import_id_fields = ("code",)  # codeで一意に識別
```

[^idfields]: Create or update model instances: <https://django-import-export.readthedocs.io/en/latest/advanced_usage.html#create-or-update-model-instances>

### **大量データ**対応 [^duplicate]

* 教材の問題は**大量**→**全件**インポート
* 同じ値の場合は**処理を飛ばす**
* 飛ばしたデータは確認画面で**表示しない**

```{code-block} python
class WorkResource(resources.ModelResource):
    class Meta:
        model = Work
        skip_unchanged = True  # 処理を飛ばす
        report_skipped = False  # 表示しない
```

[^duplicate]: Handling duplicate data: <https://django-import-export.readthedocs.io/en/latest/advanced_usage.html#handling-duplicate-data>

### **外部キー**の維持

* 教材の目次構造は**外部キー**で実現

```{mermaid}
erDiagram
    direction LR
    Work ||--|{ Unit : has
    Unit ||--|{ Question : has
    Work["Work(教材)"] {
        int id PK
        string code
        string name
    }
    Unit["Unit(ユニット)"] {
        int id PK
        int work_id FK
        string code
        string title
    }
    Question["Qustion(問題)"] {
        int id PK
        int unit_id FK
        string code
        string text
    }
```

```{revealjs-break}
```

* `id`は環境ごとに**異なる**
* 任意のフィールド（`code`）を外部キー代わりに使用 [^foreignkey]

```{code-block} python
class UnitResource(resources.ModelResource):
    class Meta:
        model = Unit

    work = fields.Field(
        column_name="work",
        attribute="work",
        widget=ForeignKeyWidget(Work, field="code"))
```

[^foreignkey]: Foreign Key relations: <https://django-import-export.readthedocs.io/en/latest/advanced_usage.html#foreign-key-relations>

### 外部キーの維持（**複数カラム**）

* 教材は任意の教科書に紐付く

```{mermaid}
erDiagram
    direction LR
    Subject ||--|{ Textbook : has
    Textbook ||--|{ Work : has
    Subject["Subject(教科)"] {
        int id PK
        string name "国語等"
    }
    Textbook["Textbook(教科書)"] {
        int id PK
        int subject_id FK "教科ID"
        int edition "発行年"
        int year "学年"
		int publisher "出版社"
    }
    Work["Work(教材)"] {
        int id PK
		int textbook_id FK "教科書ID"
        string name
    }
```

```{revealjs-break}
```

* 教科書は**複数カラム**で一意になる

```{mermaid}
erDiagram
    direction LR
    Textbook["Textbook(教科書)"] {
        int id PK
        int subject_id FK "教科ID"
        int edition "発行年"
        int year "学年"
		int publisher "出版社"
    }
```

```{revealjs-break}
```

* 外部キーの維持にnatural keyを使用[^natural]
* 複数の情報が**JSONにシリアライズ**される

[^natural]: Django Natural Keys: <https://django-import-export.readthedocs.io/en/stable/advanced_usage.html#django-natural-keys>


```{code-block} python
class TextbookManager(models.Manager):
    def get_by_natural_key(self, edition, subject_name, year, publisher):
	    """natural keyを使用してデータを取得するメソッド"""
        return self.get(
            edition=edition,
            subject__name=subject_name,
            year=year,
            publisher=publisher,
        )
```

```{revealjs-break}
```

* モデルに`natural_key`メソッド追加
* `objects`に`TextbookManager()`を指定

```{code-block} python
class Textbook(BaseModel):
    """教科書モデル"""
    objects = TextbookManager()

    def natural_key(self):
        return (
            self.edition, self.subject.name,
            self.year, self.publisher,
        )
```
 
```{revealjs-break}
```

* `ForeignKeyWidget`でnatural keyを使用

```{code-block} python
class WorkResource(resources.ModelResource):
    textbook = fields.Field(
        column_name="textbook",
        attribute="textbook",
        widget=ForeignKeyWidget(Textbook,
            use_natural_foreign_keys=True)
    )
```

### **任意のデータ**をエクスポート対象に

* 全件エクスポートだと**レビュー中の教材データ**も本番に入る
* レビュー**完了したデータ**のみをエクスポート対象にしたい

```{revealjs-break}
```

* `can_exrpot`がTrueのデータをエクスポート
* 上位がFalseならエクスポートしない

```{mermaid}
erDiagram
    direction LR
    Work ||--|{ Unit : has
    Unit ||--|{ Question : has
    Work["Work(教材)"] {
        int id PK
        string code
        bool can_export "エクスポートフラグ"
    }
    Unit["Unit(ユニット)"] {
        int id PK
        int work_id FK
        string code
        bool can_export "エクスポートフラグ"
    }
    Question["Question(問題)"] {
        int id PK
        int unit_id FK
        string code
        string text
    }
```

```{revealjs-break}
```

* `get_export_queryset()`で絞り込み [^exrpoting]

```{revealjs-code-block} python
class WorkAdmin(ImportExportModelAdmin):
    def get_export_queryset(self, request):
        return Work.objects.filter(can_export=True)
```

[^exrpoting]: Exporting via Admin action: <https://django-import-export.readthedocs.io/en/latest/admin_integration.html#exporting-via-admin-action>

```{revealjs-break}
```

```{revealjs-code-block} python
class UnitAdmin(ImportExportModelAdmin):
    def get_export_queryset(self, request):
        # UnitとWorkの両方のcan_exportがTrue
        return Unit.objects.filter(
            can_export=True,
            work__can_export=True,
        )

class QuestionAdmin(ImportExportModelAdmin):
    def get_export_queryset(self, request):
        return Question.objects.filter(
            unit__can_export=True,
            unit__work__can_export=True
        )
```

### インポート時の**データ削除**

* 原稿作成環境で削除されたデータを本番環境でも**自動で削除**したい
* →モデルに**削除フラグ**を追加

```{code-block} python
class Question(BaseModel):
    """問題のモデルクラス"""
    ...
    is_delete = models.BooleanField("削除フラグ", default=False)
    ...
```

```{revealjs-break}
```

* リソースに`for_delete()`メソッドを追加 [^delete]

```{code-block} python
class QuestionResource(resources.ModelResource):
    """Question（問題）のインポート・エクスポート用の設定"""

    def for_delete(self, row, instance):
        """is_deleteがTrueのデータを削除する"""
        return row["is_delete"] == "1"

    ...
```

[^delete]: Deleting data: <https://django-import-export.readthedocs.io/en/latest/getting_started.html#deleting-data>

## まとめ {nekochan}`juutai`

* 単純な処理以外にいろいろできる
* **対象フィールド**の指定
* **主キー**の変更
* **大量データ**対応
* **外部キー**の維持（**複数カラム**も）
* **任意のデータ**をエクスポート対象に
* インポート時の**データ削除**

## 他にもいろいろできるので<br />**インポート・エクスポート**が<br />必要なときは**思い出して**ね {nekochan}`kyapi`

{fas}`globe` [django-import-export.readthedocs.io](https://django-import-export.readthedocs.io/)
