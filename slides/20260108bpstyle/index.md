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

### **◯◯**が爆誕！！ {nekochan}`paaan`

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

[^install]: <https://django-import-export.readthedocs.io/en/latest/installation.html>

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

[^resource]: <https://django-import-export.readthedocs.io/en/latest/getting_started.html>

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

[^integration]: <https://django-import-export.readthedocs.io/en/latest/admin_integration.html>

### Django Admin画面で<br />**インポート**・**エクスポート**できる！ {nekochan}`yatta`

![](https://django-import-export.readthedocs.io/en/latest/_images/django-import-export-change.png)

### 対象フォーマットは以下

* csv, xlsx, tsv, json, yaml, html

### しかし、このままでは教材データの<br />コピーには**使えない**... {nekochan}`work-yabai`

## django-import-exportの<br />**使いこなし** {nekochan}`work-moeru`

### **対象フィールド**の指定

* インポート・エクスポート対象を指定 [^declare]

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

[^declare]: <https://django-import-export.readthedocs.io/en/latest/advanced_usage.html#declare-fields>

```{revealjs-break}
```

* 今回は`exclude`を選択
* フィールドが増えても自動で対応

```{code-block} python
class WorkResource(resources.ModelResource):
    class Meta:
        model = Work
        exclude = ("id", "created_at", "updated_at", "updated_by")
```

### **主キー**の変更

* デフォルトでは`id`を使って追加、更新する
* 環境が異なるため`id`がずれる

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

[^idfields]: <https://django-import-export.readthedocs.io/en/latest/advanced_usage.html#create-or-update-model-instances>

### **大量データ**対応 [^duplicate]

* 教材の問題は**大量**→**全件**インポート
* 同じ値の場合は**処理を飛ばす**
* 飛ばしたデータは確認画面で**表示しない**

```{code-block} python
class WorkResource(resources.ModelResource):
    class Meta:
        model = Work
        import_id_fields = ("code",)
        skip_unchanged = True  # 処理を飛ばす
        report_skipped = False  # 表示しない
```

[^duplicate]: <https://django-import-export.readthedocs.io/en/latest/advanced_usage.html#handling-duplicate-data>

### **外部キー**の維持

* 教材の目次構造は**外部キー**で実現

```{mermaid}
erDiagram
    direction LR
    Work ||--|{ Unit : has
    Unit ||--|{ Question : has
    Work {
        int id PK
        string code
        string name
    }
    Unit {
        int id PK
        int work_id FK
        string code
        string title
    }
    Question {
        int id PK
        int unit_id FK
        string code
        string text
    }
```

```{revealjs-break}
```

* しかし`id`は環境ごとに**異なる**
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

[^foreignkey]: <https://django-import-export.readthedocs.io/en/latest/advanced_usage.html#foreign-key-relations>

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
    Work {
        int id PK
        string code
        bool can_export
    }
    Unit {
        int id PK
        int work_id FK
        string code
        bool can_export
    }
    Question {
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

[^exrpoting]: <https://django-import-export.readthedocs.io/en/latest/admin_integration.html#exporting-via-admin-action>

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

