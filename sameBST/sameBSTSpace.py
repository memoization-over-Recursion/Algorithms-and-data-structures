# time complexity O( n^2 )
# space complexity O( n^2 )
def sameBsts(arrayOne, arrayTwo):
    return recursiveBSTChecker(arrayOne , arrayTwo)

def recursiveBSTChecker( ar1 , ar2 ):

    if len(ar1) == 0 and len(ar2) == 0:
        return True

    if ar1[0] != ar2[0] or len(ar1) != len(ar2):
        return False

    left1 = getSmaller( ar1 )
    left2 = getSmaller( ar2 )
    right1 = getBigger( ar1 )
    right2 = getBigger( ar2 )

    return recursiveBSTChecker( left1 , left2 ) and recursiveBSTChecker(right1 , right2 )
  

def getBigger( one ):
    result = []
    for i in range( 1 , len( one )):
        if one[0] <= one[i]:
            result.append( one[i] )
    return result

def getSmaller( one ):
    result = []
    for i in range( 1 , len( one )):
        if one[0] > one[i]:
            result.append( one[i] )
    return result
            
    
    
