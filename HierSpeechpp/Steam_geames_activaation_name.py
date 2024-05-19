import configparser
import os
import subprocess
import pygetwindow as gw
from fuzzywuzzy import fuzz
import json
# Путь к файлу .url
# with open('settings.json', 'r', encoding='utf-8') as json_file:
#     data = json.load(json_file)

# Путь к директории
# directory = 'C:\\Users\\IVNsell\\OneDrive\\Рабочий стол'
# Вывод всех файлов в директории
def close_window(window_title):
    print(1)
    target_window = gw.getWindowsWithTitle(window_title)
    if target_window:
        target_window[0].close()
def GP_open_steam(game_id):
    print(12)
    steam_path = r"C:\Program Files (x86)\Steam\steam.exe"  # Укажите путь к исполняемому файлу Steam
    subprocess.Popen([steam_path, f"steam://rungameid/{game_id}"])

def game(game_name, file_folder):
    for filename in os.listdir(file_folder):
        if os.path.isfile(os.path.join(file_folder, filename)):
            if fuzz.ratio(game_name, filename) > 60:
                file_path = f'{file_folder}\{filename}'

                # Проверяем, существует ли файл
                if os.path.exists(file_path):
                    # Используем ConfigParser для чтения файла .url
                    config = configparser.ConfigParser()
                    config.read(file_path)

                    # Извлекаем URL
                    url = config.get('InternetShortcut', 'URL')
                    print(f'URL game: {url}')
                    id = url.split('/')[-1]
                    print(f"ID: {id}")
                    window_title_to_close = "Steam"
                    close_window(window_title_to_close)
                    GP_open_steam(id)
                else:
                    print('File not found (may be a problem with the file path).')
# game_name = input("Write your game: ")
# # file_folder = data["Path_Foler_Steam"]
# file_folder = input("Write path: ")
# print(file_folder)
# game(game_name, file_folder)