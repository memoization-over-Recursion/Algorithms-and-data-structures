#time complexity O( br )
#space complexity O( br )
def apartmentHunting(blocks, reqs):
    av = list(map(lambda req : getMini(blocks , req) , reqs))
    print(av)
    v = getMaxDistances( blocks , av )
    
    return getMin(v)


def getMini( ar , req ):
    minDistances = [0 for i in range( len( ar ) ) ]
    closest = float("inf")
    for i in range( len( ar ) ):
        if(ar[i][req]):
            closest = i
        minDistances[i] = distanceBetween( i , closest)
    for j in reversed( range( len( ar ) ) ):
        if(ar[j][req]):
            closest = j
        minDistances[j] = min( minDistances[j] , distanceBetween( j , closest ) )
    return minDistances

def getMaxDistances(blocks , minim):
    maxw = [0 for b in blocks]
    for i in range( len( blocks ) ):
        minDist = list(map(lambda x : x[i] , minim ) )
        print(minDist)
        maxw[i] = max(minDist)
    return maxw
            
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