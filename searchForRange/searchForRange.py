#time complexity O( log(n) )
#space complexity O( log(n) )
def searchForRange(array, target):
    range = [-1,-1]
    binSearch( array , 0 , len( array ) - 1 , target , range , True)
    binSearch( array , 0 , len( array ) - 1 , target , range , False)
    return range

def binSearch(array , left , right , target , finalRange , L):
    if(left > right):
        return

    middle = left + (right-left) // 2

    if(array[middle] > target):
        binSearch(array , left , middle - 1 , target , finalRange , L)
    elif(array[middle] < target):
         binSearch(array , middle + 1 , right , target , finalRange , L)
    else:
        if(L):
            if(middle == 0 or array[middle - 1 ] != target):
                finalRange[0] = middle
            else:
                binSearch(array , left , middle - 1 , target , finalRange , L)
        else:
            if(middle == len(array)-1 or array[ middle + 1 ] != target):
                finalRange[1] = middle
            else:
                binSearch(array , middle + 1 , right , target , finalRange , L)
        
        
    



    
