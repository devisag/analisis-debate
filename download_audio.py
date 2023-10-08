from pytube import YouTube

youtube_video_url = "https://www.youtube.com/watch?v=WqQxBpmvxfI"
youtube_video_content = YouTube(youtube_video_url)
audio = youtube_video_content.streams.get_audio_only()
audio.download(filename='tmp.mp4')