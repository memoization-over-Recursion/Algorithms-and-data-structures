# time complexity O( n^2 )
# space complexity O( d )
def sameBsts(arrayOne, arrayTwo):
    return recursiveBSTChecker(arrayOne , arrayTwo , 0 , 0 , float("-inf") , float("inf") )

def recursiveBSTChecker( ar1 , ar2 , root1 , root2  , minVal , maxVal):
    if root1 == -1 or root2 == -1:
        return root1 == root2
    
    if ar1[root1] != ar2[root2]:
        return False

    left1 = getSmaller( ar1 , root1 , minVal )
    left2 = getSmaller( ar2 , root2 , minVal )
    right1 = getBigger( ar1 , root1 , maxVal )
    right2 = getBigger( ar2 , root2 , maxVal )
    print("first left tree " , left1)
    print("first right tree " , right1)
    current = ar1[root1]
    return recursiveBSTChecker( ar1 , ar2 , left1 , left2 , minVal , current  ) and recursiveBSTChecker(ar1 , ar2 , right1 , right2 , current , maxVal )
  

def getBigger( one , start , maxVal ):
    for i in range( start + 1 , len( one )):
        if one[i] >= one[start] and one[i] < maxVal:
            return i
    return -1

def getSmaller( one , start , minVal ):
    for i in range( start + 1  , len( one )):
        if one[i] < one[start] and one[i] >= minVal:
            return i
    return -1
            
    
    
