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
			for i in range(len(self.apples)):
				if self.apples[i] == collision:
					self.apples[i].randomize()
					self.player.grow()
		else:
			for i in range(len(self.apples)):
				self.apples[i].draw(screen)

	# Check to see if the snake head is colliding with the apple,
	# keeping in mind that the pixel block size needs to be added
	# since it is not very likely to ever get both blocks -exactly- aligned
	def check_collision(self, new_location, locations):
		signal = -1
		for i in range(len(locations)):
			if new_location[0] < locations[i].x + pixel and \
				new_location[1] < locations[i].y + pixel and \
				new_location[0] + pixel > locations[i].x and \
				new_location[1] + pixel > locations[i].y:
				signal = i

		return signal

	def game_over(self):
		message = font.render('Game Over!', False, BLACK)
		center = message.get_rect(center=(screen_width/2, screen_height/2))
		screen.blit(message, center)

		message = font.render('Press \'r\' to continue!', False, BLACK)
		center = message.get_rect(center=(screen_width/2, screen_height/2 + font_size))
		screen.blit(message, center)

		return 0


	def update(self):
		self.draw_apples()

		new_location = self.player.move()

		# Check if an apple was hit
		hit = self.check_collision(new_location, self.apples)

		if hit > -1:
			pygame.draw.rect(screen, WHITE, (self.apples[hit].x, self.apples[hit].y, pixel, pixel), 0)
			self.apples[hit].randomize()

			self.player.grow()

		# Check if the snake body was hit
		hit = self.check_collision(new_location, self.player.body)

		if hit > 0:
			return self.game_over()

		return 1
