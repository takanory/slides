from pathlib import Path

p = Path("beer.txt")
text = p.read_text(encoding="utf-8")  # ここで例外発生
