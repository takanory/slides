import jaconv
from sudachipy import Dictionary

tokenizer = Dictionary().create()
text = "今日は一月一日"  # Today is January 1st
tokens = tokenizer.tokenize(text)

print(tokens[0].surface())  # -> 今日
reading = tokens[0].reading_form()
print(reading)  # -> キョウ(Katakana)
print(jaconv.kata2hira(reading))  # -> きょう(Hiragana)
print(jaconv.kata2alphabet(reading))  # -> kyou(Roman)
