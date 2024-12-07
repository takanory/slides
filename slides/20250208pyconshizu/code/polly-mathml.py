from contextlib import closing
from pathlib import Path

import boto3
from bs4 import BeautifulSoup

# 識別子、演算子と読みの対応表
OPERATORS = {
    "±": "プラスマイナス",
    "+": "プラス",
    "−": "マイナス",
    "×": "掛ける",
    "÷": "割る",
    "(": "括弧",
    ")": "括弧閉じ",
}


def mathml_to_text(text: str) -> str:
    """MathMLを取りだして読み上げ文字列にする"""
    soup = BeautifulSoup(text, "html.parser")
    for math in soup.find_all("math"):
        # ここで変換処理

        # 識別子、演算子を変換する
        for mo_mi in math.find_all(["mo", "mi"]):
            if mo_mi.text in OPERATORS:
                mo_mi.string = OPERATORS[mo_mi.text]

        # 分母と分子の順番を逆にする
        for mfrac in math.find_all("mfrac"):
            bunshi, bunbo = mfrac.contents
            mfrac.clear()
            mfrac.append(bunbo)
            mfrac.append("ぶんの")
            mfrac.append(bunshi)

        # <msup><mi>x</mi><mn>2</mn></msup> を「x2乗」と読む
        for msup in math.find_all("msup"):
            exponent = msup.contents[1]
            exponent.string = f"{exponent.text}乗"

        # <msqrt> を「ルート」と読む
        for msqrt in math.find_all("msqrt"):
            msqrt.insert(0, "ルート")

        # その他の記号を変換する
        math_text = math.text
        math_text = math_text.replace("//", "平行")
        math_text = math_text.replace("∘C", "℃")
        math_text = math_text.replace("∘", "度")
        math.string = math_text

    # 最後に全部テキストにする
    return soup.text


if __name__ == "__main__":
    p = Path("mathml-formula.html")
    text = p.read_text(encoding="utf-8")
    result = mathml_to_text(text)
    print(result)

    polly = boto3.client('polly')
    result = polly.synthesize_speech(
        Text=result, OutputFormat="mp3", VoiceId="Mizuki")

    with closing(result["AudioStream"]) as stream:
        Path("mathml.mp3").write_bytes(stream.read())
