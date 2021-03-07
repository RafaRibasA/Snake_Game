import pygame
import random
import sys


#class of the snake and his functions
class snake(object):

    def __init__(self):

        self.length = 1
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, RIGHT, LEFT])
        self.color = (17, 24, 47)
        pass

    def get_head_position(self):
        
        return self.positions[0]

    def turn(self, point):

        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point[ ]

        return

    def move(self):
        pass

    def reset(self):
        pass

    def draw(self, surface):
        pass

    def handle_keys(self):
        pass

class food(object): 

    def __init__(self):
        pass
    
    def randomize_position(self):
        pass

    def draw(self):
        pass

    def drawGrid(surface):

        for y in range(0, int(GRID_HEIGHT)):
            
            for x in range(0, int(GRID_WIDTH)):
                
                if (x + y) % 2 == 0:
                    r = pygame.Rect((x * GRIDSIZE, Y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                    pygame.draw.rect(surface, (93, 216, 228), r)
                else: 
                    rr = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                    pygame.draw.rect(surface, (84, 194, 205), rr)

    
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)


def main():

    pygame.init()

    clock = pygame.time.Clock()
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()


    snake = snake()
    food = food()

    score = 0

    while (True): 

        clock.tick(10)

        #sdadsd

        screen.blit(surface, (0, 0))
        pygame.display.update()


main()