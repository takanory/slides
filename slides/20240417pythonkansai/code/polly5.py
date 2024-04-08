from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client('polly')  # クライアント作成

# Lexiconを名前をつけて登録
LEXICON = "DBLexicon"
data = Path("db-lexicon.xml").read_text(encoding="utf-8")
polly.put_lexicon(Name=LEXICON, Content=data)

s = "魔貫光殺砲うけてみろーーーーーーっ!!!!"
# Lexiconを使用しない
result = polly.synthesize_speech(
    Text=s, OutputFormat="mp3", VoiceId="Takumi")

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("makanko-no-lexicon.mp3").write_bytes(stream.read())

# Lexiconを使用
result = polly.synthesize_speech(
    Text=s, OutputFormat="mp3", VoiceId="Takumi",
    LexiconNames=[LEXICON])

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("makanko-with-lexicon.mp3").write_bytes(stream.read())
