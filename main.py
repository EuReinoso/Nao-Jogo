import pygame, sys
from random import randint,random
from assets.scripts.player import Player
from assets.scripts.obj import Obj

import numpy as np
import time

pygame.init()

WINDOW_SIZE = (1280, 720)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Não Jogo')

#Load Images
player_img  = pygame.image.load('assets/images/player.png')
ground_img  = pygame.image.load('assets/images/ground.png')
background1_img = pygame.image.load('assets/images/background1.png').convert()
background2_img = pygame.image.load('assets/images/background2.png').convert()
block_img = pygame.image.load('assets/images/block.png')

background1_img.set_colorkey((255, 255, 255))
background2_img.set_colorkey((255, 255, 255))

ground_img_top = pygame.transform.flip(ground_img, False, True)
background1_img_top = pygame.transform.flip(background1_img, False, True)
background2_img_top = pygame.transform.flip(background2_img, False, True)

player_init_pos = [WINDOW_SIZE[0] * 0.5, WINDOW_SIZE[1]/2]
player          = Player(player_init_pos[0], player_init_pos[1], int(WINDOW_SIZE[0] * 0.05), int(WINDOW_SIZE[0] * 0.05),img= player_img)
player_positions = [[], []]

ground_size     = [WINDOW_SIZE[0] + 20, int(WINDOW_SIZE[1] * 0.2)]
ground_bottom   = Obj(0, WINDOW_SIZE[1] - ground_size[1], ground_size[0], ground_size[1], img= ground_img)
ground_bottom_2 = Obj(WINDOW_SIZE[0], WINDOW_SIZE[1] - ground_size[1], ground_size[0], ground_size[1], img= ground_img)
ground_top      = Obj(0, 0, ground_size[0], ground_size[1], img= ground_img_top)
ground_top_2    = Obj(WINDOW_SIZE[0], 0, ground_size[0], ground_size[1], img= ground_img_top)

background1_size     = [WINDOW_SIZE[0] + 20, int(WINDOW_SIZE[1] * 0.8)]
background1_bottom   = Obj(0, int(WINDOW_SIZE[1] * 1.1) - background1_size[1], background1_size[0], background1_size[1], img= background1_img)
background1_bottom_2 = Obj(WINDOW_SIZE[0], int(WINDOW_SIZE[1] * 1.1) - background1_size[1], background1_size[0], background1_size[1], img= background1_img)
background1_top      = Obj(0, 0 - int(WINDOW_SIZE[1] * 0.1), background1_size[0], background1_size[1], img= background1_img_top)
background1_top_2    = Obj(WINDOW_SIZE[0], 0 - int(WINDOW_SIZE[1] * 0.1), background1_size[0], background1_size[1], img= background1_img_top)

background2_size     = [WINDOW_SIZE[0] + 10, int(WINDOW_SIZE[1] * 0.7)]
background2_bottom   = Obj(0, WINDOW_SIZE[1] - background2_size[1], background2_size[0], background2_size[1], img= background2_img)
background2_bottom_2 = Obj(WINDOW_SIZE[0], WINDOW_SIZE[1] - background2_size[1], background2_size[0], background2_size[1], img= background2_img)
background2_top      = Obj(0, 0, background2_size[0], background2_size[1], img= background2_img_top)
background2_top_2    = Obj(WINDOW_SIZE[0], 0, background2_size[0], background2_size[1], img= background2_img_top)

block_size_range = [int(WINDOW_SIZE[1] * 0.1), int(WINDOW_SIZE[0] * 0.1)]

grounds_list     = [ ground_bottom, ground_top, ground_bottom_2, ground_top_2]
background1_list = [ background1_bottom, background1_bottom_2, background1_top, background1_top_2]
background2_list = [ background2_bottom, background2_bottom_2, background2_top, background2_top_2]
background_list  = [ background2_bottom, background2_bottom_2, background2_top, background2_top_2,
                     background1_bottom, background1_bottom_2, background1_top, background1_top_2]
block_list = []
block_ticks = 0
block_spawn_range = [20, 60]
block_spawn_x = ground_bottom.pos[0] + WINDOW_SIZE[0]
block_tick_spaw = randint(block_spawn_range[0], block_spawn_range[1])

scroll = 0
vel = 6
fps = 60
clock = pygame.time.Clock()
loop = True

def grounds_update():
    draw_grounds()
    restart_ground()
    move_grounds()

def draw_grounds():
    for ground in grounds_list:
        ground.draw_img(window)

def move_grounds():
     [ground.set_pos([int(ground.pos[0] - vel), ground.pos[1]]) for ground in grounds_list]
         

def restart_ground():
    for ground in grounds_list:
        if ground.pos[0] < - WINDOW_SIZE[0]:
            ground.set_pos([WINDOW_SIZE[0], ground.pos[1]])

def background_update():
    draw_background()
    restart_background()
    move_background()

def draw_background():
    for bg in background_list:
        bg.draw_img(window, scroll= scroll)

def move_background():
    for bg in background1_list:
        bg.set_pos([bg.pos[0] - int(vel * 0.5), bg.pos[1]])
    for bg in background2_list:
        bg.set_pos([bg.pos[0] - int(vel * 0.2), bg.pos[1]])

def restart_background():
    for bg in background_list:
        if bg.pos[0] < -WINDOW_SIZE[0]:
            bg.set_pos([WINDOW_SIZE[0], bg.pos[1]])

def get_rects(objs):
    rects = []
    for obj in objs:
        rects.append(obj.rect)
    return rects

def spawn_blocks():
    pos = 0
    block_size = randint(block_size_range[0], block_size_range[1]) 
    block_bottom_pos = [block_spawn_x, ground_bottom.pos[1] - block_size]
    block_top_pos = [block_spawn_x, ground_top.pos[1] + ground_top.height]

    if random() > 0.5:
        pos = block_bottom_pos
    else:
        pos = block_top_pos
    
    
    block = Obj(pos[0], pos[1], block_size, block_size, img= block_img)
    block_list.append(block)

def draw_blocks():
    for block in block_list:
        block.draw_img(window)

def move_blocks():
    for block in block_list:
        block.set_pos([block.pos[0] - vel, block.pos[1]])

# def test_vel(num):
#     start_time = time.time()

#     for i in range(num):
#         

#     print("A: --- %s ms ---" % ((time.time() - start_time)* 1000))

#     start_time = time.time()
#     for i in range(num):
#         
#     print("B: --- %s ms ---" % ((time.time() - start_time)* 1000))

# test_vel(10000)
# sys.exit()

while loop:

    window.fill((47, 58, 100))

    scroll += (player.pos[1] + (player.height/2) - (WINDOW_SIZE[1]/2) - scroll)/15
    block_ticks += 1

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
    
    #block
    if block_ticks > block_tick_spaw:
        spawn_blocks()
        block_ticks = 0
        block_tick_spaw = randint(block_spawn_range[0], block_spawn_range[1])
    if len(block_list) > 0:
        draw_blocks()
        move_blocks()

    #player
    player.draw_img(window)
    player.update()
    player.collide_ground(get_rects(grounds_list))
    if player.collide_block(get_rects(block_list)):
        player.pos[0] -= vel

    if player.get_pos() != player_positions[0]:
        player_positions[1] = player_positions[0]
        player_positions[0] = player.get_pos()
        player.set_last_pos(player_positions[1])

    pygame.display.update()
    clock.tick(fps)
