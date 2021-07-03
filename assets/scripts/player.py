import pygame
from assets.scripts.obj import Obj

pygame.init()

class Player(Obj):
    def __init__(self, x, y, width, height, img):
        super().__init__(x, y, width, height, img)
        self.y_momentum = 0
        self.y_vel = 1
        self.right = False
        self.left = False
        self.ground_col = False
        self.invert = False
        self.is_flip_anim = False
        self.is_flipped = False

        self.min_height = self.height/2
        self.max_height = self.height

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

    def collide_ground(self, rects):
        hit_list = self._collision_test(rects)

        for obj in hit_list:
            if self.y_momentum > 0:
                self.pos[1] = obj.top - self.rect.height
                self.y_momentum = 0
            
            if self.y_momentum < 0:
                self.pos[1] = obj.bottom
                self.y_momentum = 0

    def collide_block(self, rects):
        hit_list = self._collision_test(rects)

        for obj in hit_list:
            if self.last_rect.bottom > obj.top and self.last_rect.top < obj.bottom:
                    return True

            else:
                if self.y_momentum > 0:
                    self.pos[1] = obj.top - self.rect.height
                    self.y_momentum = 0
                    return False

                if self.y_momentum < 0:
                    self.pos[1] = obj.bottom
                    self.y_momentum = 0
                    return False

    def _collision_test(self, rects):
        hit_list = []
        for rect in rects:
            if self.rect.colliderect(rect):
                hit_list.append(rect)
        return hit_list

    def control(self, event):
        if event.key == pygame.K_SPACE:
            self.invert = not self.invert
            self.flip_anim()

    def flip_anim(self):
        self.img = pygame.transform.flip(self.img, False, True)

    def get_pos(self):
        return [self.pos[0], self.pos[1]]

    def set_last_pos(self, pos):
        self.last_pos = pos
    
    @property
    def last_rect(self):
        return pygame.Rect(self.last_pos[0], self.last_pos[1], self.width, self.height)
            