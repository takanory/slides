import re
from contextlib import closing
from pathlib import Path
import boto3

def text2speech(polly, text, f, lang):
    """指定した言語で読み上げ"""
    voice = {"en": "Salli", "ja": "Mizuki"}[lang]
    result = polly.synthesize_speech(Text=text,
        OutputFormat="mp3", VoiceId=voice,
        LexiconNames=[LEXICON])
    with closing(result["AudioStream"]) as stream:
        f.write(stream.read())

polly = boto3.client('polly')

# Lexiconを名前をつけて登録
LEXICON = "tennolexicon"
data = Path("tenno-lexicon.xml").read_text(encoding="utf-8")
polly.put_lexicon(Name=LEXICON, Content=data)

text = "（）に当てはまる単語を選べ。 "
text += "Do, or do not. （） is no try. ① They ② There ③ Then"

with open("yoda.mp3", "wb") as f:
    while m := re.search(r"(^|[\s\b])(\w[\w\s/\.,:;'\"!?]*)([\s\b]|$)", text, re.A):
        en_text = m.group(2)
        ja_text, text = text.split(en_text, maxsplit=1)
        text2speech(polly, ja_text, f, "ja")
        text2speech(polly, en_text, f, "en")
    if text.strip():
        text2speech(polly, ja_text, f, "ja")

