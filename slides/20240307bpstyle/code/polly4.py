from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client('polly')  # クライアント作成
s1 = "mypy の目をたしょうごまかしてしまった..."

result = polly.synthesize_speech(Text=s1,
    OutputFormat="mp3", VoiceId="Mizuki")

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("fumi23.mp3").write_bytes(stream.read())

# 全体をx-slow、mypyに読み設定、「目を」のあとにbreak
s2 = ('<speak><prosody rate="x-slow">'
      '<phoneme type="ruby" ph="マイパイ">mypy</phoneme>の目を'
      '<break strength="x-strong"/>たしょうごまかしてしまった...'
      '</prosody></speak>')

result = polly.synthesize_speech(Text=s2,
    TextType="ssml", OutputFormat="mp3", VoiceId="Mizuki")

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("fumi23-ssml.mp3").write_bytes(stream.read())

