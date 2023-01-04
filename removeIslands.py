# time complexity O( wh )
# space complexity O( wh )
def removeIslands(matrix):
    for i in range( len( matrix ) ):
        for j in range( len( matrix[ i ] ) ):
            IisBorder = i == 0 or i == len(matrix) - 1
            JisBorder = j == 0 or j == len(matrix[i]) - 1
            isBorder = IisBorder or JisBorder

            if not isBorder:
                continue

            if matrix[i][j] != 1:
                continue

            change( i , j , matrix )
    

    for k in range( len( matrix ) ):
        for l in range( len( matrix[k] ) ):
            land = matrix[k][l]
            if land == 1:
                matrix[k][l] = 0
            elif land == 2:
                 matrix[k][l] = 1    
    return matrix

def change( i , j , matrix):
    
    stack = [(i,j)]
    
    while len( stack ) > 0:
        node = stack.pop()
        
        a , b = node
        matrix[a][b] = 2
        
        neighbours = getNeighbours( a , b, matrix )
        for neighbour in neighbours:
            row , col = neighbour

            if matrix[row][col] != 1:
                continue

            stack.append( neighbour )

def getNeighbours( row , col , matrix ):
    neighbours = []
    rows = len( matrix )
    cols = len( matrix[ row ] )
    if row - 1 >= 0:
        neighbours.append( (row - 1 , col ) )
    if row + 1 < rows:
        neighbours.append( (row + 1 , col ) )
    if col - 1 >= 0:
        neighbours.append( (row , col - 1 ) )
    if col + 1 < cols:
        neighbours.append( (row , col + 1 ) )
        
    return neighbours 



