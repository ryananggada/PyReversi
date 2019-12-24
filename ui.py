from pygame import *
from pygame.sprite import *
from pygame.time import *

import spriteclass as sc
import reversifunc as rf

pygame.init()

WIDTH, HEIGHT = 960, 720

screen = display.set_mode((WIDTH, HEIGHT))

def Intro():
    screen.fill((255, 255, 0))


def InGame():
    screen.fill((255, 255, 0))
    rf.resetBoard()
    curTurn = rf.BLACK
    font = pygame.font.SysFont('Arial', 20)
    big_font = pygame.font.SysFont('Arial', 100)

    tiles = Group()
    disks = Group()

    for i in range(8):
        for j in range(8):
            the_tile = sc.tile(((i+1)*72+124,(j+1)*72), '0', i, j)
            tiles.add(the_tile)

    for x in range(8):
        for y in range(8):
            if rf.curBoard[x][y] == rf.WHITE:
                wh_disk = sc.disk(((x+1)*72+128,(y+1)*72+4), rf.WHITE, x, y)
                disks.add(wh_disk)
            elif rf.curBoard[x][y] == rf.BLACK:
                bh_disk = sc.disk(((x+1)*72+128,(y+1)*72+4), rf.BLACK, x, y)
                disks.add(bh_disk)

    while True:
        while rf.getEmptyTiles(rf.curBoard) != 0 and rf.noMoves != 2:
            screen.fill((255, 255, 0))
            if curTurn == rf.BLACK:
                turn = 'black'
            else:
                turn = 'white'
            turn_text = font.render('It is ' + turn + '\'s turn.', False, (0,0,0))
            screen.blit(turn_text, (5,5))
            tiles.draw(screen)
            disks.draw(screen)
            display.update()

            validPos = rf.getValidMoves(rf.curBoard, curTurn)
            for evg in event.get():
                if evg.type == QUIT:
                    display.quit()

                if evg.type == MOUSEBUTTONDOWN:
                    for a_tile in tiles:
                        if a_tile.rect.collidepoint(mouse.get_pos()) and [a_tile.x_ind, a_tile.y_ind] in validPos:
                            diskFlipped = rf.getDisksToFlip(rf.curBoard, curTurn , a_tile.x_ind, a_tile.y_ind)
                            rf.curBoard = rf.makeMove(rf.curBoard, curTurn, a_tile.x_ind, a_tile.y_ind)
                            place_disk = sc.disk(((a_tile.x_ind+1)*72+128,(a_tile.y_ind+1)*72+4), curTurn, a_tile.x_ind, a_tile.y_ind)
                            disks.add(place_disk)

                            for the_disk in disks:
                                if [the_disk.x_ind, the_disk.y_ind] in diskFlipped:
                                    the_disk.flipDisk()

                            if curTurn == rf.BLACK:
                                curTurn = rf.WHITE
                            elif curTurn == rf.WHITE:
                                curTurn = rf.BLACK
                    #display.update()
                                
        black, white = rf.getScore(rf.curBoard)
        screen.fill((255, 255, 0))
        black_score = big_font.render('Black got ' + str(black), False, (0,0,0))
        white_score = big_font.render('White got ' + str(white), False, (0,0,0))
        screen.blit(black_score, (260,200))
        screen.blit(white_score, (260,30))
        display.update()
        for evg in event.get():
                    if evg.type == QUIT:
                        display.quit()
    

InGame()
