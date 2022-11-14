#time complexity O( log( n ) )
#space complexity O( log( n ) )
def indexEqualsValue(array):
    answer = helper(array , 0 , len( array ) - 1 )
    return answer

def helper(ar , start , end):
    if(start > end):
        return -1

    middle = start + (end - start)//2
    if(ar[middle] < middle):
        return helper(ar , middle + 1 , end)
    elif(ar[middle] == middle and middle == 0):
        return middle
    elif(ar[middle] == middle and ar[middle - 1] != middle - 1):
        return middle
    else:
        return helper(ar , start , middle-1)
    
