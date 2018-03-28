import random

random.seed()

class apple:

	def __init__(self):
		self.randomize()

	def randomize(self):
		self.x = random.randrange(0, 800)
		self.y = random.randrange(0, 800)

