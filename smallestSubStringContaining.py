#time complexity O( b + s )
#space complexity O( b + s )
def smallestSubstringContaining(bigString, smallString):
    smallStringCounts = getCharCounts( smallString )
    stringBounds = getSubBounds( bigString , smallStringCounts )
    return stringGetFromBounds( bigString , stringBounds )

    
def getSubBounds( string , counts ):
    bounds = [ 0 , float("inf")]
    substringChars = {}
    lengthOfSubstringChars = len( counts.keys() )
    uniqueChars = 0
    L = 0
    R = 0
    while( R < len( string ) ):
        rChar = string[R]
        if rChar not in counts:
            R += 1
            continue
            
        increaseDict( rChar , substringChars )
        print(substringChars)
        if( substringChars[rChar] == counts[rChar] ):
            uniqueChars += 1

        while uniqueChars == lengthOfSubstringChars and  L <= R:
            print(str(L) + ' ' + str(R))
            bounds = closerBounds( L , R , bounds[0] , bounds[1] )
            lChar = string[L] 
            if lChar not in counts:
                L += 1
                continue
            if( counts[lChar] == substringChars[lChar] ):
                uniqueChars -= 1
            decreaseDict( lChar , substringChars )
            L += 1
        R += 1
    return bounds
        
    


def closerBounds( x1 , x2 , x3 , x4 ):
    return [ x1 , x2 ] if x2 - x1 < x4 - x3 else [ x3 , x4 ]

def stringGetFromBounds( string , bounds ):
    start, end = bounds
    if end == float("inf"):
        return ""