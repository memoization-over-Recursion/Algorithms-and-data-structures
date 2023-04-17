# time complexity O( n^2 )
# spac complexity O( 1 )
def twoNumberSum(array, targetSum):
    for i in range( len( array ) ):
        for j in range( len( array ) - 1 , -1 , -1):
            if( i != j ):
                if( array[i] + array[j] == targetSum):
                    return [array[i] , array[j]]
    return []