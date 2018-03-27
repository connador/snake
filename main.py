import sys, pygame, random, apple
from snake import snake


pygame.init()
random.seed()

screen_width = 800
screen_height = 800
pixel = 8

screen = pygame.display.set_mode((screen_width, screen_height))

timer = pygame.time.Clock()


def main():
   player = snake(screen_width/2, screen_height/2)





