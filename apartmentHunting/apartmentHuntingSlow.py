#time complexity O( b^2 * r )
#space complexity O( b * r )
def apartmentHunting( blocks , reqs ):
    maxim = [float("-inf") for b in blocks]
    for i in range( len( blocks ) ):
        for req in reqs:
            closest = float("inf")
            for j in range( len( blocks ) ):
                if(blocks[j][req]):
                    closest = min( closest  , distanceBetween( i , j ) )
            maxim[i] = max( maxim[i] , closest)   

    
    return getMin(maxim)

def getMin( maxim ):
    idOfMin = 0
    min = float("inf")
    for i in range( len( maxim ) ):
        if(maxim[i] < min):
            min = maxim[i]
            idOfMin = i
    return idOfMin
    

def distanceBetween( i , j ):
    return abs( i - j )