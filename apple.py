from includes import *


class apple:

	def __eq__(self, to_compare):
		return self.x == to_compare.x and self.y == to_compare.y

	def __init__(self):
		self.x = self.y = 0
		self.randomize()

	def randomize(self):
		self.x = random.randrange(0, 800)
		self.y = random.randrange(0, 800)

	def draw(self, screen):
		pygame.draw.rect(screen, pygame.color.Color("black"), (self.x, self.y, pixel, pixel), 0)

