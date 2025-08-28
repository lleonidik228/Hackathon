import pygame
from pygame.locals import *
import consts

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)


pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

def draw_screen(sentence):
    screen.fill(consts.PYGAME_BACKGROUND_COLOR)
    text_surface = my_font.render(sentence, True, pygame.Color("white"));

    screen.blit(text_surface, (0, 0))

    pygame.display.update()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

# while True:
#     draw_screen("test")