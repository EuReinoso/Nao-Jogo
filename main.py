import pygame, sys
from pygame.locals import *
from random import randint, random
from assets.scripts.player import Player
from assets.scripts.obj import Obj
from assets.scripts.villain import Villain

pygame.init()
pygame.font.init()
pygame.mixer.init()

WINDOW_SIZE = (894, 594)

window = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption('Gravity Block')

#sounds load
music = pygame.mixer.music.load('assets/sounds/Boss Music.mp3')
pygame.mixer.music.set_volume(0.1)

dash_sound = pygame.mixer.Sound('assets/sounds/dash.wav')
dash_sound.set_volume(0.5)
invert_sound = pygame.mixer.Sound('assets/sounds/invert.wav')
invert_sound.set_volume(0.5)
lose_sound = pygame.mixer.Sound('assets/sounds/lose.wav')

#Load Images
player_img  = pygame.image.load('assets/images/player.png')
ground_img  = pygame.image.load('assets/images/ground.png')
background1_img = pygame.image.load('assets/images/background1.png').convert()
background2_img = pygame.image.load('assets/images/background2.png').convert()
block_img = pygame.image.load('assets/images/block.png')
villain_img = pygame.image.load('assets/images/villain.png')
arrow_img = pygame.image.load('assets/images/arrow.png')
wall_img = pygame.image.load('assets/images/wall.png')

background1_img.set_colorkey((255, 255, 255))
background2_img.set_colorkey((255, 255, 255))
arrow_img.set_colorkey((255, 255, 255))

ground_img_top = pygame.transform.flip(ground_img, False, True)
background1_img_top = pygame.transform.flip(background1_img, False, True)
background2_img_top = pygame.transform.flip(background2_img, False, True)

player_init_pos  = [int(WINDOW_SIZE[0] * 0.5), int(WINDOW_SIZE[1]/2)]
player           = Player(player_init_pos[0], player_init_pos[1], int(WINDOW_SIZE[0] * 0.05), int(WINDOW_SIZE[0] * 0.05),img= player_img)
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

background2_size     = [WINDOW_SIZE[0] + 20, int(WINDOW_SIZE[1] * 0.7)]
background2_bottom   = Obj(0, WINDOW_SIZE[1] - background2_size[1], background2_size[0], background2_size[1], img= background2_img)
background2_bottom_2 = Obj(WINDOW_SIZE[0], WINDOW_SIZE[1] - background2_size[1], background2_size[0], background2_size[1], img= background2_img)
background2_top      = Obj(0, 0, background2_size[0], background2_size[1], img= background2_img_top)
background2_top_2    = Obj(WINDOW_SIZE[0], 0, background2_size[0], background2_size[1], img= background2_img_top)


grounds_list     = set([ ground_bottom, ground_top, ground_bottom_2, ground_top_2])
background1_list = set([ background1_bottom, background1_bottom_2, background1_top, background1_top_2])
background2_list = set([ background2_bottom, background2_bottom_2, background2_top, background2_top_2])

block_size_range = [int(WINDOW_SIZE[1] * 0.1), int(WINDOW_SIZE[0] * 0.1)]
block_spawn_range = [20, 60]
block_spawn_x = ground_bottom.pos[0] + WINDOW_SIZE[0]
block_tick_spaw = randint(block_spawn_range[0], block_spawn_range[1])

villain_size = [int(WINDOW_SIZE[0] * 0.05), int(WINDOW_SIZE[0] * 0.05)]
villain_spawn_pos_range = [ground_size[1], WINDOW_SIZE[1] - ground_size[1] - villain_size[1]]
villain_spawn_range = [40, 120]
villain_tick_spawn = randint(villain_spawn_range[0], villain_spawn_range[1])

arrow_size = [int(WINDOW_SIZE[0] * 0.05), int(WINDOW_SIZE[0] * 0.03)]
arrow_spawn_pos_range = [ground_size[1], WINDOW_SIZE[1] - ground_size[1] - arrow_size[1]]
arrow_spawn_range = [120, 360]
arrow_tick_spawn = randint(arrow_spawn_range[0], arrow_spawn_range[1])

