import pygame, sys
from player import Player

pygame.init()

WINDOW_SIZE = (1280, 720)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Não Jogo')

player_img = pygame.image.load("assets/player.png")
player = Player(player_img, [WINDOW_SIZE[0] * 0.3, WINDOW_SIZE[1]/2])

ground_down = pygame.image.load('assets/ground.png')
ground_down = pygame.transform.scale(ground_down, (WINDOW_SIZE[0], int(WINDOW_SIZE[1] * 0.16)))
ground_down_pos = [0, WINDOW_SIZE[1] * 0.84]
ground_down_rect = pygame.Rect(ground_down_pos[0], ground_down_pos[1], ground_down.get_width(), ground_down.get_height())

ground_up = ground_down.copy()
ground_up = pygame.transform.flip(ground_up, False, True)
ground_up_pos = [0, 0]
ground_up_rect = pygame.Rect(ground_up_pos[0], ground_up_pos[1], ground_up.get_width(), ground_up.get_height())

ground2_down = ground_down.copy()
ground2_up = ground_up.copy()

grounds_rect_list = [ground_up_rect, ground_down_rect]

background1_down = pygame.image.load('assets/background1.png').convert()
background1_down.set_colorkey((255, 255, 255))
background1_down = pygame.transform.scale(background1_down, (WINDOW_SIZE[0], int(WINDOW_SIZE[1] * 0.8)))
background1_up = background1_down.copy()
background1_up = pygame.transform.flip(background1_up, False, True)
background1_pos = [0, 0]

background1_2_down = background1_down.copy()
background1_2_up = background1_up.copy()

background2_down = pygame.image.load('assets/backgound2.png').convert()
background2_down.set_colorkey((255, 255, 255))
background2_down = pygame.transform.scale(background2_down, (WINDOW_SIZE[0], int(WINDOW_SIZE[1] * 0.8)))
background2_up = background2_down.copy()
background2_up = pygame.transform.flip(background2_up, False, True)
background2_pos = [0, 0]

background2_2_down = background2_down.copy()
background2_2_up = background2_up.copy()

vel = 2

def grounds_update():
    ground_down_rect.x = ground_down_pos[0]
    ground_down_rect.y = ground_down_pos[1]

    ground_up_rect.x = ground_up_pos[0]
    ground_up_rect.y = ground_up_pos[1]

def game_move():
    ground_down_pos[0] -= vel
    ground_up_pos[0] -= vel

    background1_pos[0] -= vel  * 0.5
    background2_pos[0] -= vel * 0.2

loop = True
while loop:

    window.fill((47, 58, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.control(event)

    #background
    window.blit(background2_down, (background2_pos[0], WINDOW_SIZE[1] - background2_up.get_height()))
    window.blit(background2_up, background2_pos)
    window.blit(background1_down, (background1_pos[0], WINDOW_SIZE[1] - background1_up.get_height()))
    window.blit(background1_up, background1_pos)

    window.blit(background2_2_down, (background2_pos[0] + WINDOW_SIZE[0] -1, WINDOW_SIZE[1] - background2_up.get_height()))
    window.blit(background2_2_up, (background2_pos[0] + WINDOW_SIZE[0] -1, background2_pos[1]))
    window.blit(background1_2_down, (background1_pos[0] + WINDOW_SIZE[0] -1, WINDOW_SIZE[1] - background1_up.get_height()))
    window.blit(background1_2_up, (background1_pos[0] + WINDOW_SIZE[0] -1, background1_pos[1]))

    #ground
    window.blit(ground_down, ground_down_pos)
    window.blit(ground_up, ground_up_pos)
    window.blit(ground2_down, (ground_down_pos[0] + WINDOW_SIZE[0] - 1, ground_down_pos[1]))
    window.blit(ground2_up, (ground_up_pos[0] + WINDOW_SIZE[0] -1, ground_up_pos[1]))

    #player
    player.update()
    player.draw(window)
    player.ground_collide(ground_down_rect, ground_up_rect)

    #move
    grounds_update()
    game_move()
    
    pygame.display.update()
