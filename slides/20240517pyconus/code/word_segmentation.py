from sudachipy import Dictionary

tokenizer = Dictionary().create()

text = "すもももももももものうち"
words = [token.surface() for token in tokenizer.tokenize(text)]
print(words)
# -> ['すもも', 'も', 'もも', 'も', 'もも', 'の', 'うち']
