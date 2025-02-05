from pathlib import Path

p = Path("beer.txt")
try:
    text = p.read_text(encoding="utf-8")  # ファイル読み込みエラー
    for line in text.splitlines():
        name, price_text = line.split(",")  # 分割エラー
        price = int(price_text)  # 変換エラー
        # なにか他の処理
        ...
except Exception:
    print("エラーが発生しました")
