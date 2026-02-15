"""pydanticで複数のモデルをUnionしていい感じに処理できるか試す"""
from typing import Literal

from pydantic import BaseModel, Field, PositiveInt

class BaseForm(BaseModel):
    """解答ベースクラス"""
    question: str  # 問題文
    sort_order: int  # ソート順
    answer_format: int  # 解答形式
    body: object  # 解答欄ボディ


class CBTForm(BaseForm):
    """CBT解答ベースクラス"""
    score: PositiveInt  # 点数
    

class WorkForm(BaseForm):
    """ワーク解答ベースクラス"""
    pass    


class WrittenBody(BaseModel):
    """記述式ボディ"""
    form_width: int  # フォームの幅
    answer: str  # 正答
    placeholder: str  # プレースホルダー
    max_chars: PositiveInt  # 最大文字数

    
class CBTWritten(CBTForm):
    """CBT記述式"""
    answer_format: Literal[1]  # 解答形式は「記述式」
    body: WrittenBody  # 記述式ボディ


class WorkWritten(WorkForm):
    """ワーク記述式"""
    answer_format: Literal[1]  # 解答形式は「記述式」
    body: WrittenBody  # 記述式ボディ


class ChoicesBody(BaseModel):
    """選択式ボディ"""
    choices_selector: int  # ラジオ or セレクトボックス
    layout: str  # レイアウト
    choices: list[str]  # 選択肢
    is_collects: list[bool]  # 正解 or 不正解


class CBTChoices(CBTForm):
    """CBT選択式"""
    answer_format: Literal[2]  # 解答形式は「選択式」
    body: ChoicesBody  # 選択式ボディ


class WorkChoices(WorkForm):
    """ワーク選択式"""
    answer_format: Literal[2]  # 解答形式は「選択式」
    body: ChoicesBody  # 選択式ボディ


class SortingBody(BaseModel):
    """並べ替えボディ"""
    ...


class CBTSorting(CBTForm):
    """CBT並べ替え"""
    answer_format: Literal[3]  # 解答形式は「並べ替え式」
    body: SortingBody  # 並べ替えボディ

    
class WorkSorting(WorkForm):
    """ワーク並べ替え"""
    answer_format: Literal[3]  # 解答形式は「並べ替え式」
    body: SortingBody  # 並べ替えボディ

    
class CBTAnswer(BaseModel):
    """いずれかのCBTの解答形式にマッチするモデル"""
    form: CBTWritten | CBTChoices | CBTSorting \
        = Field(discriminator="answer_format")


class WorkAnswer(BaseModel):
    """いずれかのワークの解答形式にマッチするモデル"""
    form: WorkWritten | WorkChoices | WorkSorting \
        = Field(discriminator="answer_format")


written_sample = {  # CBT記述式のサンプル
    "score": 5,  # 点数
    "question": "Pythonの作者は？", # 採点形式
    "sort_order": 1,  # ソート順
    "answer_format": 1, # 記述式
    "body": {
        "form_width": 1,  # フォームの幅
        "answer": "Guido van Rossum",   # 正答
        "placeholder": "作者名をアルファベットで書いてください",
        "max_chars": 100, # 最大文字数
    },
}

result = CBTAnswer(form=written_sample)
print(result)
# form=CBTWritten(question='Pythonの作者は？', sort_order=1, answer_format=1, body=WrittenBody(form_width=1, answer='Guido van Rossum', placeholder='作者名をアルファベットで書いてください', max_chars=100), score=5)

choices_sample = {  # ワーク選択式のサンプル
    "question": "Python 3.14の新機能はどれ？",
    "sort_order": 2,  # ソート順
    "answer_format": 2, # 選択式
    "body": {
        "choices_selector": 1,  # ラジオ
        "layout": "default",  # レイアウト
        "choices": ["t-string", "safe external debugger", "lazy import"],
        "is_collects": [True, True, False],
    },
}

result = WorkAnswer(form=choices_sample)
print(result)
# form=WorkChoices(question='Python 3.14の新機能はどれ？', sort_order=2, answer_format=2, body=ChoicesBody(choices_selector=1, layout='default', choices=['t-string', 'safe external debugger', 'lazy import'], is_collects=[True, True, False]))

