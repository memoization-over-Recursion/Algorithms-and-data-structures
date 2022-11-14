#time complexity O( n )
#space complexity O( 1 )
def indexEqualsValue(array):
    for i in range( len( array ) ):
        if(array[i] == i):
            return i
    return -1
