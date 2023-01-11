# time complexity O( n )
# pace complexity O( 1 )
def balanceIndex(array):
    summedArray = sum( array )
    leftSum = 0
    rightSum = summedArray
    for i in range( len( array )):
        rightSum -= array[i]
        if rightSum == leftSum:
            return i
        leftSum += array[i]
    return -1

