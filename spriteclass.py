from pygame import *
from pygame.sprite import *

# text display for UI
class text(Sprite):
    def __init__(self, text, font, size, pos, color):
        Sprite.__init__(self)
        self.font = pygame.font.Font(font, size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]

# buttons for UI
class button(Sprite):
    def __init__(self, pos, type):
        Sprite.__init__(self)
        self.type = type
        self.sprites = [image.load("sprites/button0.png"), image.load("sprites/button1.png"), image.load("sprites/button2.png")]

        if self.type == '0':
            self.image = self.sprites[0]
        elif self.type == '1':
            self.image = self.sprites[1]
        elif self.type == '2':
            self.image = self.sprites[2]

        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]

# disk pieces
class disk(Sprite):
    def __init__(self, pos, type, xInd, yInd):
        Sprite.__init__(self)
        self.type = type
        self.xInd = xInd
        self.yInd = yInd
        self.sprites = [image.load("sprites/b_disk.png"), image.load("sprites/w_disk.png")]

        if self.type == 'x':
            self.image = self.sprites[0]
        elif self.type == 'o':
            self.image = self.sprites[1]

        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]

    def flipDisk(self):
        if self.type == 'x':
            self.type = 'o'
            self.image = self.sprites[1]

        elif self.type == 'o':
            self.type = 'x'
            self.image = self.sprites[0]

# board tiles
class tile(Sprite):
    def __init__(self, pos, xInd, yInd):
        Sprite.__init__(self)
        self.xInd = xInd
        self.yInd = yInd
        self.image = image.load("sprites/tile.png")

        self.rect = self.image.get_rect()
        self.rect.left = pos[0]
        self.rect.top = pos[1]
