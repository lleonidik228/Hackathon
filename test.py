import sys
import pygame
import speech_recognition as sr
# Initialize Pygame and the mixer
pygame.init()
pygame.mixer.init()

# Set up the display
screen_width, screen_height = (700, 400)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Voice Recognition Example')

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize the speech recognizer
recognizer = sr.Recognizer()

response = ""

# Function to recognize voice and return text
def recognize_speech_from_mic(recognizer, microphone):
    global response
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print('Ready to listen...')
        audio = recognizer.listen(source)

    try:
        print('Recognizing...')
        response = recognizer.recognize_google(audio)
        print(f'You said: {response}')
        return response
    except sr.UnknownValueError:
        print('Sorry, speech was unintelligible. Try again.')
        return None
    except sr.RequestError:
        print('Sorry, the speech service is down.')
        return None

# Main game loop
# running = True
# while running:
#     # Events handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         # Voice recognition integrated with an event
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_v:  # If 'v' is pressed, start voice recognition
#                 text = recognize_speech_from_mic(recognizer, sr.Microphone())
#                 if text:
#                     # Display the recognized text on the screen
#                     screen.fill(BLACK)
#                     font = pygame.font.SysFont(None, 48)
#                     text_surface = font.render(text, True, WHITE)
#                     text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2))
#                     screen.blit(text_surface, text_rect)
#
#     pygame.display.flip()
#
# # Clean up
# pygame.quit()
# sys.exit()
