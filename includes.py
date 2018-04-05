import pygame, enum, random, sys

pygame.init()
random.seed()

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
GREEN = (0, 255,   0)
RED = (255,   0,   0)

screen_width = screen_height = 800
pixel = screen_width / 100
font_size = int(pixel * 5)
number_of_apples = 3

fps = 20
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")
font = pygame.font.Font('resources/font.ttf', font_size)

timer = pygame.time.Clock()


class nav(enum.Enum):
	n = 0
	s = 1
	e = 2
	w = 3
