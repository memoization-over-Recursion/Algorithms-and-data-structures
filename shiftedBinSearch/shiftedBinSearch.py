#time complexity O( log( n ) )
#space complexity O( log( n ) )
def shiftedBinarySearch(array, target):
    return binSearch(array , 0 , len(array) - 1 , target )

def binSearch(ar , L , R , target):
    if(L > R):
        return -1
    middle = (R + L) // 2
    Middle = ar[ middle ]
    Left = ar[ L ]
    Right = ar[ R ]
    if(target == Middle):
        return middle
    elif(Left <= Middle):
        if(target < Middle and target >= Left):
            return binSearch(ar , L , middle - 1 , target)
        else:
            return binSearch(ar , middle + 1 , R , target)
    else:
        if(target > Middle and target <= Right):
             return binSearch(ar , middle + 1 , R , target)
        else:
            return binSearch(ar , L , middle - 1 , target)
        
            
   
       

