import json
import re
import sys
from jaconv import kata2hira
from sudachipy import dictionary

KANJI = r"[\u3005-\u3007\u4E00-\u9FFF]"  # 漢字を表す正規表現
KANA = r"[\u3041-\u309F\u30A1-\u30FF]+"  # ひらがなとカタカナを表す正規表現


def make_ruby(kanji: str, furi: str) -> str:
    """rubyタグを生成して返す"""
    return f"<ruby><rb>{kanji}</rb><rt>{furi}</rt></ruby>"


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
    text = ""
    while m := re.search(KANA, kanji):  # kanjiの中のすべてのかな
        okuri = m[0]
        index = hira.find(kata2hira(okuri), m.start())  # 最初のかなの位置
        furigana = hira[:index]
        hira = hira[index + len(okuri):]  # 残りのふりがな
        f_kanji, kanji = kanji.split(okuri, 1)  # kanjiを送りがなで分割
        if furigana:
            text += make_ruby(f_kanji, furigana)
        text += okuri  # 送りがなを追加
    if kanji:  # 漢字が残っている場合
        text += make_ruby(kanji, hira)
    return text


def get_kanji_grade_set() -> set[str]:
    """漢字配当表の全漢字のセットを返す"""
    kanji_grade = set()
    with open("kanji_grade.json") as f:
        for s in json.load(f):
            kanji_grade.update(set(s))
    return kanji_grade


def is_ruby_required(surface: str, kanji_grade: set[str]) -> bool:
    """フリガナが必要かを判定する"""
    if re.search(KANJI, surface) is None:  # 漢字を含んでいるか
        return False
    kanji_set = set(re.findall(KANJI, surface))
    return not kanji_set <= kanji_grade  # 配当表外の漢字があるか


def furigana(s: str) -> str:
    """文字列にフリガナを振ったHTMLを返す"""
    kanji_grade = get_kanji_grade_set()
    t = dictionary.Dictionary(dict="full").create()
    result = ""
    for token in t.tokenize(s):
        surface = token.surface()
        if is_ruby_required(surface, kanji_grade):
            result += ruby(surface, token.reading_form())
        else:
            result += surface
    return result

if __name__ == "__main__":
    print(furigana(sys.argv[1]))
