from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client('polly')

s = ('<speak><phoneme type="ruby" ph="すーぱー">超</phoneme>'
     'サイヤ人孫悟空だ!!!!!</speak>')
result = polly.synthesize_speech(
    Text=s, TextType="ssml", OutputFormat="mp3", VoiceId="Takumi")

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("goku-super.mp3").write_bytes(stream.read())
