import random
import globalvar as gv

# initialize the board to starting position
def initializeBoard(board):
    board[3][3], board[3][4] = gv.P2, gv.P1
    board[4][3], board[4][4] = gv.P1, gv.P2
    return board

# shows the board, used for debugging purposes
def showBoard(board):
    for x in range(8):
        for y in range(8):
            print(board[x][y], end=' ')
        print('')

# checks if the value assigned are within the index of the board
def isOnBoard(x, y):
    return (0<=x<=7) and (0<=y<=7)

# get the amount of empty tiles available in a board
def getEmptyTiles(board):
    empty = 0

    for x in range(8):
        for y in range(8):
            if board[x][y] == '.':
                empty += 1

    return empty

# returns opponent's pieces that can be flipped when a player place their piece in a selected position
def getDisksToFlip(board, turn, x_pos, y_pos):
    if board[x_pos][y_pos] != '.' or not isOnBoard(x_pos, y_pos):
        return []

    if (turn == gv.P1):
        enemy = gv.P2
    elif (turn == gv.P2):
        enemy = gv.P1

    validDisks = []

    for x_move, y_move in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
        x_cur, y_cur = x_pos, y_pos
        x_cur += x_move
        y_cur += y_move

        # check if the current tile is enemy's and in within the board
        if isOnBoard(x_cur, y_cur) and board[x_cur][y_cur] == enemy:
            x_cur += x_move
            y_cur += y_move

            # go back to for if the tile's coordinate is not in the board
            if not isOnBoard(x_cur, y_cur):
                continue

            # check if there is more enemy on the current move, done if
            while board[x_cur][y_cur] == enemy:
                x_cur += x_move
                y_cur += y_move

                if not isOnBoard(x_cur, y_cur):
                    break

            if not isOnBoard(x_cur, y_cur):
                continue

            if board[x_cur][y_cur] == turn:
                while True:
                    x_cur -= x_move
                    y_cur -= y_move

                    if x_cur == x_pos and y_cur == y_pos:
                        break

                    validDisks.append([x_cur, y_cur])

    return validDisks

# get the valid moves in coordinates of a board
def getValidMoves(board, turn):
    validMoves = []

    for x in range(8):
        for y in range(8):
            if getDisksToFlip(board, turn, x, y) != []:
                validMoves.append([x, y])

    return validMoves

# modify the board after a disk is placed on it
def makeMove(board, turn, x_pos, y_pos):
    tilesToFlip = getDisksToFlip(board, turn, x_pos, y_pos)

    if len(tilesToFlip) != 0:
        board[x_pos][y_pos] = turn
        for x_cur, y_cur in tilesToFlip:
            board[x_cur][y_cur] = turn

    return board

# get the score of the pieces in a board
def getScore(board):
    b_score, w_score = 0, 0

    for x in range(8):
        for y in range(8):
            if board[x][y] == gv.P1:
                b_score += 1
            elif board[x][y] == gv.P2:
                w_score += 1

    return b_score, w_score
