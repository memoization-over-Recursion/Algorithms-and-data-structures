#time complexity O( n )
#space complexity O( n )
def reverseWordsInString(string):
    final = []
    k = 0
    for i in range( len( string ) ):
        if(string[ i ] == ' '):
            final.append(string[k:i])
            k = i
        elif(string[k] == ' '):
            final.append(' ')
            k = i
    final.append(string[k:])
    
    return reverse(final)

def reverse( finalList ):
    i = 0 
    j = len(finalList) - 1

    while(i < j):
        finalList[i], finalList[j] = finalList[j], finalList[i]
        i+=1
        j-=1
    return "".join(finalList)
    
