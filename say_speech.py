import time
from gtts import gTTS
import pygame


# This module is imported so that we can
# play the converted audio

# The text that you want to convert to audio
# for i in range(len(mytext)):
#     if mytext[i] == mytext[i+1] and i+2 < len(mytext):
#        mytext.(mytext[i+1])

def create_pm3_file(text=None):
    print("Hello, create music was started")
    if not text:
        text = input("enter text: ")
    language = 'en'
    print(text)
    text = gTTS(text=text, lang=language, slow=False)
    text.save("user_sentence.mp3")
    play_sound()


def play_sound():
    pygame.mixer.init()
    sound = pygame.mixer.Sound("user_sentence.mp3")
    sound.play()
    time.sleep(sound.get_length())


if __name__ == '__main__':
    create_pm3_file()
    play_sound()

