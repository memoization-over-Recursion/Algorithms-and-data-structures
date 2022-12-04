#time complexity O( 1 ) 
#space complexity O( 1 )
def solveSudoku(board):
    solvePartial(board , 0 , 0 )
    return board


def solvePartial(board , row , col):
    currentRow = row
    currentCol = col
    
    if(currentCol == len( board[currentRow] ) ):
        currentCol = 0
        currentRow += 1
        if(currentRow == len( board ) ):
            return True 

    if(board[currentRow][currentCol] == 0):
        return tryDigit( board , currentRow , currentCol )

    return solvePartial( board , currentRow , currentCol + 1 )


def tryDigit(board , row , col ):
    for digit in range( 1 , 10 ):
        if(isValidDigitAtPos(board , row , col , digit)):
            board[row][col] = digit
            if(solvePartial(board , row , col + 1 )):
                return True

    board[row][col] = 0
    return False

def isValidDigitAtPos(board , row , col , digit):
    validRow = digit not in board[row]
    validCol = digit not in map(lambda r: r[col] , board)

    if not validRow or not validCol:
        return False

    subGridR = (row // 3) * 3
    subGridC = (col // 3) * 3
    for r in range( 3 ):
        for c in range( 3 ):
            newR = r + subGridR
            newC = c + subGridC
            val = board[newR][newC]

            if val == digit:
                return False
    return True
    
            
        