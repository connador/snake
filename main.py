from includes import *
from board import board

def check_quit():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True

	return False

def main():

	game = board()
	screen.fill(WHITE)

	finished = False
	while not finished:
		clock.tick(fps)

		status = game.update()

		while status == 0:
			pygame.display.flip()
			clock.tick(fps)
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_r:
						game = board()
						screen.fill(WHITE)
						status = 1
				elif event.type == pygame.QUIT:
					status = 1
					finished = True

		pygame.display.flip()

		#finished = check_quit

	#sys.exit()

	# while True:
	# 	events = pygame.event.get()
	# 	for event in events:
	# 		if event.type == pygame.KEYDOWN:
	# 			if event.key == pygame.K_LEFT:
	# 				print("Left Key")
	# 			elif event.key == pygame.K_RIGHT:
	# 				print("Right Key")


	# pygame.event.pump()
	# keys = pygame.key.get_pressed()
	#
	# if keys[pygame.K_RIGHT]:
	# 	print("Right arrow pressed")
	#
	# keys[pygame.K_RIGHT]


main()
