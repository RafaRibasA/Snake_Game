import pygame

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((700,700))

pygame.display.set_caption('Snake')

while True: 

    for event in pygame.event.get():

        if event.type == QUIT :

            pygame.quit()

    pygame.display.update()