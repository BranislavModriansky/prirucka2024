from openai import OpenAI

client = OpenAI()

audio_file = open(r"C:\Users\modri\Downloads\OSR_us_000_0010_8k.wav", "rb")

transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)

# Write the transcription 'transcription.txt' into a file
with open("transcription_01.txt", "w", encoding="utf-8") as f:
    f.write(transcription)