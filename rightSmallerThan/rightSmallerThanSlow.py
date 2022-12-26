# time complexity O( n^2 )
# space complexity O( n )
def rightSmallerThan(array):
    rightSmallerThan = [0] * len( array )
    for i in range( len(array) ):
        for j in range( i , len(array) ):
            if array[i] > array[j]:
                rightSmallerThan[i] += 1

            
    return rightSmallerThan
