from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client('polly')  # クライアント作成

# Lexiconを名前をつけて登録
LEXICON = "tsubasaLexicon"
data = Path("tsubasa-lexicon.xml").read_text(encoding="utf-8")
polly.put_lexicon(Name=LEXICON, Content=data)

s = "反動蹴速迅砲。"
# Lexiconを使用しない
result = polly.synthesize_speech(
    Text=s, OutputFormat="mp3", VoiceId="Takumi")

with closing(result["AudioStream"]) as stream:
    Path("hando-no-lexicon.mp3").write_bytes(stream.read())

# Lexiconを使用
result = polly.synthesize_speech(
    Text=s, OutputFormat="mp3", VoiceId="Takumi",
    LexiconNames=[LEXICON])

with closing(result["AudioStream"]) as stream:
    Path("hando-with-lexicon.mp3").write_bytes(stream.read())
