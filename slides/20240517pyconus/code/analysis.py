from sudachipy import Dictionary

tokenizer = Dictionary().create()

text = "麦酒を飲みたい"  # I need beer
tokens = tokenizer.tokenize(text)

print(tokens[0].surface())  # -> 麦酒
print(tokens[0].reading_form())  # -> ビール(biiru)
print(tokens[0].part_of_speech()[0])  # -> 名詞(noun)

