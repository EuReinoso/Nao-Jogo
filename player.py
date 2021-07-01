import pygame

pygame.init()

class Player:
    def __init__(self, img, pos):
        self.img = img
        self.pos = pos
        self.rect = img.get_rect()
        self.y_momentum = 0
        self.y_vel = 0.1

        self.right = False
        self.left = False

    def draw(self, window):
        window.blit(self.img, self.pos)

    def update(self):
        self.gravity()

    def gravity(self):
        self.y_momentum += self.y_vel
        if self.pos[1] >= 600 - self.rect.height:
            self.y_momentum = 0

        self.pos[1] += self.y_momentum


