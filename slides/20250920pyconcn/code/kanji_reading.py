import sys
from jaconv import kata2hira
from sudachipy import Dictionary

tokenizer = Dictionary().create()  # create tokenizer

def add_reading(text: str) -> str:
    """Add Hiranaga ruby to text"""
    result = ""
    for token in tokenizer.tokenize(text):
        ruby = kata2hira(token.reading_form())  # to Hiragana
        result += f"<ruby>{token}<rt>{ruby}</rt></ruby>\n"
    return result

if __name__ == "__main__":
    print(add_reading(sys.argv[1]))
