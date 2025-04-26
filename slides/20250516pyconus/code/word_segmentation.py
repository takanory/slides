import sys
from sudachipy import Dictionary

tokenizer = Dictionary().create()

def word_segmentation(text: str) -> str:
    result = []
    for token in tokenizer.tokenize(text):
        word = str(token)
        result.append(word)
    return " / ".join(result)

if __name__ == "__main__":
    print(word_segmentation(sys.argv[1]))
