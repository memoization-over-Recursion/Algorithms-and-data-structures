# time complexity O( n )
# space complexity O( n )
def longestIncreasingMatrixPath(matrix):
    longestPaths = []
    for i in range( len( matrix ) ):
        row = []
        for j in range( len( matrix[ 0 ] ) ):
            row.append(None)
        longestPaths.append(row)
    print(longestPaths)

    answer = 0
    for k in range( len( matrix ) ):
        for l in range( len( matrix[ 0 ] ) ):
            answer = max(
                getLongestPath( matrix , k , l , float("-inf") , longestPaths ),
                answer,
                    )

    return answer

def getLongestPath( matrix , row , col ,lastVal , longestVal ):
    outOfBounds = row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0])
    if outOfBounds:
        return 0

    currentVal = matrix[row][col]
    if currentVal <= lastVal:
        return 0

    if longestVal[row][col] is None:
        longestVal[row][col] = 1 + max(
            getLongestPath( matrix , row + 1 , col ,currentVal , longestVal ),
            getLongestPath( matrix , row , col + 1 ,currentVal , longestVal ),
            getLongestPath( matrix , row - 1 , col ,currentVal , longestVal ),
            getLongestPath( matrix , row , col - 1 ,currentVal , longestVal ),
        )

    return longestVal[row][col]
