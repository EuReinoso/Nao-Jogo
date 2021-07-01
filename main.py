import pygame, sys
from player import Player
from obj import Obj

pygame.init()

WINDOW_SIZE = (1280, 720)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Não Jogo')

#Load Images
player_img  = pygame.image.load('assets/player.png')
ground_img  = pygame.image.load('assets/ground.png')
background1_img = pygame.image.load('assets/background1.png').convert()
background2_img = pygame.image.load('assets/background2.png').convert()

background1_img.set_colorkey((255, 255, 255))
background2_img.set_colorkey((255, 255, 255))

ground_img_top = pygame.transform.flip(ground_img, False, True)
background1_img_top = pygame.transform.flip(background1_img, False, True)
background2_img_top = pygame.transform.flip(background2_img, False, True)

player_init_pos = [WINDOW_SIZE[0] * 0.3, WINDOW_SIZE[1]/2]
player          = Player(player_img, player_init_pos)

ground_size     = [WINDOW_SIZE[0] + 10, int(WINDOW_SIZE[1] * 0.2)]
ground_bottom   = Obj(0, WINDOW_SIZE[1] - ground_size[1], ground_size[0], ground_size[1], img= ground_img)
ground_bottom_2 = Obj(WINDOW_SIZE[0], WINDOW_SIZE[1] - ground_size[1], ground_size[0], ground_size[1], img= ground_img)
ground_top      = Obj(0, 0, ground_size[0], ground_size[1], img= ground_img_top)
ground_top_2    = Obj(WINDOW_SIZE[0], 0, ground_size[0], ground_size[1], img= ground_img_top)

background1_size     = [WINDOW_SIZE[0] + 10, int(WINDOW_SIZE[1] * 0.8)]
background1_bottom   = Obj(0, WINDOW_SIZE[1] - background1_size[1], background1_size[0], background1_size[1], img= background1_img)
background1_bottom_2 = Obj(WINDOW_SIZE[0], WINDOW_SIZE[1] - background1_size[1], background1_size[0], background1_size[1], img= background1_img)
background1_top      = Obj(0, 0, background1_size[0], background1_size[1], img= background1_img_top)
background1_top_2    = Obj(WINDOW_SIZE[0], 0, background1_size[0], background1_size[1], img= background1_img_top)

background2_size     = [WINDOW_SIZE[0] + 10, int(WINDOW_SIZE[1] * 0.9)]
background2_bottom   = Obj(0, WINDOW_SIZE[1] - background2_size[1], background2_size[0], background2_size[1], img= background2_img)
background2_bottom_2 = Obj(WINDOW_SIZE[0], WINDOW_SIZE[1] - background2_size[1], background1_size[0], background1_size[1], img= background2_img)
background2_top      = Obj(0, 0, background2_size[0], background2_size[1], img= background2_img_top)
background2_top_2    = Obj(WINDOW_SIZE[0], 0, background2_size[0], background2_size[1], img= background2_img_top)


grounds_list    = [ ground_bottom, ground_top, ground_bottom_2, ground_top_2]
background_list = [ background2_bottom, background2_bottom_2, background2_top, background2_top_2,
                    background1_bottom, background1_bottom_2, background1_top, background1_top_2]

vel = 5
fps = 60
time = pygame.time.Clock()
loop = True

def grounds_update():
    draw_grounds()
    move_grounds()
    restart_ground()

def draw_grounds():
    for ground in grounds_list:
        ground.draw_img(window)

def move_grounds():
    for ground in grounds_list:
        ground.set_pos([ground.pos[0] - int(vel), ground.pos[1]])

def restart_ground():
    for ground in grounds_list:
        if ground.pos[0] < - WINDOW_SIZE[0]:
            ground.set_pos([WINDOW_SIZE[0], ground.pos[1]])

def background_update():
    draw_background()
    move_background()
    restart_background()

def draw_background():
    for bg in background_list:
        bg.draw_img(window)

def move_background():
    for bg in background_list:
        bg.set_pos([bg.pos[0] - int(vel * 0.5), bg.pos[1]])

def restart_background():
    for bg in background_list:
        if bg.pos[0] < -WINDOW_SIZE[0]:
            bg.set_pos([WINDOW_SIZE[0], bg.pos[1]])


while loop:

    window.fill((47, 58, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.control(event)

    #background
    background_update()
    #ground
    grounds_update()

    #player
    player.update()
    player.draw(window)

    #move
    
    pygame.display.update()
    time.tick(fps)
