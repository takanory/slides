from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client('polly')  # クライアント作成

result = polly.synthesize_speech(
    Text="時すでに🍣…", OutputFormat="mp3", VoiceId="Takumi")

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("hajimo.mp3").write_bytes(stream.read())
