from pygame import *
from pygame.sprite import *

class text(Sprite):
    def __init__(self, text, font, size, pos, color):
        Sprite.__init__(self)
        self.font = pygame.font.Font(font, size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]

class disk(Sprite):
    def __init__(self, pos, type, x_ind, y_ind):
        Sprite.__init__(self)
        self.type = type
        self.x_ind = x_ind
        self.y_ind = y_ind
        self.sprites = [image.load("sprites/w_disk0.png"), image.load("sprites/w_disk1.png"), image.load("sprites/w_disk2.png"), image.load("sprites/w_disk3.png"),
                        image.load("sprites/b_disk0.png"), image.load("sprites/b_disk1.png"), image.load("sprites/b_disk2.png"), image.load("sprites/b_disk3.png")]

        if self.type == 'o':
            self.image = self.sprites[0]
        elif self.type == 'x':
            self.image = self.sprites[4]

        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]

    def flipDisk(self):
        if self.type == 'o':
            self.type = 'x'
            self.image = self.sprites[4]

        elif self.type == 'x':
            self.type = 'o'
            self.image = self.sprites[0]


class tile(Sprite):
    def __init__(self, pos, x_ind, y_ind):
        Sprite.__init__(self)
        self.type = type
        self.x_ind = x_ind
        self.y_ind = y_ind
        self.image = image.load("sprites/tile.png")

        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]

class Button(Sprite):
    def __init__(self, message, x,y,fontsize = 42, backcolor = None, color = (0,0,0)):
        Sprite.__init__(self)
        self.color = color
        self.backcolor = backcolor
        self.x = x
        self.y = y
        self.message = message
        self.font = pygame.font.Font(None, fontsize)
        self.image = self.font.render(message,1, color, backcolor)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def change_colour(self,color):
        self.color = color
        self.image = self.font.render(self.message,1,color, self.backcolor)

