from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client("polly")
# I'd like to drink good beer today and tomorrow.
text = "今日も明日もおいしいビールを飲みたい"

result = polly.synthesize_speech(
    Text=text, OutputFormat="mp3", VoiceId="Mizuki")

with closing(result["AudioStream"]) as stream:
    Path("japanese.mp3").write_bytes(stream.read())
