import re
import sys
from jaconv import kata2hira
from janome.tokenizer import Tokenizer

KANJI = r"[\u3005-\u3007\u4E00-\u9FFF]"  # 漢字を表す正規表現


def furigana(s: str) -> str:
    """文字列にフリガナを振ったHTMLを返す"""
    t = Tokenizer()
    result = ""
    for token in t.tokenize(s):
        if re.search(KANJI, token.surface):  # 漢字か？
            result += (f"<ruby><rb>{token.surface}</rb>"
                       f"<rt>{kata2hira(token.reading)}</rt></ruby>")
        else:
            result += token.surface
    return result


if __name__ == "__main__":
    print(furigana(sys.argv[1]))
