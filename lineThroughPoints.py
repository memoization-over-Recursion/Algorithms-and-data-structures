#time complexity O( n^2 )
#space complexity O( n )
def lineThroughPoints(points):
    maxPoints = 1
    for id , p1 in enumerate( points ):
        slopes = {}
        for id2 in range( id + 1 , len( points ) ):
            p2 = points[id2]
            rise , run  = getSlopeOfPoints( p1 , p2 )
            
            stringOfSlope = makeString( rise , run )
            
            if( stringOfSlope not in slopes ):
                slopes[stringOfSlope] = 1
            
            slopes[stringOfSlope] += 1
        maxPoints = max( maxPoints , max( slopes.values()  ,  default = 0 ))

    return maxPoints
            

def makeString( rise , run ):
    return str( rise ) + ":" + str( run ) 

def getSlopeOfPoints( p1 , p2 ):
    x1 , y1 = p1
    x2 , y2 = p2
    slope = [1,0]
    if( x1 != x2 ):
        xDiff = x1 - x2
        yDiff = y1 - y2
        gcdiv = gcder( abs( xDiff ) , abs( yDiff ) )
        xDiff = xDiff // gcdiv
        yDiff = yDiff // gcdiv
        if(xDiff < 0 ):
            xDiff *= -1
            yDiff *= -1

        slope = [yDiff , xDiff]

    return slope

def gcder( a1 , b1 ):
    a = a1
    b = b1
    while True:
        if( a == 0 ):
            return b
        if( b == 0 ):
            return a
        a , b = b , a % b 

        

