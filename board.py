from includes import *

from snake import snake
from apple import apple

number_of_apples = 3


class board:

	def __init__(self):
		self.player = snake(screen_width/2, screen_height/2)

		self.apples = []
		for i in range(number_of_apples):
			self.apples.append(apple())

	def randomize_all(self):
		for i in self.apples:
			self.apples[i] = random.randrange(0, 800)

	def draw_apples(self):
		for i in range(3):
			self.apples[i].draw(screen)


	def apple_collision(self):
		# TODO: change to hash table lookup?
		for i in self.apples:
			for k in self.apples:
				if self.apples[i] == self.apples[k] and self.apples[i] is not self.apples[k]:
					self.apples[k].randomize()
