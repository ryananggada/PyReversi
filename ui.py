from pygame import *
from pygame.sprite import *
from pygame.time import *

import spriteclass as sc
import reversifunc as rf
import globalvar as gv
import aifunc as af

import math

pygame.init()

screen = display.set_mode((gv.WIDTH, gv.HEIGHT))
display.set_caption('Reversi')

# menu screen
def Intro():
    texts = Group()
    buttons = Group()

    gameTitle = sc.text('REVERSI', gv.NEXT, 110, (260, 50), gv.GOLD)
    chooseDiff = sc.text('Choose Difficulty', gv.HELV, 40, (320, 300), gv.GREY)
    easyText = sc.text('Easy', gv.HELV, 30, (240, 420), gv.BLACK)
    normText = sc.text('Normal', gv.HELV, 30, (425, 420), gv.BLACK)
    hardText = sc.text('Hard', gv.HELV, 30, (640, 420), gv.BLACK)

    easyButton = sc.button((200, 400), '0')
    normButton = sc.button((400, 400), '1')
    hardButton = sc.button((600, 400), '2')

    texts.add(gameTitle, chooseDiff, easyText, normText, hardText)
    buttons.add(easyButton, normButton, hardButton)

    while True:
        for evi in event.get():
            if evi.type == MOUSEBUTTONDOWN:
                if easyButton.rect.collidepoint(mouse.get_pos()):
                    gv.diff = 2
                    InGame()

                if normButton.rect.collidepoint(mouse.get_pos()):
                    gv.diff = 4
                    InGame()

                if hardButton.rect.collidepoint(mouse.get_pos()):
                    gv.diff = 6
                    InGame()

            if evi.type == QUIT:
                display.quit()

        screen.fill(gv.BROWN)
        buttons.draw(screen)
        texts.draw(screen)
        display.update()

