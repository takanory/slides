from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client('polly')  # クライアント作成

# Lexiconを名前をつけて登録
LEXICON = "tennolexicon"
data = Path("tenno-lexicon.xml").read_text(encoding="utf-8")
polly.put_lexicon(Name=LEXICON, Content=data)

s = "yukieは実質天皇（）"
# Lexiconを使用しない
result = polly.synthesize_speech(Text=s,
    OutputFormat="mp3", VoiceId="Mizuki")

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("yukie.mp3").write_bytes(stream.read())

# Lexiconを使用
result = polly.synthesize_speech(Text=s,
    OutputFormat="mp3", VoiceId="Mizuki",
    LexiconNames=[LEXICON])

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("yukie-emperor.mp3").write_bytes(stream.read())
