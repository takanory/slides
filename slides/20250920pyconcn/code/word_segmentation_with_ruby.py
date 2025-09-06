import sys
from sudachipy import Dictionary
from kana2roman import kana_with_romaji_ruby

tokenizer = Dictionary().create()

def word_segmentation(text: str) -> str:
    result = []
    for token in tokenizer.tokenize(text):
        word = kana_with_romaji_ruby(str(token))
        result.append(word)
    return " / ".join(result)

if __name__ == "__main__":
    print(word_segmentation(sys.argv[1]))
