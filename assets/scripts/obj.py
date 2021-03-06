import pygame

pygame.init()

class Obj:
    def __init__(self, x, y, width, height, img = None):
        self.pos = [x, y]
        self.width = width
        self.height = height
        self.img = img
        
        if self.img != None:
            self.set_scale(width, height)

    def set_img(self, img):
        self.img = img

    def draw_img(self, window, scroll_y= 0):
        window.blit(self.img, [self.pos[0], self.pos[1] - scroll_y])
    
    def draw_rect(self, window, color):
        pygame.draw.rect(window, color, self.rect)

    def set_scale(self, width, height):
        self.img = pygame.transform.scale(self.img, [width, height])
        self.width = width
        self.height = height

    def set_pos(self, new_pos):
        self.pos = new_pos

    def set_colorkey(self, colorkey= (255, 255, 255)):
        self.img.set_colorkey(colorkey)
    
    @property
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        