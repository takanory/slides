import sys
import jaconv
from sudachipy import Dictionary

tokenizer = Dictionary().create()

def add_reading(text: str) -> str:
    """Add Romaji ruby to text"""
    result = ""
    for token in tokenizer.tokenize(text):
        # ruby = jaconv.kata2hira(token.reading_form())
        ruby = jaconv.kata2alphabet(token.reading_form())
        result += f"<ruby>{token}<rt>{ruby}</rt></ruby>\n"
    return result

if __name__ == "__main__":
    print(add_reading(sys.argv[1]))
