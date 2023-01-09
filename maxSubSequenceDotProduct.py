# time complexity O( wh )
# space complexity O( wh )
def maxSubsequenceDotProduct(arrayOne, arrayTwo):
    maxDot = getMatrix( arrayOne , arrayTwo )
    for i in range( 1 , len( arrayOne ) + 1 ):
        for j in range( 1 , len( arrayTwo ) + 1 ):
            current = arrayOne[ i - 1 ] * arrayTwo[ j - 1 ]
            maxDot[i][j] = max( current , 
                              maxDot[i-1][j-1] + current,
                              maxDot[i-1][j-1],
                              maxDot[i-1][j],
                              maxDot[i][j-1],
                              )
    return maxDot[len(arrayOne)][len(arrayTwo)]

def getMatrix( a , b ):
    dot = [[float("-inf") for i in range(len(b) + 1)] for j in range( len( a ) + 1)]
    return dot
