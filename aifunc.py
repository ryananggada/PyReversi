import math
import random
import copy
import reversifunc as rf

weights = [[ 200, -50,  10,   5,   5,  10, -50, 200],
           [ -50, -100,  -2,  -2,  -2,  -2, -100, -50],
           [  10,  -2,   1,   1,   1,   1,  -2,  10],
           [   5,  -2,   1,   1,   1,   1,  -2,   3],
           [   5,  -2,   1,   1,   1,   1,  -2,   3],
           [  10,  -2,   1,   1,   1,   1,  -2,  10],
           [ -50, -100,  -2,  -2,  -2,  -2, -100, -50],
           [ 200, -50,  10,   5,   5,  10, -50, 200]]

# white is max black is min
# need to improve heuristics
def evalScore(board):
    score = 0

    # mobility
    score += 2 * (len(rf.getValidMoves(board, rf.WHITE)) - len(rf.getValidMoves(board, rf.BLACK)))

    # positioning of disks
    for x in range(8):
        for y in range(8):
            if board[x][y] == rf.WHITE:
                score += weights[x][y]
            elif board[x][y] == rf.BLACK:
                score -= weights[x][y]

    return score


def miniMax(board, depth, alpha, beta, isMaxPlayer):
    bestMove = None
    if depth == 0: # need to set game over
        return evalScore(board),1

    if isMaxPlayer:
        max_value = -math.inf
        moves = rf.getValidMoves(board, rf.WHITE)

        if len(moves) > 0:
            random.shuffle(moves)

        for a_move in moves:
            tempBoard = copy.deepcopy(board)
            tempBoard = rf.makeMove(tempBoard, rf.WHITE, a_move[0], a_move[1])
            curScore, move = miniMax(tempBoard, depth-1, alpha, beta, False)
            

            if curScore > max_value:
                max_value = curScore
                bestMove = a_move

            alpha = max(alpha, max_value)
            # if alpha >= beta:
            #     break
        print("best move: " + str(bestMove) + " value: " + str(max_value))
        return max_value, bestMove

    else:
        min_value = math.inf
        moves = rf.getValidMoves(board, rf.BLACK)

        if len(moves) > 0:
            random.shuffle(moves)


        for a_move in moves:
            tempBoard = copy.deepcopy(board)
            tempBoard = rf.makeMove(tempBoard, rf.BLACK, a_move[0], a_move[1])
            curScore, move = miniMax(tempBoard, depth-1, alpha, beta, True)

            
            if curScore < min_value:
                min_value = curScore
                bestMove = a_move

            beta = min(beta, min_value)
            # if alpha >= beta:
            #     break
        print("best move: " + str(bestMove) + " value: " + str(min_value))
        return min_value, bestMove
