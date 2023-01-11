# time complexity O( nlog( m ) )
# space complexity O( 1 )
def buildFailures(buildRuns):
    longest = 1
    current = 1
    firstBuild = greenPercent(buildRuns[0])
    for i in range( 1 , len( buildRuns ) ):
        currentBuild = greenPercent( buildRuns[ i ] )
        if currentBuild < firstBuild:
            current += 1
            longest = max( longest , current )
        else:
            current = 1
        firstBuild = currentBuild
    return longest if longest > 1 else -1

def greenPercent( greens ):
    failIdx = binarySearch( greens , 0 , len( greens ) - 1)
    return failIdx / len( greens )

def binarySearch( array , left , right ):
    if left > right:
        return -1

    middle = ( left + right ) // 2
    isFalse = not array[ middle ]
    if isFalse:
        isFirstFalse = middle == 0 or array[middle-1]
        if isFirstFalse:
            return middle
        else:
            return binarySearch(array , left , middle - 1)
    else:
        return binarySearch(array , middle + 1 , right )
    