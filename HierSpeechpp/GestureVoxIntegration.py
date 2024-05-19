"""
C struct definitions credit
Author: trungkienbkhn   (https://github.com/trungkienbkhn)
Source: https://github.com/SYSTRAN/faster-whisper
"""
import pvporcupine # 2.2.1
import pyautogui
import Test_bluet
import Voice_new_commands_start_now
import psutil
import re
import asyncio
import numpy as np
import wave
from pydub import AudioSegment
from pydub.playback import play
import pyaudio
from faster_whisper import WhisperModel
import Jarvis_Voice
import Steam_games
import keyboard as keyb
from pygame import mixer
import Wheather_and_time
import Your_name
import configs
import time
from num2words import num2words
import sys
import os
from sound import Sound  # будем использовать статические функции класса Sound
import pycaw
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from comtypes import CLSCTX_ALL
import pygetwindow as gw
from pycaw.pycaw import (
    AudioUtilities,
    IAudioEndpointVolume
)#pyinstaller -F -i "C:\Users\Sergey\Desktop\ВАНЯ\10010110\Atom.ico" Voice_Test_II.py
import webbrowser
from ctypes import POINTER, cast
import pycaw
from rich import print
from fuzzywuzzy import fuzz
import json
import struct
# from gtts import gTTS
import subprocess
# import openai
from g4f.client import Client
import simpleaudio as sa #///
import random
# import vosk
# import tts_test
import Test_To_Speach
import yaml
import queue
from pvrecorder import PvRecorder
import speech_recognition as sr
import threading
from Python.Tect_OpenCV_for_project import Hotkey_press
# import inference
import FIVferen
from moviepy.editor import AudioFileClip
import YouTubePlyatlist
import screen_brightness_control as sbc
from PIL import Image, ImageTk
import ffmpeg
import pygame
import customtkinter as ctk
client = Client()
# from Python.Tect_OpenCV_for_project.OpenCV_plus_ultra import Last
porcupine = pvporcupine.create(
    access_key=configs.picovoice_token,
    keywords=['jarvis'],
    sensitivities=[1]
)

message_log = [
    {"role": "system", "content": "You're the voice assistant."}
]
# model = vosk.Model("vosk-model-en-us-0.22-lgraph")
samplerate = 16000
# kaldi_rec = vosk.KaldiRecognizer(model, samplerate)
q = queue.Queue()
# rec = sr.Recognizer()
first_request = True
# openai.api_key = configs.api_key
low_battery_say = False

commands_dict = {
    "commands": {
        # "google": ["open google", "the open google", "Open Google.", " open google"],
        # "firefox": ["open firefox", "the open firefox"],
        "off": ["switch off", "turn off", "turning off", "turn of", "during of", "during of", "the switch of", "power off", "turn up",],
        "sound_off": ["mute it", "mute the sound", "muted", "muse it"],
        "sound_on": ["turn up the sound", "turn the sound up", "turn of the sound", "turns the sound up"],
        # "tanks": ["включи танчики"],
        # "telegram": ["включи телеграм", "включи телеграмм", "открой телеграм", "открой телеграмм"],
        "rob_R": ["go to work", "go into work mode", "the goal to work", "go to work!"],
        # "tinkerkad": ["перейди в тинкеркад", "активируй тинкеркад", "открой тинкеркад", "открой тинк", "открой тинг"],
        # "open_youtube": ["open youtube", "activate youtube"],
        # "Photoshop": ["перейди в фотошоп", "активируй фотошоп", "открой фотошоп", "адоб"],
        # "PrimePro": ["перейди в адобе премьер про", "активируй адобе премьер про", "открой адобе премьер про", "адоб п"],
        # "VSC": ["перейди в виескод", "активируй виескод", "открой виескод"],
        # "Unity": ["перейди в юнити", "активируй юнити", "открой юнити"],
        # "Minecraft": ["перейди в майнкрафт", "активируй майнкрафт", "открой майнкрафт"],
        # "MainFolder": ["go to explorer", "activate the explorer", "go into explorer", "go to explore"],
        # "SverVse": ["roll down all the windows", "roll down", "are all down"],
        # "SverVseKrom": ["roll everything but", "roll everything except"],
        # "RosrVse": ["roll up all the windows", "turn everything around", "turn it all around", "turn it around",  "roll up"],
        # "Settings": ["go to settings", "activate settings", "go into settings"],
        # "SettingGame": ["go to the game settings", "activate the game settings", "go to game settings"],
        # "BustBlu": ["подключи блютуз", "бысторе подключение по блютузу", "по блт", "по белта", "по бы алтая"],
        # "StopBustBlu": ["отключи блютуз", "откл блютузу", "откл длт", "отключи б", "отключи бе"],
        # "OPENAI_Prog": ["открой чат джипити", "открой чат", "активируй чат", "открой нейросеть", "активируй нейросеть", "активирую чат", "активирую нейросеть"],
        # "Sdel_Zad": ["дело", "записуй", "напоминание"],
        "Volum_0-100": ["volume", "audio", "tone", "buzz", "alger"],
        "brightness_0-100": ["brilliance", "brightness", "luminosity", "luminance", "lumin"],
        "Clothe": ["close", "shut", "lock"],
        "Open": ["open", "unlock", "open up", "open it"],
        # "Sdel_del_text": ["очистить файл", "очистка", "очищение"],
        # "Pon_del_Zad": ["удалить файл", "удаление", "формат"],
        # "Open_Zad": ["открой файл", "открыть дела", "открыть напоминания"],
        # "Close_Zad": ["закрой файл", "закрыть"],
        "Steam": ["open up the steam", "steam", "open steam"],
        # "Cyberpunk_2077": ["открой киберпанк", "открой кб", "открой кибер панк две тисячи семдесят семь"],
        # "Dying_light_2": ["открой дайн лайт", "открой дн", "открой дайн лайт два", "открой дань лайт", "открой дэн"],
        "Terarria": ["open a terraria", "open a therraria", "therraria", "terraria"],
        # "Wallpeper_Engine": ["open the background", "background", "open zebra ground", "ground", "the ground"],
        "Razer_Vkl": ["plug in the headphones", "put your headphones on", "turn on your headphones", "headphones", "headphone"],
        "Opus_Vukl": ["unplug the headphones", "turn off the headphones", "turn the headphones off", "unplug"],
        # "Rand": ["рандом", "рандомные имена", "рандомайзер"],
        "LevelBattery": ["level battery", "level bettering", "I'll have all the battery", "battery", "level batery", "batery", "batery level", "battery level"],
        "Music_play_vrem": ["music", "Music"],
        "Pause_play_vrem": ["pause music", "Pause music", "bounce music", "False mizzou", "Follow smith", "Bao's music", "Bowser music", "Boss music", "off music", "bowl's music", "Follow some music"],
        "Сontinued_Pause_play_vrem": ["continued ", "Сontinued", "continue ", "Сontinue"],
        "Stop_play_vrem": ["stop music", "Stop music", "stop it", "stop using"],
        "Next": ["next music", "next", "next videos", "next news", "The next wizard"],
        "Previous": ["previous music", "prev music", "previous videos", "previous news", "Pre-guess music"],
        "Console": ["Console", "console", "And silent", "Cancelling", "Can't sell ya", "and solo"],
        "ListenPlayList": ["listen play list", "listen playlist", "playlist", "play list", "awesome playlist", "or listen to the playlist", "lesson playlist"],
        "Add_Music_Playlist": ["add music", "new music", "add playlist", "add play list", "create new music", "create music"],
        "Dell_Playlist": ["dell music", "delete music", "remove playlist", "delete playlist", "dell playlist", "remove music"],
        "Time": ["time now", "time", "now time", "current time", "Carrying time"],
        "Wheather": ["weather", "weather now", "now weather", "current weather"],
        "Wide_Mode": ["expanded mode", "advanced mode", "wide mode", "advanced mode"]
    }
}
num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'twenty one': 21, 'twenty two': 22, 'twenty three': 23, 'twenty four': 24, 'twenty five': 25, 'twenty six': 26, 'twenty seven': 27, 'twenty eight': 28, 'twenty nine': 29, 'thirty': 30, 'thirty one': 31, 'thirty two': 32, 'thirty three': 33, 'thirty four': 34, 'thirty five': 35, 'thirty six': 36, 'thirty seven': 37, 'thirty eight': 38, 'thirty nine': 39, 'forty': 40, 'forty one': 41, 'forty two': 42, 'forty three': 43, 'forty four': 44, 'forty five': 45, 'forty six': 46, 'forty seven': 47, 'forty eight': 48, 'forty nine': 49, 'fifty': 50, 'fifty one': 51, 'fifty two': 52, 'fifty three': 53, 'fifty four': 54, 'fifty five': 55, 'fifty six': 56, 'fifty seven': 57, 'fifty eight': 58, 'fifty nine': 59, 'sixty': 60, 'sixty one': 61, 'sixty two': 62, 'sixty three': 63, 'sixty four': 64, 'sixty five': 65, 'sixty six': 66, 'sixty seven': 67, 'sixty eight': 68, 'sixty nine': 69, 'seventy': 70, 'seventy one': 71, 'seventy two': 72, 'seventy three': 73, 'seventy four': 74, 'seventy five': 75, 'seventy six': 76, 'seventy seven': 77, 'seventy eight': 78, 'seventy nine': 79, 'eighty': 80, 'eighty one': 81, 'eighty two': 82, 'eighty three': 83, 'eighty four': 84, 'eighty five': 85, 'eighty six': 86, 'eighty seven': 87, 'eighty eight': 88, 'eighty nine': 89, 'ninety': 90, 'ninety one': 91, 'ninety two': 92, 'ninety three': 93, 'ninety four': 94, 'ninety five': 95, 'ninety six': 96, 'ninety seven': 97, 'ninety eight': 98, 'ninety nine': 99, 'one hundred': 100}
# num_dict = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10, 'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20, 'двадцать один': 21, 'двадцать два': 22, 'двадцать три': 23, 'двадцать четыре': 24, 'двадцать пять': 25, 'двадцать шесть': 26, 'двадцать семь': 27, 'двадцать восемь': 28, 'двадцать девять': 29, 'тридцать': 30, 'тридцать один': 31, 'тридцать два': 32, 'тридцать три': 33, 'тридцать четыре': 34, 'тридцать пять': 35, 'тридцать шесть': 36, 'тридцать семь': 37, 'тридцать восемь': 38, 'тридцать девять': 39, 'сорок': 40, 'сорок один': 41, 'сорок два': 42, 'сорок три': 43, 'сорок четыре': 44, 'сорок пять': 45, 'сорок шесть': 46, 'сорок семь': 47, 'сорок восемь': 48, 'сорок девять': 49, 'пятьдесят': 50, 'пятьдесят один': 51, 'пятьдесят два': 52, 'пятьдесят три': 53, 'пятьдесят четыре': 54, 'пятьдесят пять': 55, 'пятьдесят шесть': 56, 'пятьдесят семь': 57, 'пятьдесят восемь': 58, 'пятьдесят девять': 59, 'шестьдесят': 60, 'шестьдесят один': 61, 'шестьдесят два': 62, 'шестьдесят три': 63, 'шестьдесят четыре': 64, 'шестьдесят пять': 65, 'шестьдесят шесть': 66, 'шестьдесят семь': 67, 'шестьдесят восемь': 68, 'шестьдесят девять': 69, 'семьдесят': 70, 'семьдесят один': 71, 'семьдесят два': 72, 'семьдесят три': 73, 'семьдесят четыре': 74, 'семьдесят пять': 75, 'семьдесят шесть': 76, 'семьдесят семь': 77, 'семьдесят восемь': 78, 'семьдесят девять': 79, 'восемьдесят': 80, 'восемьдесят один': 81, 'восемьдесят два': 82, 'восемьдесят три': 83, 'восемьдесят четыре': 84, 'восемьдесят пять': 85, 'восемьдесят шесть': 86, 'восемьдесят семь': 87, 'восемьдесят восемь': 88, 'восемьдесят девять': 89, 'девяносто': 90, 'девяносто один': 91, 'девяносто два': 92, 'девяносто три': 93, 'девяносто четыре': 94, 'девяносто пять': 95, 'девяносто шесть': 96, 'девяносто семь': 97, 'девяносто восемь': 98, 'девяносто девять': 99, 'сто': 100}
close_dict = {'steam': 0, 'ground': 1, "Pycharm": 2, "Photoshop": 3, "firefox": 4, "google": 5, "telegram": 6, "terraria": 7}
open_dict = {'steam': 0, 'ground': 1, "Pycharm": 2, "Photoshop": 3, "firefox": 4, "google": 5, "telegram": 6, "terraria": 7, "explorer": 8, "settings": 9}

