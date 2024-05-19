import os
import simpleaudio as sa
import time
import asyncio
import numpy as np
import pyaudio
import wave
from faster_whisper import WhisperModel
from fuzzywuzzy import fuzz
import json
import FIVferen

def chose_name():
    CDIR = os.getcwd()
    filename = f"{CDIR}\\sounds\\gudok.wav"
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()


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

def saveCheckBoxValues(data):
    with open('settings.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

async def main_logic_name():
    with open('settings.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    Vup_task = data["Name_asis_default"]
    name_num = int(data["Name_number"])
    print(Vup_task.lower())
    if Vup_task.lower() == 'true':
        recordings = []
        for _ in range(name_num):  # Повторяем процесс 3 раза
            chose_name()  # Воспроизводим гудок
            record_chunk(p, stream, chunk_file)  # Записываем голос
            if os.path.exists(chunk_file):
                transcription = transcribe_chunk(model, chunk_file)
                recordings.append(transcription.lower())  # Добавляем транскрипцию в список
                print("|||||||||||||||||||||||||||||||||||")
                print(transcription)
                print("|||||||||||||||||||||||||||||||||||")
        # return recordings
        data["Asistent name"] = recordings
        print(recordings)
        saveCheckBoxValues(data)
    elif Vup_task.lower() == 'false':
        print("12341234")
        FIVferen.defaoul_asis_name_threading()
        play_audio_prost()
        recordings = []
        record_chunk(p, stream, chunk_file)  # Записываем голос
        if os.path.exists(chunk_file):
            transcription = transcribe_chunk(model, chunk_file)
            recordings.append(transcription.lower())  # Добавляем транскрипцию в список
            print("|||||||||||||||||||||||||||||||||||")
            transcription = transcription.lower().replace(".", "")
            print(transcription)
            print("|||||||||||||||||||||||||||||||||||")
            if fuzz.ratio(transcription, "yes") > 60:
                print("Yes.")
                recordings = True
            elif fuzz.ratio(transcription, "no") > 60:
                print("No.")
                recordings = False

            # return recordings
            if recordings == True:
                with open('Settings_Default.json', 'r', encoding='utf-8') as default_file:
                    default_settings = json.load(default_file)

                # Записываем содержимое в файл settings.json, перезаписывая его
                with open('settings.json', 'w', encoding='utf-8') as settings_file:
                    json.dump(default_settings, settings_file, indent=4, ensure_ascii=False)
            else:
                pass

def settext(text):
    with open("example/text.txt", 'w', encoding='utf-8') as file:
        file.write(text)

def play_audio_prost():
    file_name = "C:/Users/IVNsell/Desktop/IVNsell/Python/GestureVox Integration/Modern_GUI_PyDracula_PySide6_or_PyQt6-master/HierSpeechpp/HierSpeechpp/sounds_commands_voice/Default.wav"
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

# Инициализация модели и потока записи
model_size = "medium.en"
model = WhisperModel(model_size, device="cuda", compute_type="float16")

chunk_file = "temp_chunk_music.wav"
waiting_for_response = True
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

# Запуск основной логики
asyncio.run(main_logic_name())
# recordings_list = main_logic()
# print(recordings_list)  # Выводим список записей

# Закрытие потока и PyAudio
# stream.stop_stream()
# stream.close()
# p.terminate()