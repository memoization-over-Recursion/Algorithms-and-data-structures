# time complexity O( n^2 )
#space complexity O( n )
def minRewards(scores):
    # order matters (ie. cant sort them)
    # rule 1 each has to have at least one
    # rule 2 scores need to follow if one value is less than another
    final = [1]*len(scores)
    sums = 0
    for i in range(1, len( scores ) ):
        j = i - 1
        if(scores[i] > scores[ j ]):
            final[i] = final[j] + 1
        else:
            while( j >= 0 and scores[j] > scores[j+1]):
                final[j] = max( final[j], final[j+1]+1 )
                j-=1
    print(final)
    return sum(final)
            
            
