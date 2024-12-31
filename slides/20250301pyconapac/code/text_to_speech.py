import sys
import boto3

polly = boto3.client("polly")

def text_to_speech(text: str) -> None:
    result = polly.synthesize_speech(
        Text=text, OutputFormat="mp3", VoiceId="Mizuki")
    with open("japanese.mp3", "wb") as f:
        f.write(result["AudioStream"].read())

if __name__ == "__main__":
    text_to_speech(sys.argv[1])
