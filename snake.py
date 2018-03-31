from includes import *


class node:
	def __init__(self, data=False):
		if data:
			self.data = data
		else:
			self.data = None

		self.next = None


class linked_list:
	def __init__(self):
		self.head = None
		self.temp = None

	# insert just after head
	def insert(self, data):
		self.temp = node(data)
		self.temp.next = self.head.next
		self.head.next = self.temp


class segment:
	def __init__(self, loc_x, loc_y, direction):
		self.navigation = direction
		self.x = loc_x
		self.y = loc_y


class snake:

	def __init__(self, loc_x, loc_y):
		self.body = []
		self.body.append(segment(loc_x, loc_y, nav.n))
		self.length = 1

	def set_direction(self):
		events = pygame.event.get()

		for event in events:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.body[0].navigation = nav.w
				elif event.key == pygame.K_RIGHT:
					self.body[0].navigation = nav.e
				elif event.key == pygame.K_UP:
					self.body[0].navigation = nav.n
				elif event.key == pygame.K_DOWN:
					self.body[0].navigation = nav.s

	def draw(self, screen, i):
		# todo leap frog method of movement

		pygame.draw.rect(screen, pygame.color.Color("white"), (self.body[i].x, self.body[i].y, pixel, pixel), 0)

		if self.body[i].navigation is nav.n:
			self.body[i].y -= pixel
		elif self.body[i].navigation is nav.s:
			self.body[i].y += pixel
		elif self.body[i].navigation is nav.e:
			self.body[i].x += pixel
		else:
			self.body[i].x -= pixel

		pygame.draw.rect(screen, pygame.color.Color("black"), (self.body[i].x, self.body[i].y, pixel, pixel), 0)

	def move(self):
		# length = len(self.body)

		# Put end of tail at current head location
		# if length != 1:
		# 	old_tail = self.body.pop()
		# 	old_tail(self.x, self.y)
		# 	self.body.insert(old_tail, 0)

		# Move head in the faced direction

		self.set_direction()

		for i in range(len(self.body)):
			self.draw(screen, i)

		return [self.body[0].x, self.body[0].y]

	def grow(self):

		if self.length is 1:

			i = 0
			new_x = self.body[i].x
			new_y = self.body[i].y

			if self.body[i].navigation is nav.n:
				new_y += pixel
			elif self.body[i].navigation is nav.s:
				new_y -= pixel
			elif self.body[i].navigation is nav.e:
				new_x += pixel
			else:
				new_x -= pixel

			self.body.append(segment(new_x, new_y, self.body[i].navigation))

		else:
			length = len(self.body)

		#self.length += 1
		#self.body.append()
