import re
import json
from urllib import request


def main():
    """学年別漢字配当表をJSON形式で保存"""
    URL = "https://www.mext.go.jp/a_menu/shotou/new-cs/youryou/syo/koku/001.htm"
    kanji_grade = []
    with request.urlopen(URL) as f:
        for line in f:
            if m := re.match(r"<td>(.*)（\d+字）</td>", line.decode("utf-8")):
                kanji_grade.append(m[1].replace("　", ""))
    with open("kanji_grade.json", "w") as f:
        json.dump(kanji_grade, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
