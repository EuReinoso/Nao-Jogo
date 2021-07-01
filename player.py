import pygame
from pygame.sprite import groupcollide

pygame.init()

class Player:
    def __init__(self, img, pos):
        self.img = img
        self.pos = pos
        self.y_momentum = 0
        self.y_vel = 0.1
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.img.get_width(), self.img.get_height())
        self.right = False
        self.left = False
        
        self.ground_col = False

        self.invert = False

    def draw(self, window):
        window.blit(self.img, self.pos)

    def update(self):
       
        self.gravity()
            
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

    def gravity(self):
        if not self.invert:
            self.y_momentum += self.y_vel
        else:
            self.y_momentum -= self.y_vel

        self.pos[1] += self.y_momentum

    def ground_collide(self, ground_down_rect, ground_up_rect):
        if self.pos[1] + self.rect.height > ground_down_rect.y:
            self.pos[1] = ground_down_rect.y - self.rect.height
            self.y_momentum = 0
            return
        if self.pos[1] < ground_up_rect.y + ground_down_rect.height:
            self.pos[1] = ground_up_rect.y + ground_down_rect.height
            self.y_momentum = 0
            return
    
        self.ground_col = False
    
    def control(self, event):
        if event.key == pygame.K_SPACE:
            self.invert = not self.invert

