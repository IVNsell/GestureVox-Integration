# import speech_recognition as sr
# r = sr.Recognizer()
# def listen_for_words():
#     with sr.Microphone() as source:
#         print("Say something...")
#         audio = r.listen(source)
#
#         try:
#             # Распознавание речи с использованием Google Web Speech API
#             recognized_text = r.recognize_google(audio, language="en-US")
#             print("You said: " + recognized_text)
#             return recognized_text
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         except sr.RequestError as e:
#             print("Speech recognition service error; {0}".format(e))
from faster_whisper import WhisperModel
import pyaudio
import wave
import os
import numpy as np
import time
import asyncio
def is_silent(data, threshold=500):
    """Check if the audio chunk is silent based on the threshold."""
    return np.max(data) < threshold

def record_chunk(p, stream, file_path, silence_threshold=0.3):
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
                # print(f"Chunk length: {chunk_length} seconds")
                break

    if frames:
        frames = b''.join(frames)
        wf = wave.open(file_path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(16000)
        wf.writeframes(frames)
        wf.close()
        # print(f"Recorded chunk saved to {file_path}")
    else:
        # print("Silent chunk ignored")
        pass

def transcribe_chunk(model, chunk_file):
    segments, info = model.transcribe(chunk_file, language="en", beam_size=20, vad_filter=True, condition_on_previous_text=False)
    # print("5555555555555")
    # print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    transcription = ' '.join(segment.text for segment in segments)
    return transcription

model_size = "medium.en"
model = WhisperModel(model_size, device="cuda", compute_type="float16")
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

def spech_texte():

    chunk_file = "temp_chunk.wav"
    record_chunk(p, stream, chunk_file)

    if os.path.exists(chunk_file):  # Проверяем, существует ли файл перед транскрибацией
        transcription = transcribe_chunk(model, chunk_file)
        # print(transcription)
        # os.remove(chunk_file)
        return transcription


# if __name__ == "__main__":
#     reusult = spech_texte()
#     print(f"Result {reusult}.")