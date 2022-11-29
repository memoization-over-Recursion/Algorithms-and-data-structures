#time complexity O( n )
#space complexity O( 1 )
def longestBalancedSubstring(string):
    opening = 0
    closing = 0
    maxLength = 0
    for i in range( len( string ) ):
        if(string[i] == '('):
            opening += 1
        else:
            closing += 1
            
        if(opening == closing):
            maxLength = max( maxLength , (closing * 2) )
        elif(closing > opening):
            opening = 0
            closing = 0

    opening = 0
    closing = 0
    for j in reversed( range( len( string ) ) ):
        if(string[j] == '('):
            opening += 1
        else:
            closing += 1
            
        if(opening == closing):
            maxLength = max( maxLength , (opening * 2) )
            
        elif(closing < opening):
            opening = 0
            closing = 0
            
    return maxLength
