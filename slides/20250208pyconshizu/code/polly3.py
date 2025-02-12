from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client('polly')

# speakタグとphonemeタグ
s = """<speak>
<phoneme type="ruby" ph="すーぱーぐれーと">S・G</phoneme>・
<phoneme type="ruby" ph="ごーるきーぱー">G・K</phoneme> 
若林源三。
</speak>"""

# 引数に TextType="ssml" を追加
result = polly.synthesize_speech(
    Text=s, TextType="ssml", OutputFormat="mp3", VoiceId="Takumi")

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("super-great.mp3").write_bytes(stream.read())
