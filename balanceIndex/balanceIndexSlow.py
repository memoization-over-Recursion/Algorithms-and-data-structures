# time complexity O( n^2 )
# space complexity O( 1 )
def balanceIndex(array):
    ans = -1
    for i in range( len( array ) ):
        leftSum = 0
        rightSum = 0
        for j in range( 0 , i ):
            leftSum += array[j]

        for k in range( i + 1 , len( array ) ):
            rightSum += array[k]

        if leftSum == rightSum:
            ans = i

    return ans