# gameplay
def InGame():
    curBoard = [['.' for x in range(8)] for y in range(8)]
    noMoves = 0
    curBoard = rf.initializeBoard(curBoard)
    curTurn = gv.P1

    tiles = Group()
    disks = Group()
    texts = Group()

    for i in range(8):
        for j in range(8):
            the_tile = sc.tile(((i+1)*72+124,(j+1)*72), i, j)
            tiles.add(the_tile)

    for x in range(8):
        for y in range(8):
            if curBoard[x][y] == gv.P1:
                blDisk = sc.disk(((x+1)*72+128,(y+1)*72+4), gv.P1, x, y)
                disks.add(blDisk)
            elif curBoard[x][y] == gv.P2:
                whDisk = sc.disk(((x+1)*72+128,(y+1)*72+4), gv.P2, x, y)
                disks.add(whDisk)

    blackText = sc.text('BLACK: 2', gv.HELV, 25, (10, 10), gv.GREY)
    whiteText = sc.text('WHITE: 2', gv.HELV, 25, (10, 40), gv.GREY)
    turnText = sc.text('Your turn!', gv.HELV, 25, (840, 10), gv.GREY)
    texts.add(blackText, whiteText, turnText)

    while True:
        while rf.getEmptyTiles(curBoard) != 0 and noMoves != 2:
            validPos = rf.getValidMoves(curBoard, curTurn)
            if curTurn == gv.P1:
                if len(validPos) > 0:
                    noMoves = 0
                else:
                    curTurn = gv.P2
                    texts.empty()
                    blackText = sc.text('BLACK: {}'.format(blackScore), gv.HELV, 25, (10, 10), gv.GREY)
                    whiteText = sc.text('WHITE: {}'.format(whiteScore), gv.HELV, 25, (10, 40), gv.GREY)
                    noText = sc.text('No moves for BLACK', gv.HELV, 25, (770, 10), gv.GREY)
                    texts.add(blackText, whiteText, noText)
                    noMoves += 1

            if curTurn == gv.P2:
                if len(validPos) > 0:
                    value, oppMove = af.miniMax(curBoard, gv.diff, -math.inf, math.inf, True)
                    if oppMove in validPos:
                        diskFlipped = rf.getDisksToFlip(curBoard, curTurn, oppMove[0], oppMove[1])
                        curBoard = rf.makeMove(curBoard, curTurn, oppMove[0], oppMove[1])
                        blackScore, whiteScore = rf.getScore(curBoard)
                        placeDisk = sc.disk(((oppMove[0]+1)*72+128,(oppMove[1]+1)*72+4), curTurn, oppMove[0], oppMove[1])
                        disks.add(placeDisk)

                        for aDisk in disks:
                            if [aDisk.xInd, aDisk.yInd] in diskFlipped:
                                aDisk.flipDisk()

                        curTurn = gv.P1
                        texts.empty()
                        blackText = sc.text('BLACK: {}'.format(blackScore), gv.HELV, 25, (10, 10), gv.GREY)
                        whiteText = sc.text('WHITE: {}'.format(whiteScore), gv.HELV, 25, (10, 40), gv.GREY)
                        turnText = sc.text('Your turn!', gv.HELV, 25, (840, 10), gv.GREY)
                        texts.add(blackText, whiteText, turnText)
                        noMoves = 0

                else:
                    texts.empty()
                    blackText = sc.text('BLACK: {}'.format(blackScore), gv.HELV, 25, (10, 10), gv.GREY)
                    whiteText = sc.text('WHITE: {}'.format(whiteScore), gv.HELV, 25, (10, 40), gv.GREY)
                    noText = sc.text('No moves for WHITE', gv.HELV, 25, (770, 10), gv.GREY)
                    texts.add(blackText, whiteText, noText)
                    noMoves += 1

            for evg in event.get():
                if evg.type == QUIT:
                    display.quit()

                if evg.type == MOUSEBUTTONDOWN:
                    for aTile in tiles:
                        if aTile.rect.collidepoint(mouse.get_pos()) and [aTile.xInd, aTile.yInd] in validPos:
                            diskFlipped = rf.getDisksToFlip(curBoard, curTurn , aTile.xInd, aTile.yInd)
                            curBoard = rf.makeMove(curBoard, curTurn, aTile.xInd, aTile.yInd)
                            blackScore, whiteScore = rf.getScore(curBoard)
                            placeDisk = sc.disk(((aTile.xInd+1)*72+128,(aTile.yInd+1)*72+4), curTurn, aTile.xInd, aTile.yInd)
                            disks.add(placeDisk)

                            for aDisk in disks:
                                if [aDisk.xInd, aDisk.yInd] in diskFlipped:
                                    aDisk.flipDisk()

                            curTurn = gv.P2
                            texts.empty()
                            blackText = sc.text('BLACK: {}'.format(blackScore), gv.HELV, 25, (10, 10), gv.GREY)
                            whiteText = sc.text('WHITE: {}'.format(whiteScore), gv.HELV, 25, (10, 40), gv.GREY)
                            aiThink = sc.text('AI is thinking...', gv.HELV, 25, (770, 10), gv.GREY)
                            texts.add(blackText, whiteText, aiThink)

            screen.fill(gv.BROWN)
            tiles.draw(screen)
            disks.draw(screen)
            texts.draw(screen)
            display.update()

        Result(blackScore, whiteScore)

# screen after match is completed
def Result(blackScore, whiteScore):
    texts = Group()
    buttons = Group()

    blackText = sc.text('BLACK: {}'.format(blackScore), gv.HELV, 35, (390, 25), gv.GREY)
    whiteText = sc.text('WHITE: {}'.format(whiteScore), gv.HELV, 35, (390, 75), gv.GREY)
    retryText = sc.text('Retry', gv.HELV, 30, (335, 420), gv.BLACK)
    backText = sc.text('Back', gv.HELV, 30, (540, 420), gv.BLACK)
    texts.add(blackText, whiteText, retryText, backText)

    retryButton = sc.button((300, 400), '1')
    backButton = sc.button((500, 400), '2')
    buttons.add(retryButton, backButton)

    if blackScore > whiteScore:
        resultText = sc.text('YOU WIN!', gv.NEXT, 85, (290, 200), gv.BLACK)
        texts.add(resultText)
    elif blackScore == whiteScore:
        resultText = sc.text('DRAW!', gv.NEXT, 85, (330, 200), gv.BLACK)
        texts.add(resultText)
    elif blackScore < whiteScore:
        resultText = sc.text('YOU LOSE!', gv.NEXT, 85, (270, 200), gv.BLACK)
        texts.add(resultText)

    while True:
        for evr in event.get():
            if evr.type == QUIT:
                display.quit()

            if evr.type == MOUSEBUTTONDOWN:
                if retryButton.rect.collidepoint(mouse.get_pos()):
                    InGame()

                if backButton.rect.collidepoint(mouse.get_pos()):
                    Intro()

        screen.fill(gv.BROWN)
        buttons.draw(screen)
        texts.draw(screen)
        display.update()
