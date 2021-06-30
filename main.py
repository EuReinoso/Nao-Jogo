import pygame, sys

pygame.init()

WINDOW_SIZE = (1280, 720)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Não Jogo')

loop = True
while loop:

    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
