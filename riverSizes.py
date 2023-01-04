# time complexity O( wh )
# space complexity O( wh )
def riverSizes(matrix):
    sizes = []
    visited = [[False for i in row] for row in matrix ]
    print(visited)
    for i in range( len( matrix ) ):
        for j in range( len(matrix[ i ] ) ):
            if visited[i][j]:
                continue
            traverseNodes( i , j , matrix , visited , sizes )
    return sizes


def traverseNodes( i , j , matrix , visited , sizes):
    currentSize = 0
    stack = [[i , j]]
    while len( stack ):
        node = stack.pop()
        i = node[0]
        j = node[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentSize += 1
        neighbours = getUnvisitedNeighbours( i , j , matrix , visited )
        for n in neighbours:
            stack.append(n)
    if currentSize > 0:
        sizes.append( currentSize )
    
def getUnvisitedNeighbours( i , j , matrix , visited ):
    riverNodes = []
    if i > 0 and not visited[i-1][j]:
        riverNodes.append([ i-1 , j ])
    if j > 0 and not visited[i][j-1]:
        riverNodes.append([ i , j-1 ])
    if i < len(matrix) - 1 and not visited[i+1][j]:
        riverNodes.append([ i+1 , j ])
    if j < len(matrix[0]) - 1 and not visited[i][j+1]:
        riverNodes.append([ i , j+1 ])
    return riverNodes
    