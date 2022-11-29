#time complexity O( n )
#space complexity O( n )
def longestBalancedSubstring(string):
    maxLen = 0
    id = []
    id.append(-1)

    for i in range( len( string ) ):
        if( string[i] == "(" ):
            id.append(i)
        else:
            id.pop()
            if(len(id) == 0):
                id.append(i)
            else:
                balanced = id[ len(id) - 1 ]
                cur = i - balanced
                maxLen = max(maxLen , cur)

    return maxLen

#(()))(

            
