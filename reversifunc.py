import random

BLACK = 'x'
WHITE = 'o'
curBoard = [['.' for x in range(8)] for y in range(8)]
turn = BLACK
noMoves = 0

curBoard[3][3], curBoard[3][4] = WHITE, BLACK
curBoard[4][3], curBoard[4][4] = BLACK, WHITE

def showBoard(board):
    for x in range(8):
        for y in range(8):
            print(board[x][y], end=' ')
        print('')

def isOnBoard(x, y):
    return (0<=x<=7) and (0<=y<=7)

def getEmptyTiles(board):
    empty = 0

    for x in range(8):
        for y in range(8):
            if board[x][y] == '.':
                empty += 1

    return empty

# returns enemy's piece that can be flipped when a player place their piece in a selected position
def getDisksToFlip(board, turn, x_pos, y_pos):
    if board[x_pos][y_pos] != '.' or not isOnBoard(x_pos, y_pos):
        return []

    if (turn == BLACK):
        enemy = WHITE
    elif (turn == WHITE):
        enemy = BLACK

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

def getValidMoves(board, turn):
    validMoves = []

    for x in range(8):
        for y in range(8):
            if getDisksToFlip(board, turn, x, y) != []:
                validMoves.append([x, y])

    return validMoves

# temp function
def showValidMoves(board, validMoves):
    for x, y in validMoves:
        board[x][y] = '!'

    return board

def makeMove(board, turn, x_pos, y_pos):
    tilesToFlip = getDisksToFlip(board, turn, x_pos, y_pos)

    if len(tilesToFlip) != 0:
        board[x_pos][y_pos] = turn
        for x_cur, y_cur in tilesToFlip:
            board[x_cur][y_cur] = turn

    return board

"""while getEmptyTiles(curBoard) != 0 and noMoves != 2:
    print(turn)
    validMoves = getValidMoves(curBoard, turn)
    print(validMoves)
    showBoard(curBoard)
    if (len(validMoves) != 0):
        moveChosen = random.choice(validMoves)
        curBoard = makeMove(curBoard, turn, moveChosen[0], moveChosen[1])
        noMoves = 0
    else:
        noMoves += 1

    if turn == BLACK:
        turn = WHITE
    else:
        turn = BLACK"""
