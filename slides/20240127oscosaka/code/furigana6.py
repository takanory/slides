import re
import sys
from jaconv import kata2hira
from sudachipy import dictionary

KANJI = r"[\u3005-\u3007\u4E00-\u9FFF]"  # 漢字を表す正規表現
KANA = r"[\u3041-\u309F]+$"  # 末尾のひらがなを表す正規表現

def ruby(kanji: str, kana: str) -> str:
    """1つの単語にフリガナを振る"""
    hira = kata2hira(kana)
    okuri = ""
    if m := re.search(KANA, kanji):
        okuri = m[0]
        kanji = kanji.removesuffix(okuri)  # 送り仮名を削除
        hira = hira.removesuffix(okuri)  # 送り仮名を削除
    return f"<ruby><rb>{kanji}</rb><rt>{hira}</rt></ruby>{okuri}"

def furigana(s: str) -> str:
    """文字列にフリガナを振ったHTMLを返す"""
    t = dictionary.Dictionary().create()
    result = ""
    for token in t.tokenize(s):
        surface = token.surface()
        if re.search(KANJI, surface):  # 漢字か？
            result += ruby(surface, token.reading_form())
        else:
            result += surface
    return result

if __name__ == "__main__":
    print(furigana(sys.argv[1]))