wall_size = [int(WINDOW_SIZE[0] * 0.05), int(WINDOW_SIZE[1] - (2 * ground_size[1]))]
wall = Obj(0, ground_size[1], wall_size[0], wall_size[1], img= wall_img)

block_list = []
villain_list = []
arrow_list = []
block_ticks = 0
villain_ticks = 0
arrow_ticks = 0
scroll = 0
vel = 7
score = 0
dash_time = 0
dash_force = 10
vel_increase = 0.004
fps = 60
clock = pygame.time.Clock()
loop = True

def draw_text(text, pos, surface, fontsize= 30, font= 'calibri', color= (200, 200, 200)):
    font = pygame.font.SysFont(font, fontsize)
    render = font.render(text, False, color)
    surface.blit(render, pos) 

def move_objs(objs, vel):
    for obj in objs:
        obj.pos[0] -= vel

def draw_objs(objs, scroll_y= 0):
    for obj in objs:
        obj.draw_img(window, scroll_y)

def get_rects(objs):
    rects = []
    for obj in objs:
        rects.append(obj.rect)
    return rects

def grounds_update():
    draw_objs(grounds_list)
    move_objs(grounds_list, int(vel))
    respawn_ground()

def respawn_ground():
    if ground_top.pos[0] + ground_size[0] < 0:
        ground_top.pos[0]    = ground_top_2.pos[0] + ground_size[0]
        ground_bottom.pos[0] = ground_top_2.pos[0] + ground_size[0]
    
    if ground_top_2.pos[0] + ground_size[0] < 0:
        ground_top_2.pos[0]    = ground_top.pos[0] + ground_size[0]
        ground_bottom_2.pos[0] = ground_top.pos[0] + ground_size[0]

def background_update():
    draw_objs(background2_list, scroll_y= scroll)
    draw_objs(background1_list, scroll_y= scroll)
    move_objs(background1_list, int(vel * 0.5))
    move_objs(background2_list, int(vel * 0.2))
    respawn_background()

def respawn_background():
    if background1_top.pos[0] + background1_size[0] < 0:
        background1_top.pos[0]    = background1_top_2.pos[0] + background1_size[0] 
        background1_bottom.pos[0] = background1_top_2.pos[0] + background1_size[0]

    if background1_top_2.pos[0] + background2_size[0] < 0:
        background1_top_2.pos[0]    = background1_top.pos[0] + background1_size[0] 
        background1_bottom_2.pos[0] = background1_top.pos[0] + background1_size[0]
    
    if background2_top.pos[0] + background2_size[0] < 0:
        background2_top.pos[0]    = background2_top_2.pos[0] + background2_size[0] 
        background2_bottom.pos[0] = background2_top_2.pos[0] + background2_size[0]

    if background2_top_2.pos[0] + background2_size[0] < 0:
        background2_top_2.pos[0]    = background2_top.pos[0] + background2_size[0] 
        background2_bottom_2.pos[0] = background2_top.pos[0] + background2_size[0]

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

def update_blocks():
    draw_objs(block_list)
    move_objs(block_list, int(vel))

def spawn_villains():
    pos = [WINDOW_SIZE[0], randint(villain_spawn_pos_range[0], villain_spawn_pos_range[1])]

    villain = Villain(pos[0], pos[1], villain_size[0], villain_size[1], img = villain_img)
    villain_list.append(villain)

def update_villains():
    for villain in villain_list:
        villain.move(int(vel * 0.4))

    draw_objs(villain_list)
    outscreen_villains()

def outscreen_villains():
    for i, villain in sorted(enumerate(villain_list), reverse= True) :
        if villain.pos[0] < - villain_size[0]:
            villain_list.pop(i)

def spawn_arrows():
    pos = [WINDOW_SIZE[0], randint(arrow_spawn_pos_range[0], arrow_spawn_pos_range[1])]
    arrow = Obj(pos[0], pos[1], arrow_size[0], arrow_size[1], img= arrow_img)
    arrow_list.append(arrow)

