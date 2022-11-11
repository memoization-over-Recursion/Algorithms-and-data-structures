#time complexity O( nlog( n ) )
#space complexity O( n )
def longestIncreasingSubsequence(array):
    sequences = [None]*len(array)
    indices = [None]*(len(array)+1)
    length = 0
    for i , num in enumerate(array):
        newLen = binSearch(1 , length , indices , array , num)
        sequences[i] = indices[ newLen - 1 ]
        indices[ newLen ] = i
        length = max(length , newLen)

    return buildSequence(array, sequences , indices[length])
    
    

def binSearch( left , right , indices , array , num ):
    if(left > right):
        return left
    middle = (left + right) // 2
    if( array[ indices[ middle ] ] < num ):
        left = middle + 1
    else:
        right = middle - 1

    return binSearch(left , right , indices , array , num)
   
    
def buildSequence(array , sequence , i):
    seq = []
    while(i is not None):
        seq.append(array[i])
        i = sequence[i]
    return list(reversed(seq))