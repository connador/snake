from includes import *


class segment:
	def __init__(self, loc_x, loc_y):
		self.x = loc_x
		self.y = loc_y


class snake:

	def __init__(self, loc_x, loc_y):
		self.x = loc_x
		self.y = loc_y
		# self.body = [loc_x, loc_y]
		# self.body.append(segment(self.x, self.y))
		self.navigation = nav.n

	def move(self):
		#length = len(self.body)

		# Put end of tail at current head location
		# if length != 1:
		# 	old_tail = self.body.pop()
		# 	old_tail(self.x, self.y)
		# 	self.body.insert(old_tail, 0)

		# Move head in the faced direction

		pygame.draw.rect(screen, pygame.color.Color("white"), (self.x, self.y, pixel, pixel), 0)

		events = pygame.event.get()

		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.navigation = nav.w
				elif event.key == pygame.K_RIGHT:
					self.navigation = nav.e
				elif event.key == pygame.K_UP:
					self.navigation = nav.n
				elif event.key == pygame.K_DOWN:
					self.navigation = nav.s

		if self.navigation is nav.n:
			self.y += pixel * -1
		elif self.navigation is nav.s:
			self.y += pixel
		elif self.navigation is nav.e:
			self.x += pixel
		else:
			self.x += (pixel * -1)

		return [self.x, self.y]

	def draw(self, screen):
		pygame.draw.rect(screen, pygame.color.Color("black"), (self.x, self.y, pixel, pixel), 0)

	def grow(self):
		self.length += 1
	#self.body.append()
