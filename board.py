from apple import apple
from snake import snake
from main import screen_width, screen_height, random

random.seed()
number_of_apples = 3


class board:

	def __init__(self):
		self.player = snake(screen_width/2, screen_height/2)

		self.apples = [number_of_apples]
		for i in self.apples:
			self.apples[i] = apple()

	def randomize_all(self):
		for i in self.apples:
			self.apples[i] = random.randrange(0, 800)
