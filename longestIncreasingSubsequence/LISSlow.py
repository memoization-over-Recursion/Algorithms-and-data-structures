#time complexity O( n^2 )
#space complexity O( n )
def longestIncreasingSubsequence(array):
    lengths = [1]*len(array)
    sequences = [None]*len(array)
    maxLength = 0
    for i in range(len(array)):
        for j in range(0 , i):
            if( array[j] < array[i] and lengths[j]+1 >= lengths[i] ):
                lengths[i] = lengths[j]+1
                sequences[i] = j
        if(lengths[maxLength] <= lengths[i]):
            maxLength = i
            
    print(lengths)
    print(sequences)

    return buildSequence(array , sequences , maxLength)

def buildSequence(array , sequence , i):
    seq = []
    while(i is not None):
        seq.append(array[i])
        i = sequence[i]
    return list(reversed(seq))