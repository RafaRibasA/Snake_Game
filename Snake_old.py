import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((0, 200, 0))

while (True):

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))

    for position in snake:
        screen.blit(snake_skin, position)

    pygame.display.update()
