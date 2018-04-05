from includes import *
from board import board


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

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				finished = True


main()
