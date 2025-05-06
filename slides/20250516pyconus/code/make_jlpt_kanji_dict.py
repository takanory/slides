import json
from urllib.request import urlopen

BASE_URL = "https://raw.githubusercontent.com/obfusk/jiten/refs/heads/master/jiten/res/jlpt/"

kanji = {}
for level in range(1, 6):  # level 1 to 5
    with urlopen(f"{BASE_URL}N{level}-kanji") as f:
        data = f.read().decode("utf-8")
        kanji[level] = data

with open("JLPT_kanji.json", "w", encoding="utf-8") as f:
    json.dump(kanji, f, ensure_ascii=False, indent=2)
