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

	def draw(self, i):
		# todo leap frog method of movement
		length = len(self.body) - 1

		if length == i:

			new_head = segment(self.body[0].x, self.body[0].y, self.body[0].navigation)

			if new_head.navigation is nav.n:
				new_head.y -= pixel
			elif new_head.navigation is nav.s:
				new_head.y += pixel
			elif new_head.navigation is nav.e:
				new_head.x += pixel
			else:
				new_head.x -= pixel

			self.body.insert(0, new_head)

			old_tail = self.body.pop()

			pygame.draw.rect(screen, pygame.color.Color("white"), (old_tail.x, old_tail.y, pixel, pixel), 0)
			pygame.draw.rect(screen, pygame.color.Color("black"), (new_head.x, new_head.y, pixel, pixel), 0)
		else:
			pass


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
			self.draw(i)

		return [self.body[0].x, self.body[0].y]

	def grow(self):
		insert_at = len(self.body) - 1

		new_x = self.body[insert_at].x
		new_y = self.body[insert_at].y

		if self.body[insert_at].navigation is nav.n:
			new_y += pixel
		elif self.body[insert_at].navigation is nav.s:
			new_y -= pixel
		elif self.body[insert_at].navigation is nav.e:
			new_x -= pixel
		else:
			new_x += pixel

		self.body.append(segment(new_x, new_y, self.body[insert_at].navigation))

		#self.length += 1
		#self.body.append()
