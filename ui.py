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
    aiText = sc.text('AI Mode', gv.HELV, 30, (800, 645), gv.BLACK)

    easyButton = sc.button((200, 400), '0')
    normButton = sc.button((400, 400), '1')
    hardButton = sc.button((600, 400), '2')
    aiButton = sc.button((780, 625), '2')

    texts.add(gameTitle, chooseDiff, easyText, normText, hardText, aiText)
    buttons.add(easyButton, normButton, hardButton, aiButton)

    while True:
        for evi in event.get():
            if evi.type == QUIT:
                display.quit()

            if evi.type == MOUSEBUTTONDOWN:
                if easyButton.rect.collidepoint(mouse.get_pos()):
                    gv.diff = 2
                    gv.aiMode = False
                    InGame()
                if normButton.rect.collidepoint(mouse.get_pos()):
                    gv.diff = 3
                    gv.aiMode = False
                    InGame()
                if hardButton.rect.collidepoint(mouse.get_pos()):
                    gv.diff = 4
                    gv.aiMode = False
                    InGame()
                if aiButton.rect.collidepoint(mouse.get_pos()):
                    AiMode()

        screen.fill(gv.BROWN)
        buttons.draw(screen)
        texts.draw(screen)
        display.update()

def AiMode():
    texts = Group()
    buttons = Group()

    aiTitle = sc.text('AI Mode', gv.NEXT, 110, (260, 50), gv.GOLD)
    text1 = sc.text('E v E', gv.HELV, 30, (240, 220), gv.BLACK)
    text2 = sc.text('E v N', gv.HELV, 30, (440, 220), gv.BLACK)
    text3 = sc.text('E v H', gv.HELV, 30, (640, 220), gv.BLACK)
    text4 = sc.text('N v E', gv.HELV, 30, (240, 345), gv.BLACK)
    text5 = sc.text('N v N', gv.HELV, 30, (440, 345), gv.BLACK)
    text6 = sc.text('N v H', gv.HELV, 30, (640, 345), gv.BLACK)
    text7 = sc.text('H v E', gv.HELV, 30, (240, 470), gv.BLACK)
    text8 = sc.text('H v N', gv.HELV, 30, (440, 470), gv.BLACK)
    text9 = sc.text('H v H', gv.HELV, 30, (640, 470), gv.BLACK)
    backText = sc.text('Back', gv.HELV, 30, (820, 645), gv.BLACK)

    button1 = sc.button((200, 200), '0')
    button2 = sc.button((400, 200), '0')
    button3 = sc.button((600, 200), '0')
    button4 = sc.button((200, 325), '1')
    button5 = sc.button((400, 325), '1')
    button6 = sc.button((600, 325), '1')
    button7 = sc.button((200, 450), '2')
    button8 = sc.button((400, 450), '2')
    button9 = sc.button((600, 450), '2')
    backButton = sc.button((780, 625), '2')

    texts.add(aiTitle, text1, text2, text3, text4, text5, text6, text7, text8, text9, backText)
    buttons.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, backButton)

    while True:
        for eva in event.get():
            if eva.type == QUIT:
                display.quit()

            if eva.type == MOUSEBUTTONDOWN:
                if button1.rect.collidepoint(mouse.get_pos()):
                    gv.aiPlay = 2
                    gv.diff = 2
                    gv.aiMode = True
                    InGame()
                if button2.rect.collidepoint(mouse.get_pos()):
                    gv.aiPlay = 2
                    gv.diff = 3
                    gv.aiMode = True
                    InGame()
                if button3.rect.collidepoint(mouse.get_pos()):
                    gv.aiPlay = 2
                    gv.diff = 4
                    gv.aiMode = True
                    InGame()
                if button4.rect.collidepoint(mouse.get_pos()):
                    gv.aiPlay = 3
                    gv.diff = 2
                    gv.aiMode = True
                    InGame()
                if button5.rect.collidepoint(mouse.get_pos()):
                    gv.aiPlay = 3
                    gv.diff = 3
                    gv.aiMode = True
                    InGame()
                if button6.rect.collidepoint(mouse.get_pos()):
                    gv.aiPlay = 3
                    gv.diff = 4
                    gv.aiMode = True
                    InGame()
                if button7.rect.collidepoint(mouse.get_pos()):
                    gv.aiPlay = 4
                    gv.diff = 2
                    gv.aiMode = True
                    InGame()
                if button8.rect.collidepoint(mouse.get_pos()):
                    gv.aiPlay = 4
                    gv.diff = 3
                    gv.aiMode = True
                    InGame()
                if button9.rect.collidepoint(mouse.get_pos()):
                    gv.aiPlay = 4
                    gv.diff = 4
                    gv.aiMode = True
                    InGame()

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

                    if gv.aiMode == True:
                        value, oppMove = af.miniMax(curBoard, gv.aiPlay, -math.inf, math.inf, True, curTurn)
                        if oppMove in validPos:
                            diskFlipped = rf.getDisksToFlip(curBoard, curTurn, oppMove[0], oppMove[1])
                            curBoard = rf.makeMove(curBoard, curTurn, oppMove[0], oppMove[1])
                            blackScore, whiteScore = rf.getScore(curBoard)
                            placeDisk = sc.disk(((oppMove[0]+1)*72+128,(oppMove[1]+1)*72+4), curTurn, oppMove[0], oppMove[1])
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

                else:
                    curTurn = gv.P2
                    texts.empty()
                    blackText = sc.text('BLACK: {}'.format(blackScore), gv.HELV, 25, (10, 10), gv.GREY)
                    whiteText = sc.text('WHITE: {}'.format(whiteScore), gv.HELV, 25, (10, 40), gv.GREY)
                    noText = sc.text('No moves for BLACK', gv.HELV, 25, (730, 10), gv.GREY)
                    texts.add(blackText, whiteText, noText)
                    noMoves += 1

            if curTurn == gv.P2:
                if len(validPos) > 0:
                    noMoves = 0
                    value, oppMove = af.miniMax(curBoard, gv.diff, -math.inf, math.inf, True, curTurn)
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

                else:
                    texts.empty()
                    blackText = sc.text('BLACK: {}'.format(blackScore), gv.HELV, 25, (10, 10), gv.GREY)
                    whiteText = sc.text('WHITE: {}'.format(whiteScore), gv.HELV, 25, (10, 40), gv.GREY)
                    noText = sc.text('No moves for WHITE', gv.HELV, 25, (730, 10), gv.GREY)
                    texts.add(blackText, whiteText, noText)
                    noMoves += 1

            for evg in event.get():
                if evg.type == QUIT:
                    display.quit()

                if evg.type == MOUSEBUTTONDOWN:
                    for aTile in tiles:
                        if aTile.rect.collidepoint(mouse.get_pos()) and [aTile.xInd, aTile.yInd] in validPos and gv.aiMode == False:
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
