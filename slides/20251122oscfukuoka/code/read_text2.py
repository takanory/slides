from pathlib import Path

p = Path("beer.txt")
try:
    text = p.read_text(encoding="utf-8")
except FileNotFoundError:
    print("ファイルが存在しません")
except PermissionError:
    print("ファイルの読み込み権限がありません")
except UnicodeDecodeError:
    print("utf-8のテキストじゃありません")
