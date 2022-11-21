#time complexity O( n )
#space complexity O( n )
def minRewards(scores):
    # order matters (ie. cant sort them)
    # rule 1 each has to have at least one
    # rule 2 scores need to follow if one value is less than another
    final = [1]*len( scores )
    for i in range( 1 , len(scores) ):
        if(scores[i] > scores[i-1]):
            final[i] = final[i-1]+1
    for j in reversed( range( len( scores ) - 1 )):
        if(scores[j] > scores[j+1]):
            final[j] = max(final[j] , final[j+1]+1)
    return sum( final )
        
            
            