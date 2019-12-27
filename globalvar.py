BLACK = 'x'
WHITE = 'o'
curBoard = [['.' for x in range(8)] for y in range(8)]
noMoves = 0

curBoard[3][3], curBoard[3][4] = WHITE, BLACK
curBoard[4][3], curBoard[4][4] = BLACK, WHITE
