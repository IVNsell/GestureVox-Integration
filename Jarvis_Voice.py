import openai
import pygame

def main(text):
    client = openai.OpenAI(api_key="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")
    speech_file_path = "speech.mp3"
    # client.api_key = "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"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(speech_file_path)
    pygame.init()
    song = pygame.mixer.Sound('speech.mp3')
    clock = pygame.time.Clock()
    song.play()
    while True:
        clock.tick(60)
    pygame.quit()
# main("hello")