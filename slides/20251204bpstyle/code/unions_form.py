"""pydanticで複数のモデルをUnionしていい感じに処理できるか試す"""
from typing import Literal

from pydantic import BaseModel, Field, PositiveInt

class BaseForm(BaseModel):
    """フォームのベースクラス"""
    question: str  # 質問文
    answer_format: str  # 解答欄形式
    display: object  # フォーム形式ごとの表示形式
    body: object  # フォーム形式ごとのボディ


class WrittenDisplay(BaseModel):
    """記述式の表示形式"""
    textInputFormat: PositiveInt = Field(le=3)


class WrittenBody(BaseModel):
    """記述式のボディ"""
    answers: list[str]
    placeholder: str

    
class WrittenForm(BaseForm):
    """記述式のモデル"""
    answer_format: Literal["written"]  # 「記述式」にのみマッチ
    display: WrittenDisplay
    body: WrittenBody


class ChoicesDisplay(BaseModel):
    """選択式の表示形式"""
    choices_selector: str  # ラジオ or セレクトボックス
    choices_label: str  # ABCなどのラベル形式


class ChoicesAnswer(BaseModel):
    """選択式の1つの選択肢"""
    answer: str  # 選択肢
    is_correct: bool  # 正解フラグ


class ChoicesBody(BaseModel):
    """記述式のボディ"""
    answers: list[ChoicesAnswer]

    
class ChoicesForm(BaseForm):
    """選択式のモデル"""
    answer_format: Literal["choices"]  # 「選択式」にのみマッチ
    display: ChoicesDisplay
    body: ChoicesBody


class AnswerForm(BaseModel):
    """いずれかのフォーム形式にマッチするモデル"""
    answer_form: WrittenForm | ChoicesForm = Field(discriminator="answer_format")


# 記述式のサンプル
written = {
    "question": "Pythonの作者は？", # 採点形式: 自動
    "answer_format": "written", # 記述式
    "display": {
        "textInputFormat": 1,
    },
    "body": {
        "answers": ["Guido van Rossum"],
        "placeholder": "作者名をアルファベットで書いてください",
    },
}

# 選択式のサンプル
choices = {
    "question": "Python 3.14の新機能はどれ？",
    "answer_format": "choices",
    "display": {
        "choices_selector": "button",
        "choices_label": "ABC",
    },
    "body": {
        "answers": [
            {"answer": "t-string", "is_correct": True},
            {"answer": "safe external debugger", "is_correct": True},
            {"answer": "lazy import", "is_correct": False},
        ],
    },
}

written_form = AnswerForm(answer_form=written)
print(written_form)
# answer_form=WrittenForm(question='Pythonの作者は？', answer_format='written', display=WrittenDisplayOptions(textInputFormat=1), body=WrittenBody(answers=['Guido van Rossum'], placeholder='作者名をアルファベットで書いてください'))

choices_form = AnswerForm(answer_form=choices)
print(choices_form)
# answer_form=ChoicesForm(question='Python 3.14の新機能はどれ？', answer_format='choices', display=ChoicesDisplayOptions(choices_selector='button', choices_label='ABC'), body=ChoicesBody(answers=[ChoicesAnswer(answer='t-string', is_correct=True), ChoicesAnswer(answer='safe external debugger', is_correct=True), ChoicesAnswer(answer='lazy import', is_correct=False)]))
