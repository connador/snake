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

		# Leap frog implementation of movement.
		# Essentially, the tail moves up to the front and becomes new head

		length = len(self.body) - 1

		# Only do any draw calls if we're at the tail
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

			# Clean up location of tail before move
			pygame.draw.rect(screen, WHITE, (old_tail.x, old_tail.y, pixel, pixel), 0)

			# Draw at the front
			pygame.draw.rect(screen, BLACK, (new_head.x, new_head.y, pixel, pixel), 0)
		else:
			pass


	def move(self):

		# Change head location, based on keyboard input
		self.set_direction()

		# leap frog movement of head to tail
		self.draw(len(self.body) - 1)

		# return new location of head to check for collisions
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
