from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client('polly')

result = polly.synthesize_speech(
    Text="超サイヤ人孫悟空だ!!!!!",
    OutputFormat="mp3", VoiceId="Takumi")

with closing(result["AudioStream"]) as stream:
    Path("goku-cho.mp3").write_bytes(stream.read())
