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
    valid_moves = len(rf.getValidMoves(rf.curBoard, curTurn))

    flag = True
    while flag:
        while rf.getEmptyTiles(rf.curBoard) != 0 and valid_moves != 0:
            validPos = rf.getValidMoves(rf.curBoard, curTurn)
            valid_moves = len(validPos)
            if curTurn == rf.WHITE:
                move, value = af.miniMax(rf.curBoard, 5, -math.inf, math.inf, False)
                print(move)
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

        black, white = rf.getScore(rf.curBoard)
        screen.fill((255, 255, 0))
        black_score = big_font.render('Black got ' + str(black), False, (0,0,0))
        white_score = big_font.render('White got ' + str(white), False, (0,0,0))
        screen.blit(black_score, (260,200))
        screen.blit(white_score, (260,30))
        continue_button = sc.Button("Continue", 500,440, backcolor = (255,255,255))
        button_sprite_group = Group(continue_button)
        button_sprite_group.draw(screen)
        display.update()
        for ev in event.get():
            if ev.type == QUIT:
                pygame.quit()
                exit()

            elif ev.type == MOUSEBUTTONDOWN:
                if continue_button.rect.collidepoint(mouse.get_pos()):
                    flag = False


while True:
    InGame()

