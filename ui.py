from pygame import *
from pygame.sprite import *

import spriteclass as sc
import reversifunc as rf

pygame.init()

WIDTH, HEIGHT = 960, 720

screen = display.set_mode((WIDTH, HEIGHT))

def InGame():
    screen.fill((255, 255, 0))

    tiles = Group()
    disks = Group()

    for i in range(8):
        for j in range(8):
            a_tile = sc.tile(((i+1)*72+124,(j+1)*72), "0")
            tiles.add(a_tile)

    for x in range(8):
        for y in range(8):
            if rf.curBoard[x][y] == rf.WHITE:
                wh_disk = sc.disk(((x+1)*72+128,(y+1)*72+4), 'o')
                disks.add(wh_disk)
            elif rf.curBoard[x][y] == rf.BLACK:
                bh_disk = sc.disk(((x+1)*72+128,(y+1)*72+4), 'x')
                disks.add(bh_disk)

    while True:
        for evg in event.get():
            if evg.type == QUIT:
                display.quit()

        tiles.draw(screen)
        disks.draw(screen)
        display.update()

InGame()
