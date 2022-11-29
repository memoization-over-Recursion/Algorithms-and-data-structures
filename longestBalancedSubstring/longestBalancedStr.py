#time complexity O( n^3 )
#space complexity O( n )
def longestBalancedSubstring(string):
    maximum = 0
    for i in range( len( string ) ):
        for j in range( i+2  ,  len( string )+1 , 2 ):
            if(balancedString( string[i:j] ) ):
                current = j-i
                maximum = max( maximum , current )
    return  maximum
                
#time complexity O( n )
#space complexity O( n )
def balancedString( string ):
    brackets = []
    for bracket in string:
        if(bracket == '('):
            brackets.append(bracket)
        elif(len(brackets) > 0):
            brackets.pop()
        else:
            return False
    return len(brackets) == 0
