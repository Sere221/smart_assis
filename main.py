import speech_recognition as sr
import sys
import webbrowser
import pyttsx3
from anecAPI import anecAPI
from datetime import datetime
import yaml
import openai
import pyautogui
import pyaudio
import random
import os

KEY = ""

openai.api_key = KEY

CMD_LIST = yaml.safe_load(
    open('commands.yaml', 'rt', encoding='utf8'),
)

ANS_LIST = yaml.safe_load(
    open('answers.yaml', 'rt', encoding='utf8'),
)


def talk(words):
    print(words)
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')  # Скорость произношения
    engine.setProperty('rate', rate + 10)
    engine.say(words)
    engine.runAndWait()


talk("Доброго времени вам суток, есть работа для меня?")


def generate_response(text):
    try:
        response = openai.Completion.create(
            prompt=text,
            engine='text-davinci-003',
            max_tokens=1000,
            temperature=0.1,
            n=1,
            stop=['_'],
            timeout=15
        )
        if response and response.choices:
            return response.choices[0].text.strip()
        else:
            return None
    except:
        return 'Искуственный интелект не работает)'


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        cmd = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + cmd)
    except sr.UnknownValueError:
        talk("Пожалуйста повтори!")
        cmd = command()

    return cmd


def makeSomething(cmd):
    if cmd in CMD_LIST['open_youtube']:
        talk(random.choice(ANS_LIST['open_site']))
        url = 'https://www.youtube.com/'
        webbrowser.open(url)

    elif cmd in CMD_LIST['open_yandex']:
        talk(random.choice(ANS_LIST['open_site']))
        url = 'https://ya.ru/'
        webbrowser.open(url)

    elif cmd in CMD_LIST['stupid']:
        talk(random.choice(ANS_LIST['sorry']))

    elif cmd in CMD_LIST['thanks']:
        talk(random.choice(ANS_LIST['thanks']))

    elif cmd in CMD_LIST['off']:
        talk(random.choice(ANS_LIST['bye']))
        sys.exit()

    elif cmd in CMD_LIST['name']:
        talk(random.choice(ANS_LIST['my_name']))

    elif cmd in CMD_LIST['joke']:
        talk(anecAPI.random_joke())

    elif cmd in CMD_LIST['time']:
        now = datetime.now()
        cur_time = now.strftime("%d.%m.%y\n"
                                "%H:%M")
        talk(f"Сейчас {cur_time}")

    elif cmd in CMD_LIST['cats']:
        talk(random.choice(ANS_LIST['cats']))

    elif cmd in CMD_LIST['playpause']:
        pyautogui.press('playpause')
        talk(random.choice(ANS_LIST['open_site']))

    elif cmd in CMD_LIST['sound_off']:
        talk(random.choice(ANS_LIST['open_site']))
        pyautogui.press('volumedown', presses=50)

    elif cmd in CMD_LIST['sound_on']:
        pyautogui.press('volumeup', presses=10)
        talk(random.choice(ANS_LIST['open_site']))

    elif cmd in CMD_LIST['sound_on_max']:
        pyautogui.press('volumeup', presses=50)
        talk(random.choice(ANS_LIST['open_site']))

    elif cmd in CMD_LIST['music_play']:
        music_dir = "C:\\Users\\Sere\\Desktop\\MuzicPK"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[1]))

    else:
        res = generate_response(cmd)
        talk(res)


while True:
    makeSomething(command())
