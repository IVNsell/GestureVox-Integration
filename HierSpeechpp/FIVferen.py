"""
C struct definitions credit
Author: sh-lee-prml  (https://github.com/sh-lee-prml)
Source: https://github.com/sh-lee-prml/HierSpeechpp
"""
import inference
import time
import threading
import simpleaudio as sa
import queue
import os
import re
import json
from g4f.client import Client
# import shutil
client = Client()
time.sleep(0.3)

def settext(text):
    with open("example/text.txt", 'w', encoding='utf-8') as file:
        file.write(text)
def time_sleep_threading(VotTime):
    print(VotTime)
    time.sleep(VotTime)

def ChatGPT_INF(voice):
    print("letsgo")
    error_occurred = False
    Err = False
    speech_finished = False
    speech_chunks = []
    speechs_chunks = []
    data_queue = queue.Queue()  # Очередь для передачи данных между потоками
    num = 0
    PlayTrue = True

    lock = threading.Lock()  # Создаем объект блокировки

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

    def play_audio_file(file_path):
        wave_obj = sa.WaveObject.from_wave_file(file_path)
        play_obj = wave_obj.play()
        play_obj.wait_done()

    def play_audio():
        num = 1
        error_count = 0  # Счетчик ошибок
        created_files = []  # Список созданных файлов
        while True:
            file_name = f"C:/Users/IVNsell/Desktop/IVNsell/Python/GestureVox Integration/Modern_GUI_PyDracula_PySide6_or_PyQt6-master/HierSpeechpp/HierSpeechpp/output/reference_{num}.wav"
            try:
                play_audio_file(file_name)
            except FileNotFoundError:
                print(f"File {file_name} not found. Stopping playback.")
                error_count += 1
                if error_count >= 15:  # Если возникает ошибка пять раз подряд
                    print("Error occurred 5 times in a row. Stopping playback.")
                    break
                time.sleep(0.1)  # Добавляем небольшую задержку перед следующей попыткой воспроизведения
                continue  # Продолжаем попытки воспроизведения
            num += 1
            error_count = 0  # Сбрасываем счетчик ошибок после успешного воспроизведения
            created_files.append(file_name)  # Добавляем имя файла в список созданных файлов

        # Удаление всех созданных файлов перед завершением программы
        for file_path in created_files:
            try:
                os.remove(file_path)
                print(f"File {file_path} removed.")
            except FileNotFoundError:
                print(f"File {file_path} not found.")
            except Exception as e:
                print(f"Error occurred while deleting {file_path}: {e}")

    def process_speech(speech_text):
        # Обработка текста речи здесь
        print(speech_text)

    last_words_processed = False
    with open('settings.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    dop_text = data["Chat_GPT"]
    while True:
        try:
            if not error_occurred and not speech_finished:
                streamers = client.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[{"role": "user", "content": f"{voice}?(and consider this {dop_text}"}],
                    # and consider this
                    stream=True,
                )
                print(str(voice))
                Err = False
                for chunk in streamers:
                    if chunk.choices[0].delta.content is not None:
                        speech_chunks.append(chunk.choices[0].delta.content)
                        speechs_chunks.append(chunk.choices[0].delta.content)
                        # print(' '.join(speechs_chunks))
                        if len(' '.join(speechs_chunks).split()) >= 7:
                            num += 1
                            responce_words = ' '.join(speechs_chunks)
                            responce_words = remove_emojis(responce_words)
                            responce_words = responce_words.replace('*', '')  # Удаление символа "*"
                            responce_words = responce_words.replace(' ,', ',')
                            responce_words = responce_words.replace('. ', '.')
                            responce_words = responce_words.replace(' .', '.')
                            responce_words = responce_words.replace('  ', ' ')
                            responce_words = responce_words.replace(' ) ', ')')
                            # with open("example/text.txt", 'w', encoding='utf-8') as file:
                            #     file.write(responce_words)
                            settext(responce_words)
                            print("                                                         Playing:",
                                  responce_words)
                            print(
                                f"                                                                                             Num: {num}")
                            inference.main(num, 'output')
                            if PlayTrue:
                                audio_thread = threading.Thread(target=play_audio)
                                audio_thread.start()  # Запускаем поток для воспроизведения аудио
                                PlayTrue = False

                            words = responce_words.split()[:7]
                            data_queue.put(words)
                            speechs_chunks.clear()
                    else:
                        stream_finished = True
                        break

                if stream_finished:
                    print("#########################")
                    if len(speechs_chunks) > 0 and not last_words_processed:
                        num += 1
                        responce_words = ' '.join(speechs_chunks)
                        responce_words = remove_emojis(responce_words)
                        responce_words = responce_words.replace('*', '')  # Удаление символа "*"
                        responce_words = responce_words.replace(' ,', ',')
                        responce_words = responce_words.replace('. ', '.')
                        responce_words = responce_words.replace(' .', '.')
                        responce_words = responce_words.replace('  ', ' ')
                        responce_words = responce_words.replace(' ) ', ')')
                        if responce_words == '' or responce_words == ' ' or responce_words == '.' or responce_words == ',' or responce_words == '!':
                            break
                        print("                                                         Playing:",
                              responce_words)
                        # with open("example/text.txt", 'w', encoding='utf-8') as file:
                        #     file.write(responce_words)
                        settext(responce_words)
                        inference.main(num, 'output')
                        words = responce_words.split()
                        data_queue.put(words)
                        speechs_chunks.clear()
                        last_words_processed = True
                    speech_finished = True

            if speech_finished:
                data_queue.put(None)
                audio_thread.join()
                break
            error_occurred = False

        except Exception as e:
            print("Произошла ошибка:", e)
            error_occurred = True
            Err = True

    # response = gpt_answer()
    # message_log.append({"role": "assistant", "content": response})
    # recorder.stop()
    # engine = pyttsx3.init()
    # engine.say(response)
    # engine.runAndWait()
    # print(response)
    # tts_test.plus_minus(response)

    # Jarvis_Voice.main(response)

    # Test_To_Speach.text_to_speech(response)
    threading.Thread(target=time_sleep_threading, args=(0.5,)).start()
    # recorder.start()
    return True

