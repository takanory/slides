import jaconv
from sudachipy import Dictionary

tokenizer = Dictionary().create()
text = "今日は一月一日で日曜日"  # Today is January 1st
tokens = tokenizer.tokenize(text)

readings = []
for token in tokenizer.tokenize(text):
    readings.append(token.reading_form())

print(readings)
# -> ['キョウ', 'ハ', 'イチ', 'ガツ', 'ツイタチ', 'デ', 'ニチヨウビ']
print([jaconv.kata2hira(r) for r in readings])
# -> ['きょう', 'は', 'いち', 'がつ', 'ついたち', 'で', 'にちようび']
print([jaconv.kata2alphabet(r) for r in readings])
# -> ['kyou', 'ha', 'ichi', 'gatsu', 'tsuitachi', 'de', 'nichiyoubi']