def update_arrows():
    move_objs(arrow_list, int(vel))
    draw_objs(arrow_list)
    collide_arrow()

def collide_arrow():
    for i, arrow in sorted(enumerate(arrow_list), reverse= True):
        if player.rect.colliderect(arrow.rect):
            player_dash()
            arrow_list.pop(i)

def player_dash():
    global dash_time
    dash_sound.play()
    dash_time += 20

def dash_anim():
    move_objs(grounds_list, dash_force)
    move_objs(block_list, dash_force) 
    move_objs(background1_list, dash_force)
    move_objs(background2_list, dash_force)
    player.pos[0] += dash_force
    wall.pos[0] -= dash_force

def restart_game():
    global block_list, villain_list, arrow_list, block_ticks, villain_ticks, arrow_ticks, scroll, vel, score

    block_list = []
    villain_list = []
    arrow_list = []
    block_ticks = 0
    villain_ticks = 0
    arrow_ticks = 0
    scroll = 0
    vel = 7
    player.pos = [player_init_pos[0], player_init_pos[1]]
    if player.invert:
        player.invert = False
        player.flip_anim()
    player.y_momentum = 0

def menu():
    global score

    menu_loop = True
    while menu_loop:

        window.fill((47, 58, 100))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_loop = False

        background_update()
        grounds_update()
        if score > 0:
            draw_text('SCORE: ' + str(int(score)), [int(WINDOW_SIZE[0] * 0.34), int(WINDOW_SIZE[1] * 0.3)], window, fontsize= int(WINDOW_SIZE[1] * 0.1))

        draw_text('SPACE TO START', [int(WINDOW_SIZE[0] * 0.34), int(WINDOW_SIZE[1] * 0.5)], window, fontsize= int(WINDOW_SIZE[1] * 0.1))
        pygame.display.update()
        clock.tick(fps)

    score = 0

pygame.mixer.music.play(-1)

menu()

while loop:
    window.fill((47, 58, 100))

    score += vel
    vel += vel_increase
    scroll += (player.pos[1] + (player.height/2) - (WINDOW_SIZE[1]/2) - scroll)/15
    block_ticks += 1
    villain_ticks += 1
    arrow_ticks += 1 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.control(event)
            invert_sound.play()

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
        update_blocks()

    #player
    player.draw_img(window)
    player.update()
    player.collide_ground(get_rects(grounds_list))
    if player.collide_block(get_rects(block_list) + get_rects(villain_list)):
        player.pos[0] -= vel
        if wall.pos[0] < 0:
            wall.pos[0] += vel

    if player.get_pos() != player_positions[0]:
        player_positions[1] = player_positions[0]
        player_positions[0] = player.get_pos()
        player.set_last_pos(player_positions[1])

    if player.rect.colliderect(wall.rect):
        lose_sound.play()
        restart_game()
        menu()

    if dash_time > 0:
        dash_time -= 1
        dash_anim()
    
    #villain
    if villain_ticks > villain_tick_spawn:
        spawn_villains()
        villain_ticks = 0
        villain_tick_spawn = randint(villain_spawn_range[0], villain_spawn_range[1])
    if len(villain_list) > 0:
        update_villains()

    #arrows
    if arrow_ticks > arrow_tick_spawn:
        spawn_arrows()
        arrow_ticks = 0
        arrow_tick_spawn = randint(arrow_spawn_range[0], arrow_spawn_range[1])
    if len(arrow_list) > 0:
        update_arrows()

    draw_text('Score: ' + str(int(score)), (int(WINDOW_SIZE[0] * 0.02), int(WINDOW_SIZE[1] * 0.02)), window, fontsize= int(WINDOW_SIZE[1] * 0.08), color= (0, 0, 0))
    draw_text('Vel: ' + str(int(vel)), (int(WINDOW_SIZE[0] * 0.02), int(WINDOW_SIZE[1] * 0.1)), window, fontsize= int(WINDOW_SIZE[1] * 0.08), color= (0, 0, 0))

    #wall
    wall.draw_img(window)

    pygame.display.update()
    clock.tick(fps)
    