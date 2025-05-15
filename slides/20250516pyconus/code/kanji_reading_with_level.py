"""
usage: kanji_reading_with_level.py [-h] [-a] [-l {1,2,3,4,5}] text

Add Furigana to Japanese text

positional arguments:
  text            text to add furigana annotation

options:
  -h, --help      show this help message and exit
  -a              Alphabet(Romaji) annotation(default: Hiragana)
  -l {1,2,3,4,5}  set kanji level
"""
import argparse
import json
import re

from jaconv import kata2alphabet, kata2hira
from sudachipy import Dictionary

KANJI = r"[\u3005-\u3007\u4E00-\u9FFF]"  # Kanji pattern

tokenizer = Dictionary().create()  # create tokenizer


def get_kanji_set(level: str | None) -> set[str]:
    """Returns a set of Kanji below the specified JLPT level"""
    if level is None:
        return set()

    with open("JLPT_kanji.json", encoding="utf-8") as f:
        kanji_level_dict = json.load(f)
    kanji_set = set()
    for l, kanji_list in kanji_level_dict.items():
        if l >= level:
            kanji_set.update(set(kanji_list))
    return kanji_set


def is_ruby_required(surface: str, kanji_set: set[str]) -> bool:
    """Returns whether ruby is required"""
    if not kanji_set:  # no kanji set -> no level
        return True

    kanji_in_surface = set(re.findall(KANJI, surface))
    if not kanji_in_surface:  # word without kanji
        return False
    if kanji_in_surface <= kanji_set:  # Kanji within the level
        return False
    return True


def add_reading(text: str, level: str | None, alphabet: bool):
    """Add Furigana ruby to text"""
    kanji_set = get_kanji_set(level)
    result = ""
    for token in tokenizer.tokenize(text):
        reading = token.reading_form()
        if is_ruby_required(str(token), kanji_set):
            if alphabet:
                ruby = kata2alphabet(reading)  # to Alphabet
            else:
                ruby = kata2hira(reading)  # to Hiragana
            result += f"<ruby>{token}<rt>{ruby}</rt></ruby>\n"
        else:
            result += f"{token}\n"
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add Furigana to Japanese text")
    parser.add_argument(
        "-a",
        action="store_true",
        help="Alphabet(Romaji) annotation(default: Hiragana)",
    )
    parser.add_argument("-l", choices="12345", help="set kanji level")
    parser.add_argument("text", help="text to add furigana annotation")
    args = parser.parse_args()
    result = add_reading(args.text, args.l, args.a)
    print(result)