def Play_musc_prost_text_mus(text_mus):
    num = 1
    settext(f"Name of yout music: {text_mus}? It's that music?")
    inference.main(num, 'output')

def aud_to_text_thre():
    print("via")
    num = 1
    settext(f"Good morning")
    inference.main(num, "sounds_commands_voice/good_morning (2)")
    settext(f"Yes sir")
    inference.main(num, "sounds_commands_voice/yes_sir_I")
    settext(f"Done")
    inference.main(num, "sounds_commands_voice/done")
    settext(f"What do you want sir?")
    inference.main(num, "sounds_commands_voice/What_do_you_want_sir_I")
    settext(f"Low percentage of charge")
    inference.main(num, "sounds_commands_voice/low_battery")
    settext(f"Power off")
    inference.main(num, "sounds_commands_voice/Power_of_prog")
    settext(f"Are you sure you want everything back to the original settings?")
    inference.main(num, "sounds_commands_voice/Default")

def aud_to_text():
    print("vai")
    threading.Thread(target=aud_to_text_thre).start()

print("helpo")

# Рекурсивная функция для удаления всех папок и их содержимого
def remove_folders(path):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):  # Проверяем, является ли объект папкой
            remove_folders(item_path)  # Рекурсивно удаляем вложенные папки
        else:
            os.remove(item_path)  # Удаляем файлы внутри папки

    # После удаления всех файлов, удаляем саму папку
    try:
        os.rmdir(path)  # Удаляем пустую папку
        print(f"Удалена папка: {path}")
    except OSError as e:
        print(f"Ошибка при удалении папки {path}: {e}")

# Вызываем функцию для удаления всех папок в указанной директории
with open('Settings.json', 'r', encoding='utf-8') as default_file:
    settings = json.load(default_file)
if settings["FIV"] == "True":
    print("ok")
    directory = r'C:/Users/IVNsell/Desktop/IVNsell/Python/GestureVox Integration/Modern_GUI_PyDracula_PySide6_or_PyQt6-master/HierSpeechpp/HierSpeechpp/sounds_commands_voice/'
    remove_folders(directory)
    aud_to_text()
    settings["FIV"] = "False"
    with open('settings.json', 'w', encoding='utf-8') as settings_file:
        json.dump(settings, settings_file, indent=4, ensure_ascii=False)
def setTime(time):
    num = 1
    settext(time)
    inference.main(num, 'output')

def setWheather(wheather):
    num = 1
    settext(wheather)
    inference.main(num, 'output')

def Music_play_vrem(music):
    num = 1
    settext(f"Name of yout music: {music}? It's that music?")
    inference.main(num, 'output')

def LowBut(battery_level):
    num = 1
    settext(f"Battery level: {battery_level} percent")
    inference.main(num, 'output')

def defaoul_asis_name_threading():
    num = 1
    print(num)
    settext("Are you sure you want everything back to the original settings?")
    inference.main(num, 'output')

def defaoul_asis_name():
    threading.Thread(target=defaoul_asis_name_threading)
def youtube_video_not_found():
    settext('Video not found.')
    nuw = 1
    inference.main(nuw, 'output')