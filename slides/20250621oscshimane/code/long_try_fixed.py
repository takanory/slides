from pathlib import Path

p = Path("beer.txt")
try:
    text = p.read_text(encoding="utf-8")  # ファイル読み込みエラー
except Exception:
    print("ファイルの読み込みに失敗しました")
else:
    for line in text.splitlines():
        try:
            name, price_text = line.split(",")  # 分割エラー
            price = int(price_text)  # 変換エラー
        except ValueError as e:
            print(f"データ変換エラーが発生: {e}")
        # なにか他の処理
        ...
