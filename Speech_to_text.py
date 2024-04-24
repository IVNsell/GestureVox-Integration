from faster_whisper import WhisperModel
import pyaudio
import wave
import os
import numpy as np

def is_silent(data, threshold=5000):
    """
    Функция, которая проверяет, является ли аудио-данные тихими.
    """
    return np.max(data) < threshold

def record_chunk(p, stream, file_path, chunk_length=2):
    frames = []
    for _ in range(0, int(16000 / 1024 * chunk_length)):
        data = stream.read(1024)
        frames.append(data)

    frames = b''.join(frames)
    audio_data = np.frombuffer(frames, dtype=np.int16)  # Преобразуем в массив NumPy
    if not is_silent(audio_data):
        wf = wave.open(file_path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(16000)
        wf.writeframes(frames)
        wf.close()
    else:
        # print("Silent chunk ignored")
        pass


def transcribe_chunk(model, chunk_file):
    segments, info = model.transcribe(chunk_file, beam_size=10, language="en", vad_filter=True, condition_on_previous_text=False)

    # print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

    transcription = ' '.join(segment.text for segment in segments)
    return transcription


def main2():
    model_size = "medium.en"
    model = WhisperModel(model_size, device="cuda", compute_type="float16")

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

    accumulated_transcription = ""

    try:
        while True:
            chunk_file = "temp_chunk.wav"
            record_chunk(p, stream, chunk_file)

            if os.path.exists(chunk_file):  # Проверяем, существует ли файл перед транскрибацией
                transcription = transcribe_chunk(model, chunk_file)
                print(transcription)
                os.remove(chunk_file)

                accumulated_transcription += transcription + " "
            else:
                # print("Chunk file not created, skipping transcription.")
                pass
    except KeyboardInterrupt:
        print("Stopping...")
        with open("log.txt", "w") as log_file:
            log_file.write(accumulated_transcription)
    finally:
        print("LOG:" + accumulated_transcription)
        stream.stop_stream()
        stream.close()
        p.terminate()


if __name__ == "__main__":
    main2()