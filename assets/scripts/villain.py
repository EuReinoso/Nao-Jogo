import pygame
from assets.scripts.obj import Obj
from random import randint 

pygame.init()

class Villain(Obj):
    
    def __init__(self, x, y, width, height, img):
        super().__init__(x, y ,width, height, img= img)
        self.vel_range = vel_range = [1, 5]
        self.vel = randint(vel_range[0], vel_range[1])

    def move(self, vel):
        self.pos[0] -= vel + self.vel

    
