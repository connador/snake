import pygame, enum, random, sys

pygame.init()
random.seed()

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)

screen_width = 800
screen_height = 800
pixel = 8
fps = 20
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

timer = pygame.time.Clock()


class nav(enum.Enum):
	n = 0
	s = 1
	e = 2
	w = 3
