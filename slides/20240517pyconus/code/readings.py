from sudachipy import Dictionary

tokenizer = Dictionary().create()

text = "今日は一月一日で日曜日"
readings = []
for token in tokenizer.tokenize(text):
    readings.append(token.reading_form())
print(readings)
# -> ['キョウ', 'ハ', 'イチ', 'ガツ', 'ツイタチ', 'デ', 'ニチヨウビ']
