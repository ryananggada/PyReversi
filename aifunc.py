import math
import random
import copy
import reversifunc as rf
import globalvar as gv

# the weights of board, big positive value means top priority for opponent
weights = [[ 200, -50,  10,   5,   5,  10, -50, 200],
           [ -50,-100,  -2,  -2,  -2,  -2,-100, -50],
           [  10,  -2,   1,   1,   1,   1,  -2,  10],
           [   5,  -2,   1,   1,   1,   1,  -2,   3],
           [   5,  -2,   1,   1,   1,   1,  -2,   3],
           [  10,  -2,   1,   1,   1,   1,  -2,  10],
           [ -50,-100,  -2,  -2,  -2,  -2,-100, -50],
           [ 200, -50,  10,   5,   5,  10, -50, 200]]

# evaluate score of the opponent for minimax algorithm, based on mobility and positioning of disks
def evalScore(board):
    score = 0

    # positioning of disks
    for x in range(8):
        for y in range(8):
            if board[x][y] == gv.P2:
                score += weights[x][y]
            elif board[x][y] == gv.P1:
                score -= weights[x][y]

    return score

# minimax algorithm with alpha-beta pruning; opponent is maximizing and player is minimizing
def miniMax(board, depth, alpha, beta, isMaxPlayer):
    bestMove = None

    if depth == 0:
        return evalScore(board), 1

    # opponent's turn
    if isMaxPlayer:
        maxValue = -math.inf
        moves = rf.getValidMoves(board, gv.P2)

        if len(moves) > 0:
            random.shuffle(moves)

        for aMove in moves:
            tempBoard = copy.deepcopy(board)
            tempBoard = rf.makeMove(tempBoard, gv.P2, aMove[0], aMove[1])
            curScore, move = miniMax(tempBoard, depth-1, alpha, beta, False)

            if curScore > maxValue:
                maxValue = curScore
                bestMove = aMove

            alpha = max(alpha, maxValue)
            if alpha >= beta:
                break

        return maxValue, bestMove

    # player's turn
    else:
        minValue = math.inf
        moves = rf.getValidMoves(board, gv.P1)

        for aMove in moves:
            tempBoard = copy.deepcopy(board)
            tempBoard = rf.makeMove(tempBoard, gv.P1, aMove[0], aMove[1])
            curScore, move = miniMax(tempBoard, depth-1, alpha, beta, True)

            if curScore < minValue:
                minValue = curScore
                bestMove = aMove

            beta = min(beta, minValue)
            if alpha >= beta:
                break

        return minValue, bestMove
