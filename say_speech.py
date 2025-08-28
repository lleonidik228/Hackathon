import time
from gtts import gTTS
import pygame

# This module is imported so that we can
# play the converted audio

# The text that you want to convert to audio


pygame.mixer.init()


def create_pm3_file(text=None, lang="en"):
    print("Hello, create music was started")
    if not text:
        text = input("enter text: ")
    language = lang
    print(text)
    text = gTTS(text=text, lang=language, slow=False)
    text.save("user_sentence.mp3")
    play_sound("user_sentence.mp3")
    # play_sound("hello_mother.mp3")


def play_sound(name_file):
    sound = pygame.mixer.Sound(f"{name_file}")
    sound.play()
    time.sleep(sound.get_length())


if __name__ == '__main__':
    create_pm3_file()
    # play_sound()

