from apiclient.discovery import build
from pytube import YouTube

# Вставьте ваш API ключ от Google Developers Console
api_key = 'AIzaSyAHHO25q4gxlvbbfcYuaaYaI1RQY_bZvuA'
youtube = build('youtube', 'v3', developerKey=api_key)

def search_video_vrem(video_title, SAVE_PATH):
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
            except:
                print("Some Error!")
        except:
            # to handle exception
            print("Connection Error")
        return video_link
    else:
        print('Video not found.')
        return None

# Пример использования функции
# video_name = input('Введите название видео: ')
# search_video_vrem(video_name)