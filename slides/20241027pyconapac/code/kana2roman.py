import sys
import jaconv

def kana2romaji(kana: str) -> str:
    """Convert Hiragana and Katakana to Romaji"""
    hiragana = jaconv.kata2hira(kana)  # Katakana -> Hiragana
    return jaconv.kana2alphabet(hiragana)  # Hiragana -> alphabet

def kana_with_romaji_ruby(kana: str) -> str:
    """Add romaji ruby to Kana text"""
    romaji = kana2romaji(kana)
    return f"<ruby>{kana}<rt>{romaji}</rt></ruby>"

if __name__ == "__main__":
    print(kana_with_romaji_ruby(sys.argv[1]))