commands_dict_openai = {
    "commands": {
        "INPUT_KEY": {"who": 0, "where ": 1, "how": 2, "when": 3, "wine": 4}
    }
}


def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002500-\U00002BEF"
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"
                               u"\u3030"
                               u"\uff89"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)
def OpenCV_plus_ultra():
    subprocess.run(["python", r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\OpenCV_plus_ultra.py"])
def time_sleep_threading(VotTime):
    print(VotTime)
    time.sleep(VotTime)
def settext(text):
    with open("example/text.txt", 'w', encoding='utf-8') as file:
        file.write(text)

def get_battery_level():
    battery = psutil.sensors_battery()
    if battery is not None:
        # Уровень заряда батареи в процентах
        battery_percent = battery.percent
        return battery_percent
    else:
        return "Battery information not available."

def stop_playback_and_delete(folder_path):
    global music_paused, current_track, accumulated_time

    # Останавливаем воспроизведение музыки, если оно активно
    pygame.mixer.music.stop()

    # Удаляем текущий трек, если он есть
    if current_track:
        os.remove(os.path.join(folder_path, current_track))
        print(f"Текущий трек {current_track} был удален.")
        current_track = None
def delete_files_in_folder(folder_path):
    files = os.listdir(folder_path)

    if files:
        for file in files:
            file_path = os.path.join(folder_path, file)

            try:
                # Принудительно удаляем файл без проверки на использование процессом
                os.remove(file_path)
                print(f"Файл {file} был принудительно удален.")
            except Exception as e:
                print(f"Ошибка при удалении файла {file}: {e}")
                continue

    else:
        print("Нет файлов для удаления в этой папке.")
# def play_music_here(file_path):
#     try:
#         pygame.mixer.music.load(file_path)
#         pygame.mixer.music.play()
#
#         # Ожидаем окончания воспроизведения
#         while pygame.mixer.music.get_busy():
#             time.sleep(0.1)  # Пауза в основном потоке
#
#     except pygame.error as e:
#         print(f"Ошибка при воспроизведении файла {file_path}: {e}")
#         retry_count = 0
#         max_retries = 3
#
#         while retry_count < max_retries:
#             retry_count += 1
#             print(f"Попытка повторной загрузки и воспроизведения (попытка {retry_count}/{max_retries})...")
#             time.sleep(1)  # Пауза перед повторной попыткой
#             try:
#                 pygame.mixer.music.load(file_path)
#                 pygame.mixer.music.play()
#                 break  # Выход из цикла, если воспроизведение успешно
#             except pygame.error as e:
#                 print(f"Ошибка при повторной загрузке и воспроизведении (попытка {retry_count}/{max_retries}): {e}")
#
#
# music_paused = False
# current_track = None
# accumulated_time = 0  # Общее накопленное время воспроизведения
# music_next = False
# mp3file = ''
# mp3_files = ''
# mp33_files = ''
# def play_mp3_files_in_folder(mp3_files_test):
#     global music_paused, current_track, accumulated_time, mp3file, mp3_files, mp33_files
#     folder_path = r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist"
#     files = os.listdir(folder_path)
#     mp3_files = [f for f in files if f.endswith('.mp3')]
#     print(f"Current track: {current_track}")
#     print(f"mp3_files{mp3_files}")
#     print(f"mp3_files_test{mp3_files_test}")
#     print(len(mp3_files), len(mp3_files_test))
#     if len(mp3_files_test) < len(mp3_files):
#         mp3_files = mp3_files_test
#         print(f"1111111111{mp3_files}")
#         if mp3_files:
#             pygame.mixer.init()
#             for mp3_file in mp3_files:
#                 mp3file = mp3_file
#                 if music_paused:
#                     # Если музыка на паузе, ждем пока не будет возобновлена
#                     while music_paused:
#                         pygame.time.wait(100)
#                     # Возобновляем воспроизведение с накопленного времени
#                     mp3_file = current_track
#                     print(f"Current track: {current_track}")
#                 else:
#                     # Сохраняем текущий трек
#                     print(f"Current track: {current_track}")
#                     current_track = mp3_file
#                     accumulated_time = 0  # Сбрасываем накопленное время для нового трека
#                 # Воспроизведение музыки
#                 mp3_file_path = os.path.join(folder_path, mp3_file)
#                 try:
#                     play_music_here(mp3_file_path)
#                     # Ожидаем окончания воспроизведения текущего трека
#                     while pygame.mixer.music.get_busy():
#                         time.sleep(0.1)
#                 except pygame.error as e:
#                     print(f"Не удалось загрузить {mp3_file}: {e}")
#                     # Попытка повторной загрузки файла
#                     time.sleep(1)  # небольшая задержка перед повторной попыткой
#                     pygame.mixer.music.load(mp3_file_path)
#     elif len(mp3_files_test) == len(mp3_files):
#         mp33_files = mp3_files
#         if mp3_files:
#             pygame.mixer.init()
#             for mp3_file in mp3_files:
#                 mp3file = mp3_file
#                 if music_paused:
#                     # Если музыка на паузе, ждем пока не будет возобновлена
#                     while music_paused:
#                         pygame.time.wait(100)
#                     # Возобновляем воспроизведение с накопленного времени
#                     mp3_file = current_track
#                 else:
#                     # Сохраняем текущий трек
#                     current_track = mp3_file
#                     accumulated_time = 0  # Сбрасываем накопленное время для нового трека
#
#                 # Воспроизведение музыки
#                 mp3_file_path = os.path.join(folder_path, mp3_file)
#
#                 try:
#                     play_music_here(mp3_file_path)
#                     # Ожидаем окончания воспроизведения текущего трека
#                     while pygame.mixer.music.get_busy():
#                         time.sleep(0.1)
#                 except pygame.error as e:
#                     print(f"Не удалось загрузить {mp3_file}: {e}")
#                     # Попытка повторной загрузки файла
#                     time.sleep(1)  # небольшая задержка перед повторной попыткой
#                     pygame.mixer.music.load(mp3_file_path)
# Инициализация микшера
mixer.init()

# Путь к директории с музыкальными файлами
music_directory = r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist"

# Список музыкальных файлов
current_track = 0


# Функция воспроизведения музыки
def play_music():
    global current_track
    playlist = [f for f in os.listdir(music_directory) if f.endswith('.mp3')]
    mixer.music.load(os.path.join(music_directory, playlist[current_track]))
    mixer.music.play()


# Функция паузы
def pause_music():
    mixer.music.pause()


# Функция продолжения воспроизведения
def unpause_music():
    mixer.music.unpause()


# Функция переключения на следующий трек
def next_track():
    global current_track
    playlist = [f for f in os.listdir(music_directory) if f.endswith('.mp3')]
    current_track = (current_track + 1) % len(playlist)
    play_music()


# Функция остановки воспроизведения
def stop_music():
    mixer.music.stop()


# Функция переключения на предыдущий трек
def previous_track():
    global current_track
    playlist = [f for f in os.listdir(music_directory) if f.endswith('.mp3')]
    current_track = (current_track - 1) % len(playlist)
    play_music()


def convert_mp4_to_mp3(folder_path):
    # Найдем первый .mp4 файл в папке
    files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]
    if files:
        video_file = os.path.join(folder_path, files[0])
        output_file = video_file.replace('.mp4', '.mp3')

        # Конвертируйте аудио в .mp3 с помощью ffmpeg
        ffmpeg.input(video_file).output(output_file, acodec='libmp3lame').run()

        print(f"Файл {output_file} успешно создан.")
    else:
        print("В папке нет файлов .mp4")

def play_music_now():
    global audio_clip
    folder_path = r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist_vrem"
    convert_mp4_to_mp3(folder_path)
    # Получаем список файлов в папке
    # Получаем список файлов в указанной папке
    files = os.listdir(folder_path)

    # Находим первый файл с расширением .mp3
    mp3_files = [f for f in files if f.endswith('.mp3')]

    if mp3_files:
        # Получаем путь к первому найденному файлу .mp3
        mp3_file_path = os.path.join(folder_path, mp3_files[0])

        # Проигрываем аудио
        pygame.mixer.init()
        pygame.mixer.music.load(mp3_file_path)
        pygame.mixer.music.play()

def play_audio_prost():
    file_name = "C:/Users/IVNsell/Desktop/IVNsell/Python/GestureVox Integration/Modern_GUI_PyDracula_PySide6_or_PyQt6-master/HierSpeechpp/HierSpeechpp/output/reference_1.wav"
    while not os.path.exists(file_name):  # Пока файл не существует
        print(f"File {file_name} not found. Waiting for file to appear...")
        time.sleep(0.1)  # Добавляем небольшую задержку перед следующей попыткой проверки

    # Как только файл появится, проигрываем его
    print(f"File {file_name} found. Playing audio...")
    play_audio_file_prost(file_name)

def play_audio_file_prost(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def del_mp4_In_mp3(directory):
    # Получаем список файлов в директории
    files = os.listdir(directory)

    # Удаляем файлы с расширением .mp4
    for file in files:
        if file.endswith(".mp4"):
            file_path = os.path.join(directory, file)
            os.remove(file_path)
            print(f"File {file} removed.")

def window_delete_musik():
    ctk.set_appearance_mode("dark")  # Темная тема
    ctk.set_default_color_theme("green")  # Зеленая цветовая схема

    app = ctk.CTk()
    app.geometry("600x300")
    app.title(" Delete music Task App")
    # Установка логотипа (путь к файлу логотипа должен быть корректным)
    app.iconbitmap(r"images\images\Logo.ico")

    # Центрирование окна на экране
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    center_x = int(screen_width / 2 - 600 / 2)
    center_y = int(screen_height / 2 - 300 / 2)
    app.geometry(f"+{center_x}+{center_y}")

    # Создание фрейма для содержимого с закругленными углами
    content_frame = ctk.CTkFrame(app, corner_radius=10)
    content_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def toggle_theme():
        # Переключение темы с темной на светлую и обратно
        current_mode = ctk.get_appearance_mode()
        if current_mode == "Dark":
            ctk.set_appearance_mode("Light")
            toggle_theme_button.configure(image=sun_image)  # Изменение иконки на солнце
        else:
            ctk.set_appearance_mode("Dark")
            toggle_theme_button.configure(image=moon_image)  # Изменение иконки на луну

    def on_enter_pressed(event=None):
        # Вывод текста в консоль при нажатии Enter
        task_text = new_task_entry.get()
        if task_text:
            print(task_text)

            def delete_files_with_fuzzy_search(directory, search_term, threshold=70, prev_max_ratio=101):
                files_deleted = 0
                files_checked = 0
                max_ratio_file = None
                max_ratio = 0

                for filename in os.listdir(directory):
                    file_path = os.path.join(directory, filename)
                    if os.path.isfile(file_path):
                        files_checked += 1
                        file_name = os.path.basename(file_path)
                        ratio = fuzz.ratio(search_term.lower(), file_name.lower())
                        if ratio >= threshold:
                            # os.remove(file_path)
                            # print(f"Deleted file: {file_name} (Ratio: {ratio})")
                            files_deleted += 1
                        if ratio > max_ratio and ratio < prev_max_ratio:
                            max_ratio = ratio
                            max_ratio_file = file_path
                            max_ratio_file_name = file_name

                print(f"Total files checked: {files_checked}")
                print(f"Total files deleted: {files_deleted}")
                print(
                    f"\nThe file with the highest similarity ratio is: {max_ratio_file_name} (Ratio: {max_ratio})")
                # num = 1
                text_mus = remove_emojis(max_ratio_file_name)
                FIVferen.Play_musc_prost_text_mus(text_mus)
                # settext(f"Name of yout music: {text_mus}? It's that music?")
                # inference.main(num, 'output')
                play_audio_prost()

                def is_silent(data, threshold=500):
                    """Check if the audio chunk is silent based on the threshold."""
                    return np.max(data) < threshold

                def record_chunk(p, stream, file_path, silence_threshold=1):
                    frames = []
                    start_time = None
                    silence_start = None

                    while True:
                        data = stream.read(1024)
                        audio_data = np.frombuffer(data, dtype=np.int16)

                        if not is_silent(audio_data):
                            if start_time is None:
                                start_time = time.time()  # Начало говорения
                            frames.append(data)
                            silence_start = None  # Reset silence start time
                        elif start_time is not None:
                            if silence_start is None:
                                silence_start = time.time()  # Start of silence
                            elif time.time() - silence_start > silence_threshold:
                                # End of speech detected
                                end_time = time.time()
                                chunk_length = end_time - start_time
                                print(f"Chunk length: {chunk_length} seconds")
                                break

                    if frames:
                        frames = b''.join(frames)
                        wf = wave.open(file_path, 'wb')
                        wf.setnchannels(1)
                        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
                        wf.setframerate(16000)
                        wf.writeframes(frames)
                        wf.close()
                        print(f"Recorded chunk saved to {file_path}")
                    else:
                        print("Silent chunk ignored")

                def transcribe_chunk(model, chunk_file):
                    segments, info = model.transcribe(chunk_file, language="en", beam_size=20, vad_filter=True,
                                                      condition_on_previous_text=False)
                    # print("5555555555555")
                    # print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

                    transcription = ' '.join(segment.text for segment in segments)
                    return transcription

                chunk_file = "temp_chunk_music.wav"
                waiting_for_response = True
                p = pyaudio.PyAudio()
                stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
                while waiting_for_response:
                    record_chunk(p, stream, chunk_file)
                    if os.path.exists(chunk_file):  # Проверяем, существует ли файл перед транскрибацией
                        transcription = transcribe_chunk(model, chunk_file)
                        transcription = transcription.lower()
                        print("|||||||||||||||||||||||||||||||||||")
                        print(transcription)
                        print("|||||||||||||||||||||||||||||||||||")
                        if fuzz.ratio(transcription, "yes") > 60:
                            print("Yes.")
                            os.remove(max_ratio_file)
                            with open('settings.json', 'r', encoding='utf-8') as json_file:
                                data = json.load(json_file)
                            data["Music_DELL"] = max_ratio_file_name
                            with open('settings.json', 'w') as json_file:
                                json.dump(data, json_file, indent=4)
                            print(f"Deleted file: {max_ratio_file_name} (Ratio: {max_ratio})")
                            waiting_for_response = False  # Останавливаем ожидание ответа
                            break
                        elif fuzz.ratio(transcription, "no") > 60:
                            print("No.")
                            delete_files_with_fuzzy_search(directory, search_term, threshold, max_ratio)
                            waiting_for_response = False  # Останавливаем ожидание ответа
                            break
                        elif fuzz.ratio(transcription, "exit") > 60:
                            print("Exit.")
                            close_program()
                            return
                # while True:
                #     user_input = input(
                #         "Is this the file you want to delete? (Type 'Yes' to delete, 'No' to check another file, or 'Exit' to quit): ")
                #     if user_input.lower() == 'yes':
                #         os.remove(max_ratio_file)
                #         print(f"Deleted file: {max_ratio_file_name} (Ratio: {max_ratio})")
                #         break
                #     elif user_input.lower() == 'no':
                #         delete_files_with_fuzzy_search(directory, search_term, threshold, max_ratio)
                #         break
                #     elif user_input.lower() == 'exit':
                #         return
                # if max_ratio_file:
                #     print(
                #         f"\nThe file with the highest similarity ratio is: {file_name} (Ratio: {max_ratio})")
                #     # num = 1
                #     text_mus = remove_emojis(file_name)
                #     FIVferen.Play_musc_prost_text_mus(text_mus)
                #     # settext(f"Name of yout music: {text_mus}? It's that music?")
                #     # inference.main(num, 'output')
                #     play_audio_prost()
                #     def is_silent(data, threshold=500):
                #         """Check if the audio chunk is silent based on the threshold."""
                #         return np.max(data) < threshold
                #
                #     def record_chunk(p, stream, file_path, silence_threshold=1):
                #         frames = []
                #         start_time = None
                #         silence_start = None
                #
                #         while True:
                #             data = stream.read(1024)
                #             audio_data = np.frombuffer(data, dtype=np.int16)
                #
                #             if not is_silent(audio_data):
                #                 if start_time is None:
                #                     start_time = time.time()  # Начало говорения
                #                 frames.append(data)
                #                 silence_start = None  # Reset silence start time
                #             elif start_time is not None:
                #                 if silence_start is None:
                #                     silence_start = time.time()  # Start of silence
                #                 elif time.time() - silence_start > silence_threshold:
                #                     # End of speech detected
                #                     end_time = time.time()
                #                     chunk_length = end_time - start_time
                #                     print(f"Chunk length: {chunk_length} seconds")
                #                     break
                #
                #         if frames:
                #             frames = b''.join(frames)
                #             wf = wave.open(file_path, 'wb')
                #             wf.setnchannels(1)
                #             wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
                #             wf.setframerate(16000)
                #             wf.writeframes(frames)
                #             wf.close()
                #             print(f"Recorded chunk saved to {file_path}")
                #         else:
                #             print("Silent chunk ignored")
                #
                #     def transcribe_chunk(model, chunk_file):
                #         segments, info = model.transcribe(chunk_file, language="en", beam_size=20, vad_filter=True,
                #                                           condition_on_previous_text=False)
                #         # print("5555555555555")
                #         # print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
                #
                #         transcription = ' '.join(segment.text for segment in segments)
                #         return transcription
                #
                #     chunk_file = "temp_chunk_music.wav"
                #     waiting_for_response = True
                #     p = pyaudio.PyAudio()
                #     stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
                #     while waiting_for_response:
                #         record_chunk(p, stream, chunk_file)
                #         if os.path.exists(chunk_file):  # Проверяем, существует ли файл перед транскрибацией
                #             transcription = transcribe_chunk(model, chunk_file)
                #             transcription = transcription.lower()
                #             print("|||||||||||||||||||||||||||||||||||")
                #             print(transcription)
                #             print("|||||||||||||||||||||||||||||||||||")
                #             if fuzz.ratio(transcription, "yes") > 60:
                #                 print("Yes.")
                #                 os.remove(max_ratio_file)
                #                 print(f"Deleted file: {file_name} (Ratio: {max_ratio})")
                #                 waiting_for_response = False  # Останавливаем ожидание ответа
                #                 break
                #             elif fuzz.ratio(transcription, "no") > 60:
                #                 print("No.")
                #                 delete_files_with_fuzzy_search(directory, search_term, threshold, max_ratio)
                #                 waiting_for_response = False  # Останавливаем ожидание ответа
                #                 break
                #             elif fuzz.ratio(transcription, "exit") > 60:
                #                 print("Exit.")
                #                 close_program()
                #                 return
                #     # while True:
                #     #     user_input = input(
                #     #         "Is this the file you want to delete? (Type 'Yes' to delete, 'No' to check another file, or 'Exit' to quit): ")
                #     #     if user_input.lower() == 'yes':
                #     #         os.remove(max_ratio_file)
                #     #         print(f"Deleted file: {max_ratio_file_name} (Ratio: {max_ratio})")
                #     #         break
                #     #     elif user_input.lower() == 'no':
                #     #         delete_files_with_fuzzy_search(directory, search_term, threshold, max_ratio)
                #     #         break
                #     #     elif user_input.lower() == 'exit':
                #     #         return
                #
                # else:
                #     print("No files with similarity ratio above threshold found.")

            directory_path = r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist"
            # delete_files_with_fuzzy_search(directory_path, task_text)
            threading.Thread(target=delete_files_with_fuzzy_search, args=(directory_path, task_text)).start()
            new_task_entry.delete(0, ctk.END)
    def close_program():
        # Закрытие программы при нажатии на крестик или Escape
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", close_program)
    app.bind("<Escape>", lambda event: close_program())

    # Загрузка изображений для кнопки смены темы
    sun_image_path = r"assets/icons/sred_sun_icon.png"
    moon_image_path = r"assets/icons/sred_moon_icon.png"
    sun_image_pil = Image.open(sun_image_path)
    moon_image_pil = Image.open(moon_image_path)
    sun_image = ImageTk.PhotoImage(sun_image_pil)
    moon_image = ImageTk.PhotoImage(moon_image_pil)

    # Создание верхнего фрейма для поля ввода и кнопки
    top_frame = ctk.CTkFrame(content_frame)
    top_frame.pack(side="top", fill="x", padx=10, pady=10)

    new_task_entry = ctk.CTkEntry(top_frame, placeholder_text="Type name of the music.")
    new_task_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
    new_task_entry.bind("<Return>", on_enter_pressed)

    # Код для создания кнопки смены темы без текста и с картинкой
    toggle_theme_button = ctk.CTkButton(top_frame, image=moon_image, command=toggle_theme, text="",
                                        width=50, fg_color='transparent', bg_color='transparent',
                                        hover='transparent')
    toggle_theme_button.pack(side="right")

    app.mainloop()
def window_musik_nuw(nuw, vals):
    ctk.set_appearance_mode("dark")  # Темная тема
    ctk.set_default_color_theme("green")  # Зеленая цветовая схема

    app = ctk.CTk()
    app.geometry("600x300")
    app.title(" Music Task App")
    # Установка логотипа (путь к файлу логотипа должен быть корректным)
    app.iconbitmap(r"images\images\Logo.ico")

    # Центрирование окна на экране
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    center_x = int(screen_width / 2 - 600 / 2)
    center_y = int(screen_height / 2 - 300 / 2)
    app.geometry(f"+{center_x}+{center_y}")

    # Создание фрейма для содержимого с закругленными углами
    content_frame = ctk.CTkFrame(app, corner_radius=10)
    content_frame.pack(fill="both", expand=True, padx=10, pady=10)

    def toggle_theme():
        # Переключение темы с темной на светлую и обратно
        current_mode = ctk.get_appearance_mode()
        if current_mode == "Dark":
            ctk.set_appearance_mode("Light")
            toggle_theme_button.configure(image=sun_image)  # Изменение иконки на солнце
        else:
            ctk.set_appearance_mode("Dark")
            toggle_theme_button.configure(image=moon_image)  # Изменение иконки на луну

    def youtubeplay(task_text, my_path, vals):
        with open('settings.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        data["Music_Name"] = task_text
        with open('settings.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        YouTubePlyatlist.search_video_vrem(task_text, my_path, vals)

    def on_enter_pressed(event=None):
        # Вывод текста в консоль при нажатии Enter
        task_text = new_task_entry.get()
        if task_text:
            print(task_text)
            if nuw:
                my_path = r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist_vrem"
                threading.Thread(target=youtubeplay, args=(task_text, my_path, vals)).start()
            else:
                my_path = r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist"
                threading.Thread(target=youtubeplay, args=(task_text, my_path, vals)).start()
            new_task_entry.delete(0, ctk.END)
    def close_program():
        # Закрытие программы при нажатии на крестик или Escape
        app.destroy()

    app.protocol("WM_DELETE_WINDOW", close_program)
    app.bind("<Escape>", lambda event: close_program())

    # Загрузка изображений для кнопки смены темы
    sun_image_path = r"assets/icons/sred_sun_icon.png"
    moon_image_path = r"assets/icons/sred_moon_icon.png"
    sun_image_pil = Image.open(sun_image_path)
    moon_image_pil = Image.open(moon_image_path)
    sun_image = ImageTk.PhotoImage(sun_image_pil)
    moon_image = ImageTk.PhotoImage(moon_image_pil)

    # Создание верхнего фрейма для поля ввода и кнопки
    top_frame = ctk.CTkFrame(content_frame)
    top_frame.pack(side="top", fill="x", padx=10, pady=10)

    new_task_entry = ctk.CTkEntry(top_frame, placeholder_text="Type name of the music.")
    new_task_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
    new_task_entry.bind("<Return>", on_enter_pressed)

    # Код для создания кнопки смены темы без текста и с картинкой
    toggle_theme_button = ctk.CTkButton(top_frame, image=moon_image, command=toggle_theme, text="",
                                        width=50, fg_color='transparent', bg_color='transparent',
                                        hover='transparent')
    toggle_theme_button.pack(side="right")

    app.mainloop()

# recorder = PvRecorder(device_index=configs.MICROPHONE_INDEX, frame_length=porcupine.frame_length)
# recorder.start()
def change_speed(sound, speed=1.0):
    # Увеличиваем скорость воспроизведения без изменения высоты звука
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)
CDIR = os.getcwd()
def playsounds(phrase, wait_done=True, ltc = time.time() - 1000):
    # global recorder
    filename = f"{CDIR}\\sounds_commands_voice\\"
    print(CDIR)
    if phrase == "greet":  # for py 3.8
        filename += f"yes_sir_I\\reference_1.wav"
    elif phrase == "ok":
        filename += "done\\reference_1.wav"
    elif phrase == "not_found":
        filename += "What_do_you_want_sir_I\\reference_1.wav"
    elif phrase == "run":
        filename += "good_morning (2)\\reference_1.wav"
    elif phrase == "low_battery":
        filename += "low_battery\\reference_1.wav"
        low_battery_say = True
    elif phrase == "off":
        filename += "Power_of_prog\\reference_1.wav"
    #
    # if wait_done:
    #     recorder.stop()

    # wave_obj = sa.WaveObject.from_wave_file(filename)
    # play_obj = wave_obj.play()
    wave_obj = sa.WaveObject.from_wave_file(filename)
    sound = AudioSegment.from_file(filename, format="wav")
    faster_sound = change_speed(sound, speed=1.1)
    play(faster_sound)
    # if wait_done:
    #     play_obj.wait_done()
        # time.sleep((len(wave_obj.audio_data) / wave_obj.sample_rate) + 0.5)
        # print("END")
        # time.sleep(0.5)
        # recorder.start()

def q_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))
def DelZad(zdel):
    with open(r'to-do-list.txt', "a", encoding="UTF-8") as file:
        file.write(f"{zdel}\n")
def respondes_voice(voice: str):
    global recorder, message_log, first_request
    voice = voice.lower()
    voice_list = list(voice)
    if '.' in voice_list:
        voice_list.remove('.')
    del voice_list[0]
    voice = ''.join(voice_list)
    print(f"Recognize: {voice}")
    Voice_new_commands_start_now.ckeck_num_comands_start(voice)
    for k, v in commands_dict["commands"].items():
        # print(v)
        for phrase in v:
            # print(fuzz.ratio(voice.join(voice.split()[:1]).strip(), phrase))
            # print(voice.join(voice.split()[:1]).strip())
            # print(voice)
            # print(phrase)
            # print(fuzz.ratio(voice, phrase))
            # print("retretret")
            if fuzz.ratio(voice.join(voice.split()[:1]).strip(), 'open') < 80 and fuzz.ratio(
                    voice.join(voice.split()[:1]).strip(), 'clothe') < 80 and fuzz.ratio(
                    voice.join(voice.split()[:1]).strip(), 'Music_play_vrem') < 80 and fuzz.ratio(voice, phrase) > 80:
                # print(voice)
                # print(phrase)
                # print(fuzz.ratio(voice, phrase))
                print("what")
                execute_cmd(k, 50, voice)
                return True
        # if voice in v:
        #     # print("4")
        #     execute_cmd(k, 50, voice)
        #     return True
    # num_str = 'сто двадцать три'
    # num_list = num_str.split()

    clo = 0
    open_dict_normal_srartfile_list = ['steam', 'ground', "python", "Photoshop", "firefox", "google", "telegram",
                                       "explorer"]
    for word in open_dict_normal_srartfile_list:
        # print(word)
        # print(voice.join(voice.split()[1:]).strip().split())
        # print(fuzz.ratio(voice.join(voice.split()[1:]).strip().split(), 'Clothe'))
        # print("aaaaaaaaaaaaa")
        if fuzz.ratio(voice.join(voice.split()[1:]).strip().split(), word) > 70 and fuzz.ratio(
                voice.join(voice.split()[1:]).strip().split(), 'Clothe') > 70:
            # print(word)
            # print("rrrrrrrrr")
            clo += close_dict[word]
            # print(clo)
    # nnn = 0
    # if val == x:
    #     execute_cmd(cmd)
    #     return True
    clo_vab = clo
    # print(clo_vab)
    # print(clo)
    # print("ccc")
    for k_o, v_o in close_dict.items():
        if str(clo_vab) in str(v_o):
            for k, v in commands_dict["commands"].items():
                for phrase in v:
                    if fuzz.ratio(voice.join(voice.split()[:1]).strip(), phrase) > 80 and fuzz.ratio(
                            voice.join(voice.split()[:1]).strip().split(), 'Clothe') > 70:
                        execute_cmd(k, clo_vab, voice)
                        # print("134134123412341243")
                        return True
    for k, v in commands_dict["commands"].items():
        for phrase in v:
            # print(fuzz.ratio(voice.join(voice.split()[:1]).strip(), phrase))
            # print(fuzz.ratio(voice.join(voice.split()[:1]).strip().split(), 'Music_play_vrem'))
            # print(voice.join(voice.split()[:1]).strip())
            # print(phrase)
            if fuzz.ratio(voice.join(voice.split()[:1]).strip(), phrase) > 80 and fuzz.ratio(
                    voice.join(voice.split()[:1]).strip().split(), 'clothe') < 70 and fuzz.ratio(
                voice.join(voice.split()[:1]).strip().split(), 'open') < 70 and fuzz.ratio(
                voice.join(voice.split()[:1]).strip().split(), 'music') > 70:
                vab = ' '.join(voice.split()[1:])
                print("#########################")
                print(vab)
                print("#########################")
                execute_cmd(k, vab, voice)
                # print("134134123412341243")
                return True
    ope = 0
    open_dict_normal_srartfile_list = ['steam', 'ground', "python", "Photoshop", "firefox", "google", "telegram",
                                       "explorer"]
    for word in open_dict_normal_srartfile_list:
        # print(word)
        # print(voice.join(voice.split()[1:]).strip().split())
        # print(fuzz.ratio(voice.join(voice.split()[1:]).strip().split(), word))
        # print("aaaaaaaaaaaaa")
        if fuzz.ratio(voice.join(voice.split()[1:]).strip().split(), word) > 70:
            # print(word)
            # print("rrrrrrrrr")
            ope += open_dict[word]
            # print(ope)
    ope_vab = ope
    # print(ope_vab)
    # print("ope_vab")
    for k_o, v_o in open_dict.items():
        if str(ope_vab) in str(v_o):
            # print("ffffffffffff")
            for k, v in commands_dict["commands"].items():
                # print("lllllllllll")
                for phrase in v:
                    # print(phrase)
                    # print(voice.join(voice.split()[:1]).strip())
                    # print(fuzz.ratio(voice.join(voice.split()[:1]).strip(), phrase))
                    if fuzz.ratio(voice.join(voice.split()[:1]).strip(), phrase) > 70:
                        # print("unrial")
                        execute_cmd(k, ope_vab, voice)
                        return True

    val = 0
    for word in voice.join(voice.split()[1:]).strip().split():
        val += num_dict.get(word, 0)
        # nnn = 0
        # if val == x:
        #     execute_cmd(cmd)
        #     return True
    vab = val
    for k_o, v_o in num_dict.items():
        if str(vab) in str(v_o):
            for k, v in commands_dict["commands"].items():
                if voice.join(voice.split()[:1]).strip() in v:
                    if fuzz.ratio(k.join(k.split()[:1]).strip(), 'Volum_0-100') > 75:
                        # VolumeNum = k.join(k.split()[1:]).strip(), 'Volum_0-100'
                        # print("134313421")
                        # print(VolumeNum)
                        # print("Pringadfsa")
                        execute_cmd(k, vab, voice)
                        return True
                    elif fuzz.ratio(k.join(k.split()[:1]).strip(), 'brightness_0-100') > 75:
                        execute_cmd(k, vab, voice)
                        return True
                    elif fuzz.ratio(k.join(k.split()[:1]).strip(), 'Sdel_Zad') > 75:
                        execute_cmd(k, vab, voice)
                        return True
    for k, v in commands_dict["commands"].items():
        if voice.join(voice.split()[:1]).strip() in v:
            execute_cmd(voice.join(voice.split()[:1]).strip(), 50, voice)
            print("000000")
            return True
    # print(vab)
    # print(voice.join(voice.split()[1:]).strip())
    print("13412412341234123412341234124")
    for k_ai, v_ai in commands_dict_openai["commands"].items():
        if voice.join(voice.split()[:1]).strip() in v_ai:
            print(voice.join(voice.split()[:1]).strip())
            #         execute_cmd(k_ai)
            #         return False
            # play("not_found")
            # tts.va_speak("Что?")
            if fuzz.ratio(k_ai, "INPUT_KEY") > 75:
                print("3")
        # if voice.join(voice.split()[:1]).strip() in v_ai:
        #     print("135135813291533")
        #     #         execute_cmd(k_ai)
        #     #         return False
        #     # playsounds("not_found")
        #     # tts.va_speak("Что?")
        #     if fuzz.ratio(k_ai, "INPUT_KEY") > 75:
        #         print("3")
                # if first_request:
                #     message_log.append({"role": "user", "content": voice})
                #     first_request = True
                FIVferen.ChatGPT_INF(voice)
            else:
                playsounds("not_found")
                threading.Thread(target=time_sleep_threading, args=(1,)).start()

            return False

def aud_to_text():
    FIVferen.aud_to_text()
muninik = False
play_next_prev = False
def execute_cmd(k, vab, p):
    global audio_clip
    global music_paused, current_track, accumulated_time, mp3file, mp3_files, mp33_files, play_next_prev, muninik

    with open('settings.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    time_now_and_comp = data["Command_0_mode"]
    print(time_now_and_comp)
    # print(k.join(k.split()[:1]).strip())
    # if fuzz.ratio(k, 'google') > 55:#google
    #     subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe"])
    #     print("TRTYYY")
    #     playsounds("ok")
    # elif fuzz.ratio(k, 'firefox') > 75:#google
    #     subprocess.Popen(["C:/Users/IVNsell/AppData/Local/Mozilla Firefox/firefox.exe"])
    #     print("VNVYYY")
    #     playsounds("ok")
    # elif fuzz.ratio(k, 'open_youtube') > 75:
    #     webbrowser.open("https://www.youtube.com/", 0, True)
    #     playsounds("ok")
    if k == 'tanks':
        subprocess.Popen(["C:/Games/World_of_Tanks_RU/wgc_api.exe"])
        playsounds("ok")
    if k == 'Time' and data["Command_0_activate"].lower() == 'true':
        muninik = False
        play_next_prev = False
        if muninik == False:
            stop_music()
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            # num = 1
            print(time_now_and_comp.lower())
            if time_now_and_comp.lower() == 'true':
                time = Wheather_and_time.get_current_time()
            else:
                time = Wheather_and_time.get_current_time_comp()
            print(time)
            # settext(time)
            # inference.main(num, 'output')
            FIVferen.setTime(time)
            play_audio_prost()
    if k == 'Wheather' and data["Command_10_activate"].lower() == 'true':
        muninik = False
        play_next_prev = False
        if muninik == False:
            stop_music()
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            # num = 1
            wheather = Wheather_and_time.get_weather()
            print(wheather)
            # settext(wheather)
            # inference.main(num, 'output')
            FIVferen.setWheather(wheather)
            play_audio_prost()
    elif k == 'telegram':#google
        subprocess.Popen(["C:/Users/Sergey/AppData/Roaming/Telegram Desktop/Telegram.exe"])
        playsounds("ok")
    # elif k == 'Steam':#google
    #     subprocess.Popen(["C:/Program Files (x86)/Steam/Steam.exe"])
    #     playsounds("ok")
    elif k == 'Zad_Steam':#google
        subprocess.Popen(["C:/Program Files (x86)/Steam/Steam.exe"])
        playsounds("ok")
    elif k == 'Cyberpunk_2077':#google
        print(153)
        Steam_games.Cyberpunk_2077()
        playsounds("ok")
    elif k == 'Dying_light_2':#google
        print(153)
        Steam_games.Diying_Light_2()
        playsounds("ok")
    elif k == 'Terarria':#google
        print(153)
        Steam_games.Terarria()
        playsounds("ok")
    elif k == 'Pause_play_vrem':
        print("Pause")
        pause_music()
        # if not music_paused:  # Проверяем, не на паузе ли уже музыка
        #     print(pygame.mixer.music.get_pos())
        #     pause_time = pygame.mixer.music.get_pos() / 1000.0
        #     print(pause_time)
        #     if pause_time != -1:
        #         accumulated_time += pause_time  # Добавляем время до паузы к общему времени
        #         print(f"Acum_pause: {accumulated_time}")
        #     pygame.mixer.music.pause()
        #     music_paused = True
    elif k == 'Сontinued_Pause_play_vrem':
        print("Continue")
        unpause_music()
        # try:
        #     if music_paused:  # Проверяем, действительно ли музыка на паузе
        #         print("sssssssssssssssssssssssssssssss")
        #         print(f"Acum_continue: {accumulated_time}")
        #         pygame.mixer.music.play(start=accumulated_time)  # Возобновляем с накопленного времени
        #         music_paused = False
        # except:
        #     pass
    elif k == 'Stop_play_vrem':
        print("Stop")
        stop_music()
        muninik = False
        play_next_prev = False
        # music_paused = True
        # current_track = None
        # accumulated_time = 0  # Сбрасываем накопленное время
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        # pygame.mixer.music.stop()
        # folder_path = r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist_vrem"
        # delete_files_in_folder(folder_path)
    elif k == 'Next':
        print("Next")
        if play_next_prev == True:
            next_track()
        # try:
        #     print(f"mp3_files: {mp3_files}")
        #     print(f"mp3file: {mp3file}")
        #     index = mp3_files.index(mp3file)
        #     print(f"index: {index}")
        #     if index + 1 < len(mp3_files):
        #         # Есть следующий трек в списке
        #         result = mp3_files[index + 1:]
        #         print(result)
        #         print("3333333333")
        #     else:
        #         # Текущий трек - последний в списке, возвращаемся к началу
        #         result = mp33_files
        #         print(result)
        #         print("1111111")
        #     print(f"Result: {result}.")
        #     music_paused = False
        #     current_track = None
        #     accumulated_time = 0
        #     pygame.mixer.music.stop()
        #     threading.Thread(target=play_mp3_files_in_folder, args=(result,)).start()
        # except IndexError:
        #     print("Error not found file :/")
    elif k == 'Previous':
        print("Previous")
        if play_next_prev == True:
            previous_track()
        # try:
        #     index = mp33_files.index(mp3file)
        #     print(index)
        #     if index != 0:
        #         # Текущий трек - первый в списке, переходим к последнему треку
        #         result = mp33_files[max(0, index - 1):index + len(mp33_files)]
        #         print(result)
        #         print("GIGA MIND.")
        #     else:
        #         # Воспроизводим предыдущий трек
        #         result = mp33_files[-1]
        #         result = [result]
        #         print(result)
        #     print(f"Result: {result}.")
        #     music_paused = False
        #     current_track = None
        #     accumulated_time = 0
        #     pygame.mixer.music.stop()
        #     threading.Thread(target=play_mp3_files_in_folder, args=(result,)).start()
        # except IndexError:
        #     print("Error not found file :/")
    elif k == 'Console' and data["Command_6_activate"].lower() == 'true':
        print("Open music console.")
        muninik = True
        folder_path = r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist_vrem"
        delete_files_in_folder(folder_path)
        nuw = True
        music_paused = False
        threading.Thread(target=window_musik_nuw, args=(nuw,True)).start()
    elif k == 'Add_Music_Playlist' and data["Command_8_activate"].lower() == 'true':
        print("Add new musik to playlist.")
        nuw = False
        threading.Thread(target=window_musik_nuw, args=(nuw,False)).start()
    elif k == 'Dell_Playlist' and data["Command_9_activate"].lower() == 'true':
        print("Delete musik from playlist.")
        threading.Thread(target=window_delete_musik).start()
    elif k == 'ListenPlayList' and data["Command_7_activate"].lower() == 'true':
        print("ListenPlayList")
        muninik = True
        play_next_prev = True
        play_music()
        # music_paused = False
        # current_track = None
        # accumulated_time = 0
        # folder_path = r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist"
        # files = os.listdir(folder_path)
        # mp3_files = [f for f in files if f.endswith('.mp3')]
        # threading.Thread(target=play_mp3_files_in_folder, args=(mp3_files,)).start()
    elif k == 'Music_play_vrem' and data["Command_5_activate"].lower() == 'true':
        muninik = True
        music = vab
        # num = 1
        # settext(f"Name of yout music: {music}? It's that music?")
        # inference.main(num, 'output')
        FIVferen.Music_play_vrem(music)
        play_audio_prost()
        folder_path = r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist_vrem"
        del_mp4_In_mp3(folder_path)
        delete_files_in_folder(folder_path)
        def is_silent(data, threshold=500):
            """Check if the audio chunk is silent based on the threshold."""
            return np.max(data) < threshold
        import time
        def record_chunk(p, stream, file_path, silence_threshold=1):
            frames = []
            start_time = None
            silence_start = None

            while True:
                data = stream.read(1024)
                audio_data = np.frombuffer(data, dtype=np.int16)

                if not is_silent(audio_data):
                    if start_time is None:
                        start_time = time.time()  # Начало говорения
                    frames.append(data)
                    silence_start = None  # Reset silence start time
                elif start_time is not None:
                    if silence_start is None:
                        silence_start = time.time()  # Start of silence
                    elif time.time() - silence_start > silence_threshold:
                        # End of speech detected
                        end_time = time.time()
                        chunk_length = end_time - start_time
                        print(f"Chunk length: {chunk_length} seconds")
                        break

            if frames:
                frames = b''.join(frames)
                wf = wave.open(file_path, 'wb')
                wf.setnchannels(1)
                wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
                wf.setframerate(16000)
                wf.writeframes(frames)
                wf.close()
                print(f"Recorded chunk saved to {file_path}")
            else:
                print("Silent chunk ignored")

        def transcribe_chunk(model, chunk_file):
            segments, info = model.transcribe(chunk_file, language="en", beam_size=20, vad_filter=True,
                                              condition_on_previous_text=False)
            # print("5555555555555")
            # print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

            transcription = ' '.join(segment.text for segment in segments)
            return transcription
        chunk_file = "temp_chunk_music.wav"
        waiting_for_response = True
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
        while waiting_for_response:
            record_chunk(p, stream, chunk_file)
            if os.path.exists(chunk_file):  # Проверяем, существует ли файл перед транскрибацией
                transcription = transcribe_chunk(model, chunk_file)
                transcription = transcription.lower()
                print("|||||||||||||||||||||||||||||||||||")
                print(transcription)
                print("|||||||||||||||||||||||||||||||||||")
                if fuzz.ratio(transcription, "yes") > 60:
                    print("Yes.")
                    music_paused = False
                    YouTubePlyatlist.search_video_vrem(music, r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist_vrem", True)
                    threading.Thread(target=play_music_now).start()
                    # Здесь можно выполнить действие по воспроизведению музыки
                    waiting_for_response = False  # Останавливаем ожидание ответа
                elif fuzz.ratio(transcription, "no") > 60:
                    print("No.")
                    # Установка темы и цветовой схемы
                    nuw = True
                    music_paused = False
                    threading.Thread(target=window_musik_nuw, args=(nuw,True)).start()
                    # Здесь можно запросить у пользователя повторное название музыки
                    waiting_for_response = False  # Останавливаем ожидание ответа
                elif fuzz.ratio(transcription, "exit") > 60:
                    print("Exit.")
                    break
        print(music)
        # YouTubePlyatlist.search_video_vrem(music)

        print("okey lets go")
    elif k == 'LevelBattery' and data["Command_4_activate"].lower() == 'true':#google
        print("LevelBattery")
        stop_music()
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        battery_level = get_battery_level()
        # num = 1
        # with open("example/text.txt", 'w', encoding='utf-8') as file:
        #     file.write(f"Battery level: {battery_level} percent")
        # inference.main(num, 'output')
        FIVferen.LowBut(battery_level)
        play_audio_prost()
        print("Battery level:", battery_level, "%")  # percent
        # playsounds("ok")
    # elif k == 'Wallpeper_Engine':#google
    #     print(153)
    #     Steam_games.Wallpeper_Engine()
    #     playsounds("ok")
    elif fuzz.ratio(k, 'Razer_Vkl') > 75:#google
        Test_bluet.Connect_Rezer_Opus()
        playsounds("ok")
    elif fuzz.ratio(k, 'Opus_Vukl') > 75:#google
        Test_bluet.DisConnect_Razer_Opus()
        playsounds("ok")
    elif fuzz.ratio(k, 'Photoshop') > 75:#google
        subprocess.Popen(["C:/Users/Sergey/Downloads/Portable Adobe Photoshop/Photoshoр.exe"])
        playsounds("ok")
    elif fuzz.ratio(k, 'PrimePro') > 75:#google
        subprocess.Popen([r"C:\Users\Sergey\Downloads\Portable Adobe Premiere\Premiere.exe"])
        playsounds("ok")
    elif fuzz.ratio(k, 'VSC') > 75:#google
        subprocess.Popen([r"C:\Users\Sergey\AppData\Local\Programs\Microsoft VS Code\Code.exe"])
        playsounds("ok")
    elif fuzz.ratio(k, 'Unity') > 75:#google
        subprocess.Popen([r"C:\Program Files\Unity Hub\Unity Hub.exe"])
        playsounds("ok")
    elif fuzz.ratio(k, 'Minecraft') > 75:#google
        subprocess.Popen([r"C:\Users\Sergey\AppData\Roaming\.minecraft\TLauncher.exe"])
        playsounds("ok")
    elif fuzz.ratio(k, 'Rand') > 75:#google
        playsounds("ok")
        subprocess.run(["C:/Users/IVNsell/source/repos/Random/Random/obj/Debug/Random.exe"])
    elif fuzz.ratio(k, 'Wide_Mode') > 75 and data["Command_11_activate"].lower() == 'true':#google
        playsounds("ok")
        threading.Thread(target=OpenCV_plus_ultra).start()
    elif k == 'MainFolder':#google
        pyautogui.hotkey("win","e")
        playsounds("ok")
    elif fuzz.ratio(k, 'Sdel_del_text') > 75:
        file_path = r"C:\Users\IVNsell\Desktop\IVNsell\Jarvis\to-do-list.txt"
        if os.path.exists(file_path):
            with open('to-do-list.txt', 'w', encoding='utf-8') as file:
                file.write('')
        else:
            print("File not found.")
        playsounds("ok")
    elif fuzz.ratio(k.join(k.split()[:1]).strip(), 'Sdel_Zad') > 75:#google
        print("dd")
        zdel = p[5:]
        DelZad(zdel)
        playsounds("ok")
    elif fuzz.ratio(k, 'Pon_del_Zad') > 75:
        file_path = r"C:\Users\IVNsell\Desktop\IVNsell\Jarvis\to-do-list.txt"

        # Проверяем, существует ли файл
        if os.path.exists(file_path):
            # Удаляем файл
            os.remove(file_path)
            print("File succes delete.")
        else:
            print("File not found.")
        playsounds("ok")
    elif fuzz.ratio(k, 'Open_Zad') > 75:
        os.startfile('output/Open_dela.exe')
        playsounds("ok")
    elif fuzz.ratio(k, 'Close_Zad') > 75:
        sver_rand = random.randint(1, 2)
        if sver_rand == 1:
            pyautogui.hotkey('win', 'down')
        if sver_rand == 2:
            pyautogui.hotkey('win', 'down')
        playsounds("ok")
    elif fuzz.ratio(k.join(k.split()[:1]).strip(), 'Volum_0-100') > 75 and data["Command_2_activate"].lower() == 'true':
        # print(vab)
        # print(p.join(p.split()[1:]).strip())#////////////////
        # vat = vab / 100
        # Sound.mute()  # убрали звук
        # Sound.volume_max()  # Наоборот, прибавили на максимум
        # cur = Sound.current_volume()  # получили текущие настройки
        # vol = int(input("Введите громкость звука в единицах (0..100): "))  # получим громкость от пользователя
        try:
            VolNum = int(p.join(p.split()[1:]).strip())
            Sound.volume_set(VolNum)  # установим пользовательскую громкостьустановим громкость 90
            playsounds("ok")
        except:
            playsounds("not_found")
    elif k == 'brightness_0-100' and data["Command_3_activate"].lower() == 'true':
        # Устанавливаем яркость на определенный процент
        def set_brightness(percent):
            sbc.set_brightness(percent)
        try:
            VolNum = int(p.join(p.split()[1:]).strip())
            set_brightness(VolNum)  # установим пользовательскую громкостьустановим громкость 90
            playsounds("ok")
        except:
            playsounds("not_found")
    elif fuzz.ratio(k.join(k.split()[:1]).strip(), 'Clothe') > 75:
        # print(1111111)
        close_dict_normal = {'steam.exe': 0, 'wallpaper32.exe': 1, "python.exe": 2, "Photoshop.exe": 3, "firefox.exe": 4, "chrome.exe": 5, "Telegram.exe": 6, "explorer.exe": 7}
        reverse_dict_close = {val: key for key, val in close_dict_normal.items()}
        # print(reverse_dict_close.get(vab))
        close_dict_normal_sub_list = ['steam.exe', 'wallpaper32.exe', "python.exe", "Photoshop.exe", "firefox.exe", "chrome.exe", "Telegram.exe", "explorer.exe"]
        if reverse_dict_close.get(vab) in close_dict_normal_sub_list:
            for process in psutil.process_iter(['pid', 'name']):
                print(process.info)
            for process in psutil.process_iter(['pid', 'name']):
                if process.info['name'] == reverse_dict_close.get(vab):
                            pid = process.info['pid']
                            try:
                                psutil.Process(pid).terminate()
                                print(f"Процесс {reverse_dict_close.get(vab)} с PID {pid} завершен.")
                            except psutil.NoSuchProcess as e:
                                print(f"Процесс {reverse_dict_close.get(vab)} с PID {pid} не найден: {e}")
        # target_window = gw.getWindowsWithTitle(reverse_dict_close.get(vab))
        # if target_window:
        #     target_window[0].close()
        playsounds("ok")
    elif fuzz.ratio(k.join(k.split()[:1]).strip(), 'Open') > 75:
        # print(3333333)
        # open_dict = {'steam': 0, 'background': 1, "youtube": 2, "explorer": 3, "firefox": 4, "google": 5, "settings": 6,
        #              "terraria": 7}
        open_dict_normal_srartfile = {'steam.exe': 0, 'wallpaper32.exe': 1, "python.exe": 2, "Photoshoр.exe": 3, "firefox.exe": 4, "chrome.exe": 5, "Telegram.exe": 6, "explorer.exe": 7}
        reverse_dict_open_srartfile = {val: key for key, val in open_dict_normal_srartfile.items()}
        # print(reverse_dict_open_srartfile.get(vab))
        open_dict_normal_srartfile_list = ['steam', 'ground', "python", "Photoshop", "firefox", "google", "Telegram", "explorer"]
        for word in open_dict_normal_srartfile_list:
            # print(word)
            if fuzz.ratio(p.join(p.split()[1:]).strip(), word) > 75:
                # print("Okey")
                # print(reverse_dict_open_srartfile.get(vab))
                try:
                    os.startfile(reverse_dict_open_srartfile.get(vab))
                except:
                    if word == 'steam': (subprocess.Popen(["C:/Program Files (x86)/Steam/Steam.exe"]))
                    elif word == 'ground': (Steam_games.Wallpeper_Engine())
                    elif word == 'python': (subprocess.Popen(["C:/Program Files/JetBrains/PyCharm Community Edition 2023.2.2/bin/pycharm64.exe"]))
                    elif word == 'Photoshop': (subprocess.Popen(["C:/Users/IVNsell/Downloads/Portable Adobe Photoshop/Photoshoр.exe"]))
                    elif word == 'Telegram': (subprocess.Popen(["C:/Users/IVNsell/AppData/Roaming/Telegram Desktop/Telegram.exe"]))
                    elif word == 'explorer': (Hotkey_press.press_win_e())
        HotKey_list = ["page"]
        for word in HotKey_list:
            # print(word)
            # print(fuzz.ratio(p.join(p.split()[1:]).strip(), word))
            # print(p.join(p.split()[1:]).strip())
            if fuzz.ratio(p.join(p.split()[1:]).strip(), word) > 75:
                if fuzz.ratio(word, "page") > 75:
                    print("Open page")
                    Hotkey_press.press_ctl_T()
        link_list = ["youtube"]
        for word in link_list:
            # print(word)
            # print(fuzz.ratio(p.join(p.split()[1:]).strip(), word))
            # print(p.join(p.split()[1:]).strip())
            if fuzz.ratio(p.join(p.split()[1:]).strip(), word) > 75:
                if fuzz.ratio(word, "youtube") > 75:
                    print("Open youtube")
                    webbrowser.open("https://www.youtube.com/", 0, True)


        # target_window = gw.getWindowsWithTitle(reverse_dict_close.get(vab))
        # if target_window:
        #     target_window[0].close()
        playsounds("ok")
    elif fuzz.ratio(k, 'SverVse') > 60:#google
        sver_rand = random.randint(1, 2)
        if sver_rand == 1:
            print("OWERTUWOERUTPWOERTWET")
            threading.Thread(target=time_sleep_threading, args=(0.3,)).start()
            pyautogui.hotkey("win", "m")
        if sver_rand == 2:
            threading.Thread(target=time_sleep_threading, args=(0.3,)).start()
            pyautogui.keyDown('winleft')
            pyautogui.press('m')
            pyautogui.keyUp('winleft')
        # time.sleep(0.3)
        # time.sleep(0.3)
        print("09")
        # pyautogui.hotkey("win", "m")
        #     pyautogui.keyDown('winleft')
        #     pyautogui.press('m')
        #     pyautogui.keyUp('winleft')
        playsounds("ok")
    elif fuzz.ratio(k, 'RosrVse') > 60:#google
        # time.sleep(0.3)
        # time.sleep(0.3)
        # pyautogui.hotkey("win", "shift", "m")
        sver_rand = random.randint(1, 2)
        if sver_rand == 1:
            pyautogui.keyDown('winleft')
            pyautogui.keyDown('shift')
            pyautogui.press('m')
            pyautogui.keyUp('winleft')
            pyautogui.keyUp('shift')
        if sver_rand == 2:
            pyautogui.hotkey("win", "shift", "m")
        playsounds("ok")
    elif fuzz.ratio(k, 'SverVseKrom') > 75:#google
        threading.Thread(target=time_sleep_threading, args=(0.3,)).start()
        pyautogui.hotkey("win","home")
        playsounds("ok")
    elif k == 'Settings':#google
        pyautogui.hotkey("win","i")
        playsounds("ok")
    elif fuzz.ratio(k, 'SettingGame') > 75:#google
        pyautogui.hotkey("win","g")
        playsounds("ok")
    elif fuzz.ratio(k, 'BustBlu') > 75:#google
        # pyautogui.hotkey("win","k")
        subprocess.check_output('net start "Bluetooth Audio Gateway Service"', shell=True, universal_newlines=True)
        playsounds("ok")
    elif fuzz.ratio(k, 'StopBustBlu') > 75:#google
        # pyautogui.hotkey("win","k")
        subprocess.check_output('net stop "Bluetooth Audio Gateway Service"', shell=True, universal_newlines=True)
        playsounds("ok")
    elif fuzz.ratio(k, 'OPENAI_Prog') > 60:#google
        os.startfile('output/OpenIA_test.exe')
        playsounds("ok")
    elif fuzz.ratio(k, 'rob_R') > 60 and data["Command_1_activate"].lower() == 'true':#google
        webbrowser.open("https://mystat.itstep.org/en/main/dashboard/page/index", 0, True)
        # if webbrowser.open(url, 0, True):
        #     pyautogui.moveTo(942, 562, 1,5)
        #     pyautogui.click()
        webbrowser.open("https://teams.microsoft.com/_?culture=uk-ua&country=ua#/school/conversations/%D0%9E%D0%B1%D1%89%D0%B8%D0%B9?threadId=19:ZzjMOpR-qPpvPAwVyEYcy9PY2TbnpBT8HMbLIgnWp_Q1@thread.tacv2&ctx=channel", 0, True)
        webbrowser.open("https://www.tinkercad.com/dashboard", 0, True)
        playsounds("ok")
    elif fuzz.ratio(k, 'tinkerkad') > 75:#google
        webbrowser.open("https://www.tinkercad.com/dashboard", 0, True)
        playsounds("ok")
    elif fuzz.ratio(k, 'off') > 75:#oft
        playsounds("off", True)
        # Last()
        # main_mn.Buy()
        folder_path = r"C:\Users\IVNsell\Desktop\IVNsell\Python\GestureVox Integration\Modern_GUI_PyDracula_PySide6_or_PyQt6-master\HierSpeechpp\HierSpeechpp\playlist_vrem"
        delete_files_in_folder(folder_path)
        porcupine.delete()

        exit(0)

    # elif cmd == 'open_youtube':
    #     subprocess.Popen([f'{CDIR}\\custom-commands\\Run youtube.exe'])
    #     playsounds("ok")
    #
    # elif cmd == 'open_google':
    #     subprocess.Popen([f'{CDIR}\\custom-commands\\Run google.exe'])
    #     playsounds("ok")
    #
    # elif cmd == 'music':
    #     subprocess.Popen([f'{CDIR}\\custom-commands\\Run music.exe'])
    #     playsounds("ok")
    #
    # elif cmd == 'music_off':
    #     subprocess.Popen([f'{CDIR}\\custom-commands\\Stop music.exe'])
    #     time.sleep(0.2)
    #     playsounds("ok")
    #
    # elif cmd == 'music_save':
    #     subprocess.Popen([f'{CDIR}\\custom-commands\\Save music.exe'])
    #     time.sleep(0.2)
    #     playsounds("ok")
    #
    # elif cmd == 'music_next':
    #     subprocess.Popen([f'{CDIR}\\custom-commands\\Next music.exe'])
    #     time.sleep(0.2)
    #     playsounds("ok")
    #
    # elif cmd == 'music_prev':
    #     subprocess.Popen([f'{CDIR}\\custom-commands\\Prev music.exe'])
    #     time.sleep(0.2)
    #     playsounds("ok")
    #
    elif k == 'sound_off':
        playsounds("ok", True)

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(1, None)

    elif k == 'sound_on':
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMute(0, None)

        playsounds("ok")

    # elif cmd == 'thanks':
    #     playsounds("thanks")
    #
    # elif cmd == 'stupid':
    #     playsounds("stupid")
    #
    # elif cmd == 'gaming_mode_on':
    #     playsounds("ok")
    #     subprocess.check_call([f'{CDIR}\\custom-commands\\Switch to gaming mode.exe'])
    #     playsounds("ready")
    #
    # elif cmd == 'gaming_mode_off':
    #     playsounds("ok")
    #     subprocess.check_call([f'{CDIR}\\custom-commands\\Switch back to workspace.exe'])
    #     playsounds("ready")
    #
    # elif cmd == 'switch_to_headphones':
    #     playsounds("ok")
    #     subprocess.check_call([f'{CDIR}\\custom-commands\\Switch to headphones.exe'])
    #     time.sleep(0.5)
    #     playsounds("ready")
    #
    # elif cmd == 'switch_to_dynamics':
    #     playsounds("ok")
    #     subprocess.check_call([f'{CDIR}\\custom-commands\\Switch to dynamics.exe'])
    #     time.sleep(0.5)
    #     playsounds("ready")
    #
    # elif cmd == 'off':
    #     playsounds("off", True)
    #
    #     porcupine.delete()
    #     exit(0)

# print('Using device: %s' % recorder.selected_device)
#
# print(f"Jarvis (v3.0) start...")
# threading.Thread(target=time_sleep_threading, args=(0.7,)).start()
# playsounds("run")
# ltc = time.time() - 1000
# while True:
#     try:
#         pcm = recorder.read()
#         keyword_index = porcupine.process(pcm)
#
#         if keyword_index >= 0:
#             recorder.stop()
#             print("1")
#             playsounds("greet", True)
#             print("Yes, sir.")
#             recorder.start()  # prevent self recording
#             ltc = time.time()
#         while time.time() - ltc <= 10:
#             pcm = recorder.read()
#             sp = struct.pack("h" * len(pcm), *pcm)
#             print("14")
#             # print(time.time() - ltc)
#             # print(kaldi_rec.AcceptWaveform(sp))
#             # if kaldi_rec.AcceptWaveform(sp):
#             #     print("7")
#             #     if respondes_voice(json.loads(kaldi_rec.Result())["text"]):
#             #         ltc = time.time()
#             #         print("23")
#             #
#             #     break
#             try:
#                 with sr.Microphone() as source:
#                     rec.adjust_for_ambient_noise(source, duration=0.1)
#                     audio = rec.listen(source)
#                     text = rec.recognize_google(audio)
#                     text = text.lower()
#                     # print(f"Recognized {text}")
#                     print("TYU")
#                     if text != "":
#                         print(7)
#                         if respondes_voice(text):
#                             ltc = time.time()
#                             print("23")
#             except sr.UnknownValueError:
#                 continue
#     except Exception as err:
#         print(f"Unexpected {err=}, {type(err)=}")
#         raise
def is_silent(data, threshold=500):
    """Check if the audio chunk is silent based on the threshold."""
    return np.max(data) < threshold

async def record_chunk(p, stream, file_path, silence_threshold=0.3):
    frames = []
    start_time = None
    silence_start = None

    while True:
        data = stream.read(1024)
        audio_data = np.frombuffer(data, dtype=np.int16)

        if not is_silent(audio_data):
            if start_time is None:
                start_time = time.time()  # Начало говорения
            frames.append(data)
            silence_start = None  # Reset silence start time
        elif start_time is not None:
            if silence_start is None:
                silence_start = time.time()  # Start of silence
            elif time.time() - silence_start > silence_threshold:
                # End of speech detected
                end_time = time.time()
                chunk_length = end_time - start_time
                print(f"Chunk length: {chunk_length} seconds")
                break

    if frames:
        frames = b''.join(frames)
        wf = wave.open(file_path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(16000)
        wf.writeframes(frames)
        wf.close()
        print(f"Recorded chunk saved to {file_path}")
    else:
        print("Silent chunk ignored")

def transcribe_chunk(model, chunk_file):
    segments, info = model.transcribe(chunk_file, language="en", beam_size=20, vad_filter=True, condition_on_previous_text=False)
    # print("5555555555555")
    # print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    transcription = ' '.join(segment.text for segment in segments)
    print(transcription)
    return transcription


# def main2():
#     model_size = "medium.en"
#     model = WhisperModel(model_size, device="cuda", compute_type="float16")
#
#     p = pyaudio.PyAudio()
#     stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
#
#     accumulated_transcription = ""
#
#     try:
#         while True:
#             chunk_file = "temp_chunk.wav"
#             record_chunk(p, stream, chunk_file)
#
#             if os.path.exists(chunk_file):  # Проверяем, существует ли файл перед транскрибацией
#                 transcription = transcribe_chunk(model, chunk_file)
#                 print(transcription)
#                 os.remove(chunk_file)
#
#                 accumulated_transcription += transcription + " "
#             else:
#                 # print("Chunk file not created, skipping transcription.")
#                 pass
#     except KeyboardInterrupt:
#         print("Stopping...")
#         with open("log.txt", "w") as log_file:
#             log_file.write(accumulated_transcription)
#     finally:
#         print("LOG:" + accumulated_transcription)
#         stream.stop_stream()
#         stream.close()
#         p.terminate()
async def recognize_speech(rec):
    try:
        with sr.Microphone() as source:
            rec.adjust_for_ambient_noise(source, duration=0.1)
            audio = rec.listen(source)
            text = rec.recognize_google(audio)
            text = text.lower()
            print(f"Recognized: {text}")
            return text
    except sr.UnknownValueError:
        return None

model_size = "medium.en"
model = WhisperModel(model_size, device="cuda", compute_type="float16")

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

# accumulated_transcription = ""
name_asis = 'GestureVox Intergaration'


async def main():
    rec = sr.Recognizer()

    rec.energy_threshold = 4000
    print(f"{name_asis} (v5.0) began its work ...")
    await asyncio.sleep(0.7)
    playsounds("run")
    ltc = time.time() - 1000
    while True:
        try:

            # pcm = recorder.read()
            # keyword_index = porcupine.process(pcm)
            # keyword = Your_name.listen_for_words()
            levelbatterys = get_battery_level()
            if levelbatterys < 20 and low_battery_say == False:
                playsounds("low_battery")
            # if keyword_index >= 0:
            # Your_name.main2()
            # filename = 'example/text.txt'
            keyword = Your_name.spech_texte()
            with open('settings.json', 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)

            # Получение списка имен ассистентов и очистка каждого имени от пробелов
            cleaned_names = [name.strip() for name in data["Asistent name"]]
            for name in cleaned_names:
                if fuzz.ratio(keyword, name) > 60:

                # if fuzz.ratio(keyword, name_asis) > 70:
                    # recorder.stop()
                    print("1")
                    playsounds("greet", True)
                    print("Yes, sir.")
                    # recorder.start()  # prevent self recording
                    ltc = time.time()

                while time.time() - ltc <= 10:
                    # pcm = recorder.read()
                    # sp = struct.pack("h" * len(pcm), *pcm)
                    # print("14")
                    # print(time.time() - ltc)
                    # print(kaldi_rec.AcceptWaveform(sp))
                    # if kaldi_rec.AcceptWaveform(sp):
                    #     print("7")
                    #     if respondes_voice(json.loads(kaldi_rec.Result())["text"]):
                    #         ltc = time.time()
                    #         print("23")
                    #
                    #     break
                    chunk_file = "temp_chunk.wav"
                    await record_chunk(p, stream, chunk_file)

                    if os.path.exists(chunk_file):  # Проверяем, существует ли файл перед транскрибацией
                        # print("44444444444444")
                        transcription = transcribe_chunk(model, chunk_file)

                        print(transcription)
                        if transcription != "":
                            print(7)
                            if respondes_voice(transcription):
                                ltc = time.time()
                                print("23")
                        os.remove(chunk_file)

                    else:
                        # print("Chunk file not created, skipping transcription.")
                        pass
                    # recognized_text = await recognize_speech(rec)
        except Exception as err:
            # print(f"Unexpected {err=}, {type(err)=}")
            raise

if __name__ == "__main__":
    asyncio.run(main())