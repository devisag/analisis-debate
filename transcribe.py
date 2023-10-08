import whisper

model = whisper.load_model("small")
result = model.transcribe('tmp.mp4')
print(result['text'])
with open("transcript.txt", "w") as file:
    file.write(result["text"])
