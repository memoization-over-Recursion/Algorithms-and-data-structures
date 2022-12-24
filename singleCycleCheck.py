#time complexity O( n )
#space complexity O( 1 )
def hasSingleCycle(array):
    visitedElem = 0
    currentX = 0
    while visitedElem < len( array ):
        if visitedElem > 0 and currentX == 0:
            return False
        visitedElem += 1
        currentX = getNext(array , currentX)
    return currentX == 0

def getNext( array , currentX):
    newX = (currentX + array[currentX]) % len( array )
    return newX if newX >= 0 else newX + len( array )
