import re
from contextlib import closing
from pathlib import Path
import boto3


def text2speech(polly, text, f, lang):
    """指定した言語で読み上げる"""
    # 言語で音声切り替え
    voice = {"en": "Matthew", "ja": "Takumi"}[lang]
    result = polly.synthesize_speech(Text=text,
        OutputFormat="mp3", VoiceId=voice,
        LexiconNames=[LEXICON])
    with closing(result["AudioStream"]) as stream:
        f.write(stream.read())


polly = boto3.client('polly')

# Lexiconを名前をつけて登録
LEXICON = "DBLexicon"
data = Path("db-lexicon.xml").read_text(encoding="utf-8")
polly.put_lexicon(Name=LEXICON, Content=data)

# ファイルから問題文読み込み
p = Path("vegeta-english.txt")
text = p.read_text(encoding="utf-8")

with open("vegeta-question.mp3", "wb") as f:
    # 日本語と英語に分割
    while m := re.search(r"(^|[\s\b])(\w[\w\s/\.,:;'\"!?]*)([\s\b]|$)", text, re.A):
        en_text = m.group(2)
        ja_text, text = text.split(en_text, maxsplit=1)
        text2speech(polly, ja_text, f, "ja")
        text2speech(polly, en_text, f, "en")
    if text.strip():
        text2speech(polly, ja_text, f, "ja")
