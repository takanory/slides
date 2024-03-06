from contextlib import closing
from pathlib import Path
import boto3

polly = boto3.client('polly')  # クライアント作成
s = "zoom如きにやられるとはニューカマーのツラ汚しよ…"  # by masashinji

result = polly.synthesize_speech(
    Text=s, OutputFormat="mp3", VoiceId="Mizuki")  # テキストから音声を合成

# 音声を読み込んでファイルに保存
with closing(result["AudioStream"]) as stream:
    Path("masashinji.mp3").write_bytes(stream.read())
