# time complexity O( nlog( m ) )
# space complexity O( n + log( m ) )
def buildFailures(buildRuns):
    greens = list( map( greenPercent , buildRuns ))
    return getLongest( greens )

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
    
def getLongest( ar ):
    longestLength = 1
    current = 1
    for i in range(1 , len( ar )):
        if ar[i] < ar[i-1]:
            current += 1
            longestLength = max( current , longestLength)
        else:
            current = 1

    return longestLength if longestLength > 1 else -1
