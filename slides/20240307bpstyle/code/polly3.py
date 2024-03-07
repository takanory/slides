from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client('polly')  # クライアント作成
s = '<speak>時すでに<phoneme type="ruby" ph="おすし">🍣</phoneme>…</speak>'

result = polly.synthesize_speech(Text=s,
    TextType="ssml", OutputFormat="mp3", VoiceId="Takumi")

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("hajimo-osushi.mp3").write_bytes(stream.read())
