from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client('polly')
s1 = "クリリンのことか……クリリンのことかーーーっ！！！！！"
# 間を開ける、呼吸音追加、強調する
s2 = ('<speak><p>クリリンのことか……</p>'
      '<amazon:breath duration="medium" volume="x-loud"/>'
      '<p><emphasis level="strong">クリリンのことかーーーっ！！！！！'
      '</emphasis></p></speak>')

result = polly.synthesize_speech(
    Text=s1, OutputFormat="mp3", VoiceId="Mizuki")

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("goku-anger1.mp3").write_bytes(stream.read())

result = polly.synthesize_speech(
    Text=s2, TextType="ssml", OutputFormat="mp3", VoiceId="Mizuki")

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("goku-anger2.mp3").write_bytes(stream.read())
