from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client('polly')

result = polly.synthesize_speech(
    Text="S・G・G・K 若林源三",
    OutputFormat="mp3", VoiceId="Takumi")

with closing(result["AudioStream"]) as stream:
    Path("sggk.mp3").write_bytes(stream.read())
