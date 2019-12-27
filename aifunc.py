import math
import random
import reversifunc as rf

weights = [[ 100, -20,  10,   5,   5,  10, -20, 100],
           [ -20, -50,  -2,  -2,  -2,  -2, -50, -20],
           [  10,  -2,   1,   1,   1,   1,  -2,  10],
           [   5,  -2,   1,   1,   1,   1,  -2,   3],
           [   5,  -2,   1,   1,   1,   1,  -2,   3],
           [  10,  -2,   1,   1,   1,   1,  -2,  10],
           [ -20, -50,  -2,  -2,  -2,  -2, -50, -20],
           [ 100, -20,  10,   5,   5,  10, -20, 100]]

def evalScore(board, turn):
    score = 0

    if turn == rf.BLACK:
        opp = rf.WHITE
    elif turn == rf.WHITE:
        opp = rf.BLACK

    # mobility
    score += 10 * (len(rf.getValidMoves(board, turn)) - len(rf.getValidMoves(board, opp)))

    # positioning of disks
    for x in range(8):
        for y in range(8):
            if board[x][y] == turn:
                score += weights[x][y]
            elif board[x][y] == opp:
                score -= weights[x][y]

def miniMax(board, depth, alpha, beta, isMaxPlayer):
    if depth == 0: # need to set game over
        return evalScore(board, rf.WHITE)

    moves = rf.getValidMoves(board, rf.WHITE)
    random.shuffle(moves)
    bestMove = random.choice(moves)
    if isMaxPlayer:
        value = -math.inf
        for a_move in moves:
            tempBoard = rf.curBoard
            tempBoard = rf.makeMove(tempBoard, rf.WHITE, a_move[0], a_move[1])
            curScore = miniMax(tempBoard, depth-1, alpha, beta, False)

            if curScore > value:
                value = curScore
                bestMove = a_move

            alpha = max(alpha, value)
            if alpha >= beta:
                break
    else:
        value = math.inf
        for a_move in moves:
            tempBoard = rf.curBoard
            tempBoard = rf.makeMove(tempBoard, rf.BLACK, a_move[0], a_move[1])
            curScore = miniMax(tempBoard, depth-1, alpha, beta, True)

            if curScore > value:
                value = curScore
                bestMove = a_move

            beta = min(beta, value)
            if alpha >= beta:
                break

    return bestMove, value
