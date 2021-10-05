# Качать файл .whl Pyaudio на Win10 , затем pip install some-file.whl в той папке, где файл
# Библиотеки скачать pip install SpeechRecognition playsound gTTS
import os
import gtts
import playsound
import speech_recognition as sr


def user_input():
    print("Скажите что-нибудь >>>")


    voice_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Микрофон захвачен
        audio = voice_recognizer.listen(source) #  Запись вашего голоса
    # Микрофон снова доступен другим программам

    voice_text = voice_recognizer.recognize_google(audio, language="ru") #  Распознавание вашего голоса


    print("Вы сказали:", voice_text)

    return voice_text # сохранение переменной


def reply(text): #Функция, связанная с голосом ассистента (голосового помошника)

    print("Ассистент:", text) #Переменную задаем в функции handle_command(user_text):

    voice = gtts.gTTS(text, lang="ru") #Хранит файл голоса
    audio_file = '..\\audio.mp3' #путь к файлу
    voice.save(audio_file) #Записывает файл

    playsound.playsound(audio_file) #Проигрывает файл
    os.remove(audio_file) #Удаляет файл


def handle_command(user_text): # Функция задает условия, при которых ассистент тебе ответит
    user_text = user_text.lower()  # для соответствия написанию реплик с маленькой буквы

    if user_text == 'привет':
        reply('Привет-привет!')
    elif user_text == 'пока':
        reply('До скорого!')
        exit()  # <-- добавили сюда код выхода из функции
    elif user_text == 'закажи еду':
        reply('Пиццу или борщ?')
    else:
        reply("Не понимаю вас")


def start():
    while True:
        user_text = user_input()
        handle_command(user_text)


start()
