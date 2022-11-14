#time complexity O( log( n ) )
#space complexity O( 1 )
def indexEqualsValue(array):
    i = 0
    j = len(array) - 1
    while( i <= j ):
        middle = i + ( j - i ) // 2
        middleVal = array[ middle ]

        if(middleVal < middle):
            i = middle + 1
        elif(middleVal == middle and middle == 0):
            return middle
        elif(middleVal == middle and array[middle-1] != middle-1):
            return middle
        else:
            j = middle - 1
    return -1
        