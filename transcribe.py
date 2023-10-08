import whisper
import ffmpeg

model = whisper.load_model("base")
path = "C:/Users/alejo/OneDrive/Escritorio/analisis-discurso/dowloads/audio.mp4"

result = model.transcribe(path, fp16=False, verbose=True)
print(result["text"])
