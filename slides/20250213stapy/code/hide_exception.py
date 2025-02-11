from pathlib import Path

p = Path("beer.txt")
try:
    text = p.read_text(encoding="utf-8")  # ここで例外発生
except Exception:
    pass  # なにが問題かわからなくなる
