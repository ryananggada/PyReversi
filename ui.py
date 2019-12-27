from pygame import *
from pygame.sprite import *
from pygame.time import *

import spriteclass as sc
import reversifunc as rf
import aifunc as af

import math

pygame.init()

WIDTH, HEIGHT = 960, 720
HELV = "sprites/Helvetica.ttf"

screen = display.set_mode((WIDTH, HEIGHT))

def Intro():
    screen.fill((255, 255, 0))

def InGame():
    rf.resetBoard()
    curTurn = rf.BLACK
    font = pygame.font.SysFont('Arial', 20)
    big_font = pygame.font.SysFont('Arial', 100)

    tiles = Group()
    disks = Group()
    texts = Group()

    for i in range(8):
        for j in range(8):
            the_tile = sc.tile(((i+1)*72+124,(j+1)*72), i, j)
            tiles.add(the_tile)

    for x in range(8):
        for y in range(8):
            if rf.curBoard[x][y] == rf.WHITE:
                wh_disk = sc.disk(((x+1)*72+128,(y+1)*72+4), rf.WHITE, x, y)
                disks.add(wh_disk)
            elif rf.curBoard[x][y] == rf.BLACK:
                bh_disk = sc.disk(((x+1)*72+128,(y+1)*72+4), rf.BLACK, x, y)
                disks.add(bh_disk)

    blackText = sc.text('2', HELV, 25, (10, 10), (180, 180, 180))
    whiteText = sc.text('2', HELV, 25, (10, 40), (180, 180, 180))
    texts.add(blackText, whiteText)

    while True:
        while rf.getEmptyTiles(rf.curBoard) != 0 and rf.noMoves != 2:
            validPos = rf.getValidMoves(rf.curBoard, curTurn)
            for evg in event.get():
                if evg.type == QUIT:
                    display.quit()

                if evg.type == MOUSEBUTTONDOWN:
                    for a_tile in tiles:
                        if a_tile.rect.collidepoint(mouse.get_pos()) and [a_tile.x_ind, a_tile.y_ind] in validPos:
                            diskFlipped = rf.getDisksToFlip(rf.curBoard, curTurn , a_tile.x_ind, a_tile.y_ind)
                            rf.curBoard = rf.makeMove(rf.curBoard, curTurn, a_tile.x_ind, a_tile.y_ind)
                            blackScore, whiteScore = rf.getScore(rf.curBoard)
                            place_disk = sc.disk(((a_tile.x_ind+1)*72+128,(a_tile.y_ind+1)*72+4), curTurn, a_tile.x_ind, a_tile.y_ind)
                            disks.add(place_disk)

                            for the_disk in disks:
                                if [the_disk.x_ind, the_disk.y_ind] in diskFlipped:
                                    the_disk.flipDisk()

                            if curTurn == rf.BLACK:
                                curTurn = rf.WHITE
                            elif curTurn == rf.WHITE:
                                curTurn = rf.BLACK

                            texts.empty()
                            blackText = sc.text('{}'.format(blackScore), HELV, 25, (10, 10), (180, 180, 180))
                            whiteText = sc.text('{}'.format(whiteScore), HELV, 25, (10, 40), (180, 180, 180))
                            texts.add(blackText, whiteText)

            #print(af.miniMax(rf.curBoard, 0, -math.inf, math.inf, True))
            screen.fill((255, 255, 0))
            tiles.draw(screen)
            disks.draw(screen)
            texts.draw(screen)
            display.update()

InGame()
