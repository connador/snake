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

	def draw_apples(self, collision=False):
		if collision:
			for i in range(number_of_apples):
				if self.apples[i] == collision:
					self.apples[i].randomize()
					self.player.grow()
		else:
			for i in range(3):
				self.apples[i].draw(screen)

	# Check to see if the snake head is colliding with the apple,
	# keeping in mind that the pixel block size needs to be added
	# since it is not very likely to ever get both blocks -exactly- aligned
	def check_collision(self, collision):
		for i in range(number_of_apples):
			if collision[0] < self.apples[i].x + pixel and \
				collision[1] < self.apples[i].y + pixel and \
				collision[0] + pixel > self.apples[i].x and \
				collision[1] + pixel > self.apples[i].y:
					pygame.draw.rect(screen, pygame.color.Color("white"), (self.apples[i].x, self.apples[i].y, pixel, pixel), 0)
					self.apples[i].randomize()
					return True
		return False

	def update(self):
		new_location = self.player.move()

		hit = self.check_collision(new_location)

		if hit:
			self.player.grow()

		self.draw_apples()



	# def apple_collision(self, collision):
		# TODO: change to hash table lookup?
		# for i in self.apples:
		# 	for k in self.apples:
		# 		if self.apples[i] == self.apples[k] and self.apples[i] is not self.apples[k]:
		# 			self.apples[k].randomize()
