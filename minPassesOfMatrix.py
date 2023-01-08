#time complexity O( wh )
#space complexity O( wh )
def minimumPassesOfMatrix(matrix):
    numOfPasses = convertNeg( matrix )
    return numOfPasses - 1 if not containsNeg( matrix ) else -1

def convertNeg( matrix ):
    pos = allPosPositions( matrix )
    passes = 0
    while len( pos ) > 0:
        cur = len( pos )
        while cur  > 0:
            row , col = pos.pop(0)
            adjPos = adjacentpos( matrix , row , col )
            for p in adjPos:
                row1 , col1 = p

                val = matrix[row1][col1]
                if val < 0:
                    matrix[row1][col1] *= -1
                    pos.append([row1 , col1])

            cur -= 1

        passes += 1
    return passes

def containsNeg( matrix ):
    for row in matrix:
        for elem in row:
            if elem < 0:
                return True
    return False

def allPosPositions( matrix ):
    pos = []
    for i in range( len( matrix ) ):
        for j in range( len ( matrix[i] ) ):
            if matrix[i][j] > 0:
                pos.append([i,j])
    return pos

def adjacentpos( matrix , row , col ):
    ans = []
    if row > 0:
        ans.append([row - 1 , col])
    if col > 0:
        ans.append([row , col - 1 ])
    if row < len( matrix ) - 1:
        ans.append([row + 1 , col])
    if col < len( matrix[0]) - 1:
        ans.append([row , col+1])

    return ans
        
                