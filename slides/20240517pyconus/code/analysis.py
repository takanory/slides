from sudachipy import Dictionary

tokenizer = Dictionary().create()

text = "今日"  # today
tokens = tokenizer.tokenize(text)

print(tokens[0].surface())  # -> 今日
print(tokens[0].reading_form())  # -> キョウ(kyou)
print(tokens[0].part_of_speech()[0])  # -> 名詞(noun)
