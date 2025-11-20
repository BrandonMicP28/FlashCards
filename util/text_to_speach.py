from io import BytesIO

import pygame
from gtts import gTTS

if not pygame.mixer.get_init():
    pygame.mixer.init(frequency=24000, buffer=4096)

def text_to_german(text: str):

    tts = gTTS(text=text, lang="de")

    tts_mp3 = BytesIO()
    tts.write_to_fp(tts_mp3)

    tts_mp3.seek(0)

    pygame.mixer.music.load(tts_mp3)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)