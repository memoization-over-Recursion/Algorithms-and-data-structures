#time complexity O( log( n ) ) 
#space complexity O( 1 )
def searchForRange(array, target):
   finalRange = [ -1 , -1 ]
   binSearch( array , 0 , len( array ) - 1 , target , True , finalRange)
   binSearch( array , 0 , len( array ) - 1 , target , False , finalRange)

   return finalRange

def binSearch(ar , left , right , target , L , finalRange):
    while(left <= right):
        middle = left + (right - left) // 2
        if(ar[middle] > target):
            right = middle - 1
        elif(ar[middle] < target):
            left = middle + 1
        else:
            if(L):
                if(middle == 0 or ar[ middle - 1 ] != target):
                    finalRange[0] = middle
                    return
                else:
                    right = middle - 1
            else:
                if(middle == len( ar ) - 1 or ar[ middle + 1 ] != target):
                    finalRange[1] = middle
                    return
                else:
                     left = middle + 1
                    
        
