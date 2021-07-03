import pygame

pygame.init()

class Obj:
    def __init__(self, x, y, width, height, img = None):
        self.pos = [x, y]
        self.width = width
        self.height = height
        self.img = img
        self.rect = pygame.Rect(x, y, width, height)
        
        if self.img != None:
            self.set_scale(width, height)

    def set_img(self, img):
        self.img = img

    def draw_img(self, window, scroll= 0):
        window.blit(self.img, [self.pos[0], self.pos[1] - scroll])
    
    def draw_rect(self, window, color):
        pygame.draw.rect(window, color, self.rect)

    def set_scale(self, width, height):
        self.img = pygame.transform.scale(self.img, [width, height])
        self.rect = pygame.Rect(self.pos[0], self.pos[1], width, height)
        self.width = width
        self.height = height

    def set_pos(self, new_pos):
        self.pos = new_pos
        self.rect = pygame.Rect(new_pos[0], new_pos[1], self.width, self.height)