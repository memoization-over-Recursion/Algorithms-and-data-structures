# time complexity O( n^2 )
# space complexity O( n )
def rectangleMania(coords):
    coords_table = getCoordsTable( coords )
    return countTriangles(coords , coords_table )

def getCoordsTable( matrix ):
    answer = {}
    for coords in matrix:
        coordsString = getStringOfCoord( coords )
        answer[ coordsString ] = True
    return answer

def getStringOfCoord(coords):
     x , y = coords
     return str(x) + "-" + str(y)


def countTriangles( coords , table ):
    answer = 0
    for x1 , y1 in coords:
        for x2 , y2 in coords:
            if not upperRight( [ x1 , y1 ] , [ x2 , y2 ] ):
                continue
            upper = getStringOfCoord([ x1 , y2 ])
            right = getStringOfCoord([ x2 , y1 ])
            if upper in table and right in table:
                answer+=1
    return answer


def upperRight( a , b ):
    x1 , y1 = a 
    x2 , y2 = b
    return x2 > x1 and y2 > y1