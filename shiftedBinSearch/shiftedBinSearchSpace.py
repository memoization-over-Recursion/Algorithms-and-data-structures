#time complexity O( log( n ) )
#space complexity O( 1 )
def shiftedBinarySearch(array, target):
    return binSearch(array , 0 , len(array) - 1 , target )

def binSearch(ar , L , R , target):
    while( L <= R ):
        middle = L + (R - L) // 2
        Middle = ar[ middle ]
        Left = ar[ L ]
        Right = ar[ R ]
        if(target == Middle):
            return middle
        elif(Left <= Middle):
            if(target < Middle and target >= Left):
                R = middle - 1
            else:
                L = middle + 1
        else:
            if(target > Middle and target <= Right):
                L = middle + 1
            else:
                R = middle - 1
    return -1
        
        
           