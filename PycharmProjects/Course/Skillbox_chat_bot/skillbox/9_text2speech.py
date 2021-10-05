import playsound
import gtts
import os


text = 'Привет!'

voice = gtts.gTTS(text, lang="ru")
audio_file = 'C:\\Users\\Владимир\\PycharmProjects\\pythonProject\\skillbox\\audio.mp3'
voice.save(audio_file)

playsound.playsound(audio_file)

os.remove(audio_file)
