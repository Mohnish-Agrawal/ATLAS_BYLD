from pydub import AudioSegment
from gtts import gTTS
import os

# AudioSegment.converter = "C:\\Program Files\\ffmpeg-20200721-b5f1e05-win64-static\\bin\\ffmpeg.exe"
# AudioSegment.ffmpeg = "C:\\Program Files\\ffmpeg-20200721-b5f1e05-win64-static\\bin\\ffmpeg.exe"
# AudioSegment.ffprobe = "C:\\Program Files\\ffmpeg-20200721-b5f1e05-win64-static\\bin\\ffprobe.exe"
def speak(reply):
	tts=gTTS(reply)
	tts.save("good.mp3")

	sound=AudioSegment.from_mp3("good.mp3")
	sound.export("good.wav", format="wav")

	os.system("good.wav")
