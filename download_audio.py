from pytube import YouTube
import whisper

youtube_video_url = "https://www.youtube.com/watch?v=WqQxBpmvxfI"
youtube_video_content = YouTube(youtube_video_url)
audio = youtube_video_content.streams.get_audio_only()
audio.download(filename='tmp.mp4')

model = whisper.load_model("small")
result = model.transcribe('tmp.mp4')
print(result['text'])