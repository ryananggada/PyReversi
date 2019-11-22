from pygame import *
from pygame.sprite import *

class disk(Sprite):
    def __init__(self, pos, type):
        Sprite.__init__(self)
        self.type = type
        self.sprites = [image.load("sprites/w_disk0.png"), image.load("sprites/w_disk1.png"), image.load("sprites/w_disk2.png"), image.load("sprites/w_disk3.png"),
                        image.load("sprites/b_disk0.png"), image.load("sprites/b_disk1.png"), image.load("sprites/b_disk2.png"), image.load("sprites/b_disk3.png")]

        if self.type == 'o':
            self.image = self.sprites[0]
        elif self.type == 'x':
            self.image = self.sprites[4]

        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]

class tile(Sprite):
    def __init__(self, pos, type):
        Sprite.__init__(self)
        self.type = type
        self.sprites = [image.load("sprites/tile0.png")]

        if self.type == '0':
            self.image = self.sprites[0]

        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]
