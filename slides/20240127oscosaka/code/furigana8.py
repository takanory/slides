import re
import sys
from jaconv import kata2hira
from sudachipy import dictionary

KANJI = r"[\u3005-\u3007\u4E00-\u9FFF]"  # 漢字を表す正規表現
KANA = r"[\u3041-\u309F]+$"  # 末尾のひらがなを表す正規表現


def ruby(kanji: str, kana: str) -> str:
    """1つの単語にフリガナを振る
    >>> ruby("麦酒", "びーる")
    '<ruby><rb>麦酒</rb><rt>びーる</rt></ruby>'
    >>> ruby("飲もう", "のもう")
    '<ruby><rb>飲</rb><rt>の</rt></ruby>もう'
    >>> ruby("追い出す", "おいだす")
    '<ruby><rb>追</rb><rt>お</rt></ruby>い<ruby><rb>出</rb><rt>だ</rt></ruby>す'
    >>> ruby("しみ込む", "しみこむ")
    'しみ<ruby><rb>込</rb><rt>こ</rt></ruby>む'
    >>> ruby("立ち入り禁止", "たちいりきんし")
    '<ruby><rb>立</rb><rt>た</rt></ruby>ち<ruby><rb>入</rb><rt>い</rt></ruby>り<ruby><rb>禁止</rb><rt>きんし</rt></ruby>'
    >>> ruby("東アジア", "ひがしあじあ")
    '<ruby><rb>東</rb><rt>ひがし</rt></ruby>アジア'
    """
    hira = kata2hira(kana)
    okuri = ""
    if m := re.search(KANA, kanji):
        okuri = m[0]
        kanji = kanji.removesuffix(okuri)  # 送り仮名を削除
        hira = hira.removesuffix(okuri)  # 送り仮名を削除
    return f"<ruby><rb>{kanji}</rb><rt>{hira}</rt></ruby>{okuri}"


def furigana(s: str) -> str:
    """文字列にフリガナを振ったHTMLを返す"""
    t = dictionary.Dictionary(dict="full").create()
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
