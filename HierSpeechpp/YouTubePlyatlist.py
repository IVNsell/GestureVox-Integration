from apiclient.discovery import build
from pytube import YouTube
import FIVferen
import os
import threading
import pygame
from GestureVoxIntegration import settext, play_audio_prost, convert_mp4_to_mp3, del_mp4_In_mp3

# Вставьте ваш API ключ от Google Developers Console
api_key = 'AIzaSyAHHO25q4gxlvbbfcYuaaYaI1RQY_bZvuA'
youtube = build('youtube', 'v3', developerKey=api_key)

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
def search_vieo_vrem_thread(video_title, SAVE_PATH, vals):
    # Поиск видео по названию
    request = youtube.search().list(
        q=video_title,
        part='snippet',
        type='video',
        maxResults=1
    )
    response = request.execute()

    # Получение первого видео из результатов
    if response['items']:
        video_id = response['items'][0]['id']['videoId']
        video_link = f'https://www.youtube.com/watch?v={video_id}'
        print(f'Найдено видео: {video_link}')
        # where to save
        # link of the video to be downloaded
        # link = "https://www.youtube.com/watch?v=g56ysfczDpU"

        try:
            # object creation using YouTube
            yt = YouTube(video_link)
            # Get all streams and filter for mp4 files
            mp4_streams = yt.streams.filter(file_extension='mp4').all()

            # get the video with the highest resolution
            d_video = mp4_streams[-1]

            try:
                # downloading the video
                d_video.download(
                    output_path=SAVE_PATH)
                print('Video downloaded successfully!')
                convert_mp4_to_mp3(SAVE_PATH)
                del_mp4_In_mp3(SAVE_PATH)
            except:
                print("Some Error!")
        except:
            # to handle exception
            print("Connection Error")
        if vals:
            play_music_now()
        return video_link
    else:
        print('Video not found.')
        FIVferen.youtube_video_not_found()
        play_audio_prost()
        return None
def search_video_vrem(video_title, SAVE_PATH, vals):
    thread = threading.Thread(target=search_vieo_vrem_thread(video_title, SAVE_PATH, vals))
    thread.start()

# Пример использования функции
# video_name = input('Введите название видео: ')
# search_video_vrem(video_name)