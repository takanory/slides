import sys
from janome.tokenizer import Tokenizer


def furigana(s: str) -> str:
    """文字列にフリガナを振ったHTMLを返す"""
    t = Tokenizer()
    result = ""
    for token in t.tokenize(s):
        result += (f"<ruby><rb>{token.surface}</rb>"
                   f"<rt>{token.reading}</rt></ruby>")
    return result


if __name__ == "__main__":
    print(furigana(sys.argv[1]))
