import sys, pygame, random, apple
from snake import snake
from enum import Enum


pygame.init()
random.seed()

screen_width = 800
screen_height = 800
pixel = 8

screen = pygame.display.set_mode((screen_width, screen_height))

timer = pygame.time.Clock()

class nav(Enum):
  n = 0
  s = 1
  e = 2
  w = 3


def main():
  player = snake(screen_width/2, screen_height/2)





